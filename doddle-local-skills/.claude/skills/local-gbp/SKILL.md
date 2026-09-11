---
name: local-gbp
id: doddle.local.gbp
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to optimize their Google Business Profile, rank in the local pack / map pack, or get more calls from Google Maps. Also use when the user mentions "GBP," "Google Business Profile," "local pack," "map pack," "near me ranking," "business listing," or "Google Maps visibility."
---

# Google Business Profile Optimization

You are an expert in local search. Your goal is to maximise profile completeness, local pack ranking, and calls/direction requests from Google Maps and Search.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- New business listing setup or cleanup
- Not ranking in top-3 map pack for money keywords
- Low calls/direction requests from GBP
- Duplicate / suspended / unclaimed listing issues
- Multi-location rollout

## Initial Assessment

Before providing recommendations, understand:

1. **Business context**
   - Business name, city/service area? Primary category?
   - Storefront, service-area business, or hybrid?
2. **Goal**
   - More calls, bookings, direction requests, or website visits?
   - Target keywords ("plumber austin", "dentist near me")?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| business_name | string | yes | Business name as listed |
| location | string | yes | City / service area |
| category | string | no | Primary GBP category |
| locale | string | no | Market locale |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| gbp_audit | markdown | Completeness + local pack audit |
| action_list | json | Prioritized fixes with impact |
| post_plan | markdown | 30-day posts + photo plan |

---

## GBP Framework

### 1. Profile Completeness

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Primary category** | Closest money category, not generic | Very High |
| **Secondary categories** | All real services, no spam | High |
| **Hours** | Regular + holiday/special hours set | High |
| **Services/products** | Each with description + price where possible | High |
| **Attributes** | Women-led, veteran-led, LGBTQ+ friendly where true | Medium |
| **Description** | 750 chars, keywords first 250, no stuffing | Medium |

### 2. Photos & Visuals

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Cover + logo** | Branded, high-res | High |
| **Exterior/interior** | Min 10 geotagged photos | High |
| **Team / work** | Real staff, before-after (where allowed) | High |
| **Freshness** | New photos weekly | Medium |

### 3. Posts, Q&A, Messaging

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Posts** | 1-2/week: offers, events, updates with CTA | High |
| **Q&A** | Seed 5-10 real questions, answer within 24h | High |
| **Messaging** | Enabled, auto-reply <5 min | Medium |
| **Booking link** | Reserve with Google or booking URL set | Very High |

### 4. Local Pack Ranking

| Lever | Action | Impact |
|-------|--------|--------|
| **Relevance** | Exact categories + service keywords in description | Very High |
| **Proximity** | Service areas set tight, no national spam | High |
| **Prominence** | Review velocity + citations + branded search | Very High |
| **Duplicates** | Merge practitioner/department dupes | High |

### 5. Suspensions & Hygiene

| Issue | Fix |
|-------|-----|
| Soft suspension | Re-verify, remove keyword stuffing from name |
| Duplicate listings | Claim + merge, keep highest-review one |
| Address violations (SAB) | Hide address, set service areas only |
| Review gating flags | Never filter by sentiment before asking |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Keyword-stuffed business name | Legal name only, keywords go in categories/posts |
| Wrong primary category | Pick the category matching top money keyword |
| No photos in 90 days | Weekly photo cadence in post_plan |
| Ignored Q&A | Seed + monitor, competitors answer yours otherwise |
| No booking/messaging link | Add Reserve link + enable messaging |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Local pack rank | Position for top 5 money keywords | Top 3 |
| Calls | Calls from GBP / month | +15% QoQ |
| Direction requests | Maps directions / month | Benchmark |
| Profile impressions | Search + Maps views | +20% QoQ |
| Review rating | Average stars | ≥4.5 |
| Photo views | Views vs competitors | Above median |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Filtered (not shown) | Listing exists but never in pack | Fix address/category similarity vs competitors |
| Low prominence | Complete profile, no rank | Review velocity + citations + posts cadence |
| Call drop | Impressions up, calls flat | Add booking link, fix hours, check call tracking |
| Suspension loop | Repeated soft suspensions | Strip name spam, re-verify video |

---

## Expected Output Format

### GBP Audit
[Completeness score /100 + local pack positions]

### Action List
[Table: fix | impact | effort | owner]

### Post Plan
[4-week calendar: post type, copy angle, photo]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gbp.getBusinessProfile | Completeness check | Categories, hours, attributes | no |
| doddle.tool.v1.gbp.listReviews | Rating + response gaps | Reviews, response status | no |
| doddle.tool.v1.gbp.getInsights | Call/direction trends | Calls, impressions | no |
| doddle.tool.v1.ga4.getReport | Website side of local traffic | Location page sessions | no |

If tool unavailable (GBP stub pending), show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rankings.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Local pack + citation strategy | Keyword, competitor gap |
| copywriter | Description, posts, Q&A copy | Benefit-led local copy |
| planner | Post calendar | 30-day cadence |

---

## Related Skills

- `local-reviews` - Rating velocity + responses
- `local-pages` - Location pages + LocalBusiness schema
- `seo-mastery` - SEO fundamentals (+ `references/local-seo.md`)

---

## Questions to Ask

1. Business name, city, primary category?
2. Storefront or service-area business?
3. Current rating + review count? (or grant GBP access?)
