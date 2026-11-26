import json
import os
import subprocess
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
FIXTURES = PACK / "tests" / "fixtures"
sys.path.insert(0, str(PACK / "scripts"))

from doddle_revops.attribution import attribute_revenue  # noqa: E402
from doddle_revops.cohorts import analyze_cohorts  # noqa: E402
from doddle_revops.data_infrastructure import profile_data_infrastructure  # noqa: E402
from doddle_revops.pql import score_pql  # noqa: E402


def test_version_envelope():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "version"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["ok"] is True
    assert data["tool"] == "doddle-revops"
    assert "pql" in data["commands"]


def test_doctor_reports_healthy():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "doctor"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["metrics"]["healthy"] is True


def test_data_profile_scores_tables_identity_and_reverse_etl():
    env = profile_data_infrastructure(
        warehouse_export=str(FIXTURES / "warehouse.json"),
        dbt_manifest=str(FIXTURES / "dbt_manifest.json"),
        identity_map=str(FIXTURES / "identity_map.csv"),
        reverse_etl_config=str(FIXTURES / "reverse_etl.json"),
    )
    assert env["ok"] is True
    assert env["metrics"]["table_count"] == 3
    assert env["metrics"]["ready_tables"] == 2
    assert env["metrics"]["identity_match_rate"] == 0.75
    assert env["metrics"]["reverse_etl_ready"] is False
    assert env["metrics"]["readiness_score"] == 47.2
    assert env["evidence"]["stamp"] == "CURRENT"


def test_data_profile_marks_stale_table_and_missing_inputs():
    env = profile_data_infrastructure(
        warehouse_export=str(FIXTURES / "warehouse.json"),
    )
    legacy = [r for r in env["rows"] if r.get("table") == "legacy_crm_deals"][0]
    assert legacy["freshness"] == "STALE"
    assert legacy["status"] == "stale"
    assert "dbt_manifest" in env["completeness"]["missing"]
    assert "identity_map" in env["completeness"]["missing"]
    assert "reverse_etl_config" in env["completeness"]["missing"]


def test_data_profile_rejects_unreadable_export():
    env = profile_data_infrastructure(warehouse_export=str(FIXTURES / "does_not_exist.json"))
    assert env["ok"] is False
    assert "could not read warehouse export" in env["error"]["message"]
    assert env["error"]["hint"]


def test_pql_scores_accounts_and_flags_unknown_events():
    env = score_pql(
        events_path=str(FIXTURES / "events.jsonl"),
        accounts_path=str(FIXTURES / "accounts.csv"),
        model_path=str(FIXTURES / "pql_model.json"),
    )
    assert env["ok"] is True
    rows = {r["account_id"]: r for r in env["rows"]}
    assert rows["acct_9f3"]["tier"] == "hot"
    assert rows["acct_9f3"]["aha_count"] == 2
    assert rows["acct_2b1"]["tier"] == "nurture"
    assert rows["acct_3c4"]["tier"] == "insufficient_data"
    assert env["metrics"]["unknown_account_events"] == 1
    assert env["metrics"]["tiers"]["hot"] == 1
    assert "fit_score" in env["completeness"]["missing"]


def test_pql_requires_model_inputs():
    env = score_pql(
        events_path=str(FIXTURES / "events.jsonl"),
        accounts_path=str(FIXTURES / "accounts.csv"),
        model_path=str(FIXTURES / "missing_model.json"),
    )
    assert env["ok"] is False
    assert env["error"]["hint"]


def test_attribution_linear_allocates_won_revenue_only():
    env = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
        model="linear",
    )
    assert env["ok"] is True
    assert env["metrics"]["won_deals"] == 4
    assert env["metrics"]["attributed_deals"] == 3
    assert env["metrics"]["won_revenue"] == 3000.0
    assert env["metrics"]["attributed_revenue"] == 2300.0
    assert env["metrics"]["unattributed_revenue"] == 700.0
    assert env["metrics"]["attribution_coverage"] == 0.7667
    allocations = [r for r in env["rows"] if r["kind"] == "allocation"]
    assert round(sum(r["attributed_revenue"] for r in allocations), 2) == 2300.0


def test_attribution_models_change_allocation():
    linear = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
        model="linear",
    )
    position = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
        model="position-based",
    )
    decay = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
        model="time-decay",
    )
    for env in (linear, position, decay):
        assert env["metrics"]["attributed_revenue"] == 2300.0
    linear_d1 = sorted((r["attributed_revenue"] for r in linear["rows"]
                         if r["kind"] == "allocation" and r["deal_id"] == "d1"))
    position_d1 = sorted((r["attributed_revenue"] for r in position["rows"]
                          if r["kind"] == "allocation" and r["deal_id"] == "d1"))
    assert linear_d1 == [333.33, 333.33, 333.34]
    assert position_d1 == [200.0, 400.0, 400.0]
    decay_d1 = sorted((r["attributed_revenue"] for r in decay["rows"]
                       if r["kind"] == "allocation" and r["deal_id"] == "d1"))
    assert decay_d1[0] < 333.34 < decay_d1[2]


def test_attribution_reports_roi_per_channel():
    env = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
    )
    channels = {r["channel"]: r for r in env["rows"] if r["kind"] == "channel"}
    assert channels["email"]["attributed_revenue"] == 500.0
    assert channels["email"]["cost"] == 30.0
    assert channels["email"]["roi"] == 15.6667
    assert channels["partner"]["attributed_revenue"] == 800.0


def test_attribution_rejects_unknown_model():
    env = attribute_revenue(
        touchpoints_path=str(FIXTURES / "touchpoints.csv"),
        deals_path=str(FIXTURES / "deals.csv"),
        model="first-touch-magic",
    )
    assert env["ok"] is False
    assert "unknown attribution model" in env["error"]["message"]


def test_cohorts_builds_retention_matrix():
    env = analyze_cohorts(str(FIXTURES / "cohorts.csv"), max_periods=3)
    assert env["ok"] is True
    assert env["metrics"]["cohorts"] == 2
    matrix = {(r["cohort"], r["period"]): r for r in env["rows"]}
    assert matrix[("2026-09", 0)]["logo_retention"] == 1.0
    assert matrix[("2026-09", 1)]["logo_retention"] == 0.5
    assert matrix[("2026-09", 1)]["revenue_retention"] == 0.6667
    assert matrix[("2026-10", 0)]["cohort_size"] == 1


def test_cohorts_handles_missing_file():
    env = analyze_cohorts(str(FIXTURES / "nope.csv"))
    assert env["ok"] is False
    assert env["error"]["hint"]
