# Doddle Travel OS

> Leisure + corporate travel: search → itinerary → booking → support → reviews. Turns lookers into booked travelers and repeat bookers.

## Overview

Independent OS pack for [DoddleOS](https://github.com/DoddleHQ/DoddleOS). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. Covers family vacations and managed corporate T&E in one motion.

Naming: pack dir `doddle-travel-skills`, skills `travel-*`, IDs `doddle.travel.*`, commands `/travel:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `travel-search` | Flight/stay/activity compare, price + policy trade-offs | `/travel:search` |
| `travel-itinerary` | Day plans (leisure) + trip chains (corporate), routing + buffers | `/travel:itinerary` |
| `travel-booking` | Holds, confirmations, changes, group + policy compliance | `/travel:booking` |
| `travel-support` | Disruption rebook, visa/docs, expense capture | `/travel:support` |
| `travel-reviews` | Post-trip UGC flywheel, referrals, loyalty capture | `/travel:reviews` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-travel-skills
/plugin install doddle-travel-skills@doddle-travel-skills
```

Manual: `cp -r doddle-travel-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### travel-search (Intent → Shortlist)
- Leisure: dates ±flex, budget bands, vibe filters (beach, city, adventure)
- Corporate: policy class caps, preferred carriers, refundability first
- Compare: total cost (fees, bags, seats), cancellation terms, loyalty earn
- Output: ranked shortlist with trade-off table, no fake prices

### travel-itinerary (Shortlist → Day Plan)
- Leisure: day-by-day routing, pace (1-2 anchors/day), food + rest buffers
- Corporate: multi-city chains, meeting buffers, red-eye rules, backup flights
- Per stop: transit time, booking links to verify, rain/disruption alternative
- Output: shareable itinerary + packing/docs checklist

### travel-booking (Plan → Confirmed)
- Holds before charges, name/DOB/passport accuracy gate
- Leisure: group splits, deposit schedules, insurance nudge
- Corporate: policy guardrails (class, rate caps), approval chain, cost center tags
- Changes: fee table per fare, cancellation windows, refund tracking

### travel-support (Booked → Home)
- Disruption: rebook options ranked (fastest vs cheapest vs status-safe)
- Docs: visa, passport validity (6-mo rule), vaccines, entry forms per leg
- Expense: receipt capture, per-diem vs actuals, corp card reconciliation
- Output: action sheet with owner + deadline per item

### travel-reviews (Home → Next Booking)
- Ask moments: checkout, 48h post-return, expense approval (corporate)
- UGC: photo prompts, property + experience review routing
- Referrals: give-get credit, group-trip leader rewards
- Loyalty: points audit, status gap to next tier, expiry alerts

## Optional bindings (peer packs, no install dependency)

- `local-pages` - Destination + area pages
- `restaurant-reservations` - Dining holds inside itineraries
- `finance-reviews` - Expense + reconciliation depth
- `email-sequence` - Pre-trip + post-trip nurture

## License

MIT License - Same as DoddleOS core
