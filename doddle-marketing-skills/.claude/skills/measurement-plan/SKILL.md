---
name: measurement-plan
id: doddle.marketing.measurement-plan
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants a tracking plan, KPI targets, event taxonomy, or a measurement setup before a campaign launches. Also use when the user mentions "tracking plan," "event taxonomy," "UTM taxonomy," "dataLayer," "GTM setup," "KPI targets," "measurement plan," "analytics setup," or "how will we measure this." Produces machine-readable KPI targets, a tracking plan, and pre-agreed decision rules that feed the closed measurement loop.
---

# Measurement Plan

Lock the scoreboard before the game starts. This skill turns a campaign brief into (1) machine-readable KPI targets, (2) a tracking plan (UTM + event taxonomy + dataLayer), and (3) pre-agreed decision rules so mid-campaign reviews change actions, not opinions. Nothing spends money before wave 0 completes.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Planning a campaign that will be measured (therefore: every campaign)
- Standardizing UTM and event naming across a team
- Defining what "on target" means before data exists
- Setting dashboard and reporting cadence for a launch
- Auditing measurement gaps before spending (ads, PR, outbound)

## Initial Assessment

Before drafting, understand:

1. **Brief state**
   - Primary KPI and guardrails from intake?
   - Channels in scope?
2. **Current tracking**
   - GA4 property, CRM, tag manager in use?
   - Existing UTM conventions worth preserving?
3. **Decision cadence**
   - Weekly reviews? Daily pulse during launch weeks?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign brief with goal and channels |
| channels | string | no | Channels in scope; infer from brief if missing |
| sales_cycle | string | no | Cycle length; default per GTM motion |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| kpi_targets | json | Metric, definition, baseline, target, tool binding per KPI |
| tracking_plan | markdown | UTM taxonomy, event taxonomy, dataLayer/GTM structure, reporting cadence |
| decisions | markdown | Pre-agreed decision rules: if metric X is below target by week N, take action Y |

---

## Core Framework

### Step 1: KPI Tree from the Brief
Primary KPI ← driver metrics ← diagnostic metrics. Example: signups ← (visits × CVR) ← (impressions × CTR). Every driver gets a target; diagnostics get "watch" status only.

### Step 2: Baseline Retrieval
Pull GA4 (doddle.tool.v1.ga4.getReport) for baseline traffic/CVR. If MCP not configured → mark "⚠️ NOT AVAILABLE — GA4 not configured" and set targets from stated assumptions instead (never fabricate).

### Step 3: Write the Taxonomy
- **UTM:** `{utm_source}/{utm_medium}/{utm_campaign}` — snake_case, campaign = `[slug]_[yy][mm]`
- **Events:** `noun_verb` snake_case (`trial_started`, `checkout_completed`, `pricing_viewed`) — nouns map product objects, verbs are actions
- **dataLayer:** one `event` key; custom params under `properties`; identity via `user_id` not PII fields

### Step 4: Pre-agree the Decisions
For each KPI, write the rule as: `IF [metric] [comparison] [threshold] BY [week N] THEN [action] → [owner]`. Decisions decided now cannot be overruled later without rewriting the plan (audit note required).

### Step 5: Report Cadence
Weekly review template: metric | target | actual | status | action. Daily pulse only for launch weeks (signups, ad spend).

---

## KPI Targets Guidance

```json
{
  "primary": {
    "metric": "trial_signups_wk",
    "definition": "new signup_onboarding_completed events / wk",
    "baseline": null,
    "target": 40,
    "source_tool": "doddle.tool.v1.ga4.getReport"
  },
  "guardrails": [
    {"metric": "blended_cac", "target": "<= $150", "source_tool": "doddle.tool.v1.hubspot.contacts"},
    {"metric": "email_unsub_rate", "target": "<= 0.5%/send", "source_tool": "doddle.tool.v1.hubspot.contacts"}
  ]
}
```

If a baseline is unavailable, set the target from the brief's assumption and record the assumption in `decisions`.

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Dashboard-first thinking | 40 widgets, no decisions | One KPI tree + decision rules |
| Fabricated baselines | Targets calibrated on fake data | ⚠️ NOT AVAILABLE + assumed targets, flagged |
| No guardrails | Growth bought by scaling CAC | Ceiling KPIs alongside primary |
| Taxonomy by vibe | utm_* drift makes attribution unusable | Locked taxonomy table; changes require plan revision |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Events added after launch | Weeks of data lost | taxonomy frozen pre-launch |
| PII in dataLayer | Compliance risk; GA policies | ids + role, never email/name |
| Attribution model picked late | Reports rebuilt mid-flight | Note model (default: last-touch primary, multi-touch secondary) |

---

## MCP Tool Integration

| Tool ID | When to Use | Data | Fallback |
|---------|-------------|------|----------|
| doddle.tool.v1.ga4.getReport | Baseline traffic/CVR/goals | Sessions, conversions | "⚠️ NOT AVAILABLE" |
| doddle.tool.v1.hubspot.contacts | CRM-side baseline (leads, deals) | Contacts, deals | "⚠️ NOT AVAILABLE" |

If tools are unavailable: proceed with stated assumptions, mark every assumed number, list setup instructions at the end of `tracking_plan`.

---

## Related Skills

- `doddle.marketing.marketing-intake` — supplies the KPI targets to formalize
- `doddle.marketing.analytics-attribution` — the measurement engine; decision rules target its reports
- `doddle.marketing.media-reallocator` (planned) — consumes week-N data against these targets
