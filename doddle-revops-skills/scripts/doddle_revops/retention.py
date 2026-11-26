"""NRR/GRR, customer health, renewal risk, and expansion signals (Stage 8)."""

from __future__ import annotations

import datetime as dt
from typing import Any, Dict, List, Optional

from .envelope import make_envelope
from .io import as_float, load_rows, parse_date, pick


def analyze_retention(
    *,
    customers_path: str,
    usage_path: str,
    now: Optional[dt.datetime] = None,
    renewal_window_days: int = 90,
    dropoff_threshold: float = 0.20,
) -> Dict[str, Any]:
    try:
        customers, customer_snapshot = load_rows(customers_path)
        usage, usage_snapshot = load_rows(usage_path)
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "retention", customers_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load retention inputs: {exc}",
                   "hint": "Provide customers (CSV/JSON) with ARR components and usage (CSV/JSON) with customer_id, period, usage_value."},
        )

    reference = now or dt.datetime.now(dt.timezone.utc)
    usage_by_customer: Dict[str, List[tuple]] = {}
    for row in usage:
        customer_id = str(pick(row, "customer_id", "account_id", "account") or "").strip()
        period = str(pick(row, "period", "month") or "").strip()
        value = as_float(pick(row, "usage_value", "usage", "value", "active"))
        if not customer_id or not period:
            continue
        usage_by_customer.setdefault(customer_id, []).append((period, value))

    rows: List[Dict[str, Any]] = []
    starting_total = 0.0
    expansion_total = 0.0
    contraction_total = 0.0
    churn_total = 0.0
    at_risk = 0
    expansion_candidates = 0
    health_scores: List[float] = []

    for row in customers:
        customer_id = str(pick(row, "customer_id", "account_id", "id") or "").strip()
        if not customer_id:
            continue
        starting = as_float(pick(row, "starting_arr", "starting_mrr", "start_arr")) or 0.0
        expansion = as_float(pick(row, "expansion_arr", "expansion", "expansion_mrr")) or 0.0
        contraction = as_float(pick(row, "contraction_arr", "contraction")) or 0.0
        churned = as_float(pick(row, "churned_arr", "churn", "churned_mrr")) or 0.0
        renewal = parse_date(pick(row, "renewal_date", "renewal_at", "contract_end"))

        series = sorted(usage_by_customer.get(customer_id, []))
        values = [v for _, v in series if v is not None]
        dropoff: Optional[float] = None
        growth: Optional[float] = None
        if len(values) >= 2 and values[-2]:
            dropoff = round((values[-2] - values[-1]) / values[-2], 4)
            growth = round((values[-1] - values[-2]) / values[-2], 4)
        inactive = bool(values) and values[-1] == 0

        health = 100.0
        penalties: List[str] = []
        if not values:
            health = None
            penalties.append("no usage history")
        else:
            if inactive:
                health -= 30
                penalties.append("inactive in latest period")
            if dropoff is not None and dropoff > dropoff_threshold:
                penalty = min(40.0, dropoff * 100)
                health -= penalty
                penalties.append(f"usage drop {round(dropoff * 100, 1)}%")

        flags: List[str] = []
        days_to_renewal = (renewal - reference).days if renewal else None
        if renewal and 0 <= days_to_renewal <= renewal_window_days:
            if (dropoff is not None and dropoff > dropoff_threshold) or churned > 0 or contraction > 0 or inactive:
                flags.append("renewal_risk")
                at_risk += 1
        if growth is not None and growth > dropoff_threshold and expansion == 0:
            flags.append("expansion_candidate")
            expansion_candidates += 1

        starting_total += starting
        expansion_total += expansion
        contraction_total += contraction
        churn_total += churned
        if health is not None:
            health_scores.append(max(0.0, health))

        rows.append({
            "customer_id": customer_id,
            "plan": pick(row, "plan", "tier"),
            "starting_arr": starting,
            "expansion_arr": expansion,
            "contraction_arr": contraction,
            "churned_arr": churned,
            "ending_arr": round(starting + expansion - contraction - churned, 2),
            "usage_last": values[-1] if values else None,
            "usage_dropoff": dropoff,
            "usage_growth": growth,
            "health_score": None if health is None else round(max(0.0, health), 1),
            "health_penalties": penalties,
            "days_to_renewal": days_to_renewal,
            "flags": flags,
        })

    nrr = round((starting_total + expansion_total - contraction_total - churn_total) / starting_total, 4) if starting_total else None
    grr = round((starting_total - contraction_total - churn_total) / starting_total, 4) if starting_total else None
    average_health = round(sum(health_scores) / len(health_scores), 1) if health_scores else None

    return make_envelope(
        "retention", customers_path,
        metrics={
            "customers": len(rows),
            "starting_arr": round(starting_total, 2),
            "expansion_arr": round(expansion_total, 2),
            "contraction_arr": round(contraction_total, 2),
            "churned_arr": round(churn_total, 2),
            "nrr": nrr,
            "grr": grr,
            "average_health_score": average_health,
            "renewal_risk_count": at_risk,
            "expansion_candidates": expansion_candidates,
            "renewal_window_days": renewal_window_days,
        },
        inputs={
            "customers": customers_path,
            "usage": usage_path,
            "renewal_window_days": renewal_window_days,
            "dropoff_threshold": dropoff_threshold,
        },
        rows=rows,
        missing=["usage"] if not usage else [],
        notes=["health score is a deterministic usage signal, not a predictive churn model"],
    )
