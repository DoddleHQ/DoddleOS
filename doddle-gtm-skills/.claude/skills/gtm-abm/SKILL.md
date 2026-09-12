---
name: gtm-abm
id: doddle.gtm.abm
version: 1.0.0
blueprint: ./blueprint.yaml
description: Run account-based motion: select, personalize, orchestrate SDR/AE/ads. Use when ACV high, buying committee large, or outbound reply low. For list building, see sales-prospecting. For plan, see gtm-strategy.
---

# GTM ABM

Fit + intent → tiers → personalized plays → meetings. 1:1 / 1:few / 1:many.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- ACV >$15k or committee 3+
- Broad outbound reply <2%
- Key accounts named but untouched
- Expansion into named logos needed

## Initial Assessment

1. **Accounts**
   - List source? Fit fields? Intent signals?
2. **Capacity**
   - SDR/AE ratio? Personalization bandwidth?
   - Ad budget for 1:many?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| icp | string | yes | Titles, size, industry; ask if missing |
| account_source | string | no | List origin; infer if missing |
| acv | string | no | Deal band for tiering |
| locale | string | no | Market; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Tiers, personalization, plays, cadence |
| action_list | json | Account actions with owner + effort |

---

## Core Framework

### Step 1: Select
Fit score + intent → A/B/C. Cap A at SDR capacity.

### Step 2: Personalize
1:1 deep, 1:few vertical, 1:many programmatic.

### Step 3: Orchestrate
Warm-up → exec → SDR → ads → meeting bar.

---

## Detailed Guidance

### Selection

**Checklist:**
- [ ] Fit: size, industry, tech, geo
- [ ] Intent: hiring, funding, visits, search
- [ ] Exclude: customers, competitors, bad-fit

### Personalization

**Checklist:**
- [ ] 1:1: exec map, custom POV, direct
- [ ] 1:few: vertical pain, peer proof
- [ ] 1:many: persona ads, landing variants

### Plays

**Checklist:**
- [ ] Warm-up (ads, social, content) 2 wks
- [ ] Sequence (email + phone + social) 3-4 wks
- [ ] Handoff bar: 2+ stakeholders, pain + timeline
- [ ] No-response recycle with reason

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| 500 target accounts | No depth | A ≤50 per SDR |
| No intent | Cold waste | Intent gate |
| Marketing-only ABM | No meetings | SDR/AE SLA |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Generic copy | Ignored | Account POV first line |
| Single-thread | Dies on leave | Multi-thread 3+ |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count touches | Vanity | Meetings + progression |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Coverage | A accounts worked | 100%/qtr | CRM |
| Reply / meeting rate | Per tier | A >8% reply | CRM |
| Progression | MQA → opp | >20% | HubSpot |
| Pipeline per account | $ per A | >3x CAC | Finance |

---

## Decision Tree

No list → build fit first. No intent → warm-up only. Low capacity → shrink A tier. Reply low → rewrite POV.

---

## Quick Assessment Checklist

1. [ ] ICP + list source?
2. [ ] Intent available?
3. [ ] SDR capacity?
4. [ ] Ad budget?
5. [ ] Meeting bar defined?

---

## Expected Output Format

### Tiers
[A/B/C with counts]

### Plays
[Cadence per tier]

### Handoff
[Bar + SLA]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Too many A | Thin touches | Cut to capacity |
| No orchestration | Random acts | Shared cadence |
| No recycle | List burn | Recycle reasons |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Account baseline | Contacts, companies | no |
| doddle.tool.v1.semrush.domainOverview | Fit enrichment | Firmographics | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| lead-qualifier | Scoring, tiers | Fit filters |
| copywriter | POV, sequences | Personalization |
| sales-enabler | Exec assets | One-pagers |

---

## Related Skills

- **gtm-strategy**: Plan wrapper
- **sales-prospecting**: List mechanics
- **gtm-win-loss**: Message ammo

---

## Questions to Ask

1. ICP + account source?
2. SDR/AE capacity?
3. ACV band?
