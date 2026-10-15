---
name: gtm-enablement
id: doddle.gtm.enablement
version: 1.0.0
blueprint: ./blueprint.yaml
description: One brief to decks, one-pagers, battlecards, ramp. Use for new reps and launches.
---

# GTM Enablement

What reps send = what wins. Calls b2b-demo for click base.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Asset sprawl, no source of truth
- Ramp >60d
- Battlecards stale

## Initial Assessment

1. **Brief**
   - Context: product, buyer, use case?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, buyer, use case |
| goal | string | no | Enablement goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| asset_gap | markdown | Sent vs exists |
| enablement_kit | json | Deck, 1-pager, battlecard refs |
| ramp_plan | markdown | Cert + shadow + deals |

---

## Core Framework

### Step 1: Base
Call `doddle.b2b.demo` for click-path + script.

### Step 2: Kit
One brief → 3 assets, no forked copies.

### Step 3: Ramp
Certify → shadow → first 3 deals reviewed.

---

## Detailed Guidance

### Kit

**Checklist:**
- [ ] Single source in Notion, versioned
- [ ] Battlecard per top-3 rival, traps included
- [ ] Ramp exit = delivered demo + mutual plan, not quiz

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Deck zoo | Reps guess | One kit |
| Quiz ramp | False ready | Live demo cert |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Ramp days | Hire → first win | Down | HubSpot |
| Asset use | Kit opens / opp | Up | Notion |

---

## Decision Tree

No demo base → b2b-demo first. Stale cards → win-loss refresh.

---

## Quick Assessment Checklist

1. [ ] Enablement context?

---

## Expected Output Format

### Enablement Kit
[Gap + kit + ramp]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Forked decks | Drift | Single source |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Source | Decks, docs | no |
| doddle.tool.v1.hubspot.deals | Usage | Asset attach | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Kit build | Assets |

---

## Related Skills

- **gtm-messaging**: Message input
- **b2b-demo**: Click input

---

## Questions to Ask

1. Product/buyer context?
