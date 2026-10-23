#!/usr/bin/env python3
"""One-off generator: emit blueprint.yaml for every GTM skill from a spec table.

Kept in scripts/ for reproducibility; not part of the runtime toolkit.
Run: python3 scripts/gen_blueprints.py
"""

from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, ".claude", "skills")

# (slug, agent, kind, commands, mcp, inputs, outputs, integrations)
# kind: toolkit | advisory
SPECS = [
    ("gtm-strategy", "gtm-strategist", "toolkit", ["unit-economics", "funnel"],
     ["notion.pages"],
     [("objective", "string", True, "What the plan must achieve"),
      ("segment", "string", False, "Primary segment; defaults to SMB"),
      ("inputs", "file", False, "User-supplied assumptions (ACV, churn, funnel counts)")],
     [("plan", "markdown", "The assembled go-to-market plan")],
     ["notion"]),
    ("gtm-positioning", "positioning-strategist", "toolkit", [],
     [],
     [("product", "string", True, "The product being positioned"),
      ("alternative", "string", True, "What buyers use today instead"),
      ("differentiators", "string", False, "Why you are meaningfully better")],
     [("positioning", "markdown", "Positioning canvas and statement")],
     []),
    ("gtm-messaging", "positioning-strategist", "toolkit", [],
     [],
     [("positioning", "string", True, "The agreed positioning"),
      ("personas", "string", False, "Personas to message to")],
     [("messaging", "markdown", "Messaging house")],
     []),
    ("gtm-icp", "positioning-strategist", "toolkit", ["score"],
     ["clearbit.company"],
     [("criteria", "string", True, "Weighted qualifying criteria for the ICP"),
      ("accounts", "file", False, "Optional account list to score against the ICP")],
     [("icp", "markdown", "ICP definition"), ("envelope", "json", "Weighted score envelope")],
     ["clearbit"]),
    ("gtm-market-sizing", "revenue-analyst", "toolkit", ["size-market"],
     [],
     [("accounts", "number", False, "Total addressable accounts (bottom-up)"),
      ("acv", "number", False, "Annual contract value assumption"),
      ("sam-pct", "number", False, "Serviceable share of TAM (assumption)"),
      ("som-pct", "number", False, "Obtainable share of SAM (assumption)")],
     [("sizing", "markdown", "TAM/SAM/SOM from the given inputs"), ("envelope", "json", "Sizing envelope")],
     []),
    ("gtm-competitive", "positioning-strategist", "toolkit", [],
     [],
     [("competitors", "string", True, "Competitors to analyse"),
      ("evidence", "file", False, "Win/loss or call notes if available")],
     [("analysis", "markdown", "Competitive landscape and positioning gaps")],
     []),
    ("gtm-segmentation", "gtm-strategist", "toolkit", ["size-market"],
     ["clearbit.company"],
     [("market", "string", True, "Market to segment"),
      ("criteria", "string", False, "Segmentation axes")],
     [("segments", "markdown", "Segment definitions and priority"), ("envelope", "json", "Sizing envelope")],
     ["clearbit"]),
    ("gtm-persona", "positioning-strategist", "toolkit", [],
     [],
     [("segment", "string", True, "Segment the personas belong to"),
      ("roles", "string", False, "Buying-committee roles")],
     [("personas", "markdown", "Buyer personas")],
     []),
    ("gtm-abm", "demand-gen-strategist", "toolkit", ["score"],
     ["clearbit.company", "hubspot.deals"],
     [("accounts", "file", True, "Target account list"),
      ("criteria", "string", True, "Weighted tiering criteria")],
     [("program", "markdown", "ABM tiers and plays"), ("envelope", "json", "Account score envelope")],
     ["clearbit", "hubspot"]),
    ("gtm-demand-gen", "demand-gen-strategist", "toolkit", ["funnel"],
     ["ga4.getReport", "linkedin.ads"],
     [("pipeline-target", "number", True, "Pipeline target for the period"),
      ("funnel", "string", True, "Stage conversion assumptions"),
      ("channels", "string", False, "Candidate channels")],
     [("plan", "markdown", "Demand plan with funnel math"), ("envelope", "json", "Funnel envelope")],
     ["ga4", "linkedin"]),
    ("gtm-lead-scoring", "demand-gen-strategist", "toolkit", ["score"],
     ["hubspot.deals"],
     [("criteria", "string", True, "Weighted fit and intent criteria"),
      ("leads", "file", False, "Optional leads to score")],
     [("model", "markdown", "Lead-scoring model"), ("envelope", "json", "Score envelope")],
     ["hubspot"]),
    ("gtm-outbound", "demand-gen-strategist", "toolkit", [],
     ["linkedin.ads", "gong.calls"],
     [("icp", "string", True, "Target profile"),
      ("offer", "string", True, "Value proposition to lead with"),
      ("channels", "string", False, "Outbound channels")],
     [("sequences", "markdown", "Outbound sequence plan and copy")],
     ["linkedin"]),
    ("gtm-pipeline-analytics", "revenue-analyst", "toolkit", ["audit", "report"],
     ["hubspot.deals", "salesforce.opportunities"],
     [("export", "file", True, "Deals/opportunities export (JSON or CSV)"),
      ("segment", "string", False, "Segment filter; defaults to SMB")],
     [("report", "markdown", "Pipeline audit report"), ("envelope", "json", "Audit envelope")],
     ["hubspot", "salesforce"]),
    ("gtm-forecasting", "revenue-analyst", "toolkit", ["audit"],
     ["hubspot.deals", "salesforce.opportunities"],
     [("export", "file", True, "Deals/opportunities export (JSON or CSV)"),
      ("stages", "string", False, "Stage probabilities (assumptions)")],
     [("forecast", "markdown", "Forecast from recorded pipeline"), ("envelope", "json", "Audit envelope")],
     ["hubspot", "salesforce"]),
    ("gtm-win-loss", "revenue-analyst", "toolkit", ["audit"],
     ["gong.calls", "hubspot.deals"],
     [("export", "file", True, "Closed-deal export (JSON or CSV)"),
      ("interviews", "file", False, "Win/loss interview notes")],
     [("analysis", "markdown", "Win/loss analysis"), ("envelope", "json", "Audit envelope")],
     ["gong", "hubspot"]),
    ("gtm-launch", "gtm-strategist", "toolkit", [],
     ["notion.pages"],
     [("product", "string", True, "What is launching"),
      ("attributes", "string", True, "Objective, audience, channels")],
     [("plan", "markdown", "GTM launch plan and checklist")],
     ["notion"]),
    ("gtm-sales-narrative", "enablement-lead", "toolkit", [],
     ["gong.calls"],
     [("positioning", "string", True, "Positioning and value proposition"),
      ("audience", "string", False, "Who the narrative is for")],
     [("narrative", "markdown", "Sales narrative")],
     ["gong"]),
    ("gtm-enablement", "enablement-lead", "toolkit", [],
     ["notion.pages", "gong.calls"],
     [("team", "string", True, "Who is being enabled"),
      ("gaps", "string", False, "Known skill or knowledge gaps")],
     [("program", "markdown", "Enablement program")],
     ["notion", "gong"]),
    ("gtm-battlecards", "enablement-lead", "toolkit", [],
     ["gong.calls"],
     [("competitor", "string", True, "Competitor to arm against"),
      ("evidence", "file", False, "Teardown, win/loss or call notes")],
     [("battlecard", "markdown", "Competitive battlecard")],
     ["gong"]),
    ("gtm-case-study", "enablement-lead", "advisory", [],
     ["notion.pages"],
     [("customer", "string", True, "Customer the story is about"),
      ("results", "string", True, "User-supplied, verified results")],
     [("case_study", "markdown", "Case study")],
     ["notion"]),
    ("gtm-pricing", "gtm-strategist", "toolkit", ["pricing"],
     [],
     [("price", "number", True, "List price"),
      ("variable-cost", "number", True, "Variable cost per unit/account"),
      ("fixed-cost", "number", False, "Fixed cost for break-even")],
     [("analysis", "markdown", "Pricing analysis"), ("envelope", "json", "Pricing envelope")],
     []),
    ("gtm-packaging", "gtm-strategist", "toolkit", ["pricing"],
     [],
     [("tiers", "string", True, "Tiers with price, cost and expected mix"),
      ("value-metric", "string", False, "The value metric to meter on")],
     [("packaging", "markdown", "Packaging model with blended margins"), ("envelope", "json", "Pricing envelope")],
     []),
    ("gtm-expansion", "revenue-analyst", "toolkit", ["audit"],
     ["hubspot.deals"],
     [("export", "file", True, "Deals/opportunities export (JSON or CSV)"),
      ("motion", "string", False, "Upsell, cross-sell or renewal focus")],
     [("plan", "markdown", "Expansion plan"), ("envelope", "json", "Audit envelope")],
     ["hubspot"]),
    ("gtm-partnerships", "gtm-strategist", "toolkit", [],
     ["notion.pages"],
     [("objective", "string", True, "What the partnership must achieve"),
      ("candidates", "string", False, "Candidate partners")],
     [("model", "markdown", "Partnership model")],
     ["notion"]),
    ("gtm-channel", "revenue-analyst", "toolkit", ["unit-economics"],
     [],
     [("cac", "number", True, "Channel acquisition cost assumption"),
      ("arpa", "number", True, "Average revenue per account, monthly"),
      ("gross-margin", "number", False, "Gross margin fraction"),
      ("churn", "number", False, "Monthly churn rate")],
     [("analysis", "markdown", "Channel economics analysis"), ("envelope", "json", "Unit-economics envelope")],
     []),
    ("gtm-plg", "demand-gen-strategist", "toolkit", ["funnel"],
     ["ga4.getReport"],
     [("product", "string", True, "The product and its entry point"),
      ("funnel", "string", True, "Activation funnel counts")],
     [("loop", "markdown", "Product-led growth loop"), ("envelope", "json", "Funnel envelope")],
     ["ga4"]),
    ("gtm-metrics", "revenue-analyst", "toolkit", ["unit-economics", "funnel"],
     ["ga4.getReport", "hubspot.deals"],
     [("inputs", "file", True, "Recorded inputs for the metrics set"),
      ("window", "string", False, "Reporting window")],
     [("scorecard", "markdown", "KPI scorecard"), ("envelope", "json", "Metric envelopes")],
     ["ga4", "hubspot"]),
    ("gtm-reporting", "revenue-analyst", "toolkit", ["report"],
     ["hubspot.deals", "ga4.getReport"],
     [("export", "file", True, "Deals/opportunities export (JSON or CSV)"),
      ("window", "string", False, "Reporting window")],
     [("report", "markdown", "GTM report"), ("envelope", "json", "Audit envelope")],
     ["hubspot", "ga4"]),
    ("gtm-experimentation", "demand-gen-strategist", "toolkit", ["funnel"],
     ["ga4.getReport"],
     [("hypothesis", "string", True, "The hypothesis to test"),
      ("funnel", "string", True, "Baseline funnel counts")],
     [("brief", "markdown", "Experiment brief"), ("envelope", "json", "Funnel envelope")],
     ["ga4"]),
    ("gtm-onboarding", "enablement-lead", "advisory", [],
     ["notion.pages"],
     [("customer", "string", True, "The customer onboarding"),
      ("success", "string", True, "Definition of success and first value")],
     [("plan", "markdown", "Onboarding plan")],
     ["notion"]),
    ("gtm-advocacy", "partner-manager", "toolkit", ["report"],
     ["hubspot.deals"],
     [("proof", "string", True, "Customer proof assets or references available"),
      ("goal", "string", False, "Reviews, referrals, references or community")],
     [("program", "markdown", "Advocacy program design"), ("envelope", "json", "Audit envelope")],
     ["hubspot"]),
    ("gtm-intl", "gtm-strategist", "advisory", [],
     [],
     [("markets", "string", True, "Candidate markets to rank"),
      ("criteria", "string", False, "Ranking axes (fit, effort, readiness)")],
     [("plan", "markdown", "Locale ranking and minimum launch pack")],
     []),
]

