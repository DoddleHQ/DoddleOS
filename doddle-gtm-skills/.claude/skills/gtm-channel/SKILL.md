---
name: gtm-channel
id: doddle.gtm.channel
version: 1.0.0
blueprint: ./blueprint.yaml
description: Design partner motion: tiers, enablement, deal reg, co-sell. Use when needing sourced pipeline, reseller scale, or affiliate ops. For referrals, see referral-program.
---

# GTM Channel

Tiers → enablement → registration → co-sell → sourced share.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Direct CAC too high, partners hold trust
- Inbound referrals ad-hoc, untracked
- Reseller interest but no program
- Co-sell with adjacent vendors possible

## Initial Assessment

1. **Fit**
   - Who serves same buyer pre/post you?
   - Margin to share? Deal reg appetite?
2. **Capacity**
   - Partner manager? Enablement bandwidth?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product_offer | string | yes | Offer + margin; ask if missing |
| partner_hint | string | no | Candidate types; infer if missing |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Tiers, kit, reg rules, co-sell plays |
| action_list | json | Partner actions with owner + effort |

---

## Core Framework

### Step 1: Tier
Referral → reseller → co-sell. Criteria + payout per tier.

### Step 2: Enable
Kit: pitch, demo, pricing, FAQ, deal reg.

### Step 3: Sell
Co-marketing → sourced deals → share tracked.

---

## Detailed Guidance

### Tiers & Terms

**Checklist:**
- [ ] Referral (finders fee), reseller (margin), co-sell (split)
- [ ] Entry bar + exit for dead partners
- [ ] Deal reg: 30-day protection, conflict rules

### Enablement

**Checklist:**
- [ ] One-pager, deck, demo video, pricing sheet
- [ ] Partner landing + tracking links
- [ ] Quarterly business review format

### Co-sell

**Checklist:**
- [ ] Top 10 target partners named
- [ ] 2 co-marketing plays per quarter
- [ ] Sourced-pipeline share dashboard

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| 100 logos, 0 deals | Vanity | 10 active max |
| Equal payout all | Adverse select | Tier by effort |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No reg rules | Channel conflict | Write first |
| No enablement | Partners silent | Kit + training |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count partners | Vanity | Sourced $ |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Sourced pipeline $ | Partner-originated | >20% mix | CRM |
| Active partners | ≥1 deal/qtr | ≥5 | CRM |
| Reg conflicts | Disputed deals | 0 | Manual |
| Time to first deal | Days signed→deal | <90 | CRM |

---

## Decision Tree

No manager → referral-only. Margin thin → co-sell not resell. Conflict-prone → reg before recruiting.

---

## Quick Assessment Checklist

1. [ ] Offer + margin?
2. [ ] Candidate partners?
3. [ ] Manager capacity?
4. [ ] Reg appetite?
5. [ ] Tracking in CRM?

---

## Expected Output Format

### Tiers + Terms
[Levels, payouts, bars]

### Kit + Reg
[Assets, rules]

### Co-sell Plan
[Targets, plays, dashboard]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Logo farm | 0 sourced | Prune quarterly |
| Direct conflict | AE vs partner | Reg + split credit |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Sourced tracking | Source, stage | no |
| doddle.tool.v1.hubspot.contacts | Partner contacts | Roles, owners | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Partner mapping | Candidate lists |
| sales-enabler | Kit production | Decks, sheets |
| planner | Recruit sequencing | Outreach plan |

---

## Related Skills

- **gtm-strategy**: Mix context
- **partnerships**: Tactic depth
- **referral-program**: Flywheel mechanics

---

## Questions to Ask

1. Offer + margin shareable?
2. Candidate partner types?
3. Manager + CRM tracking?
