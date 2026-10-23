---
name: agency-reporting
id: doddle.agency.reporting
version: 1.0.0
blueprint: ./blueprint.yaml
description: When an agency reports results to a client: monthly reports, KPI dashboards, ROI proof, QBR preparation, or retention narratives. Also use when the user mentions "client report," "monthly report," "QBR," "dashboard," "show results to the client," "ROI proof," "retainer review," or "reporting cadence." Produces a client-ready report, machine-readable KPI rollup, and prioritized recommendations.
---

# Agency Reporting

Reports are retention instruments — they prove the retainer's worth and set up the next ask. This skill turns engagement data into a client-ready narrative: results vs. targets, what happened and why, and what to do next — plus a machine-readable KPI rollup for dashboards and a recommendations list that drives the next period's scope.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Weekly/monthly client reporting is due
- Preparing a QBR (quarterly business review)
- Building or refreshing a client KPI dashboard
- A retainer is up for renewal and needs a value case
- Client complained "we don't know what you're doing for us"

## Initial Assessment

Before compiling, evaluate:

1. **Engagement state**
   - KPIs and targets from the SOW or onboarding success criteria?
   - Reporting period and cadence promised?
2. **Data state**
   - Actuals available from MCP (GA4, HubSpot) or client-side? Which are missing?
3. **Audience**
   - Report read by the day-to-day contact (detail) or the signer (summary-first)?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Engagement scope, KPIs, reporting period |
| data | string | no | Actual performance data; pull via MCP or ask |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Client-ready report: results vs targets, highlights, blockers, next steps |
| kpi_summary | json | Metric rollup: target, actual, delta, status |
| recommendations | markdown | Prioritized next-period recommendations with impact estimates |

---

## Core Framework

### Step 1: Score Against Targets First
The report opens with the scoreboard: every KPI, its target, actual, delta, status (🟢/🟡/🔴). A report that buries the numbers in prose reads as spin. If targets don't exist (onboarding skipped criteria), say so and set them now — flag the gap.

### Step 2: Narrate What Happened and Why
For each notable movement: what we did, what the data shows, the causal read (labeled honestly — correlation vs. causation), and the blocker if red. Blame-free but not vague: "organic declined 12% because [known event]" beats "performance was mixed."

### Step 3: Never Fabricate a Number
Data reliability applies verbatim: MCP for actuals; missing data = "⚠️ NOT AVAILABLE — [source] not configured" with setup pointer. A report with invented numbers is the fastest way to lose a client (and the account).

### Step 4: Recommendations with Impact Estimates
3-5 prioritized recommendations for next period, each with expected impact, effort, and which KPI it moves. Ties the report forward — clients renew on trajectory, not nostalgia.

### Step 5: The Renewal Thread
Every report ends with next period's plan preview and, near renewal, an explicit value summary (cumulative outcomes vs. investment). The QBR version adds: strategic review, scope fit, and the next-quarter ask.

---

## KPI Summary Guidance

```json
{
  "period": "2026-10-01_2026-10-31",
  "kpis": [
    {"metric": "qualified_leads", "target": 40, "actual": 47, "delta": "+17%", "status": "on_track"},
    {"metric": "cost_per_lead", "target": 120, "actual": 96, "delta": "-20%", "status": "on_track"},
    {"metric": "site_conversion", "target": 0.03, "actual": 0.024, "delta": "-20%", "status": "at_risk"}
  ],
  "data_sources": ["ga4.getReport", "hubspot.contacts"],
  "unavailable": ["meta-ads spend — NOT AVAILABLE (not configured)"]
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Activity reports (what we did) | Outputs ≠ value; renewal becomes a debate | Scoreboard-first: targets vs actuals |
| No forward thread | Report is a rear-view mirror | End with next-period plan + recommendations |
| Hiding red metrics | Trust collapses on the first surprise | Lead with status flags; honest causal reads |
| One report for both audiences | Sponsor skims, PM drowns | Summary-first structure for signers |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Invented numbers | Fatal to trust; data reliability violation | MCP or ⚠️ NOT AVAILABLE — no exceptions |
| Metrics without targets | Nothing to score against | Set criteria at onboarding; flag if missing |
| 40-metric dashboards | Nobody reads them | 3-5 primary KPIs; detail in appendix |

---

## MCP Tool Integration

| Tool ID | When to Use | Data | Fallback |
|---------|-------------|------|----------|
| doddle.tool.v1.ga4.getReport | Traffic/conversion actuals | Sessions, conversions | "⚠️ NOT AVAILABLE" |
| doddle.tool.v1.hubspot.contacts | Pipeline/lead actuals | Contacts, deals | "⚠️ NOT AVAILABLE" |

---

## Related Skills

- `doddle.agency.client-onboarding` — supplies the success criteria this scores against
- `doddle.agency.proposals` — the promised outcomes this must prove
- `doddle.marketing.analytics-attribution` — deeper attribution analysis when asked "why"
- `doddle.marketing.measurement-plan` — KPI definitions and decision rules consumed here
