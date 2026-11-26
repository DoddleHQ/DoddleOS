"""Public teardown and revenue portfolio comparison (Stage 12)."""

from __future__ import annotations

import datetime as dt
import json
import statistics
from pathlib import Path
from typing import Any, Dict, List, Optional

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick

MODEL_ALIASES = {
    "seat": "seat", "seats": "seat", "per seat": "seat", "per-seat": "seat", "user": "seat", "users": "seat",
    "metered": "metered", "usage": "metered", "usage-based": "metered", "api": "metered", "consumption": "metered",
    "hybrid": "hybrid", "platform + seat": "hybrid", "base + overage": "hybrid",
    "flat": "flat", "flat-rate": "flat", "unlimited": "flat", "free": "free",
}


def _normalise_model(value: Any) -> str:
    text = str(value or "").strip().lower()
    if not text:
        return "unknown"
    if text in MODEL_ALIASES:
        return MODEL_ALIASES[text]
    for alias, canonical in MODEL_ALIASES.items():
        if alias in text:
            return canonical
    return "unknown"


def build_portfolio(
    *,
    companies_path: str,
    observations_path: str,
    now: Optional[dt.datetime] = None,
) -> Dict[str, Any]:
    try:
        companies = json.loads(Path(companies_path).read_text(encoding="utf-8"))
        observations, snapshot = load_rows(observations_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "portfolio", companies_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load portfolio inputs: {exc}",
                   "hint": "Provide companies JSON with name/pricing_model/value_metric/price and observations CSV with company, observation, observed_at."},
        )

    reference = now or dt.datetime.now(dt.timezone.utc)
    obs_by_company: Dict[str, List[Dict[str, Any]]] = {}
    for row in observations:
        company = str(pick(row, "company", "name", "competitor") or "").strip()
        if not company:
            continue
        observed = parse_date(pick(row, "observed_at", "date", "captured_at"))
        obs_by_company.setdefault(company, []).append({
            "observation": str(pick(row, "observation", "note", "finding") or ""),
            "source_url": pick(row, "source_url", "url", "source"),
            "observed_at": observed.isoformat() if observed else None,
        })

    rows: List[Dict[str, Any]] = []
    prices: List[float] = []
    models: set = set()
    for company in companies:
        name = str(company.get("name", "unnamed"))
        model = _normalise_model(company.get("pricing_model") or company.get("model"))
        price = as_float(company.get("price"))
        company_observations = obs_by_company.get(name, [])
        dated = [o for o in company_observations if o["observed_at"]]
        latest = max(dated, key=lambda o: o["observed_at"]) if dated else None
        age_days = None
        if latest and latest["observed_at"]:
            age_days = round((reference - parse_date(latest["observed_at"])).total_seconds() / 86400.0, 1)
        confidence = "low"
        if len(company_observations) >= 3 and age_days is not None and age_days <= 180:
            confidence = "high"
        elif len(company_observations) >= 1 and age_days is not None and age_days <= 365:
            confidence = "medium"
        models.add(model)
        if price is not None:
            prices.append(price)
        rows.append({
            "company": name,
            "pricing_model": model,
            "value_metric": company.get("value_metric"),
            "price": price,
            "free_tier": company.get("free_tier"),
            "segment": company.get("segment"),
            "observations": len(company_observations),
            "latest_observed_at": latest["observed_at"] if latest else None,
            "observation_age_days": age_days,
            "confidence": confidence,
            "url": company.get("url"),
        })

    comparable = len(models) == 1 and "unknown" not in models
    comparison = None
    if comparable and prices:
        comparison = {
            "min": min(prices),
            "max": max(prices),
            "median": round(statistics.median(prices), 2),
        }

    outline = [
        {"section": "Positioning and narrative", "evidence_needed": "public pricing/packaging page, dated"},
        {"section": "ICP and segments", "evidence_needed": "public docs or case studies, dated"},
        {"section": "Pricing and packaging", "evidence_needed": "captured pricing page with date"},
        {"section": "Channels and motion", "evidence_needed": "public partner/affiliate pages, dated"},
        {"section": "Proof and traction", "evidence_needed": "cited, dated public claims only"},
        {"section": "Gaps we can exploit", "evidence_needed": "derived from the evidence above"},
    ]

    return make_envelope(
        "portfolio", companies_path,
        metrics={
            "companies": len(rows),
            "observations": len(observations),
            "pricing_models": sorted(models),
            "comparable": comparable,
            "price_min": comparison["min"] if comparison else None,
            "price_max": comparison["max"] if comparison else None,
            "price_median": comparison["median"] if comparison else None,
            "low_confidence_companies": sum(1 for r in rows if r["confidence"] == "low"),
        },
        inputs={"companies": companies_path, "observations": observations_path, "as_of": reference.isoformat()},
        rows=[{"kind": "company", **r} for r in rows] + [{"kind": "outline", **o} for o in outline],
        missing=["price"] if any(r["price"] is None for r in rows) else [],
        notes=["pricing models differ, so price comparison is withheld — like-for-like only"]
        if not comparable and rows else [],
    )
