"""Deterministic cohort retention and revenue-retention matrices."""

from __future__ import annotations

from typing import Any, Dict, List

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick, snapshot_freshness


def _month_index(start, period) -> int:
    return (period.year - start.year) * 12 + period.month - start.month


def analyze_cohorts(path: str, *, max_periods: int = 12) -> Dict[str, Any]:
    try:
        rows, snapshot = load_rows(path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "cohorts", path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load cohort input: {exc}",
                   "hint": "Provide JSON/CSV rows with account_id, cohort_start, period_start, active, and optional revenue."},
        )

    cohorts: Dict[str, Dict[str, Any]] = {}
    skipped = 0
    for row in rows:
        account_id = str(pick(row, "account_id", "customer_id", "id") or "").strip()
        cohort_date = parse_date(pick(row, "cohort_start", "cohort", "signup_at", "started_at"))
        period_date = parse_date(pick(row, "period_start", "period", "month")) or cohort_date
        if not account_id or not cohort_date or not period_date:
            skipped += 1
            continue
        period = _month_index(cohort_date, period_date)
        if period < 0 or period >= max_periods:
            continue
        cohort_key = cohort_date.strftime("%Y-%m")
        active_raw = pick(row, "active", "is_active", "retained")
        if active_raw in (None, ""):
            active = (as_float(pick(row, "revenue", "mrr", "arr")) or 0) > 0
        else:
            active = str(active_raw).strip().lower() in {"1", "true", "yes", "y", "active"}
        revenue = as_float(pick(row, "revenue", "mrr", "arr")) or 0.0
        bucket = cohorts.setdefault(cohort_key, {"size": 0, "accounts": set(), "periods": {}})
        bucket["accounts"].add(account_id)
        p = bucket["periods"].setdefault(period, {"active": set(), "revenue": 0.0})
        if active:
            p["active"].add(account_id)
            p["revenue"] += revenue

    matrix: List[Dict[str, Any]] = []
    for cohort_key in sorted(cohorts):
        bucket = cohorts[cohort_key]
        size = len(bucket["accounts"])
        base_revenue = bucket["periods"].get(0, {}).get("revenue", 0.0)
        for period in range(max_periods):
            p = bucket["periods"].get(period, {"active": set(), "revenue": 0.0})
            active = len(p["active"])
            revenue = round(p["revenue"], 2)
            matrix.append({
                "cohort": cohort_key,
                "period": period,
                "cohort_size": size,
                "active_accounts": active,
                "logo_retention": round(active / size, 4) if size else None,
                "revenue": revenue,
                "revenue_retention": round(revenue / base_revenue, 4) if base_revenue else None,
            })

    freshness = snapshot_freshness(snapshot, 31)[0]
    return make_envelope(
        "cohorts", path,
        evidence_stamp=freshness,
        metrics={
            "cohorts": len(cohorts),
            "accounts": sum(len(c["accounts"]) for c in cohorts.values()),
            "max_periods": max_periods,
            "skipped_rows": skipped,
        },
        inputs={"cohorts": path, "max_periods": max_periods},
        rows=matrix,
        notes=[] if freshness == "CURRENT" else ["cohort snapshot is older than 31 days"],
    )
