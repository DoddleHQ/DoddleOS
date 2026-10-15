---
name: b2b-list
id: doddle.b2b.list
version: 1.0.0
blueprint: ./blueprint.yaml
description: Build tiered ICP account lists with intent triggers. Use for TAM build, A/B/C tiering. For sequencing see b2b-outbound.
---

# B2B List

TAM → tiers → triggers. Calls customer-research, outputs scored list.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New TAM or ICP refresh
- List quality tanks connect rate
- Intent sources to wire

## Initial Assessment

1. **ICP**
   - Titles, size, industry? Goal meetings/mo?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | ICP, TAM, existing data |
| goal | string | no | Pipeline goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| tam_audit | markdown | Sizing with tiers |
| tiered_list | json | Accounts + scores + triggers |
| enrich_playbook | markdown | Enrich + refresh SOP |

---

## Core Framework

### Step 1: Research
Call `customer-research` for fit + intent signals.

### Step 2: Tier
A/B/C by effort split (10/30/60).

### Step 3: Enrich
Verify + refresh cadence.

---

## Detailed Guidance

### Tiers

**Checklist:**
- [ ] Fit = title x size x tech, intent = hiring/funding/trigger
- [ ] No bought stale lists without re-verify
- [ ] Refresh 30d, recycle with reason

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Volume over fit | Burns domains | Tier + personalize |
| No triggers | Cold = ignored | Trigger-first sequencing |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Connect rate | Positive / worked | Up | HubSpot |
| Meeting quality | Held + qualified | Up | HubSpot |

---

## Decision Tree

No ICP → research first. Low connect → re-tier + triggers before copy rewrite.

---

## Quick Assessment Checklist

1. [ ] ICP + TAM context?
2. [ ] Goal?

---

## Expected Output Format

### TAM Audit
[Tiers + triggers]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Stale data | Bounce >5% | Re-verify |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Base + dedupe | Contacts | no |
| doddle.tool.v1.semrush.domainOverview | Account intel | Firmographics | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | TAM intel | Fit, triggers |

---

## Related Skills

- **b2b-outbound**: Sequencing from list

---

## Questions to Ask

1. ICP + TAM context + goal?
