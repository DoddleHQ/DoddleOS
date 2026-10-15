---
name: saas-emails
id: doddle.saas.emails
version: 1.0.0
blueprint: ./blueprint.yaml
description: Trial, activation, dunning, winback emails as one lifecycle drip. Use for day 0/3/7/13, past-due, 30/60/90 winback. For one-off sequences see email-sequence.
---

# SaaS Emails

One lifecycle, not five tools. Calls email-sequence, adds SaaS triggers + suppression.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Trial drip missing or generic
- Past-due + winback ad hoc
- Activation email underperforms

## Initial Assessment

1. **Lifecycle**
   - Brief: type, trigger, goal, count?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Type, trigger, goal, count |
| audience | string | no | Segment |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| drip_pack | markdown | Sequences with timing + CTAs |
| variant_pack | json | Subject/CTA variants |
| send_checklist | markdown | Triggers, suppression, QA |

---

## Core Framework

### Step 1: Map
Trial → activation → PQL → dunning → winback triggers.

### Step 2: Draft
Call `email-sequence` for full copy + variants.

### Step 3: Guard
Suppression (paid, cancelled, bounced) + QA.

---

## Detailed Guidance

### Lifecycle

**Checklist:**
- [ ] Day 0 value + 1 action, day 3 unblock, day 7 proof, day 13 expiry
- [ ] Past-due separate sender + plain-text
- [ ] Winback 30/60/90 with reason-based offer
- [ ] Unsub + preference respected

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Blast trial + marketing | Noise → churn | Lifecycle suppression |
| HTML-only dunning | Spam folder | Plain-text + 1 link |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Activation lift | Email-attributed aha | Up | HubSpot |
| Recovery rate | Past-due → paid | Up | Stripe |

---

## Decision Tree

No list hygiene → checklist first. Low open → subject + sender fix before copy rewrite.

---

## Quick Assessment Checklist

1. [ ] Brief + audience?
2. [ ] Triggers live?

---

## Expected Output Format

### Drip Pack
[Sequences + timing]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Over-send | Unsub spike | Suppression pass |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Segments | Lists, stages | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| email-wizard | Copy + timing | Drip logic |

---

## Related Skills

- **saas-onboarding**: Activation pulls forward
- **saas-dunning**: Past-due depth

---

## Questions to Ask

1. Brief (type/trigger/goal/count) + audience?
