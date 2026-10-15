---
name: affiliate-keywords
id: doddle.affiliate.keywords
version: 1.0.0
blueprint: ./blueprint.yaml
description: Build affiliate keyword portfolios and programmatic patterns. Use for best-X, vs, alternatives at scale. For briefs see affiliate-content.
---

# Affiliate Keywords

Portfolio + templates, not one page per keyword. Never fabricate volumes.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New cluster or site section
- Best-X / vs / alternatives at scale
- Cannibalization or thin pages

## Initial Assessment

1. **Niche**
   - Approved niche? Seed URL?
2. **Pattern**
   - Template-able intent?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| niche | string | yes | Approved niche |
| seed_url | string | no | Seed site or competitor |
| locale | string | no | Locale, default en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| report | markdown | Portfolio + template + plan |
| action_list | json | Clusters and launch steps |

---

## Core Framework

### Step 1: Cluster
Buyer vs info vs comparison split.

### Step 2: Template
One template per pattern (best-X, vs, single review).

### Step 3: Launch
Priority by impact x difficulty.

---

## Detailed Guidance

### Patterns

**Checklist:**
- [ ] Intent mapped per cluster
- [ ] Schema (Review, ItemList, FAQ) per template
- [ ] Internal link hub defined

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Page per keyword | Bloat | Template patterns |
| Info-only chase | No revenue | Buyer-first |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Coverage | Live / planned | 100% | GSC |
| Cannibalization | Competing URLs | 0 | GSC |

---

## Decision Tree

Template-able → programmatic. One-off → single brief via affiliate-content.

---

## Quick Assessment Checklist

1. [ ] Niche approved?
2. [ ] Seed URL?
3. [ ] Locale?

---

## Expected Output Format

### Report
[Portfolio + templates]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Thin scale | <200 words/page | Merge or enrich |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.keywordResearch | Portfolio | Keywords | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP check | SERP | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Coverage | Queries | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Portfolio QA | Cannibalization check |
| planner | Launch order | Priorities |

---

## Related Skills

- **affiliate-content**: Briefs from portfolio
- **affiliate-niche**: Upstream pick

---

## Questions to Ask

1. Niche + seed URL?
2. Locale?
