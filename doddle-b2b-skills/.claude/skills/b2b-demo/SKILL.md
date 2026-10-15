---
name: b2b-demo
id: doddle.b2b.demo
version: 1.0.0
blueprint: ./blueprint.yaml
description: Demos that close with click-path and talk track. Use for live demos and POC scoping.
---

# B2B Demo

Situation → click → value, never tour. Calls product-marketing for message.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Demo → proposal <30%
- New feature or vertical demo
- POC scope creep

## Initial Assessment

1. **Buyer**
   - Context: product, buyer, use case?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Product, buyer, use case |
| goal | string | no | Demo goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| demo_audit | markdown | Deck vs live gaps |
| click_path | json | Clicks with fallbacks |
| demo_script | markdown | Talk track |

---

## Core Framework

### Step 1: Message
Call `product-marketing` for positioning input.

### Step 2: Path
3 clicks max to value, backup dataset ready.

### Step 3: Close
POC exit criteria + dated next step.

---

## Detailed Guidance

### Live Rules

**Checklist:**
- [ ] Hero click in <2 min
- [ ] Customer story per click, not feature list
- [ ] Fallback video if live breaks
- [ ] POC has success metric + date

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Full tour | Lost attention | Use-case path |
| No next step | Stall | Dated mutual plan |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Demo → proposal | Conversion | >40% | HubSpot |
| POC win | POC → closed | Up | HubSpot |

---

## Decision Tree

No use case → discovery again. Tech win unclear → POC scope before proposal.

---

## Quick Assessment Checklist

1. [ ] Product + buyer context?

---

## Expected Output Format

### Demo Script
[Clicks + talk track]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Demo gods | Live break | Backup video |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Asset base | Decks, docs | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Demo assets | Click paths |

---

## Related Skills

- **b2b-discovery**: Use-case input
- **b2b-proposals**: Demo → proposal

---

## Questions to Ask

1. Product + buyer + use case?
