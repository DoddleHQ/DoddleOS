---
name: b2b-onboarding
id: doddle.b2b.onboarding
version: 1.0.0
blueprint: ./blueprint.yaml
description: SOW to value in 30 days. Use for kickoff, success plans, churn defense. For QBRs see b2b-qbr.
---

# B2B Onboarding

Value fast or churn early. Calls email-sequence for comms, synthesizes kickoff pack.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New SOW signed, kickoff pending
- Onboarding stalls past 30d
- Scope creep threatens value

## Initial Assessment

1. **Scope**
   - Client? Goals, timeline, comms cadence?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| client_name | string | yes | Client name |
| brief | string | yes | Scope, goals, timeline, cadence |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| kickoff_pack | markdown | Agenda, roles, criteria, comms |
| value_plan | json | 30-day milestones + owners |
| risk_register | markdown | Risks + mitigations |

---

## Core Framework

### Step 1: Comms
Call `email-sequence` for kickoff + weekly cadence.

### Step 2: Value
One measurable win in 30d, owner + date.

### Step 3: Risk
Red / yellow flags with mitigation owner.

---

## Detailed Guidance

### Kickoff

**Checklist:**
- [ ] Success criteria signed, not vibes
- [ ] Weekly comms owner + channel set
- [ ] Value milestone dated in first 30d

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Kickoff theater | No criteria | Sign success first |
| No risk log | Surprise churn | Register + owner |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| TTV | Signed → first value | <30d | HubSpot |

---

## Decision Tree

No criteria → define before kickoff. Stalled → risk review + re-scope.

---

## Quick Assessment Checklist

1. [ ] Client + brief?

---

## Expected Output Format

### Kickoff Pack
[Agenda + plan + risks]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Scope creep | No value | Re-scope + date |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Deal link | Stage | no |
| doddle.tool.v1.notion.pages | Plan base | Docs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| continuity-specialist | Success plan | Milestones |

---

## Related Skills

- **b2b-qbr**: Post-onboarding reviews
- **b2b-retainers**: Recurring wrapper

---

## Questions to Ask

1. Client + scope brief?
