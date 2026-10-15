---
name: b2b-referrals
id: doddle.b2b.referrals
version: 1.0.0
blueprint: ./blueprint.yaml
description: Turn wins into intros via proof + ask engine. Use for client and partner referrals.
---

# B2B Referrals

Ask at value peak with proof in hand. Calls b2b-cases for asset.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Win delivered, no intro asked
- Referral motion ad hoc
- Partner intros stalled

## Initial Assessment

1. **Win**
   - Client + metric + industry?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| client_name | string | yes | Customer name |
| metric | string | yes | Result + timeframe |
| industry | string | no | Industry |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| proof_pack | markdown | One-pager from case |
| referral_engine | json | Moments, scripts, incentives |
| ask_sequences | markdown | Email + call timing |

---

## Core Framework

### Step 1: Proof
Call `b2b-cases` for case asset.

### Step 2: Moments
QBR, value milestone, renewal — ask then.

### Step 3: Ease
Named intro request, draft forwardable blurb.

---

## Detailed Guidance

### Asks

**Checklist:**
- [ ] Ask within 7d of value moment
- [ ] Named ask (who, why them), not broadcast
- [ ] Forwardable blurb supplied, 3 lines max

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Generic blast | Ignored | Named + proof |
| Late ask | Cold win | 7d window |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Intro rate | Asks → intros | >20% | HubSpot |

---

## Decision Tree

No proof → cases first. No moment → create via QBR.

---

## Quick Assessment Checklist

1. [ ] Client + metric?

---

## Expected Output Format

### Referral Engine
[Proof + asks]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No permission | Can't name | Anonymized proof |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Target map | Contacts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Ask copy | Scripts |

---

## Related Skills

- **b2b-cases**: Proof input
- **b2b-qbr**: Ask moment

---

## Questions to Ask

1. Client + metric + industry?
