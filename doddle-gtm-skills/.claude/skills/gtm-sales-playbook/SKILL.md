---
name: gtm-sales-playbook
id: doddle.gtm.sales-playbook
version: 1.0.0
blueprint: ./blueprint.yaml
description: Codify sales motion: MEDDIC, demo script, RFP kit, discount matrix, ramp. Use when onboarding reps, stages vague, demos ramble, discounts uncontrolled.
---

# GTM Sales Playbook

Qualify → demo → propose → guardrailed close → ramped reps.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Stages lack exit criteria (vibes pipeline)
- Demos feature tours, no value close
- Discounts ad-hoc, approvals unclear
- New reps ramp >90 days

## Initial Assessment

1. **Motion**
   - ACV, cycle, stakeholders? Current stages?
2. **Assets**
   - Deck, one-pagers, demo env exist?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product_offer | string | yes | Offer + proof; ask if missing |
| acv | string | no | Deal band; infer if missing |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Stages, MEDDIC, demo script, RFP kit, matrix |
| action_list | json | Rollout actions with owner + effort |

---

## Core Framework

### Step 1: Qualify
MEDDIC-lite + exit criteria per stage. Disqualify fast.

### Step 2: Show
Demo: situation → click → value. No tour.

### Step 3: Close
Mutual plan + discount matrix + ramp certification.

---

## Detailed Guidance

### Qualification

**Checklist:**
- [ ] Metrics, econ buyer, decision + paper process
- [ ] Champion test (access + action)
- [ ] Stage exits written, no skip
- [ ] No-go reasons coded

### Demo + Proposal

**Checklist:**
- [ ] 3 click-paths max, customer data
- [ ] Value recap per stakeholder
- [ ] RFP kit: boilerplate, proof, security answers
- [ ] Proposal: options (good/better), expiry

### Guardrails + Ramp

**Checklist:**
- [ ] Discount floor + approver matrix + give-gets
- [ ] Multi-thread rule over $X
- [ ] Close plan dated, mutual
- [ ] Ramp: shadow → mock → certified → first deals

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Stages = vibes | Unforecastable | Exit criteria |
| Discount to win | Margin death | Give-get + floor |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Demo everything | Bored buyer | 3 moments max |
| Single-thread | Dies on PTO | 3+ contacts |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Blame price | Hides real loss | Code reasons |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Stage conversion | Per-stage % | Improving | CRM |
| Sales cycle | Days open→close | Shrinking | HubSpot |
| Avg discount | % off list | Guardrailed | CRM |
| Ramp time | Days to quota | <90 | Manual |
| Forecast accuracy | Commit hit | >85% | CRM |

---

## Decision Tree

No stages → define exits first. Demo fails → script before training. Discount chaos → matrix before SPIF. Ramp slow → certification gate.

---

## Quick Assessment Checklist

1. [ ] Offer + ACV?
2. [ ] Stages today?
3. [ ] Demo env?
4. [ ] Discount policy?
5. [ ] Rep count?

---

## Expected Output Format

### Stages + MEDDIC
[Criteria, exits]

### Demo + RFP
[Scripts, kit]

### Matrix + Ramp
[Guardrails, cert]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Shelf playbook | Unused | Drill weekly |
| No enforcement | Skipped exits | Manager inspect |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Stage audit | Pipeline, slippage | no |
| doddle.tool.v1.hubspot.contacts | Multi-thread check | Stakeholders | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| sales-enabler | Assets, certification | Decks, drills |
| researcher | RFP boilerplate | Proof points |
| planner | Rollout | Ramp plan |

---

## Related Skills

- **gtm-win-loss**: Trap ammo
- **sales-negotiation**: Objection depth
- **sales-forecasting**: Inspection cadence

---

## Questions to Ask

1. Offer + ACV + cycle?
2. Stages + discount policy?
3. Rep count + ramp pain?
