---
name: b2b-qbr
id: doddle.b2b.qbr
version: 1.0.0
blueprint: ./blueprint.yaml
description: QBRs that retain and expand. Use for renewals, health reviews, expansion plays.
---

# B2B QBR

Proof + roadmap + ask. Calls revops for lifecycle truth.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Renewal or QBR upcoming
- Health unclear, expansion possible
- Churn risk flagged

## Initial Assessment

1. **Account**
   - Context: usage, tickets, revenue?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Account, usage, tickets, revenue |
| goal | string | no | QBR goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| health_audit | markdown | Usage, value, risks |
| qbr_deck | json | Slides + proof + roadmap |
| expansion_playbook | markdown | Triggers + offers |

---

## Core Framework

### Step 1: Lifecycle
Call `revops` for health + scoring truth.

### Step 2: Deck
Value delivered → roadmap → ask, 30 min max.

### Step 3: Expand
Trigger-tied offers, dated next step.

---

## Detailed Guidance

### Deck

**Checklist:**
- [ ] Value in numbers first, roadmap second
- [ ] Risk named with mitigation, not hidden
- [ ] One expansion ask, not five

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Status readout | No value | Proof + ask |
| No ask | Wasted room | One trigger offer |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Gross retention | Renewed revenue | >90% | HubSpot |
| Expansion attach | QBR → upsell | Up | HubSpot |

---

## Decision Tree

Red health → save plan before upsell. Green → expansion ask.

---

## Quick Assessment Checklist

1. [ ] Account context?

---

## Expected Output Format

### QBR Pack
[Health + deck + expansion]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No data | Gut QBR | Lifecycle fix first |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Revenue | Deals | no |
| doddle.tool.v1.hubspot.contacts | Stakeholders | Contacts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| continuity-specialist | Health read | Risks |

---

## Related Skills

- **b2b-onboarding**: Value baseline
- **b2b-referrals**: QBR → intros

---

## Questions to Ask

1. Account context + QBR goal?
