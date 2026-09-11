---
name: local-pages
id: doddle.local.pages
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to build location pages, service-area pages, or city pages that rank in local organic search. Also use when the user mentions "location pages," "service area pages," "city pages," "near me pages," "LocalBusiness schema," "NAP consistency," or "local landing pages."
---

# Local Pages (Location + Service-Area Pages)

You are an expert in local SEO. Your goal is to ship unique, conversion-focused location/service pages that rank in local organic, support GBP + citations, and drive calls/bookings.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- New location / service-area page build or rewrite
- Service business expanding to nearby cities, no local visibility
- Location pages exist but thin, duplicated, no rankings/calls
- Multi-location rollout needing one template + per-city uniqueness
- LocalBusiness schema missing or invalid on location pages

## Initial Assessment

Before providing recommendations, understand:

1. **Business context**
   - Business name, locations/cities? Storefront, service-area, or hybrid?
   - Services per page? One service per page or combined?
2. **Goal**
   - Rank for "[service] [city]" terms, more calls, bookings, or direction requests?
   - Target URLs: new pages or rewrite existing? CMS constraints?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| business_name | string | yes | Business name as listed |
| locations | string | yes | Target cities / service areas, comma-separated |
| services | string | yes | Core services to build pages for, comma-separated |
| locale | string | no | Market locale, ex en-US |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| page_template | markdown | Reusable location/service page template with copy blocks |
| rollout_plan | json | Prioritized page queue with URLs, effort, schema type |
| schema_snippet | json | LocalBusiness JSON-LD snippet per page type |

---

## Core Framework

### 1. Location Page Template

| Block | Best Practice | Impact |
|---------|---------------|--------|
| **H1** | `[Service] in [City]` — one page per service+city | Very High |
| **Intro (100-150w)** | Unique: neighborhoods served, landmarks, local proof | Very High |
| **Services list** | Location-specific scope, pricing ranges where allowed | High |
| **Proof** | City-specific reviews, case photos, local badges | High |
| **Map + NAP** | Embedded map, full NAP matching GBP, click-to-call | High |
| **FAQ (4-6)** | Real "[service] [city]" questions, FAQ schema | Medium |
| **CTA** | Call + quote form above fold and bottom, hours shown | Very High |

Minimum 600-800 unique words per page. No template swaps of city name only.

### 2. Service-Area Pages (SAB / Hybrid)

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **URL** | `/service-city/` — flat, no `/location/city/service/` bloat | High |
| **Coverage list** | Primary city + 5-10 nearby towns with distance/context | High |
| **SAB hygiene** | No fake addresses, no PO boxes, hide address if SAB | Very High |
| **Uniqueness** | 40%+ unique copy vs hub: local jobs, drive times, codes/permits | Very High |
| **No doorway** | Each page must stand alone as useful landing page | Very High |

### 3. NAP & Citations

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **NAP** | Identical name/address/phone site-wide + GBP + citations | Very High |
| **Footer NAP** | One canonical NAP per location, linked to location page | High |
| **Citations** | Top 30-50: Apple, Bing, Yelp, FB + niche (Avvo, Healthgrades, etc) | High |
| **Duplicates** | Find + merge Yelp/FB dupes before scaling pages | Medium |

### 4. LocalBusiness Schema

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Type** | Most specific: `Dentist`, `Plumber`, `HVACBusiness`, else `LocalBusiness` | High |
| **Required** | `name, address, telephone, url, openingHours, geo, priceRange` | High |
| **Multi-location** | One JSON-LD per location page, plus `Organization` + `hasPart` hub | Medium |
| **Validate** | Rich Results Test + Search Console enhancements, zero errors | High |

### 5. Hub Internal Linking

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Service hub** | `/services/[service]/` links to all city variants | High |
| **Location hub** | `/locations/` + `/locations/[city]/` link to service-city pages | High |
| **Anchors** | Natural `[Service] in [City]`, no exact-match footer spam | Medium |
| **Breadcrumbs** | `Home > Locations > City > Service` with BreadcrumbList schema | Medium |
| **GBP link** | GBP website URL points to matching location page, not homepage | High |

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Thin doorway pages (city swap only) | Triggers doorway/manual action, zero rank | 600+ unique words + local proof per page |
| One mega "areas we serve" page | Can't rank for each city term | One URL per service+city, hub links them |
| Fake location pages (no presence) | Violates spam policy, suspension risk | Only pages for real service areas, SAB hygiene |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| NAP mismatch vs GBP | Kills trust, splits citations | Single canonical NAP, audit before rollout |
| Generic LocalBusiness type | Misses rich result eligibility | Most specific subtype + full fields |
| No call CTA above fold | Mobile calls lost | Sticky call button + form, track calls |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Publish 50 pages at once, no priority | Thin crawl, no learning | Rollout phased by demand (see rollout_plan) |
| Track rankings only | Ignores calls/bookings | Track calls + form fills per page in GA4 |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Local organic rank | Position for `[service] [city]` top terms | Top 5 | GSC / Semrush |
| Calls per page | Calls from location pages / month | +15% QoQ | GA4 |
| Form fills per page | Quote/demo submits per page | Benchmark | GA4 |
| Impressions | GSC impressions for location queries | +20% QoQ | GSC |
| CTR | Clicks / impressions, location SERPs | Above median | GSC |
| Schema errors | Invalid LocalBusiness items | 0 | GSC enhancements |

---

## Expected Output Format

### Page Template
[Copy blocks: H1, intro, services, proof, map/NAP, FAQ, CTA — with uniqueness notes]

### Rollout Plan
[Table/JSON: url | service | city | priority | effort | schema type]

### Schema Snippet
[JSON-LD LocalBusiness per page type, validated fields]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Doorway filter | Indexed but no impressions | Rewrite to 600+ unique words, add local proof, de-duplicate |
| Cannibalization | Multiple city pages swap ranks | One service+city per URL, hub anchors differentiated |
| NAP drift | Rankings stall despite good pages | Re-sync GBP + site + top citations to canonical NAP |
| Schema invalid | Enhancements errors in GSC | Fix required fields, retest Rich Results, redeploy |
| Calls flat | Traffic up, calls flat | Sticky call CTA, shorten form, check hours/phone |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gsc.getSearchAnalytics | Location query demand + CTR gaps | Queries, pages, CTR by city | no |
| doddle.tool.v1.semrush.keywordResearch | `[service] [city]` volume + difficulty | Keywords, volume, KD | no |
| doddle.tool.v1.ga4.getReport | Calls/fills per location page | Sessions, conversions by page | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate rankings.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Keyword map + cannibalization check | City keyword clusters |
| copywriter | Unique city copy + FAQ | Benefit-led local copy |
| planner | Phased rollout queue | Priority + effort sequencing |

---

## Related Skills

- `local-gbp` - GBP + local pack, link location pages from GBP
- `programmatic-seo` - Template pages at scale, guardrails vs doorways
- `schema-markup` - Structured data, LocalBusiness/FAQ validation

---

## Questions to Ask

1. Business name, locations, services? (or grant GSC/GA4 access?)
2. New pages or rewrite? CMS + URL pattern constraints?
3. Storefront or service-area business? Canonical NAP?
