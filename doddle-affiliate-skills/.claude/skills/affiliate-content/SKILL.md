---
name: affiliate-content
id: doddle.affiliate.content
version: 1.0.0
blueprint: ./blueprint.yaml
description: Write affiliate reviews, vs, best-X that convert with E-E-A-T and disclosure. Use for briefs and QA. For portfolio see affiliate-keywords.
---

# Affiliate Content

Briefs that survive updates: tested picks, entities, disclosure above fold.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New review / vs / best-X
- Refresh losing pages
- Disclosure or E-E-A-T fail

## Initial Assessment

1. **Intent**
   - Cluster? Buyer question?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| keyword_cluster | string | yes | Cluster or URL pattern |
| brand_voice | string | no | Voice constraints |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| brief_pack | markdown | Outline, entities, FAQ, schema |
| draft_checklist | json | E-E-A-T + disclosure + CRO checks |

---

## Core Framework

### Step 1: Angle
Tested winner, who-for, deal-breakers first.

### Step 2: Proof
Specs, pros/cons from testing, alternatives.

### Step 3: Convert
Placement above fold, comparison table, single CTA.

---

## Detailed Guidance

### E-E-A-T

**Checklist:**
- [ ] Disclosure above fold + near CTA
- [ ] Author + testing method stated
- [ ] Cons + who-not-for included
- [ ] Prices marked verify-live, never invented

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No testing | No trust | Hands-on or mark desk-only |
| Hidden disclosure | Policy risk | Above fold |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| CTR | SERP click rate | Up | GSC |
| EPC | Earnings / click | Up | Network |

---

## Decision Tree

No testing possible → desk-review label + limit claims.

---

## Quick Assessment Checklist

1. [ ] Cluster?
2. [ ] Voice?

---

## Expected Output Format

### Brief Pack
[Outline + entities + FAQ]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Fake specs | Wrong details | Verify or cut |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | Intent check | Queries, CTR | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Briefs | Outlines |
| brand-voice-guardian | QA | Disclosure check |

---

## Related Skills

- **affiliate-keywords**: Upstream portfolio
- **affiliate-revenue**: Downstream CRO

---

## Questions to Ask

1. Cluster + voice?
