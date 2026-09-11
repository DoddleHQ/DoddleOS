---
name: paid-advertising
id: doddle.marketing.paid-advertising
version: 1.5.1
blueprint: ./blueprint.yaml
description: Paid media strategy and optimization across platforms. Use when planning paid campaigns, optimizing ad performance, managing budgets, or setting up tracking for paid channels.
---

# Paid Advertising

Paid media strategy and optimization across platforms for profitable customer acquisition.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply paid advertising expertise when:
- Planning paid campaign strategy
- Optimizing ad performance and ROAS
- Managing budgets across platforms
- Setting up tracking and attribution
- Creating ad copy and creative briefs
- Troubleshooting underperforming campaigns

## Core Concepts

### Campaign Objectives by Goal

| Objective | Use When | Primary KPI | Platform Features |
|-----------|----------|-------------|-------------------|
| Awareness | Building brand | CPM, Reach | Brand awareness, video views |
| Traffic | Driving site visits | CPC, CTR | Traffic campaigns |
| Engagement | Growing social | CPE, engagement rate | Engagement campaigns |
| Leads | Generating contacts | CPL, lead quality | Lead forms, conversions |
| Conversions | Driving sales | ROAS, CPA | Purchase, signup events |
| App Installs | Mobile acquisition | CPI, install rate | App campaigns |

### Funnel-Based Targeting Strategy

**TOFU (Awareness) - Cold Audiences**
- Broad interest targeting
- Lookalike audiences (1-3%)
- Video viewers (3s+)
- Content: Educational, entertaining
- Bid: CPM or ThruPlay

**MOFU (Consideration) - Warm Audiences**
- Website visitors (7-30 days)
- Email list matches
- Engaged social audiences
- Content: Case studies, comparisons
- Bid: Landing page views

**BOFU (Decision) - Hot Audiences**
- High-intent visitors (pricing, demo pages)
- Cart abandoners (1-7 days)
- Trial users, demo requesters
- Content: Offers, urgency, testimonials
- Bid: Conversions, ROAS

### Platform-Specific Guidelines

**Google Ads**
| Campaign Type | Best For | Key Settings |
|---------------|----------|--------------|
| Search | High intent, BOFU | Exact match, SKAG |
| Display | Awareness, retargeting | Placement exclusions |
| Shopping | E-commerce | Feed optimization |
| Performance Max | Full-funnel automation | Asset variety |
| YouTube | Awareness, TOFU | Audience targeting |

**Meta Ads (Facebook/Instagram)**
| Campaign Type | Best For | Key Settings |
|---------------|----------|--------------|
| Traffic | Website visits | Landing page optimization |
| Conversions | Sales, signups | Pixel setup, CAPI |
| Leads | B2B, services | Lead form optimization |
| Catalog Sales | E-commerce | Dynamic product ads |
| Advantage+ | Automation | Broad targeting |

**LinkedIn Ads**
| Campaign Type | Best For | Key Settings |
|---------------|----------|--------------|
| Sponsored Content | Awareness, leads | Job title targeting |
| Message Ads | Direct response | Personalization |
| Lead Gen Forms | B2B leads | Pre-filled forms |
| Document Ads | Thought leadership | Gated content |

### Key Metrics & Benchmarks

| Metric | Formula | Good Range | Action If Below |
|--------|---------|------------|-----------------|
| CTR | Clicks / Impressions | 1-3% | Improve creative/targeting |
| CPC | Spend / Clicks | <$1-5 (varies) | Improve quality score |
| CPL | Spend / Leads | <$20-100 | Optimize landing page |
| CPA | Spend / Conversions | < 1/3 LTV | Full funnel review |
| ROAS | Revenue / Ad Spend | 3:1+ | Improve AOV or CVR |
| CVR | Conversions / Clicks | 2-5% | Landing page optimization |

### Budget Allocation Framework

**70-20-10 Rule for Mature Programs**:
- 70% to proven, profitable campaigns
- 20% to optimization tests
- 10% to new channel/audience experiments

**Startup/Testing Phase**:
- Equal split across channels until data
- Minimum viable spend per test ($500-1000)
- 2 weeks minimum per test

## Best Practices

### Campaign Setup Excellence
1. **Pixel/Tracking First**: Never launch without proper tracking
2. **Exclusion Lists**: Exclude converters, competitors, irrelevant audiences
3. **Naming Conventions**: Consistent, searchable campaign names
4. **UTM Discipline**: Track all campaigns in analytics

### Creative Excellence
1. **Hook in 3 Seconds**: Capture attention immediately
2. **Mobile-First**: Design for mobile, adapt to desktop
3. **Test Variations**: 3-5 creatives per ad set minimum
4. **Refresh Regularly**: Combat creative fatigue

### Optimization Excellence
1. **Let Data Accumulate**: 50+ conversions before major changes
2. **One Variable at a Time**: Isolate what's working
3. **Weekly Review Cadence**: Regular but not daily changes
4. **Segment Performance**: Break down by audience, placement

## Agent Integration

