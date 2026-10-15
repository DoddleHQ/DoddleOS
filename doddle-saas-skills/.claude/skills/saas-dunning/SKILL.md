---
name: saas-dunning
id: doddle.saas.dunning
version: 1.0.0
blueprint: ./blueprint.yaml
description: Recover failed payments and at-risk accounts via dunning, save, winback. Use for involuntary churn, cancel flow, 30/60/90 winback. For general churn theory see churn-prevention.
---

# SaaS Dunning

Split involuntary vs voluntary, then recover. Calls churn-prevention, adds Stripe-aware playbook.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Failed-payment rate rising
- Cancel flow has no save path
- Winback ad hoc

## Initial Assessment

1. **Churn**
   - Context: rates, MRR, dunning state?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Churn rates, types, lifecycle |
| goal | string | no | Retention goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| dunning_audit | markdown | Involuntary vs voluntary split |
| save_playbook | markdown | Day 0/3/7/14 + cancel-save |
| winback_pack | json | 30/60/90 with offers |

---

## Core Framework

### Step 1: Diagnose
Call `churn-prevention` for taxonomy + save-rate math.

### Step 2: Dunning
Card retries + in-app banner + plain-text email.

### Step 3: Save/Winback
Reason → offer matrix, then timed winback.

---

## Detailed Guidance

### Recovery

**Checklist:**
- [ ] Day 0 in-app + email, day 3 retry, day 7 card update, day 14 pause offer
- [ ] Cancel reasons coded, save offer = reason-matched
- [ ] Stripe stub → manual review until live; never invent MRR
- [ ] Winback suppressed for refund-abuse

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Discount blast | Margin leak | Reason-matched save |
| No pause | Forced churn | Pause > cancel |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Recovery rate | Past-due → paid | Up | Stripe |
| Save rate | Cancel → kept | Up | HubSpot |

---

## Decision Tree

Involuntary heavy → dunning first. Voluntary heavy → save flow + winback.

---

## Quick Assessment Checklist

1. [ ] Churn context?
2. [ ] Stripe live or manual?

---

## Expected Output Format

### Dunning Audit
[Split + playbook]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Stub MRR | NOT AVAILABLE | Manual CSV + review |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.stripe.getMrr | MRR movement | MRR, churn | no |
| doddle.tool.v1.hubspot.contacts | At-risk list | Lifecycle | no |
| doddle.tool.v1.ga4.getReport | Cancel funnel | Drop steps | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| continuity-specialist | Save logic | Offer matrix |

---

## Related Skills

- **saas-retention**: Sibling depth
- **saas-emails**: Drip execution

---

## Questions to Ask

1. Churn context + Stripe access?
