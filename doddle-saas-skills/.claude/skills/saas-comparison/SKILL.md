---
name: saas-comparison
id: doddle.saas.comparison
version: 1.0.0
blueprint: ./blueprint.yaml
description: Vs and alternative pages that rank. Use for evaluation queries. For pricing tiers see saas-pricing.
---

# SaaS Comparison

Fair fights you win. Calls competitor-alternatives.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Vs queries go to rivals
- New comparison hub needed
- Biased pages hurt trust

## Initial Assessment

1. **Matchup**
   - Product or URL + rival query?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| topic_or_url | string | yes | Product or competitor URL/topic |
| keyword | string | no | Vs or alternative query |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| comparison_audit | markdown | Gap + angle |
| page_pack | markdown | Structure + copy + tables |
| schema_notes | json | Schema + links |

---

## Core Framework

### Step 1: Compare
Call `competitor-alternatives` for structure.

### Step 2: Prove
Fair table + migration path + proof.

### Step 3: Convert
Trial CTA per use case, not generic demo.

---

## Detailed Guidance

### Pages

**Checklist:**
- [ ] Rival named fairly, strengths admitted
- [ ] Migration + switching cost addressed
- [ ] ItemList + FAQ schema, hub linked

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Hit piece | Distrust + bounce | Fair + proof |
| No migration | Fear stalls | Path + timeline |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Rank | Vs query position | Top 3 | GSC |
| Page → trial | Conversion | Up | GA4 |

---

## Decision Tree

No search demand → sales asset only. Demand + loss → page first.

---

## Quick Assessment Checklist

1. [ ] Product/URL + query?

---

## Expected Output Format

### Page Pack
[Structure + tables]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Stale compare | Wrong rival pricing | Quarterly refresh |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.keywordResearch | Demand | Vs queries | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Rank | Queries | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Page copy | Tables |

---

## Related Skills

- **saas-pricing**: Tier proof
- **saas-homepage**: Hub link

---

## Questions to Ask

1. Product/URL + rival query?
