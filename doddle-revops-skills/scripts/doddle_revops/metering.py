"""Usage metering, credits, and invoice preview (Stage 5)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .envelope import make_envelope
from .io import as_float, load_rows, pick


def meter_usage(
    *,
    usage_path: str,
    plan_path: str,
) -> Dict[str, Any]:
    try:
        usage_rows, snapshot = load_rows(usage_path)
        plan = json.loads(Path(plan_path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "meter", plan_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load metering inputs: {exc}",
                   "hint": "Provide usage rows (JSONL/CSV) and a plan (JSON) with tiers[]."},
        )

    currency = plan.get("currency", "USD")
    tiers: Dict[str, Dict[str, Any]] = {}
    for tier in plan.get("tiers", []):
        name = str(tier.get("name", "")).strip()
        if not name:
            continue
        tiers[name] = {
            "name": name,
            "price": as_float(tier.get("price")) or 0.0,
            "included_units": as_float(tier.get("included_units")) or 0.0,
            "unit_price": as_float(tier.get("unit_price")) or 0.0,
            "credits": as_float(tier.get("credits")) or 0.0,
            "accounts": [str(a) for a in tier.get("accounts", [])],
        }

    buckets: Dict[tuple, Dict[str, Any]] = {}
    unrated = 0
    for row in usage_rows:
        account_id = str(pick(row, "account_id", "account", "customer_id") or "").strip()
        period = str(pick(row, "period", "month", "billing_period") or "").strip()
        quantity = as_float(pick(row, "quantity", "units", "value")) or 0.0
        tier_name = str(pick(row, "tier", "plan") or "").strip()
        if not account_id or not period:
            unrated += 1
            continue
        if not tier_name:
            for candidate in tiers.values():
                if account_id in candidate["accounts"]:
                    tier_name = candidate["name"]
                    break
        if tier_name not in tiers:
            unrated += 1
            continue
        bucket = buckets.setdefault((account_id, period), {"account_id": account_id, "period": period, "quantity": 0.0, "tier": tier_name})
        bucket["quantity"] += quantity

    rows: List[Dict[str, Any]] = []
    total_base = 0.0
    total_overage = 0.0
    total_credits_used = 0.0
    for (account_id, period), bucket in sorted(buckets.items()):
        tier = tiers[bucket["tier"]]
        quantity = bucket["quantity"]
        credits_available = tier["credits"]
        included = tier["included_units"]
        credits_used = min(quantity, credits_available)
        units_after_credits = quantity - credits_used
        billable_units = max(0.0, units_after_credits - included)
        base_amount = tier["price"]
        overage_amount = round(billable_units * tier["unit_price"], 2)
        total_amount = round(base_amount + overage_amount, 2)
        total_base += base_amount
        total_overage += overage_amount
        total_credits_used += credits_used
        rows.append({
            "account_id": account_id,
            "period": period,
            "tier": tier["name"],
            "quantity": quantity,
            "credits_available": credits_available,
            "credits_used": round(credits_used, 2),
            "included_units": included,
            "billable_units": round(billable_units, 2),
            "base_amount": base_amount,
            "overage_amount": overage_amount,
            "total_amount": total_amount,
            "currency": currency,
        })

    return make_envelope(
        "meter", plan_path,
        metrics={
            "rated_account_periods": len(rows),
            "unrated_usage_rows": unrated,
            "total_base_amount": round(total_base, 2),
            "total_overage_amount": round(total_overage, 2),
            "total_billed": round(total_base + total_overage, 2),
            "credits_used": round(total_credits_used, 2),
            "currency": currency,
        },
        inputs={"usage": usage_path, "plan": plan_path, "tiers": sorted(tiers)},
        rows=rows,
        missing=["tier"] if unrated else [],
        notes=["this is an invoice preview — no billing object is created"] if rows else [],
    )
