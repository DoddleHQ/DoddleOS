---
name: gsc-reporting
id: doddle.marketing.gsc-reporting
version: 1.0.0
blueprint: ./blueprint.yaml
description: Report SEO via Search Console, GA4, index, CTR, experiments. Use when proving what moved, winner/loser analysis, forecasts, stakeholder digests. For audits, see seo-mastery. For attribution, see analytics-attribution.
---

# GSC Reporting

GSC + GA4 proof layer: performance, deltas, cannibalization evidence, forecasts, stakeholder outputs. Covers infographic block 9 (177-200).

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Proving clicks, impressions, CTR, position moves
- Winner/loser, period deltas, incident impact
- Index coverage, cannibalization evidence
- Weekly / monthly stakeholder reporting, forecasts

## Initial Assessment

1. **Access**
   - GSC / GA4 connected? Date range?
   - Brand vs non-brand split needed?
2. **Scope**
   - Pages, queries, countries, devices?
   - Experiment or incident to explain?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| site_or_property | string | yes | GSC property or domain; ask if missing |
| date_range | string | no | Comparison period; default last 28d vs prior |
| segment | string | no | Brand/non-brand, device, country filter |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Performance, deltas, evidence, forecast |
| action_list | json | Next actions from findings |

---

## Core Framework

### Step 1: Pull
GSC performance, pages, queries, CTR, coverage, GA4 assists.

### Step 2: Prove
Deltas, winners/losers, cannibalization evidence, incident review.

### Step 3: Report
Digest, recap, backlog, forecast baseline. No fabrication.

---

## Detailed Guidance

### Performance Pull

**Checklist:**
- [ ] GSC review (177), page table (178), query trends (179)
- [ ] CTR list (180), impression share (181)
- [ ] Landing delta (182), device split (188), country cut (189)
- [ ] Branded view (187), non-brand growth (186)
- [ ] Index summary (190), dashboard pack (185)

### Evidence & Deltas

**Checklist:**
- [ ] Winner/loser (183), annotation log (184)
- [ ] Cannibalization evidence (191) — prove overlap
- [ ] Experiment readout (193), incident review (197)
- [ ] Conversion assist (198), revenue tracker (199)

### Reporting Out

**Checklist:**
- [ ] Opportunity backlog (194) — findings → tasks
- [ ] Weekly digest (195), monthly recap (196)
- [ ] Action sheet (200) — next actions plainly
- [ ] Forecast baseline (192) — likely trend, mark assumptions

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Report vanity impressions | No decisions | Tie to clicks + revenue |
| No annotations | Unexplained drops | Log changes/releases |
| Mix brand + non-brand | Hides SEO | Split views |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No date compare | No movement proof | Prior-period delta always |
| Ignore CTR | Missed quick wins | CTR opportunity list |
| Skip index check | False alarms | Coverage first |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fabricate missing data | Violates reliability | State NOT AVAILABLE |
| Over-forecast | False precision | Baseline + range |
| No backlog | Report dies | Every finding → task |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Clicks / impressions | GSC totals | Growing | GSC |
| Avg CTR / position | Click rate, rank | CTR >3%, pos improving | GSC |
| Winners / losers | Top movers | Net positive | GSC delta |
| Index coverage | Indexed vs submitted | >90% | GSC |
| Assists / revenue pages | Search → conversion | Growing | GA4 |

---

## Decision Tree

No GSC access → manual template + NOT AVAILABLE tags. Drop detected → incident review + annotations. Overlap suspected → cannibalization evidence. Stakeholder ask → digest/recap, not raw dump.

---

## Quick Assessment Checklist

1. [ ] Property + date range?
2. [ ] Brand split needed?
3. [ ] Device / country cuts?
4. [ ] Incident / experiment context?
5. [ ] Tool access or manual?

---

## Expected Output Format

### Performance
[Clicks, CTR, pages, queries]

### Movers + Evidence
[Winners/losers, cannibalization, incidents]

### Next Actions
[Backlog, forecast, digest]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No tool access | Empty tables | NOT AVAILABLE, manual fallback |
| Sampling noise | Tiny deltas overread | Threshold movers |
| Missing annotations | Mystery drops | Rebuild change log |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | All reporting | Queries, pages, CTR, position | no |
| doddle.tool.v1.ga4.getReport | Assists, revenue | Sessions, conversions | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP context | Features, volatility | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Evidence review | Cannibalization, index triage |
| researcher | Trend context | Market shifts |
| planner | Backlog grooming | Task prioritization |

---

## Related Skills

- **seo-mastery**: Audits feeding reports
- **analytics-attribution**: Cross-channel attribution
- **content-strategy**: Refresh queue from decay

---

## Questions to Ask

1. GSC property + date range?
2. Brand / non-brand split?
3. Weekly digest or monthly recap?
