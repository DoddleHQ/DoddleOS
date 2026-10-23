"""The GTM framework registry.

Named templates a skill can pull a structure from, versioned as one unit. A framework is a
*structure*, not a market figure — it carries no statistics, so it never goes stale the way a
benchmark does. Bump :data:`__init__.DATA_VERSION` when the set changes.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

FRAMEWORKS: Dict[str, Dict[str, Any]] = {
    "positioning-canvas": {
        "name": "Positioning Canvas",
        "purpose": "Define who you serve, the alternative, the differentiated value and the proof.",
        "sections": ["Target segment", "Category / frame of reference", "Alternative & status quo",
                     "Unique differentiated value", "Reasons to believe", "Positioning statement"],
    },
    "messaging-house": {
        "name": "Messaging House",
        "purpose": "Turn positioning into a vocabulary the whole team uses.",
        "sections": ["Roof: core value proposition", "Pillars (3)", "Proof per pillar",
                     "Message by persona", "Message by stage", "Words to use / avoid"],
    },
    "icp-template": {
        "name": "ICP Definition",
        "purpose": "A scored ideal-customer profile.",
        "sections": ["Firmographics", "Technographics", "Trigger events", "Buying committee",
                     "Qualifying criteria + weights", "Disqualifiers"],
    },
    "persona-template": {
        "name": "Buyer Persona",
        "purpose": "A role-level view of goals, pains and objections.",
        "sections": ["Role & reporting line", "Goals", "Pains", "Success metrics", "Objections",
                     "Where they learn", "Message that lands"],
    },
    "launch-checklist": {
        "name": "GTM Launch Checklist",
        "purpose": "Plan a launch across positioning, content, demand, sales and success.",
        "sections": ["Objective & success metric", "Narrative & positioning", "Assets", "Channel plan",
                     "Sales enablement", "Pricing & packaging", "Readiness gate", "Launch day",
                     "Post-launch measurement"],
    },
    "battlecard": {
        "name": "Competitive Battlecard",
        "purpose": "Arm sellers against a specific competitor.",
        "sections": ["Their pitch", "Where they win", "Where we win", "Landmines & questions",
                     "Objection handling", "Proof points", "Do not say"],
    },
    "sales-narrative": {
        "name": "Sales Narrative",
        "purpose": "A pitch structured as a story from problem to proof.",
        "sections": ["Status quo", "Rising cost of inaction", "The shift", "Our approach",
                     "Proof", "The ask"],
    },
    "pipeline-review": {
        "name": "Pipeline Review Agenda",
        "purpose": "Run a forecast-honest pipeline meeting.",
        "sections": ["Coverage & pace", "Stage conversion", "Stalled deals", "Slippage",
                     "Deal risks", "Commit vs upside", "Actions & owners"],
    },
    "unit-economics-model": {
        "name": "Unit Economics Model",
        "purpose": "Assemble the CAC, LTV and payback inputs.",
        "sections": ["CAC (fully loaded)", "ARPA", "Gross margin", "Churn", "Expansion",
                     "LTV", "LTV:CAC", "CAC payback"],
    },
    "pricing-model": {
        "name": "Pricing & Packaging Model",
        "purpose": "Model tiers, margins and a value metric.",
        "sections": ["Value metric", "Good / better / best", "Price per tier", "Variable cost per tier",
                     "Expected mix", "Blended margin", "Migration & grandfathering"],
    },
    "abm-tiering": {
        "name": "ABM Tiering",
        "purpose": "Tier target accounts and match effort to value.",
        "sections": ["Tier 1 (1:1)", "Tier 2 (1:few)", "Tier 3 (1:many)", "Account criteria",
                     "Play per tier", "Owners", "Success metric"],
    },
    "win-loss-interview": {
        "name": "Win/Loss Interview",
        "purpose": "A structured interview script for closed deals.",
        "sections": ["Buying trigger", "Options considered", "Decision criteria", "Who decided",
                     "Why us / why not us", "Pricing reaction", "Would recommend?"],
    },
    "onboarding-plan": {
        "name": "Customer Onboarding Plan",
        "purpose": "Time-to-value for a new customer.",
        "sections": ["Success criteria", "Milestones & dates", "First value moment", "Owners",
                     "Risks", "Expansion path"],
    },
    "partnership-model": {
        "name": "Partnership Model",
        "purpose": "Design an alliance with clear mutual value.",
        "sections": ["Partner type", "Mutual value", "Integrated motion", "Commercial terms",
                     "Enablement", "Attribution", "Review cadence"],
    },
    "plg-loop": {
        "name": "Product-Led Growth Loop",
        "purpose": "Model acquisition and expansion through the product.",
        "sections": ["Entry point", "Activation moment", "Habit", "Loop mechanic", "Monetization",
                     "Referral / virality", "Guardrail metrics"],
    },
    "demand-gen-plan": {
        "name": "Demand Generation Plan",
        "purpose": "Plan channels against a pipeline target.",
        "sections": ["Pipeline target", "Funnel math", "Source mix", "Content & offers",
                     "Cadence", "Budget assumptions", "Measurement"],
    },
    "experimentation-brief": {
        "name": "Experimentation Brief",
        "purpose": "A test designed before it runs.",
        "sections": ["Hypothesis", "Metric & guardrails", "Population", "Variants", "Sample & duration",
                     "Decision rule", "Result & learning"],
    },
    "forecast-model": {
        "name": "Forecast Model",
        "purpose": "Build a forecast from recorded pipeline, not optimism.",
        "sections": ["Stage probabilities", "Coverage", "Commit / best / worst case",
                     "Historical accuracy", "Assumptions (dated)", "Risk register"],
    },
    "competitive-teardown": {
        "name": "Competitive Teardown",
        "purpose": "A structured read of a competitor's go-to-market.",
        "sections": ["Positioning & narrative", "ICP & segments", "Pricing & packaging",
                     "Channels & motion", "Proof & traction signals", "Strengths", "Gaps we can exploit"],
    },
    "case-study-brief": {
        "name": "Case Study Brief",
        "purpose": "Turn a customer win into proof.",
        "sections": ["Customer & context", "Problem", "Evaluation", "Solution", "Quantified result",
                     "Quote", "Approvals"],
    },
    "jtbd-interview": {
        "name": "Jobs-to-be-Done Interview",
        "purpose": "Uncover the job the buyer hired the product to do.",
        "sections": ["First thought", "Passive looking", "Active looking", "Decision & pull",
                     "Anxiety & habit", "Struggling moment", "Forces (push/pull/habit/anxiety)",
                     "Hired to do / fired"],
    },
    "buying-committee-map": {
        "name": "Buying Committee Map",
        "purpose": "Map every role in a B2B deal and how to reach each.",
        "sections": ["Champion", "Economic buyer", "Technical evaluator", "End users",
                     "Blockers / influencers", "Decision process & criteria", "Per-role message & proof"],
    },
    "aarrr-metrics": {
        "name": "AARRR Metrics Framework",
        "purpose": "Structure growth metrics from acquisition to revenue.",
        "sections": ["Acquisition (sources & counts)", "Activation (first-value moment)",
                     "Retention (cohorts)", "Referral (loops & rate)", "Revenue (monetization)",
                     "Bottleneck & priority"],
    },
    "territory-plan": {
        "name": "Sales Territory Plan",
        "purpose": "Allocate accounts and capacity to territories.",
        "sections": ["Territory segmentation axis", "Account counts by tier", "Quota per territory",
                     "Capacity check", "Coverage gaps", "Rebalance triggers"],
    },
    "sales-capacity-model": {
        "name": "Sales Capacity Model",
        "purpose": "Derive pipeline needed from reps, productivity and win rate.",
        "sections": ["Reps & ramp state", "Quota per rep", "Win rate (assumption)",
                     "Deal size (assumption)", "Pipeline coverage ratio", "Required pipeline",
                     "Gap vs current pipeline"],
    },
    "partnership-scorecard": {
        "name": "Partnership Scorecard",
        "purpose": "Evaluate or review a partner relationship on evidence.",
        "sections": ["Sourced & influenced pipeline", "Activation & enablement state",
                     "Deal registration hygiene", "Revenue contribution", "Strategic fit",
                     "Next actions & owner"],
    },
    "channel-fit-matrix": {
        "name": "Channel Fit Matrix",
        "purpose": "Score candidate channels against fit criteria before spending.",
        "sections": ["ICP presence per channel", "Cost assumption per channel",
                     "CAC payback expectation", "Sales-cycle fit", "Capacity to execute",
                     "Priority & pilot plan"],
    },
    "win-loss-program": {
        "name": "Win/Loss Program",
        "purpose": "Run a continuous win/loss interview program.",
        "sections": ["Selection criteria (win/loss/recruited)", "Interview cadence & owner",
                     "Script (see win-loss-interview)", "Coding scheme", "Themes & frequency",
                     "Actions into battlecards & roadmap"],
    },
    "nrr-waterfall": {
        "name": "Net Revenue Retention Waterfall",
        "purpose": "Decompose NRR into expansion, contraction, churn and new.",
        "sections": ["Starting ARR", "Expansion ARR", "Contraction ARR", "Churned ARR",
                     "New ARR", "NRR & GRR", "Largest drivers (dated)"],
    },
    "launch-readiness-gate": {
        "name": "Launch Readiness Gate",
        "purpose": "A go / no-go gate scored before launch day.",
        "sections": ["Positioning & messaging locked", "Assets shipped", "Enablement done",
                     "Pricing & packaging ready", "Measurement instrumented", "Support ready",
                     "Verdict: go / no-go / conditional"],
    },
}

REGISTRY_VERSION = "gtm-frameworks-2026-10-2"


def get(slug: str) -> Optional[Dict[str, Any]]:
    if not slug:
        return None
    key = slug.strip().lower()
    fw = FRAMEWORKS.get(key)
    return dict(fw, slug=key) if fw else None


def all_frameworks() -> List[Dict[str, Any]]:
    return [dict(fw, slug=slug) for slug, fw in sorted(FRAMEWORKS.items())]


def slugs() -> List[str]:
    return sorted(FRAMEWORKS)
