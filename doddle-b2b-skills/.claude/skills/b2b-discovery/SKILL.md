---
name: b2b-discovery
id: doddle.b2b.discovery
version: 1.0.0
blueprint: ./blueprint.yaml
description: MEDDIC-lite discovery with stakeholder map and no-go discipline. Use for qualification and deal review.
---

# B2B Discovery

Qualify fast, disqualify faster. Calls customer-research, outputs exit criteria.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Deals stall post-first-call
- Single-threaded risk
- No-go discipline missing

## Initial Assessment

1. **Deal**
   - Context: stakeholders, notes?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Deal, stakeholders, notes |
| goal | string | no | Qualification goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| discovery_audit | markdown | Gaps vs MEDDIC-lite |
| stakeholder_map | json | Roles + coverage |
| qualification_pack | markdown | Questions + exit + recycle |

---

## Core Framework

### Step 1: Intel
Call `customer-research` for stakeholder context.

### Step 2: Map
Champion, blocker, econ buyer, users — coverage %.

### Step 3: Exit
Go / no-go / recycle with reason + date.

---

## Detailed Guidance

### MEDDIC-lite

**Checklist:**
- [ ] Metrics, decision process, paper process asked
- [ ] Multi-threaded over threshold, never single
- [ ] Recycle has reason + re-entry trigger

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Happy ears | Slip surprise | Exit criteria |
| No econ buyer | No close | Map before demo |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Qual rate | First → qualified | Up | HubSpot |
| Slip rate | Pushed deals | Down | HubSpot |

---

## Decision Tree

No champion → find or recycle. No process → discovery again before demo.

---

## Quick Assessment Checklist

1. [ ] Deal context?

---

## Expected Output Format

### Discovery Audit
[Gaps + map]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Thin notes | Can't score | Call plan template |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Stage data | Deals | no |
| doddle.tool.v1.notion.pages | Notes | Call docs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Qualification | Exit logic |

---

## Related Skills

- **b2b-demo**: Qualified handoff
- **b2b-list**: Account context

---

## Questions to Ask

1. Deal context + stakeholders?
