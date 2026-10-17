"""Render an audit/score envelope as a markdown report. Numbers are copied, never recomputed."""

from __future__ import annotations

from typing import Any, Dict, List


def _fmt_score(v: Any) -> str:
    return "not scored" if v is None else f"{v}/100"


def render_markdown(env: Dict[str, Any]) -> str:
    lines: List[str] = []
    scores = env.get("scores") or {}
    target = env.get("target", "")
    result = scores.get("composite")
    tier = scores.get("tier", "")
    command = env.get("command", "audit")
    title = {"report": "SEO & GEO Report", "audit": "SEO & GEO Audit"}.get(command, command.title())
    lines.append(f"# {title} — {target}")
    lines.append("")
    lines.append(f"**{_fmt_score(result)} ({tier})** · evidence `{env['evidence']['stamp']}` · "
                 f"pages ok: {env['evidence']['pages_ok']} · scoring `{env.get('scoring_version')}` · data `{env.get('data_version')}`")
    lines.append("")
    if env.get("error"):
        err = env["error"]
        lines.append(f"**Error:** {err.get('message')}")
        lines.append("")
        lines.append(f"> {err.get('hint')}")
        return "\n".join(lines) + "\n"

    cats = scores.get("categories") or {}
    if cats:
        lines.append("## Category scores")
        lines.append("")
        lines.append("| Category | Score |")
        lines.append("|----------|-------|")
        for name, val in cats.items():
            lines.append(f"| {name} | {_fmt_score(val)} |")
        lines.append("")

    signals = env.get("signals") or []
    if signals:
        lines.append("## Signals")
        lines.append("")
        lines.append("| Signal | Value | Max | Class | Note |")
        lines.append("|--------|-------|-----|-------|------|")
        for s in signals:
            note = s.get("skipped_reason") or ""
            if not note and isinstance(s.get("detail"), dict):
                note = _detail_note(s["detail"])
            lines.append(f"| {s['id']} | {_num(s.get('value'))} | {s.get('max')} | {s.get('class')} | {note} |")
        lines.append("")

    findings = env.get("findings") or []
    if findings:
        lines.append("## Prioritized findings")
        lines.append("")
        for f in findings:
            pages = f.get("pages") or []
            scope = f"{len(pages)} page(s)" if len(pages) > 1 else (pages[0] if pages else "site")
            lines.append(f"{f['priority']}. **{f['title']}** — {f['severity']}, effort {f['effort']}, "
                         f"~{f['points_lost']} pts · {scope}")
            lines.append(f"   - {f['detail']}")
            if f.get("excerpt"):
                lines.append(f"   - excerpt: `{f['excerpt'][:140]}`")
        lines.append("")

    if env["evidence"].get("pages_failed"):
        lines.append("## Pages that could not be evaluated")
        lines.append("")
        for p in env["evidence"]["pages_failed"]:
            lines.append(f"- {p.get('url')} — {p.get('reason')}")
        lines.append("")

    lines.append(f"_Generated {env.get('generated_at')} by doddle-seo-geo toolkit {env.get('toolkit_version')}._")
    return "\n".join(lines) + "\n"


def _detail_note(detail: Dict[str, Any]) -> str:
    for key in ("ratio", "content_ratio", "word_count", "h1_count", "sections", "candidate_blocks"):
        if key in detail and detail[key] is not None:
            return f"{key}={detail[key]}"
    return ""


def _num(v: Any) -> str:
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:g}"
    return str(v)
