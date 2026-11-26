import json
import os
import subprocess
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
FIXTURES = PACK / "tests" / "fixtures"
sys.path.insert(0, str(PACK / "scripts"))

from doddle_revops.attribution import attribute_revenue  # noqa: E402
from doddle_revops.call_intel import search_calls  # noqa: E402
from doddle_revops.cohorts import analyze_cohorts  # noqa: E402
from doddle_revops.data_infrastructure import profile_data_infrastructure  # noqa: E402
from doddle_revops.integrations import audit_integrations  # noqa: E402
from doddle_revops.metering import meter_usage  # noqa: E402
from doddle_revops.pql import score_pql  # noqa: E402
from doddle_revops.portfolio import build_portfolio  # noqa: E402
from doddle_revops.qbr import build_qbr, render_qbr_markdown  # noqa: E402
from doddle_revops.retention import analyze_retention  # noqa: E402
from doddle_revops.sdr import validate_sdr_claims  # noqa: E402
from doddle_revops.signals import community_attribution, route_signals  # noqa: E402

NOW = "2026-11-26T00:00:00Z"
NOW_DT = __import__("datetime").datetime.fromisoformat(NOW.replace("Z", "+00:00"))


def test_version_envelope():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "version"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["ok"] is True
    assert data["tool"] == "doddle-revops"
    assert "pql" in data["commands"]
    assert "community-attribution" in data["commands"]


def test_doctor_reports_healthy():
    out = subprocess.run([sys.executable, str(PACK / "scripts" / "drev"), "doctor"],
                         capture_output=True, text=True, check=True)
    data = json.loads(out.stdout)
    assert data["metrics"]["healthy"] is True


# --------------------------------------------------------------------------
# Stage 1 — data infrastructure
# --------------------------------------------------------------------------

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
    env = profile_data_infrastructure(warehouse_export=str(FIXTURES / "warehouse.json"))
    legacy = [r for r in env["rows"] if r.get("table") == "legacy_crm_deals"][0]
    assert legacy["freshness"] == "STALE"
    assert legacy["status"] == "stale"
    assert "dbt_manifest" in env["completeness"]["missing"]


def test_data_profile_rejects_unreadable_export():
    env = profile_data_infrastructure(warehouse_export=str(FIXTURES / "does_not_exist.json"))
    assert env["ok"] is False
    assert "could not read warehouse export" in env["error"]["message"]


# --------------------------------------------------------------------------
# Stage 4 — PQL scoring
# --------------------------------------------------------------------------

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


def test_pql_requires_model_inputs():
    env = score_pql(
        events_path=str(FIXTURES / "events.jsonl"),
        accounts_path=str(FIXTURES / "accounts.csv"),
        model_path=str(FIXTURES / "missing_model.json"),
    )
    assert env["ok"] is False
    assert env["error"]["hint"]


# --------------------------------------------------------------------------
# Stage 6 — attribution and cohorts
# --------------------------------------------------------------------------

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
    linear = attribute_revenue(touchpoints_path=str(FIXTURES / "touchpoints.csv"),
                               deals_path=str(FIXTURES / "deals.csv"), model="linear")
    position = attribute_revenue(touchpoints_path=str(FIXTURES / "touchpoints.csv"),
                                  deals_path=str(FIXTURES / "deals.csv"), model="position-based")
    decay = attribute_revenue(touchpoints_path=str(FIXTURES / "touchpoints.csv"),
                               deals_path=str(FIXTURES / "deals.csv"), model="time-decay")
    for env in (linear, position, decay):
        assert env["metrics"]["attributed_revenue"] == 2300.0
    linear_d1 = sorted(r["attributed_revenue"] for r in linear["rows"]
                       if r["kind"] == "allocation" and r["deal_id"] == "d1")
    position_d1 = sorted(r["attributed_revenue"] for r in position["rows"]
                         if r["kind"] == "allocation" and r["deal_id"] == "d1")
    assert linear_d1 == [333.33, 333.33, 333.34]
    assert position_d1 == [200.0, 400.0, 400.0]
    decay_d1 = sorted(r["attributed_revenue"] for r in decay["rows"]
                      if r["kind"] == "allocation" and r["deal_id"] == "d1")
    assert decay_d1[0] < 333.34 < decay_d1[2]


