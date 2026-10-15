---
name: gtm-icp
id: doddle.gtm.icp
version: 1.0.0
blueprint: ./blueprint.yaml
description: Define ICP, tier TAM, map triggers. Use for new motion or ICP refresh. For sequencing see gtm-abm.
---

# GTM ICP

Fit + intent before spend. Calls b2b-list (which calls customer-research) — depth 2, within limit.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New GTM motion or segment
- TAM too big to work
- Intent sources unclear

## Initial Assessment

1. **Market**
   - Context: product, hints, data?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, market hints, data |
| goal | string | no | Pipeline goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| icp_audit | markdown | ICP with fit criteria |
| tam_tiers | json | A/B/C with triggers |
| trigger_map | markdown | Sources + SOP |

---

## Core Framework

### Step 1: List
Call `doddle.b2b.list` for tiers + triggers.

### Step 2: Sharpen
ICP fences: in/out, deal-breakers.

### Step 3: Wire
Enrichment + refresh cadence.

---

## Detailed Guidance

### ICP

**Checklist:**
- [ ] Fit (title x size x tech) + intent (hiring/funding/trigger)
- [ ] Out-of-ICP logged with reason
- [ ] Tier effort split 10/30/60

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Everyone ICP | No focus | Fences |
| Static TAM | Rots | 30d refresh |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Tier-A coverage | Worked / total A | 100%/q | HubSpot |

---

## Decision Tree

No data → research via b2b-list first. Too big → tier harder.

---

## Quick Assessment Checklist

1. [ ] Context + goal?

---

## Expected Output Format

### ICP Audit
[Fit + tiers + triggers]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Depth breach | Schedule depth error | Keep chain ≤3 (here 2) |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Base | Contacts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | TAM | Tiers |

---

## Related Skills

- **gtm-strategy**: Full plan consumer
- **gtm-abm**: Tier-1 execution

---

## Questions to Ask

1. Product context + goal?
