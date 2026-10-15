---
name: travel-growth
id: doddle.travel.growth
version: 1.0.0
blueprint: ./blueprint.yaml
description: Grow a travel business via GBP, reviews, itineraries, programmatic SEO. Use when marketing a travel agency, tour operator, or DMC. For pure trip planning see travel-search. For reputation depth see local-reviews.
---

# Travel Growth

Composition skill: operational travel product + local presence + SEO pages in one growth plan. Never fabricate ratings, prices, or rankings — mark NOT AVAILABLE without live access.

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply when:
- Marketing a travel agency / tour operator / DMC in a city
- GBP + reviews limit local pack visibility for destination queries
- Need destination pages at scale from real itineraries
- Corporate T&E + leisure demand in one motion

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| business_name | string | yes | Agency name as listed |
| location | string | yes | City / service area |
| destination_dates | string | yes | Hero destination + dates for itinerary pull |
| seed_topic | string | yes | Seed topic or URL for destination pages |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| growth_audit | markdown | GBP + reputation + itinerary synthesis with priorities |
| destination_pack | markdown | Programmatic destination page plan |
| review_engine | json | Review ask flows + response playbook refs |

---

## Core Framework

### Step 1: Presence
Call `doddle.local.gbp` + `doddle.local.reviews` for profile completeness + rating velocity.

### Step 2: Product
Call `doddle.travel.itinerary` for a real sellable itinerary (no invented prices).

### Step 3: Scale
Call `doddle.marketing.programmatic-seo` to turn itinerary stops into page patterns.

---

## Detailed Guidance

### Presence Checks

**Checklist:**
- [ ] GBP categories, hours, photos, Q&A complete
- [ ] Review ask flow live (checkout + 48h post-return)
- [ ] Negative review response SLA <24h

### Product Rules

**Checklist:**
- [ ] Itinerary has routing + buffers + rain alternative
- [ ] No exact fares without live verify — ranges + links
- [ ] Corporate policy guardrails flagged if applicable

### Scale Rules

**Checklist:**
- [ ] One template per destination pattern, not per page
- [ ] LocalBusiness + FAQ schema on every page
- [ ] Internal link hub: city → destination → booking

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Ads before reputation | Low rating kills CTR | Reviews → 4.5+ then spend |
| Pages before product | Thin content | Itinerary first, then scale |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fake prices/ratings | Hallucination | NOT AVAILABLE + verify |
| One page per keyword | Unmaintainable | Template patterns |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| GBP completeness | Profile fields filled | 100% | GBP |
| Rating velocity | Reviews / 30d | Up | GBP |
| Page coverage | Live patterns / planned | 100% | GSC |

---

## Decision Tree

No GBP access → manual audit + ask for access. No itinerary → run `travel-itinerary` first. Low rating (<4.0) → reputation before paid.

---

## Quick Assessment Checklist

1. [ ] Business name + location as listed?
2. [ ] Hero destination + dates?
3. [ ] Seed topic / URL for pages?
4. [ ] Live GBP / booking access or manual?

---

## Expected Output Format

### Growth Audit
[Priorities: presence, product, scale]

### Destination Pack
[Page patterns + launch steps]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Missing callee input | Schedule failed | Ask for business_name/location/dates/topic |
| Stub tool | NOT AVAILABLE | Manual review note, continue partial |

---

## MCP Tool Integration

Machine binding. Tool IDs MUST use `doddle.tool.v1` namespace. Full DAG lives in `blueprint.yaml`.

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.dataforseo.serpGoogle | Destination demand | SERP, carriers | no |
| doddle.tool.v1.gbp.listReviews | Reputation check | Reviews | no |
| doddle.tool.v1.hubspot.contacts | Past traveler base | Contacts | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Synthesis | Growth audit priorities |
| researcher | Demand intel | Route + provider data |
| copywriter | Page/GBP copy | Posts, responses |

---

## Related Skills

- **travel-itinerary**: Product input for pages
- **local-reviews**: Reputation engine detail
- **local-gbp**: Profile depth

---

## Questions to Ask

1. Agency name + city as listed on Google?
2. Hero destination + dates to feature?
3. Seed URL or topic for destination pages?
