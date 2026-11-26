"""Deterministic product-qualified lead scoring from exported events."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick


def _load_model(path: str) -> Dict[str, Any]:
    model = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(model, dict):
        raise ValueError("PQL model must be a JSON object")
    return model


def score_pql(
    *,
    events_path: str,
    accounts_path: str,
    model_path: str,
) -> Dict[str, Any]:
    try:
        events, event_snapshot = load_rows(events_path)
        accounts, account_snapshot = load_rows(accounts_path)
        model = _load_model(model_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "pql", model_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load PQL inputs: {exc}",
                   "hint": "Provide events (JSONL/CSV), accounts (JSON/CSV), and a JSON model with aha_events, event_weights, thresholds, and weights."},
        )

    as_of = parse_date(model.get("as_of")) or dt.datetime.now(dt.timezone.utc)
    window_days = int(model.get("window_days", 30))
    window_start = as_of - dt.timedelta(days=window_days)
    aha_events = {str(x) for x in model.get("aha_events", [])}
    min_aha = int(model.get("min_aha_count", 1))
    event_weights = {str(k): as_float(v) or 0.0 for k, v in model.get("event_weights", {}).items()}
    weights = model.get("weights", {})
    w_fit = as_float(weights.get("fit")) or 0.4
    w_intent = as_float(weights.get("intent")) or 0.4
    w_recency = as_float(weights.get("recency")) or 0.2
    weight_sum = w_fit + w_intent + w_recency
    if weight_sum <= 0:
        w_fit, w_intent, w_recency = 0.4, 0.4, 0.2
        weight_sum = 1.0
    pql_threshold = as_float(model.get("thresholds", {}).get("pql")) or 70.0
    hot_threshold = as_float(model.get("thresholds", {}).get("hot")) or 85.0

    account_map: Dict[str, Dict[str, Any]] = {}
    for row in accounts:
        account_id = str(pick(row, "account_id", "id", "account") or "").strip()
        if account_id:
            account_map[account_id] = row

    by_account: Dict[str, List[Dict[str, Any]]] = {}
    unknown_events = 0
    for event in events:
        account_id = str(pick(event, "account_id", "account", "id") or "").strip()
        if not account_id:
            unknown_events += 1
            continue
        if account_id not in account_map:
            unknown_events += 1
            continue
        occurred = parse_date(pick(event, "event_at", "occurred_at", "timestamp", "time"))
        if not occurred or occurred < window_start or occurred > as_of:
            continue
        by_account.setdefault(account_id, []).append({**event, "_occurred": occurred})

    results: List[Dict[str, Any]] = []
    for account_id, account in account_map.items():
        account_events = by_account.get(account_id, [])
        fit = as_float(pick(account, "fit_score", "fit", "icp_score"))
        event_names = [str(pick(e, "event_name", "event", "name") or "") for e in account_events]
        aha_count = sum(1 for name in event_names if name in aha_events)
        intent = min(100.0, sum(event_weights.get(name, 0.0) for name in event_names))
        last_event = max((e["_occurred"] for e in account_events), default=None)
        days_since = (as_of - last_event).total_seconds() / 86400.0 if last_event else None
        recency = max(0.0, 100.0 * (1.0 - days_since / window_days)) if days_since is not None else 0.0
        if fit is None:
            score = None
            tier = "insufficient_data"
        else:
            score = round((fit * w_fit + intent * w_intent + recency * w_recency) / weight_sum, 1)
            if score >= hot_threshold and aha_count >= min_aha:
                tier = "hot"
            elif score >= pql_threshold and aha_count >= min_aha:
                tier = "pql"
            else:
                tier = "nurture"
        results.append({
            "account_id": account_id,
            "segment": pick(account, "segment", "tier"),
            "owner": pick(account, "owner"),
            "fit_score": fit,
            "intent_score": round(intent, 1),
            "recency_score": round(recency, 1),
            "aha_count": aha_count,
            "event_count": len(account_events),
            "last_event_at": last_event.isoformat() if last_event else None,
            "pql_score": score,
            "tier": tier,
        })

    results.sort(key=lambda r: (r["pql_score"] is not None, r["pql_score"] or 0), reverse=True)
    tiers = {name: sum(1 for r in results if r["tier"] == name) for name in ("hot", "pql", "nurture", "insufficient_data")}
    scored = [r for r in results if r["pql_score"] is not None]
    freshness = "CURRENT"
    if event_snapshot or account_snapshot:
        from .io import snapshot_freshness
        stamps = [snapshot_freshness(s, window_days)[0] for s in (event_snapshot, account_snapshot) if s]
        if "STALE" in stamps:
            freshness = "STALE"

    return make_envelope(
        "pql", model_path,
        evidence_stamp=freshness,
        metrics={
            "accounts": len(results),
            "scored_accounts": len(scored),
            "average_pql_score": round(sum(r["pql_score"] for r in scored) / len(scored), 1) if scored else None,
            "tiers": tiers,
            "unknown_account_events": unknown_events,
            "window_days": window_days,
            "as_of": as_of.isoformat(),
        },
        inputs={
            "events": events_path,
            "accounts": accounts_path,
            "model": model_path,
            "aha_events": sorted(aha_events),
            "weights": {"fit": w_fit, "intent": w_intent, "recency": w_recency},
            "thresholds": {"pql": pql_threshold, "hot": hot_threshold},
        },
        rows=results,
        missing=["fit_score"] if any(r["fit_score"] is None for r in results) else [],
        notes=[] if freshness == "CURRENT" else [f"event/account snapshot is older than {window_days} days"],
    )