INTEGRATION_TOOL = {
    "notion": "doddle.tool.v1.notion.pages",
    "hubspot": "doddle.tool.v1.hubspot.deals",
    "salesforce": "doddle.tool.v1.salesforce.opportunities",
    "gong": "doddle.tool.v1.gong.calls",
    "clearbit": "doddle.tool.v1.clearbit.company",
    "ga4": "doddle.tool.v1.ga4.getReport",
    "linkedin": "doddle.tool.v1.linkedin.ads",
}


def _inputs_yaml(inputs):
    out = ["inputs:"]
    for name, typ, req, desc in inputs:
        out.append(f'  - {{name: {name}, type: {typ}, required: {str(req).lower()}, '
                   f'description: "{desc}"}}')
    return out


def _outputs_yaml(outputs):
    out = ["outputs:"]
    for name, typ, desc in outputs:
        out.append(f'  - {{name: {name}, type: {typ}, description: "{desc}"}}')
    return out


def build(spec):
    slug, agent, kind, commands, mcp, inputs, outputs, integrations = spec
    if kind == "toolkit" and not commands:
        commands = ["frameworks"]
    sid = f"doddle.gtm.{slug}"
    tools = ["tools:", f"  - {{id: doddle.tool.cli.dgtm, required: false, fallback: manual_review}}"]
    for m in mcp:
        tools.append(f"  - {{id: doddle.tool.v1.{m}, required: false, fallback: manual_review}}")
    lines = [
        f"id: {sid}",
        "version: 0.2.0",
        "kind: skill",
        "engine: doddle-os>=1.0",
        f'description: "{agent} skill for {slug.replace("gtm-", "").replace("-", " ")}."',
        *_inputs_yaml(inputs),
        *_outputs_yaml(outputs),
        *tools,
    ]
    if integrations:
        lines.append("integrations:")
        for i in integrations:
            lines.append(f"  - {i}")
    md_out = next((o[0] for o in outputs if o[1] == "markdown"), "report")
    env_out = next((o[0] for o in outputs if o[1] == "json"), "envelope")
    lines.append("nodes:")
    if kind == "toolkit":
        node_ids = []
        for i, cmd in enumerate(commands):
            nid = "run" if i == 0 else f"run_{i+1}"
            node_ids.append(nid)
            lines.append(f'  - {{id: {nid}, type: tool, ref: doddle.tool.cli.dgtm, args: ["{cmd}"], '
                         f'needs: [{"inputs" if i == 0 else node_ids[i-1]}], produces: [{env_out}]}}')
        last = node_ids[-1]
        lines.append(f'  - {{id: narrate, type: agent, ref: {agent}, needs: [{last}], produces: [{md_out}]}}')
    else:
        lines.append(f'  - {{id: analyze, type: agent, ref: {agent}, needs: [inputs], produces: [{md_out}]}}')
    lines.append("on_fail: {retry: 1, fallback: manual_review}")
    return "\n".join(lines) + "\n"


def main():
    for spec in SPECS:
        slug = spec[0]
        d = os.path.join(SKILLS, slug)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "blueprint.yaml"), "w", encoding="utf-8") as fh:
            fh.write(build(spec))
    print(f"wrote {len(SPECS)} blueprints")


if __name__ == "__main__":
    main()
