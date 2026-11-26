"""Deterministic multi-touch attribution from exported touchpoints and deals."""

from __future__ import annotations

import datetime as dt
from typing import Any, Dict, List, Optional

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick, snapshot_freshness

MODELS = {"linear", "time-decay", "position-based"}


def _weights(model: str, count: int, ages: List[float], half_life_days: float) -> List[float]:
    if count <= 0:
        return []
    if model == "linear":
        return [1.0 / count] * count
    if model == "time-decay":
        raw = [0.5 ** (age / half_life_days) for age in ages]
        total = sum(raw)
        return [w / total for w in raw]
    if count == 1:
        return [1.0]
    if count == 2:
        return [0.5, 0.5]
    result = [0.0] * count
    result[0] = 0.4
    result[-1] = 0.4
    middle = 0.2 / (count - 2)
    for i in range(1, count - 1):
        result[i] = middle
    return result


def _allocate(amount: float, weights: List[float]) -> List[float]:
    """Split ``amount`` across weights so the parts sum exactly to ``amount`` (2dp).

    Uses the largest-remainder method: floor each share to cents, then hand the leftover
    cents to the shares with the largest fractional parts. Without this, attributed revenue
    silently fails to reconcile with won revenue.
    """
    if not weights:
        return []
    raw = [amount * w for w in weights]
    cents = [int(round(value * 100)) for value in raw]
    target = int(round(amount * 100))
    remainder = target - sum(cents)
    if remainder:
        order = sorted(range(len(cents)), key=lambda i: (raw[i] * 100 - cents[i]), reverse=True)
        for step in range(abs(remainder)):
            index = order[step % len(order)]
            cents[index] += 1 if remainder > 0 else -1
    return [c / 100 for c in cents]


