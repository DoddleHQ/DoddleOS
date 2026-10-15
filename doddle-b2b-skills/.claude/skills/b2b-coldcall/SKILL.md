---
name: b2b-coldcall
id: doddle.b2b.coldcall
version: 1.0.0
blueprint: ./blueprint.yaml
description: Cold call scripts that connect: openers, bridges, objection trees. Use for AE/AE prospecting and connect-rate rescue.
---

# B2B Coldcall

Permission + reason + question in 15s. No feature dumps.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Connect → meeting <5%
- New call motion or list
- Objections kill calls

## Initial Assessment

1. **List**
   - ICP + triggers? Offer?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| icp | string | yes | ICP + triggers |
| offer | string | yes | Offer + proof |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| call_audit | markdown | List-to-connect diagnosis |
| script_pack | json | Openers, bridges, closes |
| objection_tree | markdown | Objection → reframe → question |

---

## Core Framework

### Step 1: Open
Permission + trigger + 1-line reason.

### Step 2: Bridge
Problem → question, not pitch.

### Step 3: Close
Two-time offer + SMS fallback.

---

## Detailed Guidance

### Objections

**Checklist:**
- [ ] Every objection → question, not battle
- [ ] Voicemail <20s + SMS with reason
- [ ] No-show → 2x reschedule then recycle

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Monologue | Hung up | Ask in 15s |
| No trigger | Sounds cold | Trigger-first open |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Connect → meeting | Meetings / connects | >8% | HubSpot |
| Callback rate | VM → callback | Up | Manual |

---

## Decision Tree

Low connect → list + time-of-day fix. Low convert → opener + offer fix.

---

## Quick Assessment Checklist

1. [ ] ICP + offer?

---

## Expected Output Format

### Script Pack
[Openers + trees]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Bad numbers | <5% connect | List refresh |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | List quality | Connects | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Scripts | Talk tracks |

---

## Related Skills

- **b2b-list**: List input
- **b2b-discovery**: Meeting handoff

---

## Questions to Ask

1. ICP + offer + triggers?
