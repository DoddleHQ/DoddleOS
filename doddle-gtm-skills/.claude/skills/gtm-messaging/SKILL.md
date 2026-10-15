---
name: gtm-messaging
id: doddle.gtm.messaging
version: 1.0.0
blueprint: ./blueprint.yaml
description: Positioning to message house with proof. Use for launches and repositioning. For assets see gtm-enablement.
---

# GTM Messaging

One house, every team speaks it. Calls product-marketing.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New product or segment message
- Sales says deck doesn't land
- Competitor reframing wins

## Initial Assessment

1. **Product**
   - Context: product, audience, proof, rivals?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, audience, proof, rivals |
| goal | string | no | Messaging goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| message_house | markdown | Pillars, proof, voice |
| proof_bank | json | Claims + refs |
| objection_map | markdown | Reframes |

---

## Core Framework

### Step 1: Position
Call `product-marketing` for strategy input.

### Step 2: House
3 pillars max, proof per pillar.

### Step 3: Arm
Objections + traps for sales.

---

## Detailed Guidance

### House

**Checklist:**
- [ ] Every claim has proof ref
- [ ] Cons + fences stated (trust)
- [ ] One-liner passes hallway test

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Feature list | No value | Pillar → proof → outcome |
| No proof | Ignored | Bank or cut claim |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Message pull-through | Deck → call usage | Up | Manual |

---

## Decision Tree

No proof → cut or mark unproven. Too many pillars → merge to 3.

---

## Quick Assessment Checklist

1. [ ] Product context?

---

## Expected Output Format

### Message House
[Pillars + proof]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Jargon house | Reps skip | Plain + proof |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Source docs | Context | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | House copy | Pillars |

---

## Related Skills

- **gtm-enablement**: Asset production
- **b2b-demo**: Demo consumer

---

## Questions to Ask

1. Product + audience + rivals?
