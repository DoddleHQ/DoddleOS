"""Toolkit tests: the calculators, scoring, pipeline audit, frameworks and the CLI."""

import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from doddle_gtm import calc, frameworks, scoring  # noqa: E402
from doddle_gtm.pipeline import audit_pipeline  # noqa: E402

DEALS = os.path.join(ROOT, "tests", "fixtures", "deals.json")
INCOMPLETE = os.path.join(ROOT, "tests", "fixtures", "deals_incomplete.json")
CLI = os.path.join(ROOT, "scripts", "dgtm")


def test_funnel_conversions():
    r = calc.funnel([{"name": "leads", "count": 1000}, {"name": "mql", "count": 200},
                     {"name": "won", "count": 20}])
    assert r["steps"][0]["conversion"] == pytest.approx(0.2)
    assert r["overall_conversion"] == pytest.approx(0.02)


def test_funnel_zero_stage_is_null_not_zero():
    r = calc.funnel([{"name": "a", "count": 0}, {"name": "b", "count": 10}])
    assert r["steps"][0]["conversion"] is None
    assert r["reasons"]


def test_unit_economics():
    r = calc.unit_economics(cac=400, arpa=100, gross_margin=0.8, churn=0.03)
    assert r["monthly_gross_profit"] == pytest.approx(80.0)
    assert r["ltv"] == pytest.approx(2666.67, rel=1e-3)
    assert r["cac_payback_months"] == pytest.approx(5.0)
    assert r["ltv_cac"] == pytest.approx(6.67, rel=1e-2)


def test_unit_economics_zero_churn_is_undefined():
    r = calc.unit_economics(cac=400, arpa=100, gross_margin=0.8, churn=0)
    assert r["ltv"] is None
    assert any("undefined" in n for n in r["notes"])


def test_pricing_single_and_tiers():
    r = calc.pricing(price=99, variable_cost=20, fixed_cost=50000,
                     tiers=[{"name": "A", "price": 49, "variable_cost": 10, "mix": 0.6},
                            {"name": "B", "price": 99, "variable_cost": 20, "mix": 0.4}])
    assert r["single"]["gross_margin"] == pytest.approx(0.798, rel=1e-3)
    assert r["single"]["breakeven_units"] == pytest.approx(632.9, rel=1e-2)
    assert r["tiers"]["blended_price"] == pytest.approx(69.0)
    assert r["tiers"]["blended_price_margin"] == pytest.approx(0.7971, rel=1e-3)


def test_size_market_bottom_up():
    r = calc.size_market(total_accounts=50000, acv=6000, sam_pct=0.2, som_pct=0.05)
    assert r["tam"] == 300_000_000
    assert r["sam"] == 60_000_000
    assert r["som"] == 3_000_000


def test_size_market_missing_is_null_with_reason():
    r = calc.size_market(total_accounts=1000)
    assert r["tam"] is None
    assert "acv/unit_price" in r["missing"]


def test_scoring_weighted_and_coverage():
    r = scoring.score_attributes([
        {"name": "fit", "weight": 0.5, "score": 80},
        {"name": "intent", "weight": 0.5, "score": 60},
        {"name": "tech", "weight": 0.5, "score": None},
    ])
    assert r["composite"] == pytest.approx(70.0)
    assert r["coverage"] < 1.0
    assert "tech" in r["missing"]


def test_audit_pipeline_signals():
    env = audit_pipeline(DEALS)
    assert env["ok"] is True
    ids = {s["id"] for s in env["signals"]}
    assert {"pipeline.win_rate", "pipeline.cycle_time", "pipeline.data_completeness"} <= ids
    assert env["scores"]["composite"] is not None
    assert env["totals"]["open_deals"] == 7


def test_audit_incomplete_marks_missing():
    env = audit_pipeline(INCOMPLETE)
    assert env["ok"] is True
    assert "pipeline.win_rate" in env["completeness"]["missing"]
    assert any(f["id"] == "pipeline.data_completeness" for f in env["findings"])


def test_audit_unreadable_file_is_error_envelope():
    env = audit_pipeline(os.path.join(ROOT, "does-not-exist.json"))
    assert env["ok"] is False
    assert env["error"]["hint"]


def test_audit_is_deterministic():
    a, b = audit_pipeline(DEALS), audit_pipeline(DEALS)
    a.pop("generated_at"), b.pop("generated_at")
    assert a == b


def test_frameworks_registry():
    assert "battlecard" in frameworks.slugs()
    assert frameworks.get("battlecard")["sections"]
    assert frameworks.get("nope") is None


@pytest.mark.parametrize("args,expect", [
    (["version"], "toolkit_version"),
    (["doctor"], "checks"),
    (["frameworks"], "frameworks"),
    (["funnel", "--stage", "a:100", "--stage", "b:50"], "metrics"),
    (["unit-economics", "--cac", "400", "--arpa", "100", "--gross-margin", "0.8", "--churn", "0.03"], "metrics"),
    (["size-market", "--accounts", "10", "--acv", "1000"], "metrics"),
    (["score", "--criteria", "fit:0.5:80"], "metrics"),
    (["audit", DEALS], "signals"),
])
def test_cli_commands_emit_envelopes(args, expect):
    out = subprocess.run([sys.executable, CLI, *args], capture_output=True, text=True, check=True)
    payload = json.loads(out.stdout)
    assert expect in payload
