---
name: saas-analytics
id: doddle.saas.analytics
version: 1.0.0
blueprint: ./blueprint.yaml
description: PQL scoring, TTV, funnel diagnosis from GA4 and CRM. Use for tracking gaps, attribution, handoff SLA. For copy fixes see saas-onboarding.
---

# SaaS Analytics

Measure aha, not pageviews. Calls analytics-attribution, adds PQL model.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- PQL definition disputed
- TTV unknown or rising
- Sales complains about lead quality

## Initial Assessment

1. **Setup**
   - Context: channels, tracking, funnel?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Channels, campaigns, tracking setup |
| goal | string | no | Measurement goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| measurement_audit | markdown | Gaps + attribution findings |
| pql_dashboard | json | Thresholds, TTV, stages |
| action_list | markdown | Prioritized fixes |

---

## Core Framework

### Step 1: Audit
Call `analytics-attribution` for tracking + ROI gaps.

### Step 2: Score
Fit + intent + aha recency → PQL tiers.

### Step 3: SLA
Handoff rules +Stage-0 honesty.

---

## Detailed Guidance

### PQL

**Checklist:**
- [ ] Aha event defined + instrumented
- [ ] Score = fit x intent x recency, not MQL points
- [ ] No raw PII in ledger — hashes only
- [ ] Slippage reasons coded weekly

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Vanity MQLs | Sales ignore | PQL + SLA |
| No TTV | Can't prioritize | TTV per cohort |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| PQL rate | Signup → PQL | Up | HubSpot |
| TTV p50 | Median to aha | Down | GA4 |

---

## Decision Tree

No events → instrumentation list first. Score drift → re-tier monthly.

---

## Quick Assessment Checklist

1. [ ] Context + goal?
2. [ ] Events live?

---

## Expected Output Format

### Measurement Audit
[Gaps + PQL model]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Dirty data | Score noise | Tracking fix first |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Funnel | Steps, TTV | no |
| doddle.tool.v1.hubspot.contacts | Stages | Lifecycle | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Funnel read | Diagnosis |

---

## Related Skills

- **saas-trial**: Handoff consumer
- **saas-dunning**: Churn input

---

## Questions to Ask

1. Context (channels/tracking/funnel) + goal?
