"""Render a GTM envelope as a markdown report. Numbers are copied, never recomputed."""

from __future__ import annotations

from typing import Any, Dict, List

TITLES = {
    "audit": "GTM Pipeline Report",
    "report": "GTM Pipeline Report",
    "funnel": "Funnel Analysis",
    "unit-economics": "Unit Economics",
    "pricing": "Pricing Model",
    "size-market": "Market Sizing",
    "score": "GTM Scorecard",
    "frameworks": "GTM Frameworks",
}


def _fmt_score(v: Any) -> str:
    return "not scored" if v is None else f"{v}/100"


def _num(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:g}"
    return str(v)


def render_markdown(env: Dict[str, Any]) -> str:
    lines: List[str] = []
    command = env.get("command", "report")
    scores = env.get("scores") or {}
    title = TITLES.get(command, command.replace("-", " ").title())
    lines.append(f"# {title} — {env.get('target', '')}")
    lines.append("")
    lines.append(f"**{_fmt_score(scores.get('composite'))} ({scores.get('tier', '')})** · evidence "
                 f"`{env.get('evidence', {}).get('stamp', '—')}` · scoring `{env.get('scoring_version')}` · "
                 f"data `{env.get('data_version')}`")
    lines.append("")
    if env.get("error"):
        lines.append(f"**Error:** {env['error'].get('message')}")
        lines.append("")
        lines.append(f"> {env['error'].get('hint')}")
        return "\n".join(lines) + "\n"

    cats = (scores.get("categories") or {})
    if cats:
        lines.append("## Category scores")
        lines.append("")
        lines.append("| Category | Score |")
        lines.append("|----------|-------|")
        for name, val in cats.items():
            lines.append(f"| {name} | {_fmt_score(val)} |")
        lines.append("")

    metrics = env.get("metrics")
    if metrics:
        lines.append("## Metrics")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        for name, val in metrics.items():
            lines.append(f"| {name} | {_num(val)} |")
        lines.append("")

    signals = env.get("signals") or []
    if signals:
        lines.append("## Signals")
        lines.append("")
        lines.append("| Signal | Value | Max | Class | Note |")
        lines.append("|--------|-------|-----|-------|------|")
        for s in signals:
            note = s.get("skipped_reason") or ""
            lines.append(f"| {s['id']} | {_num(s.get('value'))} | {s.get('max')} | {s.get('class')} | {note} |")
        lines.append("")

    findings = env.get("findings") or []
    if findings:
        lines.append("## Prioritized findings")
        lines.append("")
        for f in findings:
            lines.append(f"{f['priority']}. **{f['title']}** — {f['severity']}, effort {f['effort']}, "
                         f"~{f['points_lost']} pts")
            lines.append(f"   - {f['detail']}")
        lines.append("")

    lines.append(f"_Generated {env.get('generated_at')} by doddle-go-to-market toolkit {env.get('toolkit_version')}._")
    return "\n".join(lines) + "\n"
