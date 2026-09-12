---
name: gtm-strategy
id: doddle.gtm.strategy
version: 1.0.0
blueprint: ./blueprint.yaml
description: Build go-to-market plan: ICP, TAM, message, channel mix, launch gates. Use when launching, entering segment, or aligning product-marketing-sales. For ABM execution, see gtm-abm. For audits, see seo-mastery.
---

# GTM Strategy

Orchestrator: TAM → ICP → message → channels → launch gates →數 pipeline plan. Calls peer packs, never installs them.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New product, segment, geo, or pricing launch
- Marketing + sales misaligned on ICP / message
- Channel mix unclear (inbound vs outbound vs partners)
- Launch readiness unknown across teams

## Initial Assessment

1. **Market**
   - ICP hypothesis? TAM source + size?
   - Incumbent + differentiation in one line?
2. **Motion**
   - ACV range? Sales cycle? Self-serve possible?
   - Existing pipeline source split?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product_offer | string | yes | Product + offer + proof; ask if missing |
| icp_hint | string | no | Titles, size, industry; infer if missing |
| acv | string | no | Deal size band; default SMB/mid-market |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | ICP, TAM tiers, message house, channel mix, gates |
| action_list | json | Sequenced GTM actions with owner + effort |

---

## Core Framework

### Step 1: Size
TAM → ICP → A/B/C tiers. Fit + intent scoring.

### Step 2: Message
Positioning → message house → proof per persona.

### Step 3: Sequence
Channel mix → launch gates → 90-day plan. Call peer skills.

---

## Detailed Guidance

### Sizing & Tiers

**Checklist:**
- [ ] TAM source, filter to ICP (size, industry, geo, tech)
- [ ] A (1:1) / B (1:few) / C (1:many) effort split
- [ ] Intent signals (hiring, funding, tech, search)

### Message House

**Checklist:**
- [ ] Positioning: for X who Y, unlike Z
- [ ] 3 pillars + proof each (cases, numbers)
- [ ] Objection pre-handles (price, incumbent, timing)

### Channel + Gates

**Checklist:**
- [ ] Mix by ACV: PLG / inbound / outbound / partners / events
- [ ] Gates: product ready, assets live, reps certified, CS staffed
- [ ] 90-day milestones, kill criteria

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Everyone ICP | No focus | Tier ruthlessly |
| Channels all at once | Thin spread | 1-2 motions first |
| Launch = announce | No pipeline | Gates + pipeline bar |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No owner per gate | Slips | Named approver |
| Message untested | Falls flat | 5 customer reads |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Vanity TAM | Misleads | Workable accounts |
| No win-loss loop | Repeats losses | Feed gtm-win-loss |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Workable A accounts | Tier-A count | ≥100 | CRM |
| Gate pass rate | Gates green | 100% pre-launch | Manual |
| Sourced mix | Per-channel pipeline | Matches plan | HubSpot |
| CAC payback | Cost per $1 ARR | <12 mo | Finance |

---

## Decision Tree

ACV <$5k → PLG/inbound first. $5-50k → outbound + inbound. >$50k → ABM + partners. No proof → advocacy before scale.

---

## Quick Assessment Checklist

1. [ ] Product + proof?
2. [ ] ICP + TAM?
3. [ ] ACV + cycle?
4. [ ] Channels live?
5. [ ] Launch date fixed?

---

## Expected Output Format

### ICP + Tiers
[Segments, counts, signals]

### Message + Channels
[House, mix, budget split]

### Gates + 90-day
[Checklist, owners, milestones]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Fuzzy ICP | Low reply | Narrow + tier |
| Gate skip | Launch chaos | Freeze till green |
| No feedback | Same losses | Win-loss cadence |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | TAM / pipeline baseline | Contacts, companies | no |
| doddle.tool.v1.semrush.domainOverview | Demand sizing | Traffic, gaps | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | TAM, competitors | Sizing, gaps |
| lead-qualifier | Tiering, scoring | ICP filters |
| planner | 90-day sequencing | Milestones |

---

## Related Skills

- **gtm-abm**: Account execution
- **gtm-win-loss**: Competitive learning
- **product-marketing**: Positioning depth

---

## Questions to Ask

1. Product, offer, proof?
2. ICP hypothesis + TAM source?
3. ACV + launch date?
