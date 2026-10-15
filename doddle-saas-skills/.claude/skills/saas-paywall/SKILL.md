---
name: saas-paywall
id: doddle.saas.paywall
version: 1.0.0
blueprint: ./blueprint.yaml
description: Lift free-to-paid via paywall and upgrade-moment CRO. Use for usage walls, seat upsell, annual nudges. For pricing tiers see saas-pricing.
---

# SaaS Paywall

Right moment + right offer + proof. Calls paywall-upgrade-cro, adds SaaS trigger map.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Free → paid stall at limits
- New paywall or packaging change
- Annual vs monthly decision friction

## Initial Assessment

1. **Wall**
   - Paywall URL? Trigger event?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| paywall_url | string | yes | Paywall or upgrade screen URL |
| plan | string | no | Target plan or tier |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| paywall_audit | markdown | Scored audit with copy/design notes |
| upgrade_playbook | markdown | Trigger moments + framing |
| test_plan | json | Hypotheses ordered by impact |

---

## Core Framework

### Step 1: Wall
Call `paywall-upgrade-cro` for clarity, proof, CTA.

### Step 2: Moment
Usage-limit vs value-moment mapping.

### Step 3: Offer
Annual framing, trial extension vs discount.

---

## Detailed Guidance

### Triggers

**Checklist:**
- [ ] Wall at value moment, not on open
- [ ] Usage meter visible pre-wall
- [ ] Proof (logos, numbers) beside CTA
- [ ] Dismiss path preserves state

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Wall on landing | No value felt | Wall at limit |
| Discount first | Margin leak | Annual framing first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Wall CVR | Views → paid | Up | GA4 |
| Expansion attach | Upsell take | Up | Stripe |

---

## Decision Tree

Low views → trigger earlier. High views low convert → offer/proof fix.

---

## Quick Assessment Checklist

1. [ ] Paywall URL + trigger?
2. [ ] Target plan?

---

## Expected Output Format

### Paywall Audit
[Scores + fixes]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No traffic split | Can't A/B | Ship + measure |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Wall funnel | Views, CVR | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Audit | Priorities |

---

## Related Skills

- **saas-pricing**: Tier context
- **saas-expansion**: Post-upgrade motion

---

## Questions to Ask

1. Paywall URL + trigger moment?
