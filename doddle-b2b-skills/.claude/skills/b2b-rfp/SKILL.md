---
name: b2b-rfp
id: doddle.b2b.rfp
version: 1.0.0
blueprint: ./blueprint.yaml
description: Answer RFPs and security reviews fast. Use for bid/no-bid, response kit, redlines.
---

# B2B RFP

Shall-win first, then answer once, reuse always.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New RFP or security questionnaire
- Redlines stall legal
- Win rate <20%

## Initial Assessment

1. **Bid**
   - Context: requirements, deadline?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | RFP, requirements, deadlines |
| goal | string | no | Win theme |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| rfp_audit | markdown | Bid/no-bid + effort |
| response_kit | json | Answers + proof + opens |
| risk_register | markdown | Redlines + gaps + owners |

---

## Core Framework

### Step 1: Triage
Win probability x deal size vs effort.

### Step 2: Draft
Reuse library first, new writing last.

### Step 3: Risk
Security + legal gaps with owners + dates.

---

## Detailed Guidance

### Response

**Checklist:**
- [ ] No-bid has reason logged, not silent
- [ ] Every claim has proof ref
- [ ] Open items dated, never TBD
- [ ] Security answers versioned

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Bid everything | Burnout | Triage gate |
| Custom promises | Delivery pain | Library + fences |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Win rate | Submitted → won | >25% | HubSpot |
| Cycle time | Open → submit | Down | Manual |

---

## Decision Tree

Low fit + high effort → no-bid with reason. Security gap → owner + date before submit.

---

## Quick Assessment Checklist

1. [ ] RFP context + deadline?

---

## Expected Output Format

### RFP Audit
[Bid decision + kit]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Last-minute | Rushed errors | Triage at receipt |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.notion.pages | Library | Past answers | no |
| doddle.tool.v1.hubspot.deals | Deal link | Stage | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Response kit | Drafts |

---

## Related Skills

- **b2b-proposals**: Win → SOW
- **b2b-discovery**: Win themes

---

## Questions to Ask

1. RFP context + deadline?
