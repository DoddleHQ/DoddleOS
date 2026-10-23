"""``dgtm`` — the deterministic command line for doddle-go-to-market-skills.

Skills call these commands and read the JSON. The CLI computes; the model narrates.

Commands::

    dgtm version
    dgtm frameworks [--name SLUG] [--json]
    dgtm funnel --stage name:count [--stage name:count ...] [--json]
    dgtm unit-economics --cac C --arpa A --gross-margin G --churn R [--json]
    dgtm pricing --price P --variable-cost V [--fixed-cost F] [--tier name:price:cost:mix ...] [--json]
    dgtm size-market --accounts N --acv X [--sam-pct S --som-pct O] [--json]
    dgtm score --criteria name:weight:score [--target T] [--json]
    dgtm audit  <deals.json|csv> [--json]
    dgtm report <deals.json|csv> [--out FILE] [--json]
    dgtm doctor
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_VERSION
from . import calc, frameworks as fw_mod, scoring as scoring_mod
from .envelope import CURRENT, utc_now
from .pipeline import audit_pipeline
from .report import render_markdown


def _emit(obj: Any, as_json: bool) -> None:
    if as_json:
        sys.stdout.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
    else:
        sys.stdout.write(_human(obj) + "\n")


def _base(command: str, target: str) -> Dict[str, Any]:
    return {
        "ok": True, "command": command, "target": target,
        "generated_at": utc_now(), "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION, "data_version": DATA_VERSION,
        "evidence": {"stamp": CURRENT},
    }


def _human(obj: Dict[str, Any]) -> str:
    if obj.get("error"):
        e = obj["error"]
        return f"ERROR: {e.get('message')}\n  hint: {e.get('hint')}"
    command = obj.get("command")
    if command == "report":
        return obj.get("markdown", "")
    if command in ("audit",):
        s = obj.get("scores") or {}
        lines = [f"{command} {obj.get('target')}: {s.get('composite')}/100 ({s.get('tier')}) · "
                 f"evidence {obj.get('evidence', {}).get('stamp')}"]
        for f in (obj.get("findings") or [])[:6]:
            lines.append(f"  #{f['priority']} [{f['severity']}] {f['title']} (~{f['points_lost']} pts)")
        return "\n".join(lines)
    if command == "frameworks":
        rows = obj.get("frameworks") or []
        return "\n".join(f"{r['slug']}: {r['name']} — {r['purpose']}" for r in rows)
    if obj.get("metrics"):
        return f"{command} {obj.get('target')}: " + ", ".join(f"{k}={v}" for k, v in obj["metrics"].items())
    return json.dumps(obj, indent=2, ensure_ascii=False)


def _wants_json(args: argparse.Namespace) -> bool:
    return bool(getattr(args, "json", False)) or not sys.stdout.isatty()


def _num(value: Optional[str]) -> Optional[float]:
    if value in (None, ""):
        return None
    try:
        return float(str(value))
    except ValueError:
        return None


def _pairs(values: Optional[List[str]], arity: int, kw: int = 0) -> List[Dict[str, Any]]:
    """Parse ``name:field:field`` specs into dicts keyed by a fixed field list."""
    keys = ["name", "price", "variable_cost", "mix"][:arity]
    out = []
    for spec in values or []:
        parts = spec.split(":")
        out.append({k: parts[i] if i < len(parts) else None for i, k in enumerate(keys)})
    return out


def cmd_version(args: argparse.Namespace) -> int:
    _emit({
        "toolkit": "doddle-go-to-market",
        "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION,
        "data_version": DATA_VERSION,
        "frameworks": fw_mod.slugs(),
        "python": sys.version.split()[0],
    }, True)
    return 0


def cmd_frameworks(args: argparse.Namespace) -> int:
    if args.name:
        fw = fw_mod.get(args.name)
        if fw is None:
            _emit({"ok": False, "command": "frameworks", "target": args.name, "error": {
                "message": f"unknown framework '{args.name}'",
                "hint": "Known: " + ", ".join(fw_mod.slugs())}}, _wants_json(args))
            return 1
        payload = dict(_base("frameworks", fw["slug"]), frameworks=[fw],
                       registry_version=fw_mod.REGISTRY_VERSION)
    else:
        payload = dict(_base("frameworks", "all"), frameworks=fw_mod.all_frameworks(),
                       registry_version=fw_mod.REGISTRY_VERSION)
    _emit(payload, _wants_json(args))
    return 0


def cmd_funnel(args: argparse.Namespace) -> int:
    stages = []
    for spec in args.stage or []:
        name, _, count = spec.partition(":")
        stages.append({"name": name.strip(), "count": _num(count)})
    if len(stages) < 2:
        _emit({"ok": False, "command": "funnel", "target": "funnel", "error": {
            "message": "need at least two stages",
            "hint": "Pass --stage name:count at least twice, e.g. --stage leads:1000 --stage mql:200"}},
            _wants_json(args))
        return 1
    result = calc.funnel(stages)
    payload = _base("funnel", " -> ".join(s["name"] for s in stages))
    payload["metrics"] = {
        "overall_conversion": result["overall_conversion"],
        "steps": result["steps"],
    }
    payload["notes"] = result["reasons"]
    _emit(payload, _wants_json(args))
    return 0


def cmd_unit_economics(args: argparse.Namespace) -> int:
    result = calc.unit_economics(
        cac=_num(args.cac), arpa=_num(args.arpa),
        gross_margin=_num(args.gross_margin), churn=_num(args.churn))
    payload = _base("unit-economics", "unit-economics")
    payload["metrics"] = {
        "ltv": result["ltv"], "ltv_cac": result["ltv_cac"],
        "cac_payback_months": result["cac_payback_months"],
        "monthly_gross_profit": result["monthly_gross_profit"],
    }
    payload["inputs"] = result["inputs"]
    payload["notes"] = result["notes"] + [f"missing input: {m}" for m in result["missing"]]
    _emit(payload, _wants_json(args))
    return 0


def cmd_pricing(args: argparse.Namespace) -> int:
    tiers = []
    for t in _pairs(args.tier, 4):
        tiers.append({"name": t["name"], "price": _num(t["price"]),
                      "variable_cost": _num(t["variable_cost"]), "mix": _num(t["mix"])})
    result = calc.pricing(price=_num(args.price), variable_cost=_num(args.variable_cost),
                          fixed_cost=_num(args.fixed_cost), tiers=tiers or None)
    payload = _base("pricing", "pricing")
    payload["metrics"] = result
    _emit(payload, _wants_json(args))
    return 0


def cmd_size_market(args: argparse.Namespace) -> int:
    result = calc.size_market(
        total_accounts=_num(args.accounts), acv=_num(args.acv),
        units=_num(args.units), unit_price=_num(args.unit_price),
        sam_pct=_num(args.sam_pct), som_pct=_num(args.som_pct))
    payload = _base("size-market", "size-market")
    payload["metrics"] = {"tam": result["tam"], "sam": result["sam"], "som": result["som"]}
    payload["inputs"] = result["inputs"]
    payload["notes"] = ([result["notes"]] if result["notes"] else []) + \
                       [f"missing input: {m}" for m in result["missing"]]
    _emit(payload, _wants_json(args))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    criteria = []
    for spec in args.criteria or []:
        name, _, rest = spec.partition(":")
        weight, _, score = rest.partition(":")
        criteria.append({"name": name.strip(), "weight": _num(weight), "score": _num(score)})
    if not criteria:
        _emit({"ok": False, "command": "score", "target": args.target or "target", "error": {
            "message": "no criteria provided",
            "hint": "Pass --criteria name:weight:score (repeatable), e.g. --criteria firmographic:0.4:80"}},
            _wants_json(args))
        return 1
    result = scoring_mod.score_attributes(criteria, target=args.target or "target")
    payload = _base("score", result["target"])
    payload["metrics"] = {"composite": result["composite"], "coverage": result["coverage"]}
    payload["criteria"] = result["criteria"]
    payload["notes"] = [f"unmeasured criterion: {m}" for m in result["missing"]]
    _emit(payload, _wants_json(args))
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    env = audit_pipeline(args.export)
    _emit(env, _wants_json(args))
    return 0 if env["ok"] else 1


def cmd_report(args: argparse.Namespace) -> int:
    env = audit_pipeline(args.export)
    env["command"] = "report"
    env["markdown"] = render_markdown(env)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(env["markdown"])
    _emit(env, _wants_json(args))
    return 0 if env["ok"] else 1


def cmd_doctor(args: argparse.Namespace) -> int:
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 9), "detail": sys.version.split()[0]},
        {"name": "toolkit_import", "ok": True, "detail": TOOLKIT_VERSION},
        {"name": "frameworks", "ok": len(fw_mod.slugs()) >= 1, "detail": f"{len(fw_mod.slugs())} registered"},
        {"name": "stdout_tty", "ok": True, "detail": str(sys.stdout.isatty())},
    ]
    ok = all(c["ok"] for c in checks)
    _emit({"ok": ok, "command": "doctor", "checks": checks}, True)
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="force JSON output")

    p = argparse.ArgumentParser(prog="dgtm", description="Doddle Go-To-Market deterministic toolkit")
    p.add_argument("--version", action="store_true", help="print toolkit version and exit")
    sub = p.add_subparsers(dest="subcommand")

    sp = sub.add_parser("version", help="print versions")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_version)

    sp = sub.add_parser("frameworks", parents=[common], help="the GTM framework registry")
    sp.add_argument("--name", help="one framework slug")
    sp.set_defaults(func=cmd_frameworks)

    sp = sub.add_parser("funnel", parents=[common], help="stage-to-stage conversion")
    sp.add_argument("--stage", action="append", required=True, help="name:count (repeatable)")
    sp.set_defaults(func=cmd_funnel)

    sp = sub.add_parser("unit-economics", parents=[common], help="LTV, LTV:CAC, payback")
    sp.add_argument("--cac")
    sp.add_argument("--arpa", help="average revenue per account, monthly")
    sp.add_argument("--gross-margin", dest="gross_margin", help="fraction 0..1")
    sp.add_argument("--churn", help="monthly churn rate 0..1")
    sp.set_defaults(func=cmd_unit_economics)

    sp = sub.add_parser("pricing", parents=[common], help="margin and break-even")
    sp.add_argument("--price")
    sp.add_argument("--variable-cost", dest="variable_cost")
    sp.add_argument("--fixed-cost", dest="fixed_cost")
    sp.add_argument("--tier", action="append", help="name:price:cost:mix (repeatable)")
    sp.set_defaults(func=cmd_pricing)

    sp = sub.add_parser("size-market", parents=[common], help="bottom-up TAM/SAM/SOM")
    sp.add_argument("--accounts")
    sp.add_argument("--acv", help="annual contract value")
    sp.add_argument("--units")
    sp.add_argument("--unit-price", dest="unit_price")
    sp.add_argument("--sam-pct", dest="sam_pct")
    sp.add_argument("--som-pct", dest="som_pct")
    sp.set_defaults(func=cmd_size_market)

    sp = sub.add_parser("score", parents=[common], help="weighted ICP/account scoring")
    sp.add_argument("--criteria", action="append", help="name:weight:score (repeatable)")
    sp.add_argument("--target", help="name of the account/ICP being scored")
    sp.set_defaults(func=cmd_score)

    sp = sub.add_parser("audit", parents=[common], help="audit a deals/pipeline export (JSON/CSV)")
    sp.add_argument("export")
    sp.set_defaults(func=cmd_audit)

    sp = sub.add_parser("report", parents=[common], help="audit an export and render markdown")
    sp.add_argument("export")
    sp.add_argument("--out")
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
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
