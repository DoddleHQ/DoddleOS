---
name: gtm-win-loss
id: doddle.gtm.win-loss
version: 1.0.0
blueprint: ./blueprint.yaml
description: Build battlecards, run loss interviews, code reasons. Use when losing to incumbent, discounting blind, or message untested. For positioning, see product-marketing.
---

# GTM Win-Loss

Traps + proof + loss loop. Turns losses into message and product fixes.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Loss rate rising vs named competitor
- Reps discounting without guardrails
- No battlecard or stale (>6 mo)
- Product blind to loss reasons

## Initial Assessment

1. **Field**
   - Top 3 competitors faced? Loss reasons hypothesized?
2. **Data**
   - CRM loss notes usable? Interview access to buyers?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| competitor | string | yes | Rival name; ask if missing |
| product_offer | string | no | Own offer + proof; infer if missing |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Battlecard, traps, proof, interview script |
| action_list | json | Fixes with owner + effort |

---

## Core Framework

### Step 1: Map
Competitor claims → traps → own proof.

### Step 2: Card
One-page battlecard: landmines, questions, kill shots.

### Step 3: Loop
Interview → code → feed message + product.

---

## Detailed Guidance

### Battlecard

**Checklist:**
- [ ] Rival positioning + pricing (as known)
- [ ] 3 traps + discovery questions exposing them
- [ ] Proof: logos, numbers, migration stories
- [ ] When to walk away (bad-fit)

### Interviews

**Checklist:**
- [ ] 15-min script, third-party tone
- [ ] Code: price, features, trust, timing, incumbent
- [ ] 5 interviews per quarter minimum

### Feedback

**Checklist:**
- [ ] Message fixes → copywriter
- [ ] Product gaps → roadmap note
- [ ] Card refresh date stamped

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Trash-talk card | Loses trust | Facts + questions |
| No walk-away | Wastes cycles | Disqualify fast |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| 10-page card | Unused | One page |
| AE interviews own loss | Biased | Neutral interviewer |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Anecdote as trend | Misleads | Code 5+ first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Win rate vs named | Wins / (wins+losses) | Improving | CRM |
| Discount rate | Avg discount | Guardrailed | CRM |
| Card usage | Reps opening | >70% | Enablement |
| Interview cadence | Per quarter | ≥5 | Manual |

---

## Decision Tree

No card → build for top rival first. Discount chaos → guardrails before cards. Low volume → interview every loss.

---

## Quick Assessment Checklist

1. [ ] Rival + context?
2. [ ] Loss notes access?
3. [ ] Buyer interview OK?
4. [ ] Proof assets?
5. [ ] Card owner?

---

## Expected Output Format

### Battlecard
[Traps, questions, proof]

### Interview Kit
[Script, codes]

### Fixes
[Message + product]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Stale card | Wrong pricing | Expiry date |
| No adoption | PDF graveyard | 5-min drill |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.deals | Loss coding | Stages, reasons | no |
| doddle.tool.v1.semrush.domainOverview | Rival sizing | Traffic, overlap | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Rival intel | Claims, pricing |
| sales-enabler | Card production | One-pager |
| copywriter | Trap phrasing | Questions |

---

## Related Skills

- **gtm-strategy**: Plan context
- **gtm-sales-playbook**: Guardrails
- **product-marketing**: Message depth

---

## Questions to Ask

1. Which competitor?
2. Loss notes available?
3. Interview access?
