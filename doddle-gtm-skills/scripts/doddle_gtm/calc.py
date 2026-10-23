"""Deterministic GTM calculators.

Pure arithmetic over recorded inputs. Formula, inputs and outputs are documented so a skill can
explain them. Missing inputs yield ``None`` (not measured), never 0, and never a guess.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def _ratio(num: Optional[float], den: Optional[float]) -> Optional[float]:
    if num is None or den in (None, 0):
        return None
    return round(num / den, 6)


def funnel(stages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Stage-to-stage conversion for an ordered funnel.

    ``stages`` is ``[{"name": str, "count": int|float}, …]`` in order. Returns per-step
    conversion, drop-off and overall conversion. A zero-in stage yields ``None`` conversions
    (divide-by-zero is not measured, not a zero rate).
    """
    clean = [{"name": str(s.get("name", f"stage{i+1}")), "count": s.get("count")} for i, s in enumerate(stages)]
    steps: List[Dict[str, Any]] = []
    for i in range(1, len(clean)):
        prev, cur = clean[i - 1]["count"], clean[i]["count"]
        steps.append({
            "from": clean[i - 1]["name"],
            "to": clean[i]["name"],
            "from_count": prev,
            "to_count": cur,
            "conversion": _ratio(cur, prev),
            "dropoff": None if prev is None or cur is None else prev - cur,
        })
    overall = _ratio(clean[-1]["count"], clean[0]["count"]) if len(clean) >= 2 else None
    return {
        "stages": clean,
        "steps": steps,
        "overall_conversion": overall,
        "worst_step": (min((s for s in steps if s["conversion"] is not None),
                           key=lambda s: s["conversion"]) if any(s["conversion"] is not None for s in steps) else None),
        "reasons": ([f"{c['name']} count is zero or missing" for c in clean if not c["count"]]
                    if any(not c["count"] for c in clean) else []),
    }


def unit_economics(
    *,
    cac: Optional[float],
    arpa: Optional[float],
    gross_margin: Optional[float],
    churn: Optional[float],
) -> Dict[str, Any]:
    """Classic SaaS unit economics.

    - ``cac``  — customer acquisition cost (currency)
    - ``arpa`` — average revenue per account **per month**
    - ``gross_margin`` — fraction 0..1
    - ``churn`` — monthly logo/revenue churn rate 0..1

    Formulas: LTV = arpa x gross_margin / churn; CAC payback (months) =
    cac / (arpa x gross_margin); LTV:CAC = LTV / cac.
    """
    gm = gross_margin
    monthly_gross_profit = arpa * gm if (arpa is not None and gm is not None) else None
    ltv = _ratio(monthly_gross_profit, churn)
    payback = _ratio(cac, monthly_gross_profit)
    ltv_cac = _ratio(ltv, cac)
    missing = [name for name, val in (("cac", cac), ("arpa", arpa),
                                      ("gross_margin", gross_margin), ("churn", churn)) if val is None]
    return {
        "inputs": {"cac": cac, "arpa": arpa, "gross_margin": gross_margin, "churn": churn},
        "monthly_gross_profit": None if monthly_gross_profit is None else round(monthly_gross_profit, 4),
        "ltv": None if ltv is None else round(ltv, 2),
        "ltv_cac": None if ltv_cac is None else round(ltv_cac, 2),
        "cac_payback_months": None if payback is None else round(payback, 2),
        "missing": missing,
        "notes": (["churn is zero: LTV and LTV:CAC are undefined, not infinite"] if churn == 0 else []),
    }


def pricing(
    *,
    price: Optional[float],
    variable_cost: Optional[float],
    fixed_cost: Optional[float] = None,
    tiers: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Gross margin and break-even for a single plan or a tier mix.

    A tier is ``{"name", "price", "variable_cost", "mix"}`` where ``mix`` is the expected share
    of customers (the mix is normalised to sum to 1). Blended figures use the mix.
    """
    out: Dict[str, Any] = {"single": None, "tiers": None, "missing": []}
    if price is not None and variable_cost is not None:
        contribution = price - variable_cost
        margin = _ratio(contribution, price)
        breakeven = _ratio(fixed_cost, contribution) if fixed_cost is not None else None
        out["single"] = {
            "price": price,
            "variable_cost": variable_cost,
            "contribution_margin": round(contribution, 4),
            "gross_margin": None if margin is None else round(margin, 4),
            "breakeven_units": None if breakeven is None else round(breakeven, 1),
        }
        out["missing"] = (["fixed_cost"] if fixed_cost is None else [])
    else:
        out["missing"] = [n for n, v in (("price", price), ("variable_cost", variable_cost)) if v is None]

    if tiers:
        total_mix = sum((t.get("mix") or 0) for t in tiers) or None
        blended_price = blended_cost = 0.0
        rows = []
        for t in tiers:
            mix = (t.get("mix") or 0) / total_mix if total_mix else None
            contribution = (t["price"] - t["variable_cost"]) if (t.get("price") is not None and t.get("variable_cost") is not None) else None
            rows.append({"name": t.get("name"), "price": t.get("price"), "variable_cost": t.get("variable_cost"),
                         "mix": None if mix is None else round(mix, 4), "contribution_margin": contribution})
            if contribution is not None and mix is not None:
                blended_price += t["price"] * mix
                blended_cost += t["variable_cost"] * mix
        blended_margin = _ratio((blended_price - blended_cost), blended_price) if blended_price else None
        out["tiers"] = {
            "rows": rows,
            "blended_price": None if total_mix is None else round(blended_price, 2),
            "blended_price_margin": None if blended_margin is None else round(blended_margin, 4),
        }
        if total_mix is None:
            out["missing"].append("tier mix")
    return out


def size_market(
    *,
    total_accounts: Optional[float] = None,
    acv: Optional[float] = None,
    units: Optional[float] = None,
    unit_price: Optional[float] = None,
    sam_pct: Optional[float] = None,
    som_pct: Optional[float] = None,
) -> Dict[str, Any]:
    """Bottom-up TAM/SAM/SOM.

    TAM = accounts x ACV  (or units x unit_price). SAM = TAM x sam_pct. SOM = SAM x som_pct.
    Every value derives from a provided input; nothing is looked up or estimated.
    """
    per = acv if acv is not None else unit_price
    count = total_accounts if total_accounts is not None else units
    tam = None if (count is None or per is None) else round(count * per, 2)
    sam = None if (tam is None or sam_pct is None) else round(tam * sam_pct, 2)
    som = None if (sam is None or som_pct is None) else round(sam * som_pct, 2)
    missing = [n for n, v in (("accounts/units", count), ("acv/unit_price", per)) if v is None]
    return {
        "inputs": {"total_accounts": total_accounts, "acv": acv, "units": units, "unit_price": unit_price,
                   "sam_pct": sam_pct, "som_pct": som_pct},
        "tam": tam, "sam": sam, "som": som, "missing": missing,
        "notes": ["SAM and SOM require sam_pct/som_pct; they are your assumptions, not measured facts."
                  if (sam is None or som is None) else []][0],
    }
