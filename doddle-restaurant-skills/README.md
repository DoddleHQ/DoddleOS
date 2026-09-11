# Doddle Restaurant Skills

> Restaurant/F&B marketing skills for reservations, direct ordering, loyalty, events, and reputation.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). 5 specialised restaurant skills covering discovery → booked table → regular → catered event.

Naming: pack dir `doddle-restaurant-skills`, skills `restaurant-*`, IDs `doddle.restaurant.*`, commands `/restaurant:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `restaurant-reservations` | Booking, waitlist, no-show recovery | `/restaurant:reservations` |
| `restaurant-ordering` | Direct vs aggregator, catering, QR dine-in | `/restaurant:ordering` |
| `restaurant-loyalty` | Repeat visits, clubs, winback | `/restaurant:loyalty` |
| `restaurant-events` | Private dining, buyouts, holiday parties | `/restaurant:events` |
| `restaurant-reputation` | Google/Yelp/delivery-app ratings + responses | `/restaurant:reputation` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-restaurant-skills
/plugin install doddle-restaurant-skills@doddle-restaurant-skills
```

Manual: `cp -r doddle-restaurant-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### restaurant-reservations (Browsing → Seated)
- Reservation UX (party size, time slots, mobile-first)
- Waitlist + quote-time SMS flow
- Confirmation + day-of reminders
- No-show recovery + deposit policy for large parties

### restaurant-ordering (Hungry → Ordered Direct)
- Direct-order margin math vs aggregator commission
- First-party ordering page + Google food ordering
- QR dine-in upsell (dessert, drinks, sides)
- Catering menu + minimums + lead time

### restaurant-loyalty (Visitor → Regular)
- Visit-based rewards (not discount spirals)
- Birthday/anniversary clubs with data capture
- Lapsed-guest winback (45/90-day tiers)
- Staff-driven enrollment (host script, check presenter)

### restaurant-events (Venue → Buyouts)
- Private dining packages + per-head minimums
- Corporate/holiday party prospecting
- Event inquiry response SLA (<2h) + tasting close
- Post-event review + referral capture

### restaurant-reputation (Meal → Rating)
- Ask flow (receipt QR, post-visit SMS, server handoff)
- Response playbooks (food, service, delivery-app issues)
- Platform coverage (Google, Yelp, TripAdvisor, DoorDash/Uber Eats)
- Rating rescue (<4.0 plan, fake-review disputes)

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Reservation conversion + no-show rate | `restaurant-reservations` |
| Direct order share vs aggregators | `restaurant-ordering` |
| Repeat rate + lapsed % | `restaurant-loyalty` |
| Event revenue share | `restaurant-events` |
| Rating + response coverage | `restaurant-reputation` |

## Dependencies

Core + packs:
- `local-booking`, `local-reviews`, `local-gbp` (doddle-local-skills)
- `form-cro` - Reservation/ordering forms
- `email-sequence`, `sms` - Reminders, clubs, winback
- `referral-program` - Bring-a-friend + catering referrals
- `events` - Event fundamentals
- `analytics-attribution` - Channel-to-cover attribution

## License

MIT License - Same as Doddle Marketing OS core
