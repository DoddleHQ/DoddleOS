# Doddle Local OS

> Local-services marketing skills for Google Business Profile, reviews, location pages, booking/call flows, and local ads.

## Overview

Independent OS pack for [DoddleOS](https://github.com/doddleOS/doddleOS-marketing). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. 5 specialised local skills covering discovery → call/booking → review.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `local-gbp` | Profile optimisation + local pack rank | `/local:gbp` |
| `local-reviews` | Review generation, responses, rating recovery | `/local:reviews` |
| `local-pages` | Location/service-area pages at scale | `/local:pages` |
| `local-booking` | Click-to-call, quote/booking flow, no-show recovery | `/local:booking` |
| `local-ads` | Local Services Ads + geo paid, call tracking | `/local:ads` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-local-skills
/plugin install doddle-local-skills@doddle-local-skills
```

Manual: `cp -r doddle-local-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### local-gbp (Profile + Local Pack)
- Profile completeness (categories, hours, services, attributes)
- Photos, posts, Q&A, products/services
- Local pack ranking (proximity, relevance, prominence)
- GBP insights (calls, direction requests, impressions)

### local-reviews (Reputation)
- Review ask flows (SMS, email, QR, NFC)
- Response playbooks (positive, neutral, negative)
- Rating recovery (<4.0 rescue plan)
- Platform coverage (Google, Yelp, Facebook, industry)

### local-pages (Location SEO)
- Location + service-area page templates at scale
- NAP consistency, citations
- LocalBusiness schema, hours, geo pages
- Internal linking hub (city → service → booking)

### local-booking (Call → Booked Job)
- Click-to-call UX, call tracking numbers
- Quote/booking form (minimum fields, photo upload)
- Speed-to-lead (5-min response, missed-call textback)
- No-show + estimate-followup recovery

### local-ads (Paid Local)
- Local Services Ads (background check, responsiveness score)
- Geo-targeted search + call-only ads
- Call tracking + cost-per-booked-job attribution
- Budget split: LSA vs search vs retargeting

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| GBP completeness + local pack rank | `local-gbp` |
| Rating + review velocity | `local-reviews` |
| Location page coverage | `local-pages` |
| Call/booking conversion | `local-booking` |
| Paid local efficiency | `local-ads` |

## Optional bindings (peer packs, no install dependency)

Core [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing) skills:
- `seo-mastery` - SEO fundamentals (+ `references/local-seo.md`)
- `programmatic-seo` - Location pages at scale
- `schema-markup` - LocalBusiness structured data
- `form-cro` - Quote/booking form optimisation
- `paid-advertising` - Paid fundamentals
- `analytics-attribution` - Call + booking attribution
- `email-sequence`, `sms` - Review asks + followup

## License

MIT License - Same as DoddleOS core
