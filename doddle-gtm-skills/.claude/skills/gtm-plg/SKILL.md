---
name: gtm-plg
id: doddle.gtm.plg
version: 1.0.0
blueprint: ./blueprint.yaml
description: Choose PLG vs SLG with loops and PQL triggers. Use for self-serve vs sales-assist decisions.
---

# GTM PLG

Loops acquire, triggers hand off. Calls revops for funnel truth.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- PLG vs SLG debate unresolved
- Self-serve stalls at activation
- Sales wants PQLs, product resists

## Initial Assessment

1. **Funnel**
   - Context: product, funnel, CRM state?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, funnel, CRM state |
| goal | string | no | Motion goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| motion_audit | markdown | Readiness + gaps |
| plg_loops | json | Invite, usage, content loops |
| slg_triggers | markdown | PQL + handoff rules |

---

## Core Framework

### Step 1: Ops
Call `revops` for lifecycle + scoring truth.

### Step 2: Loops
One loop instrumented end-to-end before adding.

### Step 3: Triggers
PQL = fit x aha x recency, SLA attached.

---

## Detailed Guidance

### Loops

**Checklist:**
- [ ] Single loop metric owned weekly
- [ ] Viral actions preserve core value
- [ ] Sales trigger fires on behavior, not form fill

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| PLG theater | Signup with sales gate | Self-serve aha first |
| No SLA | PQLs rot | Handoff + time budget |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Loop coefficient | Invites → activated | >1 | GA4 |
| PQL → opp | Conversion | Up | HubSpot |

---

## Decision Tree

No aha → SLG assist first. Aha + virality → PLG loop.

---

## Quick Assessment Checklist

1. [ ] Funnel context?

---

## Expected Output Format

### Motion Audit
[Readiness + loops + triggers]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Vanity signup | No activation | Aha before scale |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Funnel | Steps | no |
| doddle.tool.v1.hubspot.contacts | Stages | Lifecycle | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Motion design | Loops |

---

## Related Skills

- **saas-trial**: Loop surface
- **saas-analytics**: PQL model

---

## Questions to Ask

1. Product/funnel context + goal?
