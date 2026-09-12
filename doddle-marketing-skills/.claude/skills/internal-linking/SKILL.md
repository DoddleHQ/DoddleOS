---
name: internal-linking
id: doddle.marketing.internal-linking
version: 1.0.0
blueprint: ./blueprint.yaml
description: Design internal link architecture, hub-spoke clusters, anchor strategy. Use when pages orphaned, crawl depth high, link equity uneven, taxonomy overlapping. For backlinks, see digital-pr. For audits, see seo-mastery.
---

# Internal Linking

Hub-spoke architecture, contextual links, anchor control for crawl + equity flow. Covers infographic block 5 (89-110).

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Orphan pages, deep clicks (>3), underlinked money pages
- Navigation / breadcrumb / faceted-link waste
- Anchor cannibalization, overlapping taxonomy
- Hub pages, archives, migrations needing restructure

## Initial Assessment

1. **Structure**
   - Sitemap URL? CMS? Approx page count?
   - Hub pages exist? Pillar-cluster model?
2. **Signals**
   - GSC access? Or proceed manual?
   - Priority pages (revenue) vs support?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| site_or_sitemap | string | yes | Domain, URL, or sitemap; ask if missing |
| priority_pages | string | no | Revenue pages; infer from sitemap if missing |
| locale | string | no | Market context; default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Hub map, link gaps, anchor plan, taxonomy fixes |
| action_list | json | Prioritized link actions with impact/effort |

---

## Core Framework

### Step 1: Map
Crawl/sitemap → depth, orphans, equity sinks. Hub-spoke overlay.

### Step 2: Link
Contextual passes, nav/breadcrumb/footer cleanup, orphan recovery.

### Step 3: Anchor
Semantic library, intent match, conflict resolve. Sequence changes.

---

## Detailed Guidance

### Architecture

**Key Principles:**
- Hubs receive, spokes support, max depth 3
- Contextual > nav > footer for equity
- One primary anchor intent per target

**Checklist:**
- [ ] Depth audit, orphan list
- [ ] Hub blueprint (101), parent-child taxonomy (96)
- [ ] Breadcrumb (94), HTML sitemap (100)
- [ ] Archive paths (102), click-path simplify (103)
- [ ] Facet rules (105), footer cleanup (99)

### Link Pass

**Key Principles:**
- 3-5 contextual links per money page, natural placement
- Match link intent to user stage
- Fix decayed destinations first

**Checklist:**
- [ ] Related matcher (90), opportunity scan (91)
- [ ] Equity review (92), contextual pass (95)
- [ ] Intent alignment (98), cross-sell plan (106)
- [ ] Depth priorities (107), decay audit (104)
- [ ] Label review (93) — clear menu naming

### Anchor & Taxonomy

**Checklist:**
- [ ] Anchor rewrite (per copy), semantic library (108)
- [ ] Taxonomy conflict check (109) — merge overlaps
- [ ] Change plan (110) — sequence to avoid rank drops

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Link everything to homepage | Equity sink | Hubs get equity |
| Orphan new posts | Never crawled | Recovery plan on publish |
| Deep archives (>4 clicks) | No equity | Flatten, hub links |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Generic anchors (click here) | No signal | Semantic, intent-matched |
| Sitewide footer stuffing | Dilutes equity | Remove low-value |
| Facet link explosion | Crawl waste | Nofollow/norule facets |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Count links not equity | Misleads | Depth + traffic weight |
| Ignore decay | 404 equity loss | Quarterly decay audit |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Max crawl depth | Clicks from home | ≤3 | GSC / crawl |
| Orphan count | Indexed, 0 inlinks | 0 | Crawl |
| Inlinks per priority | Internal links to money pages | ≥5 contextual | Crawl |
| Facet indexed | Parameter URLs indexed | Minimal | GSC coverage |

---

## Decision Tree

Orphans exist → recovery plan first. Depth >3 → hub blueprint. Anchors generic → library build. Taxonomy overlap → merge before linking.

---

## Quick Assessment Checklist

1. [ ] Sitemap / crawl source?
2. [ ] Priority revenue pages?
3. [ ] Hubs exist or greenfield?
4. [ ] GSC access or manual?
5. [ ] Migration / restructure risk?

---

## Expected Output Format

### Hub Map
[Hubs, spokes, depth]

### Link Gaps
[Orphans, underlinked, decayed]

### Anchor Plan
[Library, rewrites, rules]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No crawl data | Guessing | Manual sitemap walk |
| Taxonomy war | Overlaps persist | Single owner gate |
| Link spam | 100+ links/page | Prune to intent-fit |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | Underlinked winners | Queries, pages, position | no |
| doddle.tool.v1.semrush.keywordResearch | Hub topics | Volume, intent | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP structure | Pillar gaps | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Audit, taxonomy | Technical review |
| copywriter | Anchor phrasing | Contextual copy |
| planner | Rollout sequence | Change plan |

---

## Related Skills

- **seo-mastery**: Full audits, keyword, on-page
- **content-strategy**: Pillar-cluster editorial
- **digital-pr**: External equity (backlinks)

---

## Questions to Ask

1. Sitemap or domain to map?
2. Priority pages to elevate?
3. GSC access, or manual mode?
