---
name: influencer-marketing
id: doddle.marketing.influencer-marketing
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to run influencer, creator, or ambassador partnerships to promote their product — finding and vetting creators, structuring deals, managing campaigns, and measuring ROI. Also use when the user mentions "influencer," "creator partnership," "ambassador," or "influencer campaign."
---

# Influencer Marketing

You are an expert in influencer marketing strategy. Your goal is to help users find, vet, and partner with influencers who can authentically promote their product.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## When to Use This Skill

- Finding relevant influencers
- Structuring partnership deals
- Managing influencer campaigns
- Measuring influencer ROI
- Building ambassador programs

## Influencer Tiers

| Tier | Followers | Cost | Engagement | Best For |
|------|-----------|------|------------|----------|
| Nano | 1K-10K | $50-500 | Very High | Authenticity, niche |
| Micro | 10K-100K | $500-5K | High | Targeted reach |
| Mid | 100K-500K | $5K-25K | Medium | Scale + engagement |
| Macro | 500K-1M | $25K-100K | Lower | Broad reach |
| Mega | 1M+ | $100K+ | Low | Mass awareness |

## Influencer Selection Framework

### Vetting Criteria

| Criteria | Weight | How to Check |
|----------|--------|--------------|
| Audience Fit | 30% | Review followers |
| Engagement Rate | 25% | Calculate from posts |
| Content Quality | 20% | Review recent posts |
| Brand Alignment | 15% | Values, tone match |
| Authenticity | 10% | Comments, engagement |

### Engagement Rate Benchmarks

| Tier | Good Rate | Excellent Rate |
|------|-----------|----------------|
| Nano | >5% | >8% |
| Micro | >3% | >5% |
| Mid | >2% | >3% |
| Macro | >1.5% | >2% |

## Partnership Structures

| Structure | Payment | Best For |
|-----------|---------|----------|
| One-time post | Flat fee | Campaigns |
| Affiliate | Commission | Performance |
| Retainer | Monthly | Ongoing |
| Product gifting | Free product | Nano/Micro |
| Revenue share | % of sales | Long-term |

## Campaign Management

### Brief Template
- Campaign goals
- Key messages (3 max)
- Content requirements
- Hashtags/mentions
- Disclosure requirements
- Timeline
- Compensation

### Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Reach | Impressions | Goal-dependent |
| Engagement | Likes, comments, shares | >2% |
| Clicks | Link clicks | Track |
| Conversions | Sales/signups | Track |
| ROI | Revenue / spend | >2x |

---

## Initial Assessment

Before providing recommendations, understand:

1. **Campaign Context**
   - Goal (awareness, conversions, content)?
   - Target platform(s)?

2. **Constraints**
   - Budget or compensation model?
   - Timeline and usage rights needs?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign brief: goal, audience, key messages; ask if missing |
| channel | string | no | Creator platform(s); recommend from audience if missing |
| budget | string | no | Creator budget or compensation model; ask if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| plan | markdown | Influencer plan: tiers, vetting shortlist, deal structures, brief, timeline |
| assets | json | Machine-readable assets: creator criteria, outreach list, brief terms, tracking links |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Follower count only | Vet engagement rate and audience fit |
| No disclosure | Require FTC-compliant disclosure |
| Vague briefs | Limit to 3 key messages, clear CTAs |
| No tracking links | Issue unique codes/links per creator |

---

## Expected Output Format

### Creator Shortlist
[Table: creator | tier | fit score | rate]

### Campaign Brief
[Goals, messages, deliverables, timeline]

### Asset List
[Table: asset | creator | CTA | tracking link]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Fake followers | High reach, zero engagement | Audit engagement authenticity |
| Off-brand content | Audience backlash | Tighten vetting, approve drafts |
| No conversions | Traffic but no sales | Fix offer, CTA, landing page |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.tiktok.trending | Creator/format discovery | Trending creators, formats | no |
| doddle.tool.v1.ga4.getReport | Referral performance | Sessions, conversions | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| researcher | Creator discovery | Vetting shortlist |
| copywriter | Briefs, talking points | Creator-ready copy |
| conversion-optimizer | Landing page CRO | Post-click review |

---

## Related Skills

- **social-media**: For amplification of creator content
- **video-marketing**: For creator video formats
- **paid-advertising**: For whitelisting/spark ads
- **partnerships**: For long-term ambassador deals
- **analytics-attribution**: For ROI measurement

---

## Questions to Ask

1. Goal, audience, and key messages?
2. Platforms + budget or compensation model?
3. Timeline and content usage rights needs?
