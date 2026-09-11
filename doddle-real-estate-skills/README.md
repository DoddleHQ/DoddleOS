# Doddle Real Estate Skills

> Agent/team marketing skills for listings, valuation lead-gen, open houses, long-cycle nurture, and referrals.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). 5 specialised real-estate skills covering click → listing → closing → repeat/referral.

Naming: pack dir `doddle-real-estate-skills`, skills `realty-*`, IDs `doddle.realty.*`, commands `/realty:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `realty-listings` | Listing pages SEO, media, schema, syndication | `/realty:listings` |
| `realty-valuation` | "What's my home worth" estimator funnel | `/realty:valuation` |
| `realty-openhouse` | Open-house promo, RSVP, post-event followup | `/realty:openhouse` |
| `realty-nurture` | Buyer/seller long-cycle drip (6-18 mo) | `/realty:nurture` |
| `realty-referrals` | Past-client + agent-to-agent referrals | `/realty:referrals` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-real-estate-skills
/plugin install doddle-real-estate-skills@doddle-real-estate-skills
```

Manual: `cp -r doddle-real-estate-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### realty-listings (Search → Tour)
- Listing page template (photos, video, 3D, map, schools)
- RealEstateListing schema + image SEO
- Hyperlocal area pages (neighborhood → listings hub)
- Syndication hygiene (portal accuracy, duplicate suppression)

### realty-valuation (Curious → Captured Lead)
- Instant-estimate UX (address → range, not false precision)
- Accuracy disclaimer + CMA upgrade path
- Speed-to-lead (<5 min call/text on high-intent)
- Nurture handoff for "just looking" sellers

### realty-openhouse (Listing → Foot Traffic → Offers)
- 7-day promo calendar (portal, social, signage, neighbor invites)
- RSVP capture + reminder flow
- Day-of sign-in (digital, consent for followup)
- 24h followup: attendees, no-shows, neighbor circle

### realty-nurture (Lead → Client in 6-18 Months)
- Buyer/seller track split from day one
- Listing alerts + monthly market update
- Re-engagement triggers (saved search, valuation repeat)
- Agent task prompts (calls on hot behavior)

### realty-referrals (Closing → Next Deal)
- Closing-day review + referral ask sequence
- Anniversary + equity-update touches
- Agent-to-agent referral network (relocation, niche)
- Referral fee + compliance basics (check local rules)

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Listing page traffic + tour rate | `realty-listings` |
| Valuation lead volume + contact rate | `realty-valuation` |
| Open-house turnout + followup | `realty-openhouse` |
| Database engagement + aging | `realty-nurture` |
| Referral share of closings | `realty-referrals` |

## Compliance Note

Real-estate marketing must respect fair-housing rules (no discriminatory language/targeting) and local referral-fee regulations. Every skill includes a compliance checkpoint. Not legal advice.

## Dependencies

Core + packs:
- `programmatic-seo`, `schema-markup` - Listings + area pages
- `lead-magnets`, `form-cro` - Valuation funnel
- `events` - Open houses
- `email-sequence`, `sms` - Nurture + followup
- `referral-program` - Referral engine
- `analytics-attribution` - Source-to-closing attribution

## License

MIT License - Same as Doddle Marketing OS core
