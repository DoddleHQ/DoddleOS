"""Toolkit tests: the calculators, scoring, pipeline audit, frameworks and the CLI."""

import datetime
import json
import os
import shutil
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
NOW = datetime.datetime(2026, 11, 26, tzinfo=datetime.timezone.utc)


def _export_with_age(tmp_path, age_days, *, source=DEALS):
    path = tmp_path / "deals.json"
    shutil.copyfile(source, path)
    modified = NOW.timestamp() - age_days * 86400
    os.utime(path, (modified, modified))
    return str(path)


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


def test_pricing_tier_only_does_not_require_single_plan_inputs():
    r = calc.pricing(
        tiers=[{"name": "A", "price": 49, "variable_cost": 10, "mix": 0.6},
               {"name": "B", "price": 99, "variable_cost": 20, "mix": 0.4}],
    )
    assert r["single"] is None
    assert r["missing"] == []
    assert r["tiers"]["blended_price"] == pytest.approx(69.0)
    assert r["tiers"]["blended_price_margin"] == pytest.approx(0.7971, rel=1e-3)


def test_pricing_tiers_with_partial_single_input_still_reports_single_gap():
    r = calc.pricing(
        price=99, variable_cost=None,
        tiers=[{"name": "A", "price": 49, "variable_cost": 10, "mix": 1}],
    )
    assert r["single"] is None
    assert r["missing"] == ["variable_cost"]


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


@pytest.mark.parametrize("age_days,max_age_days,expected", [
    (1, 30, "CURRENT"),
    (30, 30, "CURRENT"),
    (31, 30, "STALE"),
    (10, 5, "STALE"),
])
def test_audit_export_mtime_freshness(tmp_path, age_days, max_age_days, expected):
    path = _export_with_age(tmp_path, age_days)
    env = audit_pipeline(path, max_age_days=max_age_days, now=NOW)
    assert env["ok"] is True
    assert env["evidence"]["stamp"] == expected
    assert env["evidence"]["export"]["age_days"] == pytest.approx(age_days)
    assert env["evidence"]["export"]["max_age_days"] == max_age_days
    assert env["evidence"]["export"]["modified_at"]
    if expected == "STALE":
        assert any(note.startswith("STALE:") for note in env["evidence"]["notes"])


def test_old_empty_export_is_not_current(tmp_path):
    empty = tmp_path / "empty.json"
    empty.write_text("[]", encoding="utf-8")
    path = _export_with_age(tmp_path, 31, source=str(empty))
    env = audit_pipeline(path, now=NOW)
    assert env["ok"] is False
    assert env["evidence"]["stamp"] == "STALE"


def test_audit_segment_filter_is_case_insensitive():
    env = audit_pipeline(DEALS, segment=" SMB ")
    assert env["ok"] is True
    assert env["filters"] == {"segment": "SMB"}
    assert env["totals"] == {
        "deals": 7, "open_deals": 4, "open_pipeline_value": 18300.0,
    }
    assert "[segment=SMB]" in env["target"]


def test_audit_segment_filter_no_match_is_error():
    env = audit_pipeline(DEALS, segment="enterprise")
    assert env["ok"] is False
    assert "no deals match segment" in env["error"]["message"]
    assert "segment" in env["error"]["hint"]


def test_audit_segment_filter_csv(tmp_path):
    path = tmp_path / "deals.csv"
    path.write_text(
        "stage,amount,created_at,outcome,segment\n"
        "Discovery,100,2026-01-01,open,SMB\n"
        "Demo,200,2026-01-02,open,mid\n",
        encoding="utf-8",
    )
    env = audit_pipeline(str(path), segment="smb")
    assert env["ok"] is True
    assert env["totals"]["deals"] == 1
    assert env["totals"]["open_pipeline_value"] == 100.0


def test_audit_unreadable_file_is_error_envelope():
    env = audit_pipeline(os.path.join(ROOT, "does-not-exist.json"))
    assert env["ok"] is False
    assert env["evidence"]["stamp"] == "PARTIAL"
    assert env["evidence"]["export"]["modified_at"] is None
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


def test_cli_pricing_tier_only():
    out = subprocess.run([
        sys.executable, CLI, "pricing",
        "--tier", "A:49:10:0.6", "--tier", "B:99:20:0.4", "--json",
    ], capture_output=True, text=True, check=True)
    metrics = json.loads(out.stdout)["metrics"]
    assert metrics["single"] is None
    assert metrics["missing"] == []
    assert metrics["tiers"]["blended_price"] == pytest.approx(69.0)


def test_cli_audit_default_and_custom_freshness_limits(tmp_path):
    path = _export_with_age(tmp_path, 31)
    default = subprocess.run(
        [sys.executable, CLI, "audit", path, "--json"],
        capture_output=True, text=True, check=True)
    assert json.loads(default.stdout)["evidence"]["stamp"] == "STALE"

    relaxed = subprocess.run(
        [sys.executable, CLI, "audit", path, "--max-age-days", "60", "--json"],
        capture_output=True, text=True, check=True)
    payload = json.loads(relaxed.stdout)
    assert payload["evidence"]["stamp"] == "CURRENT"
    assert payload["evidence"]["export"]["max_age_days"] == 60.0


def test_cli_report_keeps_stale_stamp_in_markdown(tmp_path):
    path = _export_with_age(tmp_path, 31)
    out = subprocess.run(
        [sys.executable, CLI, "report", path, "--json"],
        capture_output=True, text=True, check=True)
    payload = json.loads(out.stdout)
    assert payload["evidence"]["stamp"] == "STALE"
    assert "evidence `STALE`" in payload["markdown"]


@pytest.mark.parametrize("value", ["-1", "nan", "inf", "not-a-number"])
def test_cli_rejects_invalid_max_age_days(value):
    out = subprocess.run(
        [sys.executable, CLI, "audit", DEALS, "--max-age-days", value],
        capture_output=True, text=True)
    assert out.returncode == 2
    assert "finite, non-negative" in out.stderr or "must be a number" in out.stderr


@pytest.mark.parametrize("command", ["audit", "report"])
def test_cli_segment_filter(command):
    out = subprocess.run([
        sys.executable, CLI, command, DEALS, "--segment", "smb", "--json",
    ], capture_output=True, text=True, check=True)
    payload = json.loads(out.stdout)
    assert payload["filters"] == {"segment": "smb"}
    assert payload["totals"]["deals"] == 7
    assert payload["totals"]["open_deals"] == 4


def test_cli_segment_filter_no_match_exits_one():
    out = subprocess.run([
        sys.executable, CLI, "audit", DEALS, "--segment", "enterprise", "--json",
    ], capture_output=True, text=True)
    assert out.returncode == 1
    payload = json.loads(out.stdout)
    assert payload["ok"] is False
    assert "no deals match segment" in payload["error"]["message"]
