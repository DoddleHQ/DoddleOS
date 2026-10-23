"""Audit a deals/pipeline export.

Input is a CRM export the user provides (JSON array/object or CSV). Every number is computed
from those rows. Nothing is fetched from a CRM.
"""

from __future__ import annotations

import csv
import datetime
import json
from typing import Any, Dict, List, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from .envelope import CURRENT, Finding, Signal, make_envelope, tier_for

STAGE_KEYS = ("stage", "pipeline_stage", "dealstage")
AMOUNT_KEYS = ("amount", "value", "deal_amount", "arr", "mrr")
CREATED_KEYS = ("created_at", "created", "createdate", "open_date")
CLOSED_KEYS = ("closed_at", "closed", "closedate", "close_date")
OUTCOME_KEYS = ("outcome", "status", "result", "state")
SEGMENT_KEYS = ("segment", "tier", "source", "channel", "owner")
WON = {"won", "closed won", "closedwon", "win", "closed-won"}
LOST = {"lost", "closed lost", "closedlost", "loss", "closed-lost"}


def _pick(row: Dict[str, Any], keys: tuple) -> Any:
    for k in keys:
        for rk in row:
            if rk.lower().strip() == k:
                return row[rk]
    return None


def _as_date(value: Any) -> Optional[datetime.date]:
    if value in (None, ""):
        return None
    try:
        return datetime.date.fromisoformat(str(value).strip()[:10])
    except ValueError:
        return None


def _as_float(value: Any) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", "").replace("$", ""))
    except ValueError:
        return None


def load_export(path: str) -> List[Dict[str, Any]]:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if path.lower().endswith(".csv"):
        return [dict(r) for r in csv.DictReader(raw.splitlines())]
    data = json.loads(raw)
    if isinstance(data, dict):
        for key in ("deals", "rows", "items", "data", "records"):
            if isinstance(data.get(key), list):
                return data[key]
        return [data]
    if isinstance(data, list):
        return data
    raise ValueError("export must be a JSON array/object or CSV")


def _normalise(row: Dict[str, Any]) -> Dict[str, Any]:
    outcome_raw = str(_pick(row, OUTCOME_KEYS) or "").strip().lower()
    outcome = "won" if outcome_raw in WON else "lost" if outcome_raw in LOST else "open"
    return {
        "stage": _pick(row, STAGE_KEYS),
        "amount": _as_float(_pick(row, AMOUNT_KEYS)),
        "created": _as_date(_pick(row, CREATED_KEYS)),
        "closed": _as_date(_pick(row, CLOSED_KEYS)),
        "outcome": outcome,
        "segment": _pick(row, SEGMENT_KEYS),
    }


def _hhi(values: List[Any]) -> Optional[float]:
    """Herfindahl index over category shares; 1 = one category, ->0 = evenly spread."""
    if not values:
        return None
    counts: Dict[Any, int] = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    n = len(values)
    return round(sum((c / n) ** 2 for c in counts.values()), 4)


def audit_pipeline(path: str, *, target: Optional[str] = None) -> Dict[str, Any]:
    try:
        rows = [_normalise(r) for r in load_export(path)]
    except Exception as exc:  # noqa: BLE001 - surfaced to the user
        return make_envelope(
            "audit", target or path,
            toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
            evidence_stamp="PARTIAL",
            error={"message": f"could not read export: {exc}",
                   "hint": "Provide a JSON array of deals or a CSV with columns like stage, amount, created_at, closed_at, outcome, segment."},
        )
    if not rows:
        return make_envelope(
            "audit", target or path,
            toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
            error={"message": "export contains no deals",
                   "hint": "Check the file has a non-empty list of deal rows."},
        )
    return _audit(rows, target or path)


