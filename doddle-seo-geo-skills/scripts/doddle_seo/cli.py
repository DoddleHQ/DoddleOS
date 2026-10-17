"""``dseo`` — the deterministic command line for doddle-seo-geo-skills.

Skills call these commands and read the JSON. The CLI computes; the model narrates.

Commands::

    dseo version
    dseo score   <url|file>   [--json] [--allow-private]
    dseo audit   <url>        [--json] [--max-pages N] [--rate R]
    dseo citability <url|file> [--json]
    dseo technical  <url|file> [--json]
    dseo schema  <url|file>   [--json]
    dseo robots  <url|file>   [--json]
    dseo llmstxt <url|file>   [--json] [--generate]
    dseo report  <url>        [--json]
    dseo doctor
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from . import llmstxt as llmstxt_mod
from . import robots as robots_mod
from . import schema as schema_mod
from .audit import audit_site
from .envelope import CURRENT, make_envelope, tier_for, utc_now
from .fetch import fetch
from .htmlparse import parse
from .report import render_markdown
from .scoring import analyze_page, score_to_envelope


def _emit(obj: Any, as_json: bool) -> None:
    if as_json:
        sys.stdout.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    else:
        sys.stdout.write(_human(obj) + "\n")


def _human(obj: Dict[str, Any]) -> str:
    if obj.get("command") in ("score", "audit", "report") and not obj.get("error"):
        if obj["command"] == "report":
            return obj.get("markdown", "")
        s = obj.get("scores") or {}
        head = f"{obj.get('command')} {obj.get('target')}: {s.get('composite')}/100 ({s.get('tier')}) · evidence {obj['evidence']['stamp']}"
        lines = [head]
        for name, val in (s.get("categories") or {}).items():
            lines.append(f"  {name}: {val}/100")
        for f in (obj.get("findings") or [])[:5]:
            lines.append(f"  #{f['priority']} [{f['severity']}] {f['title']} (~{f['points_lost']} pts)")
        return "\n".join(lines)
    if obj.get("error"):
        e = obj["error"]
        return f"ERROR: {e.get('message')}\n  hint: {e.get('hint')}"
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _wants_json(args: argparse.Namespace) -> bool:
    return bool(getattr(args, "json", False)) or not sys.stdout.isatty()


def cmd_version(args: argparse.Namespace) -> int:
    payload = {
        "toolkit": "doddle-seo-geo",
        "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION,
        "data_version": DATA_VERSION,
        "python": sys.version.split()[0],
    }
    _emit(payload, _wants_json(args) or args.subcommand == "version")
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    env = score_to_envelope(args.target, allow_private=args.allow_private, timeout=args.timeout)
    _emit(env, _wants_json(args))
    return 0 if env["ok"] else 1


def cmd_audit(args: argparse.Namespace) -> int:
    env = audit_site(args.target, max_pages=args.max_pages, rate=args.rate,
                     allow_private=args.allow_private, timeout=args.timeout)
    _emit(env, _wants_json(args))
    return 0 if env["ok"] else 1


def cmd_citability(args: argparse.Namespace) -> int:
    report = analyze_page(args.target, allow_private=args.allow_private, timeout=args.timeout)
    if not report.ok:
        _emit({"ok": False, "command": "citability", "target": args.target,
               "error": {"message": report.error, "hint": "check the URL/file"}}, _wants_json(args))
        return 1
    cites = [s.to_dict() for s in report.signals if s.id.startswith("citability.")]
    composite = report.categories.get("citability")
    measured = [s for s in cites if s["value"] is not None]
    env = make_envelope(
        "citability", args.target,
        toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
        signal_count=len(measured), signal_total=len(cites), missing=report.missing,
        scores={"composite": composite, "tier": tier_for(composite)},
        signals=[s for s in report.signals if s.id.startswith("citability.")],
        findings=[f for f in report.findings if f.id.startswith("citability.")],
    )
    _emit(env, _wants_json(args))
    return 0


def cmd_technical(args: argparse.Namespace) -> int:
    report = analyze_page(args.target, allow_private=args.allow_private, timeout=args.timeout)
    if not report.ok:
        _emit({"ok": False, "command": "technical", "target": args.target,
               "error": {"message": report.error, "hint": "check the URL/file"}}, _wants_json(args))
        return 1
    env = make_envelope(
        "technical", args.target,
        toolkit_version=TOOLKIT_VERSION, scoring_version=SCORING_VERSION, data_version=DATA_VERSION,
        scores={"composite": report.categories.get("technical"), "tier": tier_for(report.categories.get("technical")),
                "categories": {"technical": report.categories.get("technical")}},
        signals=[s for s in report.signals if s.id.startswith("technical.")],
        findings=[f for f in report.findings if f.id.startswith("tech.")],
    )
    _emit(env, _wants_json(args))
    return 0


def _load_target_text(target: str, allow_private: bool, timeout: float) -> Dict[str, Any]:
    """Fetch target, or if it looks like robots.txt/llms.txt directly, use the root."""
    parsed = urlparse(target)
    if parsed.scheme in ("http", "https"):
        if target.endswith(".txt") or target.endswith(".xml"):
            f = fetch(target, allow_private=allow_private, timeout=timeout)
            return {"text": f.body, "url": target, "ok": f.ok, "error": f.error}
        root = f"{parsed.scheme}://{parsed.netloc}"
        return {"root": root}
    # local file
    f = fetch(target, allow_private=allow_private, timeout=timeout)
    return {"text": f.body, "url": target, "ok": f.ok, "error": f.error}


def cmd_robots(args: argparse.Namespace) -> int:
    loaded = _load_target_text(args.target, args.allow_private, args.timeout)
    if "text" in loaded:
        text, url = loaded["text"], loaded["url"]
    else:
        url = f"{loaded['root']}/robots.txt"
        f = fetch(url, allow_private=args.allow_private, timeout=args.timeout)
        text = f.body
    data = robots_mod.evaluate(text, base_path="/")
    env = {
        "ok": True, "command": "robots", "target": url, "generated_at": utc_now(),
        "toolkit_version": TOOLKIT_VERSION, "data_version": DATA_VERSION,
        "evidence": {"stamp": CURRENT},
        "robots": data,
        "summary": f"{data['blocked_count']} of {len(data['crawlers'])} AI crawlers blocked"
                   + (f"; search crawlers blocked: {', '.join(data['blocked_search'])}" if data["blocked_search"] else ""),
    }
    _emit(env, _wants_json(args))
    return 0


def cmd_schema(args: argparse.Namespace) -> int:
    parsed = urlparse(args.target)
    if parsed.scheme in ("http", "https") and not parsed.path.lower().endswith((".html", ".htm")):
        report = analyze_page(args.target, allow_private=args.allow_private, timeout=args.timeout)
        if not report.ok:
            _emit({"ok": False, "command": "schema", "target": args.target,
                   "error": {"message": report.error, "hint": "check the URL/file"}}, _wants_json(args))
            return 1
        page = report.page
    else:
        f = fetch(args.target, allow_private=args.allow_private, timeout=args.timeout)
        if not f.ok and not f.body:
            _emit({"ok": False, "command": "schema", "target": args.target,
                   "error": {"message": f.error, "hint": "check the URL/file"}}, _wants_json(args))
            return 1
        page = parse(f.body, base_url=args.target)
    result = schema_mod.analyze(page.jsonld)
    env = {
        "ok": True, "command": "schema", "target": args.target, "generated_at": utc_now(),
        "toolkit_version": TOOLKIT_VERSION, "scoring_version": SCORING_VERSION, "data_version": DATA_VERSION,
        "evidence": {"stamp": CURRENT},
        "schema": schema_mod.signals(result),
        "summary": _schema_summary(result),
    }
    _emit(env, _wants_json(args))
    return 0


def _schema_summary(result: schema_mod.SchemaReport) -> str:
    if not result.present:
        return "No JSON-LD structured data found."
    parts = [f"{result.node_count} node(s): {', '.join(result.types) or 'no typed nodes'}"]
    if result.errors:
        parts.append(f"{len(result.errors)} error(s)")
    if result.same_as:
        parts.append(f"{len(result.same_as)} sameAs link(s)")
    return "; ".join(parts)


def cmd_llmstxt(args: argparse.Namespace) -> int:
    parsed = urlparse(args.target)
    if parsed.scheme in ("http", "https"):
        root = f"{parsed.scheme}://{parsed.netloc}"
        url = f"{root}/llms.txt"
        f = fetch(url, allow_private=args.allow_private, timeout=args.timeout)
        text = f.body if f.status and f.status < 400 else ""
    else:
        f = fetch(args.target, allow_private=args.allow_private, timeout=args.timeout)
        text = f.body
        root = ""
    doc = llmstxt_mod.parse(text)
    payload: Dict[str, Any] = {
        "ok": True, "command": "llmstxt", "target": args.target, "generated_at": utc_now(),
        "toolkit_version": TOOLKIT_VERSION, "data_version": DATA_VERSION,
        "evidence": {"stamp": CURRENT},
        "llmstxt": llmstxt_mod.stats(doc),
        "summary": ("llms.txt present: " + f"{doc.link_count} link(s), {len(doc.sections)} section(s)")
        if doc.present else "No llms.txt found at /llms.txt.",
    }
    if args.generate and root:
        pages = _draft_pages(root, args)
        payload["generated"] = llmstxt_mod.build_from_pages(parsed.netloc, "", pages)
    _emit(payload, _wants_json(args))
    return 0


def _draft_pages(root: str, args: argparse.Namespace) -> List[Dict[str, str]]:
    from .audit import discover

    pages: List[Dict[str, str]] = []
    for url in discover(root, max_pages=args.max_pages, allow_private=args.allow_private, timeout=args.timeout)[: args.max_pages]:
        f = fetch(url, allow_private=args.allow_private, timeout=args.timeout)
        if not f.ok:
            continue
        p = parse(f.body, base_url=url)
        pages.append({"url": url, "title": p.title or url, "description": p.meta_description, "section": "Pages"})
    return pages


def cmd_report(args: argparse.Namespace) -> int:
    env = audit_site(args.target, max_pages=args.max_pages, rate=args.rate,
                     allow_private=args.allow_private, timeout=args.timeout)
    env["command"] = "report"
    env["markdown"] = render_markdown(env)
    _emit(env, _wants_json(args))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(env["markdown"])
    return 0 if env["ok"] else 1


def cmd_doctor(args: argparse.Namespace) -> int:
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 9), "detail": sys.version.split()[0]},
        {"name": "toolkit_import", "ok": True, "detail": TOOLKIT_VERSION},
        {"name": "stdout_tty", "ok": True, "detail": str(sys.stdout.isatty())},
    ]
    ok = all(c["ok"] for c in checks)
    _emit({"ok": ok, "command": "doctor", "checks": checks}, _wants_json(args) or True)
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("target", nargs="?", help="URL or local file path")
    common.add_argument("--json", action="store_true", help="force JSON output")
    common.add_argument("--allow-private", action="store_true", help="allow localhost/staging hosts")
    common.add_argument("--timeout", type=float, default=20.0, help="per-request timeout seconds")

    p = argparse.ArgumentParser(prog="dseo", description="Doddle SEO & GEO deterministic toolkit")
    p.add_argument("--version", action="store_true", help="print toolkit version and exit")
    sub = p.add_subparsers(dest="subcommand")

    sp = sub.add_parser("version", help="print versions")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_version)

    sp = sub.add_parser("score", parents=[common], help="score one page (citability + foundations)")
    sp.set_defaults(func=cmd_score)

    sp = sub.add_parser("audit", parents=[common], help="crawl and score a site")
    sp.add_argument("--max-pages", type=int, default=50)
    sp.add_argument("--rate", type=float, default=1.0, help="seconds between requests")
    sp.set_defaults(func=cmd_audit)

    sp = sub.add_parser("citability", parents=[common], help="citability signals for one page")
    sp.set_defaults(func=cmd_citability)

    sp = sub.add_parser("technical", parents=[common], help="technical signals for one page")
    sp.set_defaults(func=cmd_technical)

    sp = sub.add_parser("schema", parents=[common], help="JSON-LD analysis for one page")
    sp.set_defaults(func=cmd_schema)

    sp = sub.add_parser("robots", parents=[common], help="AI-crawler access from robots.txt")
    sp.set_defaults(func=cmd_robots)

    sp = sub.add_parser("llmstxt", parents=[common], help="analyze or generate llms.txt")
    sp.add_argument("--generate", action="store_true", help="draft an llms.txt from the site")
    sp.add_argument("--max-pages", type=int, default=20)
    sp.set_defaults(func=cmd_llmstxt)

    sp = sub.add_parser("report", parents=[common], help="audit a site and render a markdown report")
    sp.add_argument("--max-pages", type=int, default=50)
    sp.add_argument("--rate", type=float, default=1.0)
    sp.add_argument("--out", help="write the markdown report to this path")
    sp.set_defaults(func=cmd_report)

    sp = sub.add_parser("doctor", help="check the environment")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_doctor)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "version", False):
        return cmd_version(argparse.Namespace(subcommand="version", json=True))
    if not getattr(args, "func", None):
        parser.print_help()
        return 0
    if args.subcommand != "doctor" and getattr(args, "func", None) not in (cmd_version,) and getattr(args, "target", None) is None:
        parser.error(f"'{args.subcommand}' requires a target")
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
