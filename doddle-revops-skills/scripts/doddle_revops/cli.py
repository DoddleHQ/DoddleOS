"""``drev`` — deterministic, read-only revenue-operations commands."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_NAME, TOOLKIT_VERSION
from .attribution import MODELS, attribute_revenue
from .cohorts import analyze_cohorts
from .data_infrastructure import profile_data_infrastructure
from .envelope import make_envelope
from .pql import score_pql


def _emit(obj: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def cmd_version(_: argparse.Namespace) -> int:
    _emit({
        "ok": True,
        "tool": TOOLKIT_NAME,
        "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION,
        "data_version": DATA_VERSION,
        "commands": ["data-profile", "pql", "attribution", "cohorts", "doctor"],
    })
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 9), "detail": sys.version.split()[0]},
        {"name": "stdlib_only", "ok": True, "detail": "no third-party runtime dependencies"},
        {"name": "commands", "ok": True, "detail": "data-profile,pql,attribution,cohorts"},
    ]
    _emit(make_envelope("doctor", "environment", metrics={"checks": checks, "healthy": all(c["ok"] for c in checks)}))
    return 0


def cmd_data_profile(args: argparse.Namespace) -> int:
    env = profile_data_infrastructure(
        warehouse_export=args.warehouse_export,
        dbt_manifest=args.dbt_manifest,
        identity_map=args.identity_map,
        reverse_etl_config=args.reverse_etl_config,
        max_age_days=args.max_age_days,
    )
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_pql(args: argparse.Namespace) -> int:
    env = score_pql(events_path=args.events, accounts_path=args.accounts, model_path=args.model)
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_attribution(args: argparse.Namespace) -> int:
    env = attribute_revenue(
        touchpoints_path=args.touchpoints,
        deals_path=args.deals,
        model=args.model,
        window_days=args.window_days,
        half_life_days=args.half_life_days,
    )
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_cohorts(args: argparse.Namespace) -> int:
    env = analyze_cohorts(args.input, max_periods=args.max_periods)
    _emit(env)
    return 0 if env["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="drev", description="Doddle RevOps deterministic toolkit")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("version").set_defaults(func=cmd_version)
    sub.add_parser("doctor").set_defaults(func=cmd_doctor)

    p = sub.add_parser("data-profile", help="profile warehouse/dbt/identity/reverse-ETL readiness")
    p.add_argument("--warehouse-export", required=True)
    p.add_argument("--dbt-manifest")
    p.add_argument("--identity-map")
    p.add_argument("--reverse-etl-config")
    p.add_argument("--max-age-days", type=int, default=30)
    p.set_defaults(func=cmd_data_profile)

    p = sub.add_parser("pql", help="score product-qualified leads from exported events")
    p.add_argument("--events", required=True)
    p.add_argument("--accounts", required=True)
    p.add_argument("--model", required=True)
    p.set_defaults(func=cmd_pql)

    p = sub.add_parser("attribution", help="allocate won revenue across touchpoints")
    p.add_argument("--touchpoints", required=True)
    p.add_argument("--deals", required=True)
    p.add_argument("--model", choices=sorted(MODELS), default="linear")
    p.add_argument("--window-days", type=int, default=90)
    p.add_argument("--half-life-days", type=float, default=7.0)
    p.set_defaults(func=cmd_attribution)

    p = sub.add_parser("cohorts", help="build logo/revenue retention matrices")
    p.add_argument("input")
    p.add_argument("--max-periods", type=int, default=12)
    p.set_defaults(func=cmd_cohorts)
    return parser


def main(argv: Optional[list] = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