def test_attribution_rejects_unknown_model():
    env = attribute_revenue(touchpoints_path=str(FIXTURES / "touchpoints.csv"),
                            deals_path=str(FIXTURES / "deals.csv"), model="first-touch-magic")
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


# --------------------------------------------------------------------------
# Stage 2 — signal routing
# --------------------------------------------------------------------------

def test_route_signals_routes_recent_signals_and_reports_unrouted():
    env = route_signals(events_path=str(FIXTURES / "signals.jsonl"),
                        rules_path=str(FIXTURES / "signal_rules.json"),
                        now=NOW_DT)
    assert env["ok"] is True
    assert env["metrics"]["signals_seen"] == 5
    assert env["metrics"]["signals_routed"] == 3
    assert env["metrics"]["signals_unrouted"] == 1
    assert env["metrics"]["accounts_routed"] == 2
    assert "unknown_signal" in env["completeness"]["missing"]
    routed = [r for r in env["rows"] if r["account_id"] == "acct_9f3"]
    assert routed
    assert routed[0]["slack_payload"]["delivery"].startswith("dry-run")


def test_route_signals_requires_rules_file():
    env = route_signals(events_path=str(FIXTURES / "signals.jsonl"),
                        rules_path=str(FIXTURES / "missing_rules.json"))
    assert env["ok"] is False
    assert env["error"]["hint"]


# --------------------------------------------------------------------------
# Stage 3 — AI SDR evidence gate
# --------------------------------------------------------------------------

def test_sdr_validate_supports_only_evidence_backed_claims():
    env = validate_sdr_claims(account_path=str(FIXTURES / "sdr_account.json"),
                              evidence_path=str(FIXTURES / "sdr_evidence.csv"))
    assert env["ok"] is True
    assert env["metrics"]["claims"] == 5
    assert env["metrics"]["supported"] == 3
    assert env["metrics"]["unsupported"] == 2
    assert env["metrics"]["coverage"] == 0.6
    unsupported = [r for r in env["rows"] if not r["supported"]]
    reasons = " ".join(r["reason"] for r in unsupported)
    assert "no evidence with this id" in reasons
    assert "not for this account domain" in reasons


# --------------------------------------------------------------------------
# Stage 5 — usage metering
# --------------------------------------------------------------------------

def test_meter_rates_usage_consumes_credits_and_previews_invoice():
    env = meter_usage(usage_path=str(FIXTURES / "usage_metering.jsonl"),
                      plan_path=str(FIXTURES / "metering_plan.json"))
    assert env["ok"] is True
    rows = {(r["account_id"], r["period"]): r for r in env["rows"]}
    pro = rows[("acct_9f3", "2026-11")]
    assert pro["quantity"] == 1500
    assert pro["credits_used"] == 100
    assert pro["billable_units"] == 400
    assert pro["overage_amount"] == 20.0
    assert pro["total_amount"] == 119.0
    starter = rows[("acct_2b1", "2026-11")]
    assert starter["billable_units"] == 0
    assert starter["total_amount"] == 29.0
    assert env["metrics"]["unrated_usage_rows"] == 1
    assert env["metrics"]["total_billed"] == 148.0


# --------------------------------------------------------------------------
# Stage 7 — call intelligence
# --------------------------------------------------------------------------

def test_call_search_returns_excerpts_and_themes():
    env = search_calls(transcripts_path=str(FIXTURES / "transcripts.jsonl"),
                       query="pricing",
                       themes_path=str(FIXTURES / "themes.json"))
    assert env["ok"] is True
    assert env["metrics"]["matches"] == 2
    assert env["metrics"]["calls_matched"] == 1
    assert env["metrics"]["themes_hit"] == {"pricing": 2}
    assert env["rows"][0]["excerpt"]
    assert env["rows"][0]["rep_talk_share"] is not None


def test_call_search_requires_transcripts():
    env = search_calls(transcripts_path=str(FIXTURES / "missing.jsonl"), query="pricing")
    assert env["ok"] is False
    assert env["error"]["hint"]


# --------------------------------------------------------------------------
# Stage 8 — retention, NRR, health
# --------------------------------------------------------------------------