def _audit(rows: List[Dict[str, Any]], target: str) -> Dict[str, Any]:
    signals: List[Signal] = []
    findings: List[Finding] = []
    notes: List[str] = []

    # data completeness -------------------------------------------------
    complete = [r for r in rows if r["stage"] not in (None, "") and r["amount"] is not None and r["created"]]
    rate = round(100.0 * len(complete) / len(rows), 1)
    dpts = round(25.0 * rate / 100.0, 1)
    signals.append(Signal("pipeline.data_completeness", dpts, 25,
                          detail={"deals": len(rows), "complete": len(complete), "rate_pct": rate}))
    if rate < 100:
        findings.append(Finding("pipeline.data_completeness", 0, "high", "low", round(25 - dpts, 1),
                                "Deals are missing stage, amount or created date",
                                f"{len(complete)}/{len(rows)} deals have all of stage, amount and created_at."))

    # win rate ----------------------------------------------------------
    closed = [r for r in rows if r["outcome"] in ("won", "lost")]
    won = [r for r in closed if r["outcome"] == "won"]
    if closed:
        wr = round(len(won) / len(closed), 4)
        wpts = round(25.0 * min(wr, 0.5) / 0.5, 1) if wr < 0.5 else 25.0
        signals.append(Signal("pipeline.win_rate", wpts, 25,
                              detail={"closed": len(closed), "won": len(won), "rate": wr}))
        if wr < 0.2:
            findings.append(Finding("pipeline.win_rate", 0, "high", "medium", round(25 - wpts, 1),
                                    "Win rate is below the 20% starting line",
                                    f"{len(won)}/{len(closed)} closed deals won ({round(wr*100,1)}%)."))
    else:
        signals.append(Signal("pipeline.win_rate", None, 25, detail={},
                              skipped_reason="not applicable: no closed (won/lost) deals in the export"))
        wpts = None

    # cycle time --------------------------------------------------------
    cycle = [(r["closed"] - r["created"]).days for r in closed if r["created"] and r["closed"]]
    if cycle:
        avg = round(sum(cycle) / len(cycle), 1)
        cpts = 20.0 if avg <= 90 else round(max(0.0, 20.0 * 90 / avg), 1)
        signals.append(Signal("pipeline.cycle_time", cpts, 20,
                              detail={"deals": len(cycle), "avg_days": avg, "min": min(cycle), "max": max(cycle)}))
        if avg > 90:
            findings.append(Finding("pipeline.cycle_time", 0, "medium", "medium", round(20 - cpts, 1),
                                    "Average sales cycle exceeds 90 days",
                                    f"Mean cycle is {avg} days across {len(cycle)} closed deals."))
    else:
        signals.append(Signal("pipeline.cycle_time", None, 20, detail={},
                              skipped_reason="not applicable: no closed deals with both created and closed dates"))

    # stage spread (balance of open pipeline) ---------------------------
    open_deals = [r for r in rows if r["outcome"] == "open" and r["stage"] not in (None, "")]
    stage_names = {r["stage"] for r in open_deals}
    if len(open_deals) >= 2 and len(stage_names) >= 2:
        hhi = _hhi([r["stage"] for r in open_deals])
        k = len(stage_names)
        balance = None if hhi is None else max(0.0, min(1.0, (1.0 - hhi) / (1.0 - 1.0 / k)))
        spts = 15.0 if balance is None else round(15.0 * balance, 1)
        signals.append(Signal("pipeline.stage_spread", spts, 15,
                              detail={"open_deals": len(open_deals), "stages": k,
                                      "hhi": hhi, "balance": None if balance is None else round(balance, 4)}))
    else:
        signals.append(Signal("pipeline.stage_spread", None, 15,
                              detail={"open_deals": len(open_deals), "stages": len(stage_names)},
                              skipped_reason="not applicable: needs at least two open deals spread across two or more stages"))

    # segment/source coverage (data hygiene) ----------------------------
    open_rows = [r for r in rows if r["outcome"] == "open"]
    knowable = [r for r in open_rows if r["segment"] not in (None, "")]
    if open_rows:
        sc = round(100.0 * len(knowable) / len(open_rows), 1)
        spts2 = round(15.0 * sc / 100.0, 1)
        signals.append(Signal("pipeline.segment_coverage", spts2, 15,
                              detail={"open_deals": len(open_rows), "tagged": len(knowable), "rate_pct": sc}))
        if sc < 100:
            findings.append(Finding("pipeline.segment_coverage", 0, "low", "low", round(15 - spts2, 1),
                                    "Some open deals have no segment/source/owner tag",
                                    f"{len(knowable)}/{len(open_rows)} open deals carry a segment/source/owner tag."))
    else:
        signals.append(Signal("pipeline.segment_coverage", None, 15, detail={},
                              skipped_reason="not applicable: no open deals"))

    measured = [s for s in signals if s.value is not None]
    earned = sum(s.value for s in measured)
    possible = sum(s.max for s in measured)
    composite = round(100.0 * earned / possible, 1) if possible else None

    total_open_value = sum(r["amount"] or 0 for r in open_deals)

    def _category(ids: tuple) -> Optional[float]:
        vals = [s for s in signals if s.id in ids and s.value is not None]
        if not vals:
            return None
        return round(100.0 * sum(s.value for s in vals) / sum(s.max for s in vals), 1)

    categories = {
        "hygiene": _category(("pipeline.data_completeness", "pipeline.segment_coverage")),
        "velocity": _category(("pipeline.win_rate", "pipeline.cycle_time")),
    }
    for i, f in enumerate(sorted(findings, key=lambda f: (-f.points_lost, f.id)), start=1):
        f.priority = i
    env = make_envelope(
        "audit", target,
        toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
        evidence_stamp=CURRENT, pages_ok=len(rows),
        notes=notes, categories=categories, missing=[s.id for s in signals if s.value is None],
        signal_count=len(measured), signal_total=len(signals),
        scores={"composite": composite, "tier": tier_for(composite), "categories": categories},
        signals=signals, findings=findings,
    )
    env["totals"] = {"deals": len(rows), "open_deals": len(open_deals),
                     "open_pipeline_value": round(total_open_value, 2)}
    return env
