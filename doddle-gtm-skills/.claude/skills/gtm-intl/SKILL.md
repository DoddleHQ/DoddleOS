---
name: gtm-intl
id: doddle.gtm.intl
version: 1.0.0
blueprint: ./blueprint.yaml
description: Prioritize locales and ship min viable localization. Use for market expansion.
---

# GTM Intl

Demand proof before translation. One locale done beats five started.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Expansion ask with no ranking
- Translation without payments/support
- EU/data-residency blind spots

## Initial Assessment

1. **Markets**
   - Context: traction, constraints?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Markets, traction, constraints |
| goal | string | no | Expansion goal |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| market_rank | markdown | Ranked locales + proof |
| locale_pack | json | Pages, payments, support min |
| rollout_plan | markdown | Sequence + gates |

---

## Core Framework

### Step 1: Rank
Demand + willingness-to-pay + support cost.

### Step 2: Pack
Min: pricing page, checkout, DPA, support hours.

### Step 3: Gate
Pilot revenue before second locale.

---

## Detailed Guidance

### Expansion

**Checklist:**
- [ ] Payment method + tax covered per locale
- [ ] Support hours stated, no fake 24/7
- [ ] No invented demand — tool or NOT AVAILABLE

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Translate all | Cost, no return | Min pack + pilot |
| Ignore residency | Deal blocker | DPA + region first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Pilot revenue | Locale ARR / q | Hurdle | HubSpot |

---

## Decision Tree

No demand proof → test with English + local payment first.

---

## Quick Assessment Checklist

1. [ ] Markets context?

---

## Expected Output Format

### Market Rank
[Locales + packs]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Thin locale | Bounce | Full min pack or skip |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.dataforseo.serpGoogle | Demand | SERP per locale | no |
| doddle.tool.v1.semrush.keywordResearch | Sizing | Keywords | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Market intel | Demand |

---

## Related Skills

- **gtm-launch**: Rollout execution
- **gtm-pricing**: Locale pricing

---

## Questions to Ask

1. Markets + constraints?