| Agent | How They Use This Skill |
|-------|------------------------|
| `attraction-specialist` | Paid campaign strategy and setup |
| `copywriter` | Ad copy creation |
| `researcher` | Competitor ad analysis |
| `planner` | Budget allocation planning |

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Do This Instead |
|--------------|----------------|-----------------|
| Launching without tracking | Can't measure success | Pixel first, always |
| Too broad targeting | Wasted spend | Start narrow, expand |
| One creative only | No learning, fatigue | Test 3-5 variations |
| Daily bid changes | Disrupts algorithm | Weekly optimization |
| Ignoring landing page | Blames ads for LP issues | Optimize full funnel |

## Metrics to Track

### Campaign Performance Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| ROAS (Return on Ad Spend) | Revenue / Ad spend | >3x | Ad platform + GA |
| CPA (Cost per Acquisition) | Cost per conversion | Below customer LTV | Ad platform |
| CTR (Click-Through Rate) | % clicking ad | >2% (varies by platform) | Ad platform |
| CPC (Cost per Click) | Cost per click | Industry-dependent | Ad platform |

### Funnel Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Impression Share | % of available impressions | >50% for branded | Ad platform |
| Quality Score | Ad relevance and landing page | >7/10 | Google Ads |
| Conversion Rate | % converting after click | >2% | Google Analytics |
| Bounce Rate (Paid) | % leaving without action | <50% | Google Analytics |

### Efficiency Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Frequency | Times user sees ad | <3 (avoid fatigue) | Ad platform |
| CPM (Cost per 1000 impressions) | Brand awareness cost | Platform-dependent | Ad platform |
| View Rate (Video) | % watching video | >30% | Ad platform |
| Engagement Rate (Social) | Interactions / Impressions | >1% | Ad platform |

### Budget Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Budget Utilization | % of budget spent | >90% | Ad platform |
| Pacing | Spend vs. timeline | On track | Ad platform |
| Lifetime vs. Daily Budget | Flexibility | Test both | Ad platform |
| Campaign ROI | Total return / Total spend | Positive | Finance + GA |

### Platform-Specific Benchmarks
| Platform | Good CTR | Good CPC | Good ROAS |
|----------|----------|----------|-----------|
| Google Search | >3% | <$2 | >4x |
| Google Display | >0.5% | <$1 | >2x |
| Facebook/Instagram | >1% | <$1.5 | >3x |
| LinkedIn | >0.5% | <$5 | >2x |
| TikTok | >1% | <$1 | >2x |

---

## Platform-Specific Resources

- `references/meta-ads.md` - Facebook/Instagram advertising
- `references/google-ads.md` - Search and display
- `references/linkedin-ads.md` - B2B advertising
- `references/tiktok-ads.md` - TikTok advertising

## Related Commands

- `/content/ads` - Create ad copy for platforms
- `/analytics/roi` - Calculate campaign ROI
- `/campaign/plan` - Full campaign planning

---

## Initial Assessment

Before providing recommendations, understand:

1. **Campaign Context**
   - Goal (awareness, leads, conversions)?
   - Platform(s) in scope?

2. **Constraints**
   - Budget and timeline?
   - Tracking/attribution setup?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign brief: goal, audience, offer; ask if missing |
| channel | string | no | Ad platform(s); recommend from brief if missing |
| budget | string | no | Total/monthly ad budget; ask if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| plan | markdown | Media plan: objectives, targeting, budgets, creative briefs, KPIs |
| assets | json | Machine-readable ad assets: copy variants, creatives, targeting, pacing |

---

## Common Mistakes

| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No conversion tracking | Can't optimize | Fix pixel/CAPI before spend |
| Too many ad sets | Splits learning | Consolidate, test sequentially |
| Killing tests early | False negatives | Wait for statistical significance |
| Ignoring creative fatigue | CTR decay | Refresh creative every 2-4 weeks |

---

## Expected Output Format

### Media Plan
[Objectives, targeting, budgets, pacing]

### Creative Briefs
[Hooks, copy variants, CTA per ad set]

### Asset List
[Table: asset | audience | budget | KPI]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Broken tracking | Zero conversions recorded | Audit pixel, events, UTMs |
| Audience overlap | Rising CPMs | Consolidate, exclude converters |
| Creative fatigue | Falling CTR | Rotate hooks and formats |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.meta-ads.adsInsights | Ad performance review | Spend, CTR, ROAS | no |
| doddle.tool.v1.ga4.getReport | Post-click behavior | Conversions, CPA | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Ad copy variants | Hooks, headlines, CTAs |
| conversion-optimizer | Landing page CRO | Post-click audit |
| seo-specialist | Search ads keywords | Keyword, intent review |

---

## Related Skills

- **social-media**: For organic + paid social synergy
- **video-marketing**: For video ad creatives
- **image**: For ad creatives and thumbnails
- **analytics-attribution**: For ROAS and attribution
- **copywriting**: For ad copy

---

## Questions to Ask

1. Goal, audience, and offer?
2. Platforms in scope + budget and timeline?
3. Tracking setup or ad account access?
