---
name: gtm-compete
id: doddle.gtm.compete
version: 1.0.0
blueprint: ./blueprint.yaml
description: Intel loop to battlecard refresh. Use for rival moves and loss patterns.
---

# GTM Compete

Learn from losses, arm with traps. Calls win-loss.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Loss rate to one rival rising
- Battlecard >90d stale
- Rival reprices or relaunches

## Initial Assessment

1. **Rival**
   - Competitor + own offer?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| competitor | string | yes | Rival name |
| product_offer | string | no | Own offer and proof |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| intel_brief | markdown | Moves + shifts |
| trap_map | json | Traps with proof |
| battlecard_refresh | markdown | Updated card + tracks |

---

## Core Framework

### Step 1: Learn
Call `win-loss` for loss coding + traps.

### Step 2: Trap
Landmine per rival claim, proof attached.

### Step 3: Arm
Card + 2 talk tracks (exec, user).

---

## Detailed Guidance

### Traps

**Checklist:**
- [ ] Every trap has proof ref, no FUD
- [ ] Loss interview quoted (anon), not invented
- [ ] Card versioned + dated

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| FUD card | Loses trust | Proof traps |
| Stale card | Wrong pricing | 30d refresh on moves |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Win rate vs rival | Head-to-head | Up | HubSpot |

---

## Decision Tree

No loss data → interview 3 losses before card rewrite.

---

## Quick Assessment Checklist

1. [ ] Competitor + offer?

---

## Expected Output Format

### Battlecard Refresh
[Intel + traps + card]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Invented intel | Wrong moves | Tool or NOT AVAILABLE |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.domainOverview | Rival moves | Traffic, pages | no |
| doddle.tool.v1.notion.pages | Loss notes | Interviews | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Card build | Talk tracks |

---

## Related Skills

- **gtm-win-loss**: Loss source
- **gtm-messaging**: Trap language

---

## Questions to Ask

1. Competitor + own offer?
