---
name: affiliate-revenue
id: doddle.affiliate.revenue
version: 1.0.0
blueprint: ./blueprint.yaml
description: Lift affiliate EPC via CRO and placement. Use for revenue audits and test plans. For traffic see affiliate-keywords.
---

# Affiliate Revenue

Find leakage, then test by impact. Never invent EPC — tool or NOT AVAILABLE.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Traffic flat, revenue down
- High bounce on money pages
- Network mix review

## Initial Assessment

1. **Funnel**
   - URL? Networks?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| site_url | string | yes | Site or page URL |
| networks | string | no | Networks in use |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| revenue_audit | markdown | Leakage + drivers |
| cro_plan | json | Tests ordered by impact |

---

## Core Framework

### Step 1: Leak
Speed, placement, table, mobile CTA.

### Step 2: Offer
Network EPC + cookie + refund compare.

### Step 3: Test
One variable, ship winner.

---

## Detailed Guidance

### CRO

**Checklist:**
- [ ] Table above fold on mobile
- [ ] Single CTA per viewport
- [ ] Price = verify-live note
- [ ] Disclosure near CTA

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Multi-test | No learning | One variable |
| Lowest commission chase | Refunds kill | Net EPC |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| EPC | Earnings / click | Up | Network |
| CTR-out | Clicks to merchant | Up | GA4 |

---

## Decision Tree

Low CTR-out → placement/table first. Low EPC → network swap test.

---

## Quick Assessment Checklist

1. [ ] URL?
2. [ ] Networks?

---

## Expected Output Format

### Revenue Audit
[Leaks + drivers]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| No data | GA4 missing | Manual CTA audit |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Funnel | Clicks, bounce | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Demand | Queries | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Test plan | Hypotheses |

---

## Related Skills

- **affiliate-content**: Page input
- **affiliate-links**: Authority input

---

## Questions to Ask

1. URL + networks?
