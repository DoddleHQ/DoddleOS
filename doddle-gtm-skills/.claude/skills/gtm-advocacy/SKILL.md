---
name: gtm-advocacy
id: doddle.gtm.advocacy
version: 1.0.0
blueprint: ./blueprint.yaml
description: Turn customers into proof: references, reviews, cases, community. Use when proof thin, sales needs logos, or reviews flat. For cases, see sales-enablement.
---

# GTM Advocacy

Ask → approve → publish → amplify. Reviews flywheel + reference bench.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Deals stall for lack of peer proof
- Reviews <4.3 or volume flat
- Zero referenceable logos per segment
- Expansion signals ignored

## Initial Assessment

1. **Base**
   - NPS / CSAT? Happy accounts named?
   - Ask permission culture? Legal blocks?
2. **Proof gap**
   - Which segment lacks case? Which rival cited?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product_offer | string | yes | Offer + outcomes; ask if missing |
| segment | string | no | Proof gap segment; infer if missing |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Reference bench, review plan, case pipeline |
| action_list | json | Advocacy actions with owner + effort |

---

## Core Framework

### Step 1: Recruit
Happy → asked → permissioned. Bench per segment.

### Step 2: Publish
Case pipeline: draft → approve → publish in 14 days.

### Step 3: Amplify
Reviews → social → sales deck → expansion triggers.

---

## Detailed Guidance

### Recruitment

**Checklist:**
- [ ] Bench: 3 refs per segment minimum
- [ ] Ask moments: onboarding win, renewal, support save
- [ ] Incentive: early access, community, not cash

### Cases + Reviews

**Checklist:**
- [ ] Case: pain → action → metric, 1 page
- [ ] Review asks: G2, Capterra, GBP per motion
- [ ] Response SLA: all reviews <48h

### Amplification

**Checklist:**
- [ ] Sales: proof mapped to objections
- [ ] Marketing: quotes → ads, pages, PR
- [ ] Expansion: advocate health → upsell trigger

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Ask only at renewal | Too late | Ask at wins |
| One mega-case | No coverage | 3 small per segment |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Draft never approved | Dies in legal | Pre-approved template |
| Ignore negatives | Festers | Reply + fix loop |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count cases | Vanity | Usage in deals |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Reference coverage | Segments with 3+ refs | 100% | CRM |
| Review velocity | New reviews / mo | Growing | G2/GBP |
| Rating | Avg stars | >4.3 | Listings |
| Case usage | Deals citing proof | >50% | Enablement |
| Advocacy-sourced | Expansion $ | Tracked | CRM |

---

## Decision Tree

No refs → recruit before asking for public. Rating low → fix + reply before scaling asks. Proof unused → map to objections.

---

## Quick Assessment Checklist

1. [ ] Offer + outcomes?
2. [ ] Happy accounts?
3. [ ] Proof gap segment?
4. [ ] Review platforms?
5. [ ] Legal constraints?

---

## Expected Output Format

### Bench
[Refs per segment]

### Pipeline
[Cases + reviews plan]

### Amplification
[Sales + marketing use]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Ask fatigue | Same 2 logos | Rotate bench |
| Approval stall | Drafts rot | 7-day nudge + short form |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Happy-account find | Health, tenure | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Review impact | Branded queries | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Case production | Drafts, decks |
| copywriter | Quote polish | Proof copy |
| researcher | Review mining | Theme analysis |

---

## Related Skills

- **gtm-win-loss**: Proof gaps
- **gtm-channel**: Partner proof
- **referral-program**: Flywheel mechanics

---

## Questions to Ask

1. Offer + outcomes delivered?
2. Happy accounts to recruit?
3. Proof gap segment?