def test_retention_computes_nrr_grr_health_and_risk():
    env = analyze_retention(customers_path=str(FIXTURES / "retention_customers.csv"),
                            usage_path=str(FIXTURES / "retention_usage.csv"),
                            now=NOW_DT)
    assert env["ok"] is True
    assert env["metrics"]["nrr"] == 1.0551
    assert env["metrics"]["grr"] == 0.9407
    assert env["metrics"]["renewal_risk_count"] == 2
    assert env["metrics"]["expansion_candidates"] == 1
    assert env["metrics"]["average_health_score"] == 78.0
    rows = {r["customer_id"]: r for r in env["rows"]}
    assert "renewal_risk" in rows["cust_1"]["flags"]
    assert "expansion_candidate" in rows["cust_5"]["flags"]
    assert rows["cust_3"]["health_score"] == 30.0


# --------------------------------------------------------------------------
# Stage 9 — integration-led growth
# --------------------------------------------------------------------------

def test_integration_audit_scores_readiness():
    env = audit_integrations(catalog_path=str(FIXTURES / "integrations.json"))
    assert env["ok"] is True
    assert env["metrics"]["integrations"] == 2
    assert env["metrics"]["ready"] == 1
    rows = {r["integration"]: r for r in env["rows"]}
    assert rows["hubspot"]["readiness_score"] == 100.0
    assert rows["zapier"]["readiness_score"] == 16.7
    assert "listing_complete" in rows["zapier"]["failures"]


# --------------------------------------------------------------------------
# Stage 10 — automated QBR
# --------------------------------------------------------------------------

def test_qbr_builds_scoreboard_roi_and_deck():
    env = build_qbr(account_path=str(FIXTURES / "qbr_account.json"))
    assert env["ok"] is True
    assert env["metrics"]["kpis"] == 3
    assert env["metrics"]["on_track"] == 1
    assert env["metrics"]["at_risk"] == 2
    assert env["metrics"]["roi"] == 3.5
    assert env["metrics"]["slides"] == 4
    slides = [r for r in env["rows"] if r["kind"] == "slide"]
    assert slides[0]["id"] == "value-delivered"


def test_qbr_markdown_marks_missing_roi():
    payload = json.loads((FIXTURES / "qbr_account.json").read_text())
    payload.pop("investment")
    payload.pop("revenue")
    tmp = PACK / "tests" / "fixtures" / "_tmp_qbr.json"
    tmp.write_text(json.dumps(payload))
    try:
        env = build_qbr(account_path=str(tmp))
        assert env["metrics"]["roi"] is None
        assert "roi_inputs" in env["completeness"]["missing"]
        assert "NOT AVAILABLE" in render_qbr_markdown(env)
    finally:
        tmp.unlink()


# --------------------------------------------------------------------------
# Stage 11 — dark social and community attribution
# --------------------------------------------------------------------------

def test_community_attribution_separates_self_reported_and_modeled():
    env = community_attribution(community_path=str(FIXTURES / "community.csv"),
                                 surveys_path=str(FIXTURES / "surveys.csv"),
                                 deals_path=str(FIXTURES / "community_deals.csv"))
    assert env["ok"] is True
    assert env["metrics"]["community_members"] == 3
    assert env["metrics"]["survey_responses"] == 3
    assert env["metrics"]["influenced_revenue"] == 6500.0
    assert env["metrics"]["consent_missing"] == 1
    assert env["metrics"]["confidence"] == "low"
    bases = {r["basis"] for r in env["rows"] if r.get("kind") == "source"}
    assert bases == {"self_reported", "modeled"}


# --------------------------------------------------------------------------
# Stage 12 — revenue portfolio
# --------------------------------------------------------------------------

def test_portfolio_withholds_price_comparison_when_models_differ():
    env = build_portfolio(companies_path=str(FIXTURES / "companies.json"),
                          observations_path=str(FIXTURES / "observations.csv"),
                          now=NOW_DT)
    assert env["ok"] is True
    assert env["metrics"]["companies"] == 3
    assert env["metrics"]["comparable"] is False
    assert env["metrics"]["price_median"] is None
    rows = {r["company"]: r for r in env["rows"] if r.get("kind") == "company"}
    assert rows["Alpha Tool"]["pricing_model"] == "seat"
    assert rows["Beta Suite"]["pricing_model"] == "metered"
    assert rows["Alpha Tool"]["confidence"] == "medium"
    assert any(r.get("kind") == "outline" for r in env["rows"])
