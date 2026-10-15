---
name: affiliate-niche
id: doddle.affiliate.niche
version: 1.0.0
blueprint: ./blueprint.yaml
description: Score affiliate niches on demand, competition, monetization. Use when picking a niche, validating vertical, or killing a bad idea. For keywords see affiliate-keywords.
---

# Affiliate Niche

Pick winnable niches before building. Never invent search volume — mark NOT AVAILABLE without tools.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- New affiliate site or vertical expansion
- Seed idea needs demand vs difficulty check
- Network commissions decide viability

## Initial Assessment

1. **Demand**
   - Seed vertical? Buyer vs info intent split?
2. **Feasibility**
   - Budget band? Content velocity possible?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| seed_vertical | string | yes | Seed vertical or interests |
| budget_band | string | no | Content + links budget |
| monetization | string | no | Networks in scope |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| niche_audit | markdown | Demand vs competition vs monetization |
| shortlist | json | Ranked niches with go/no-go |

---

## Core Framework

### Step 1: Demand
SERP + keyword pull for buyer intent share.

### Step 2: Difficulty
Competitor authority, link velocity, E-E-A-T bar.

### Step 3: Money
EPC proxies, commission stability, cookie windows.

---

## Detailed Guidance

### Scoring

**Checklist:**
- [ ] Buyer-intent share >30% of cluster
- [ ] No invented volumes — tool or NOT AVAILABLE
- [ ] Commission + refund risk noted

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Passion-only pick | No buyer intent | Demand first |
| Giant niche | Unwinnable | Sub-niche wedge |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Buyer share | Buyer vs info | >30% | Semrush |
| Difficulty | Avg authority | Beat top 3 | Semrush |

---

## Decision Tree

No buyer intent → kill. High difficulty + low budget → sub-niche. Weak commissions → kill.

---

## Quick Assessment Checklist

1. [ ] Seed vertical?
2. [ ] Budget band?
3. [ ] Monetization options?

---

## Expected Output Format

### Niche Audit
[Scores + rationale]

### Shortlist
[Ranked go/no-go]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Volume hallucination | Exact numbers, no source | NOT AVAILABLE |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.semrush.keywordResearch | Demand sizing | Keywords | no |
| doddle.tool.v1.dataforseo.serpGoogle | SERP difficulty | SERP | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Niche intel | Demand, competitors |

---

## Related Skills

- **affiliate-keywords**: Portfolio after niche pick

---

## Questions to Ask

1. Seed vertical + budget?
2. Networks in scope?
