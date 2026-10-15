---
name: b2b-negotiation
id: doddle.b2b.negotiation
version: 1.0.0
blueprint: ./blueprint.yaml
description: Win without leaking margin via guardrails and give-gets. Use for discount pressure and procurement.
---

# B2B Negotiation

Every give has a get. Calls pricing-strategy + offers for fences.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Discount >15% requested
- Procurement stalls
- Multi-thread needed

## Initial Assessment

1. **Deal**
   - Context: size, pricing, procurement?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Deal size, pricing, procurement |
| goal | string | no | Negotiation goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| negotiation_audit | markdown | Leverage + leakage |
| guardrail_matrix | json | Floor, approvals, fences |
| giveget_playbook | markdown | Pairs + close plan |

---

## Core Framework

### Step 1: Price
Call `pricing-strategy` for value metric + fences.

### Step 2: Offer
Call `offers` for stack + guarantee design.

### Step 3: Close
Give-get pairs + dated mutual actions.

---

## Detailed Guidance

### Guardrails

**Checklist:**
- [ ] Floor + approver per tier, no verbal discounts
- [ ] Every concession = term, logo, prepay, or scope
- [ ] Single-thread over threshold → escalate, never discount
- [ ] Procurement mapped: buyer → legal → finance

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Free discount | Trains haggle | Give-get always |
| Single-thread | No leverage | Multi-thread |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Discount leakage | Avg discount | Down | HubSpot |
| Win rate | Proposal → signed | Up | HubSpot |

---

## Decision Tree

No leverage → create via multi-thread + deadline. Procurement-only → map + champion re-entry.

---

## Quick Assessment Checklist

1. [ ] Deal context?

---

## Expected Output Format

### Negotiation Audit
[Leverage + guardrails]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| End-quarter giveaway | Margin collapse | Fences pre-approved |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Deal state | Stage, size | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Close plan | Dated actions |

---

## Related Skills

- **b2b-proposals**: Proposal input
- **b2b-discovery**: Leverage context

---

## Questions to Ask

1. Deal context + procurement stage?
