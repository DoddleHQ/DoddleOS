"""Automated QBR pack and CSM deck outline (Stage 10)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .envelope import make_envelope
from .io import as_float, pick


def _status(target: float, actual: float) -> str:
    if target == 0:
        return "on_track" if actual >= 0 else "off_track"
    ratio = actual / target
    if ratio >= 1.0:
        return "on_track"
    if ratio >= 0.8:
        return "at_risk"
    return "off_track"


def build_qbr(*, account_path: str) -> Dict[str, Any]:
    try:
        payload = json.loads(Path(account_path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return make_envelope(
            "qbr", account_path, ok=False, evidence_stamp="PARTIAL",
            error={"message": f"could not load account payload: {exc}",
                   "hint": "Provide JSON with account{}, kpis[], outcomes[], risks[], asks[]."},
        )

    profile = payload.get("account", {}) if isinstance(payload, dict) else {}
    kpis = payload.get("kpis", []) if isinstance(payload, dict) else []
    outcomes = payload.get("outcomes", []) if isinstance(payload, dict) else []
    risks = payload.get("risks", []) if isinstance(payload, dict) else []
    asks = payload.get("asks", []) if isinstance(payload, dict) else []
    investment = as_float(payload.get("investment")) if isinstance(payload, dict) else None
    revenue = as_float(payload.get("revenue")) if isinstance(payload, dict) else None
    period = payload.get("period", "current period") if isinstance(payload, dict) else "current period"

    scoreboard: List[Dict[str, Any]] = []
    counts = {"on_track": 0, "at_risk": 0, "off_track": 0, "not_measured": 0}
    for kpi in kpis:
        metric = str(pick(kpi, "metric", "name", "kpi") or "unnamed")
        target = as_float(pick(kpi, "target", "goal"))
        actual = as_float(pick(kpi, "actual", "value"))
        if target is None or actual is None:
            status = "not_measured"
            delta = None
        else:
            status = _status(target, actual)
            delta = round(actual - target, 4)
        counts[status] += 1
        scoreboard.append({
            "metric": metric,
            "target": target,
            "actual": actual,
            "delta": delta,
            "status": status,
            "unit": pick(kpi, "unit", "format"),
        })

    roi = None
    if investment is not None and revenue is not None and investment:
        roi = round((revenue - investment) / investment, 4)

    deck = [
        {
            "id": "value-delivered",
            "title": "Value delivered",
            "bullets": [str(o) for o in outcomes] or ["No outcomes supplied — do not present a value claim"],
        },
        {
            "id": "scorecard",
            "title": "Scorecard",
            "bullets": [f"{row['metric']}: {row['actual']} vs {row['target']} ({row['status']})"
                        for row in scoreboard] or ["No KPIs supplied"],
        },
        {
            "id": "risks",
            "title": "Risks and mitigations",
            "bullets": [str(r) for r in risks] or ["No risks supplied — say so rather than inventing one"],
        },
        {
            "id": "ask",
            "title": "The ask",
            "bullets": [str(a) for a in asks] or ["No ask defined"],
        },
    ]

    markdown_lines = [
        f"# QBR — {profile.get('name', 'Account')} ({period})",
        "",
        "## Scoreboard",
        "",
        "| Metric | Target | Actual | Delta | Status |",
        "|---|---|---|---|---|",
    ]
    for row in scoreboard:
        markdown_lines.append(
            f"| {row['metric']} | {row['target'] if row['target'] is not None else 'NOT AVAILABLE'} "
            f"| {row['actual'] if row['actual'] is not None else 'NOT AVAILABLE'} "
            f"| {row['delta'] if row['delta'] is not None else '—'} | {row['status']} |"
        )
    if roi is not None:
        markdown_lines += ["", f"**ROI:** {roi} (revenue {revenue} − investment {investment})"]
    else:
        markdown_lines += ["", "**ROI:** NOT AVAILABLE — investment and revenue were not supplied"]
    markdown_lines += ["", "## Outcomes", *[f"- {o}" for o in outcomes], "", "## Risks", *[f"- {r}" for r in risks], "", "## The ask", *[f"- {a}" for a in asks], ""]

    missing = []
    if investment is None or revenue is None:
        missing.append("roi_inputs")
    if any(row["status"] == "not_measured" for row in scoreboard):
        missing.append("kpi_actuals")

    return make_envelope(
        "qbr", account_path,
        metrics={
            "kpis": len(scoreboard),
            "on_track": counts["on_track"],
            "at_risk": counts["at_risk"],
            "off_track": counts["off_track"],
            "not_measured": counts["not_measured"],
            "roi": roi,
            "investment": investment,
            "revenue": revenue,
            "slides": len(deck),
        },
        inputs={"account": account_path, "period": period, "account_name": profile.get("name")},
        rows=[{"kind": "kpi", **row} for row in scoreboard]
             + [{"kind": "slide", **slide} for slide in deck],
        missing=missing,
        notes=[],
    )


def render_qbr_markdown(envelope: Dict[str, Any]) -> str:
    rows = [r for r in envelope.get("rows", []) if r.get("kind") == "kpi"]
    deck = [r for r in envelope.get("rows", []) if r.get("kind") == "slide"]
    inputs = envelope.get("inputs", {})
    lines = [f"# QBR — {inputs.get('account_name', 'Account')} ({inputs.get('period', 'current period')})", ""]
    lines += ["## Scoreboard", "", "| Metric | Target | Actual | Delta | Status |", "|---|---|---|---|---|"]
    for row in rows:
        target = row["target"] if row["target"] is not None else "NOT AVAILABLE"
        actual = row["actual"] if row["actual"] is not None else "NOT AVAILABLE"
        delta = row["delta"] if row["delta"] is not None else "—"
        lines.append(f"| {row['metric']} | {target} | {actual} | {delta} | {row['status']} |")
    metrics = envelope.get("metrics", {})
    if metrics.get("roi") is not None:
        lines += ["", f"**ROI:** {metrics['roi']}"]
    else:
        lines += ["", "**ROI:** NOT AVAILABLE — investment and revenue were not supplied"]
    for slide in deck:
        lines += ["", f"## {slide['title']}", *[f"- {b}" for b in slide["bullets"]]]
    lines.append("")
    return "\n".join(lines)
