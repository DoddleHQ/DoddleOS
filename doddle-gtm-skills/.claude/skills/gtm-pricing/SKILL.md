---
name: gtm-pricing
id: doddle.gtm.pricing
version: 1.0.0
blueprint: ./blueprint.yaml
description: Packaging and guardrails for launch. Use for tiers, annual framing, discount fences.
---

# GTM Pricing

Price the value, fence the discount. Calls pricing-strategy.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New packaging or packaging change
- Discount leakage
- Annual push stalls

## Initial Assessment

1. **Deal**
   - Context: product, pricing, motion?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, pricing, market, motion |
| goal | string | no | Pricing goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| pricing_audit | markdown | Metric + tier diagnosis |
| tier_model | json | Tiers + fences |
| guardrail_notes | markdown | Floors + approvals |

---

## Core Framework

### Step 1: Metric
Call `pricing-strategy` for value metric.

### Step 2: Tiers
Good/better/best + decoy + annual frame.

### Step 3: Fence
Floor + approver per tier.

---

## Detailed Guidance

### Fences

**Checklist:**
- [ ] Value metric ties to outcome
- [ ] Enterprise fence (contact-us) scoped
- [ ] No verbal discounts — matrix only

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Seat-only default | Misaligned value | Metric test |
| Discount-first annual | Margin leak | Frame + term first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Discount avg | Mean discount | Down | HubSpot |

---

## Decision Tree

Leakage high → fences before packaging redo.

---

## Quick Assessment Checklist

1. [ ] Pricing context?

---

## Expected Output Format

### Pricing Audit
[Metric + tiers + fences]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No data | Guess tiers | Audit + test |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Deal mix | Sizes, discounts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Tier logic | Packaging |

---

## Related Skills

- **gtm-strategy**: Launch context
- **b2b-negotiation**: Fence consumer

---

## Questions to Ask

1. Product/pricing context + goal?