def attribute_revenue(
    *,
    touchpoints_path: str,
    deals_path: str,
    model: str = "linear",
    window_days: int = 90,
    half_life_days: float = 7.0,
) -> Dict[str, Any]:
    model = model.lower()
    if model not in MODELS:
        return make_envelope(
            "attribution", model, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"unknown attribution model '{model}'",
                   "hint": "Choose linear, time-decay, or position-based."},
        )
    try:
        touchpoints, touch_snapshot = load_rows(touchpoints_path)
        deals, deal_snapshot = load_rows(deals_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "attribution", deals_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load attribution inputs: {exc}",
                   "hint": "Provide touchpoints and deals as JSON/CSV with IDs, channels, timestamps, and deal amounts."},
        )

    norm_deals: List[Dict[str, Any]] = []
    for row in deals:
        outcome = str(pick(row, "outcome", "status", "result") or "").strip().lower()
        if outcome not in {"won", "closed won", "closed-won", "win"}:
            continue
        closed = parse_date(pick(row, "closed_at", "closed", "close_date", "closedate"))
        amount = as_float(pick(row, "amount", "value", "arr", "deal_amount"))
        if not closed or amount is None:
            continue
        norm_deals.append({
            "deal_id": str(pick(row, "deal_id", "id", "opportunity_id") or ""),
            "contact_id": str(pick(row, "contact_id", "person_id", "lead_id") or ""),
            "amount": amount,
            "closed": closed,
        })

    by_deal: Dict[str, List[Dict[str, Any]]] = {}
    by_contact: Dict[str, List[Dict[str, Any]]] = {}
    for row in touchpoints:
        occurred = parse_date(pick(row, "occurred_at", "timestamp", "event_at", "time"))
        if not occurred:
            continue
        tp = {
            "deal_id": str(pick(row, "deal_id", "opportunity_id") or ""),
            "contact_id": str(pick(row, "contact_id", "person_id", "lead_id") or ""),
            "channel": str(pick(row, "channel", "source", "medium") or "unknown"),
            "campaign": str(pick(row, "campaign", "campaign_name") or "unknown"),
            "occurred": occurred,
            "cost": as_float(pick(row, "cost", "spend")),
        }
        if tp["deal_id"]:
            by_deal.setdefault(tp["deal_id"], []).append(tp)
        if tp["contact_id"]:
            by_contact.setdefault(tp["contact_id"], []).append(tp)

    allocations: List[Dict[str, Any]] = []
    attributed_deals = 0
    unattributed_revenue = 0.0
    for deal in norm_deals:
        candidates = by_deal.get(deal["deal_id"], []) if deal["deal_id"] else []
        if not candidates and deal["contact_id"]:
            candidates = by_contact.get(deal["contact_id"], [])
        eligible = [tp for tp in candidates if deal["closed"] - tp["occurred"] <= dt.timedelta(days=window_days) and tp["occurred"] <= deal["closed"]]
        eligible.sort(key=lambda tp: tp["occurred"])
        if not eligible:
            unattributed_revenue += deal["amount"]
            continue
        attributed_deals += 1
        ages = [(deal["closed"] - tp["occurred"]).total_seconds() / 86400.0 for tp in eligible]
        weights = _weights(model, len(eligible), ages, half_life_days)
        shares = _allocate(deal["amount"], weights)
        for tp, weight, share in zip(eligible, weights, shares):
            allocations.append({
                "deal_id": deal["deal_id"],
                "channel": tp["channel"],
                "campaign": tp["campaign"],
                "occurred_at": tp["occurred"].isoformat(),
                "weight": round(weight, 6),
                "attributed_revenue": share,
                "cost": tp["cost"],
            })

    summary: Dict[str, Dict[str, Any]] = {}
    for row in allocations:
        key = (row["channel"], row["campaign"])
        item = summary.setdefault(key, {"channel": row["channel"], "campaign": row["campaign"], "touches": 0, "deals": set(), "attributed_revenue": 0.0, "cost": 0.0, "cost_known": False})
        item["touches"] += 1
        item["deals"].add(row["deal_id"])
        item["attributed_revenue"] += row["attributed_revenue"]
        if row["cost"] is not None:
            item["cost"] += row["cost"]
            item["cost_known"] = True
    summary_rows = []
    for item in summary.values():
        revenue = round(item["attributed_revenue"], 2)
        cost = round(item["cost"], 2)
        summary_rows.append({
            "channel": item["channel"],
            "campaign": item["campaign"],
            "touches": item["touches"],
            "deals": len(item["deals"]),
            "attributed_revenue": revenue,
            "cost": cost if item["cost_known"] else None,
            "roi": round((revenue - cost) / cost, 4) if item["cost_known"] and cost > 0 else None,
        })
    summary_rows.sort(key=lambda r: r["attributed_revenue"], reverse=True)

    freshness = "CURRENT"
    stamps = [snapshot_freshness(s, window_days)[0] for s in (touch_snapshot, deal_snapshot) if s]
    if "STALE" in stamps:
        freshness = "STALE"

    total_won = sum(d["amount"] for d in norm_deals)
    total_attributed = sum(r["attributed_revenue"] for r in allocations)
    return make_envelope(
        "attribution", deals_path,
        evidence_stamp=freshness,
        metrics={
            "model": model,
            "window_days": window_days,
            "won_deals": len(norm_deals),
            "attributed_deals": attributed_deals,
            "unattributed_deals": len(norm_deals) - attributed_deals,
            "won_revenue": round(total_won, 2),
            "attributed_revenue": round(total_attributed, 2),
            "unattributed_revenue": round(unattributed_revenue, 2),
            "attribution_coverage": round(total_attributed / total_won, 4) if total_won else None,
        },
        inputs={"touchpoints": touchpoints_path, "deals": deals_path, "model": model, "window_days": window_days, "half_life_days": half_life_days},
        rows=[{"kind": "allocation", **r} for r in allocations] + [{"kind": "channel", **r} for r in summary_rows],
        notes=[] if freshness == "CURRENT" else [f"touchpoint/deal snapshot is older than {window_days} days"],
    )
