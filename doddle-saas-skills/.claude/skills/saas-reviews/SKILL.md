---
name: saas-reviews
id: doddle.saas.reviews
version: 1.0.0
blueprint: ./blueprint.yaml
description: G2/Capterra flywheel that lifts rating and velocity. Use for review gaps and response SLA.
---

# SaaS Reviews

Ask power users in-app, respond in 24h, recover laggards.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Rating <4.5 or velocity flat
- No ask flow in product
- Negative reviews unanswered

## Initial Assessment

1. **Base**
   - Product? Primary site?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product_name | string | yes | Product name |
| review_site | string | no | Primary site |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| review_audit | markdown | Rating + gaps |
| ask_flow | json | In-app + email asks |
| response_playbook | markdown | Templates |

---

## Core Framework

### Step 1: Audit
Rating, recency, response SLA.

### Step 2: Ask
Power-user trigger (aha x3 + 30d retained).

### Step 3: Respond
24h SLA, product fix loop for themes.

---

## Detailed Guidance

### Asks

**Checklist:**
- [ ] Ask after value, never on signup
- [ ] 1-click link, no login maze
- [ ] Detractor → support, promoter → public

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Blast all | Review gating risk | Triggered asks |
| Ignore negatives | Trust loss | 24h + fix |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Velocity | Reviews / 30d | Up | Manual |
| Response SLA | Median hours | <24 | Manual |

---

## Decision Tree

Low count → ask flow first. Low rating → fix themes + recovery.

---

## Quick Assessment Checklist

1. [ ] Product + site?

---

## Expected Output Format

### Review Pack
[Audit + asks + responses]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Incentivized spam | Removal | No quid pro quo |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Advocates | Power users | no |
| doddle.tool.v1.ga4.getReport | Usage | Retained cohorts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Responses | Templates |

---

## Related Skills

- **saas-expansion**: Advocacy → referral
- **saas-dunning**: Detractor save

---

## Questions to Ask

1. Product + review site?
