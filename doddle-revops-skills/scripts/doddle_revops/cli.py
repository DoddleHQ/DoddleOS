"""``drev`` — deterministic, read-only revenue-operations commands."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from typing import Any, Dict, Optional

from . import DATA_VERSION, SCORING_VERSION, TOOLKIT_NAME, TOOLKIT_VERSION
from .attribution import MODELS, attribute_revenue
from .call_intel import search_calls
from .cohorts import analyze_cohorts
from .data_infrastructure import profile_data_infrastructure
from .envelope import make_envelope
from .integrations import audit_integrations
from .metering import meter_usage
from .pql import score_pql
from .portfolio import build_portfolio
from .qbr import build_qbr, render_qbr_markdown
from .retention import analyze_retention
from .sdr import validate_sdr_claims
from .signals import community_attribution, route_signals

COMMANDS = [
    "data-profile", "pql", "attribution", "cohorts",
    "route-signals", "sdr-validate", "meter", "call-search", "retention",
    "integration-audit", "qbr", "community-attribution", "portfolio",
    "doctor", "version",
]


def _parse_now(value: Optional[str]) -> Optional[dt.datetime]:
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def _emit(obj: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def cmd_version(_: argparse.Namespace) -> int:
    _emit({
        "ok": True,
        "tool": TOOLKIT_NAME,
        "toolkit_version": TOOLKIT_VERSION,
        "scoring_version": SCORING_VERSION,
        "data_version": DATA_VERSION,
        "commands": COMMANDS,
    })
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    checks = [
        {"name": "python", "ok": sys.version_info >= (3, 9), "detail": sys.version.split()[0]},
        {"name": "stdlib_only", "ok": True, "detail": "no third-party runtime dependencies"},
        {"name": "commands", "ok": True, "detail": f"{len(COMMANDS)} commands registered"},
        {"name": "read_only", "ok": True, "detail": "no command writes to a system of record"},
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


def cmd_route_signals(args: argparse.Namespace) -> int:
    env = route_signals(events_path=args.events, rules_path=args.rules, now=_parse_now(args.now))
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_sdr_validate(args: argparse.Namespace) -> int:
    env = validate_sdr_claims(account_path=args.account, evidence_path=args.evidence)
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_meter(args: argparse.Namespace) -> int:
    env = meter_usage(usage_path=args.usage, plan_path=args.plan)
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_call_search(args: argparse.Namespace) -> int:
    env = search_calls(
        transcripts_path=args.transcripts,
        query=args.query,
        themes_path=args.themes,
        limit=args.limit,
    )
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_retention(args: argparse.Namespace) -> int:
    env = analyze_retention(
        customers_path=args.customers,
        usage_path=args.usage,
        renewal_window_days=args.renewal_window_days,
        dropoff_threshold=args.dropoff_threshold,
        now=_parse_now(args.now),
    )
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_integration_audit(args: argparse.Namespace) -> int:
    env = audit_integrations(catalog_path=args.catalog)
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_qbr(args: argparse.Namespace) -> int:
    env = build_qbr(account_path=args.account)
    if env["ok"] and args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(render_qbr_markdown(env))
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_community_attribution(args: argparse.Namespace) -> int:
    env = community_attribution(
        community_path=args.community,
        surveys_path=args.surveys,
        deals_path=args.deals,
        min_sample=args.min_sample,
    )
    _emit(env)
    return 0 if env["ok"] else 1


def cmd_portfolio(args: argparse.Namespace) -> int:
    env = build_portfolio(companies_path=args.companies, observations_path=args.observations, now=_parse_now(args.now))
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

    p = sub.add_parser("route-signals", help="route buyer signals to owners (dry-run)")
    p.add_argument("--events", required=True)
    p.add_argument("--rules", required=True)
    p.add_argument("--now", help="Override the reference time (ISO-8601) for deterministic windows")
    p.set_defaults(func=cmd_route_signals)

    p = sub.add_parser("sdr-validate", help="check every personalization claim against evidence")
    p.add_argument("--account", required=True)
    p.add_argument("--evidence", required=True)
    p.set_defaults(func=cmd_sdr_validate)

    p = sub.add_parser("meter", help="rate usage, consume credits, preview an invoice")
    p.add_argument("--usage", required=True)
    p.add_argument("--plan", required=True)
    p.set_defaults(func=cmd_meter)

    p = sub.add_parser("call-search", help="search call transcripts for themes and coaching flags")
    p.add_argument("--transcripts", required=True)
    p.add_argument("--query", required=True)
    p.add_argument("--themes")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_call_search)

    p = sub.add_parser("retention", help="compute NRR/GRR, health, renewal risk, expansion signals")
    p.add_argument("--customers", required=True)
    p.add_argument("--usage", required=True)
    p.add_argument("--renewal-window-days", type=int, default=90)
    p.add_argument("--dropoff-threshold", type=float, default=0.20)
    p.add_argument("--now", help="Override the reference time (ISO-8601) for deterministic windows")
    p.set_defaults(func=cmd_retention)

    p = sub.add_parser("integration-audit", help="audit integration-led growth readiness")
    p.add_argument("--catalog", required=True)
    p.set_defaults(func=cmd_integration_audit)

    p = sub.add_parser("qbr", help="build the QBR pack and CSM deck outline")
    p.add_argument("--account", required=True)
    p.add_argument("--out")
    p.set_defaults(func=cmd_qbr)

    p = sub.add_parser("community-attribution", help="model community and dark-social attribution")
    p.add_argument("--community", required=True)
    p.add_argument("--surveys", required=True)
    p.add_argument("--deals", required=True)
    p.add_argument("--min-sample", type=int, default=30)
    p.set_defaults(func=cmd_community_attribution)

    p = sub.add_parser("portfolio", help="normalize a public pricing/teardown portfolio")
    p.add_argument("--companies", required=True)
    p.add_argument("--observations", required=True)
    p.add_argument("--now", help="Override the reference time (ISO-8601) for deterministic windows")
    p.set_defaults(func=cmd_portfolio)
    return parser


def main(argv: Optional[list] = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
