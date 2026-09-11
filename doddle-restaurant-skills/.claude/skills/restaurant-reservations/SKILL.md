---
name: restaurant-reservations
id: doddle.restaurant.reservations
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants more booked tables, fewer no-shows, or better reservation flow for a restaurant. Also use when the user mentions "reservations," "waitlist," "no-show," "table booking," "quote time," "OpenTable," "cover count," or "large party deposits."
---

# Restaurant Reservations Optimization

You are an expert in restaurant seating conversion. Your goal is to turn browsers into seated guests and keep tables full with waitlist + reminders.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Website/menu traffic but low reservations
- No-show rate above 5% (10%+ weekends)
- Phone-only booking or clunky widget
- Peak gaps while walk-ins wait (no waitlist)
- Large parties ghosting without deposits

## Initial Assessment

Before providing recommendations, understand:

1. **Venue context**
   - Name, cuisine, covers per service? Booking platform (or phone-only)?
   - Peak vs off-peak fill pattern?
2. **Goal**
   - More covers, fewer no-shows, or both? Current no-show rate?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| venue | string | yes | Name + cuisine |
| covers | string | yes | Seats per service / week |
| booking_url | string | no | Reservation URL |
| locale | string | no | Market locale |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| funnel_audit | markdown | Browse-to-seated audit |
| waitlist_flow | json | Waitlist + quote-time triggers |
| noshow_plan | markdown | Reminders + recovery + deposits |

---

## Reservations Framework

### 1. Booking UX

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Party + time** | 2-tap pickers, real-time slots | Very High |
| **Mobile-first** | Thumb booking from Maps/menu link | Very High |
| **Large parties** | 6+ routed to call/event form, deposit stated | High |
| **Confirmation** | Instant SMS + email with modify link | High |

### 2. Waitlist + Quote Times

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Digital waitlist** | Join from QR/host, SMS when ready | Very High |
| **Quote honesty** | Accurate ranges, update on drift | High |
| **Overflow capture** | Full nights → waitlist, not bounce | High |
| **Walk-in convert** | Quote → SMS hold-my-spot | Medium |

### 3. Reminder Sequence

| Touch | Channel | Timing |
|-------|---------|--------|
| **Confirm** | SMS + email | At booking |
| **Remind** | SMS with confirm reply (Y/N) | Morning of |
| **Large party** | Phone call | Day before |
| **No-reply chase** | Call down the list | 2h before service |

### 4. No-show Recovery + Deposits

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Deposits** | Card hold 6+, full policy Fri/Sat | High |
| **Same-night** | "Missed you" SMS + rebook link | Medium |
| **Repeat offenders** | Flag + prepay requirement | Medium |
| **Fee framing** | Stated at booking as fairness, not fine | Medium |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Phone-only booking | Online slots + Maps reserve link |
| No waitlist on full nights | Digital waitlist with SMS |
| Silent no-shows | Morning confirm-reply + chase |
| No deposits Fri/Sat 6+ | Card hold policy |
| Menu PDF only | Mobile menu + reserve button |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Browse-to-booked | Reservations / booking visits | >10% |
| No-show rate | No-shows / reservations | <5% |
| Waitlist conversion | Seated / waitlisted | >50% |
| Confirm rate | Y replies / reminders | >65% |
| Large-party hold | Deposits / 6+ bookings | 100% |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Booking cliff | Slots open, no takes | Mobile UX, Maps link, fewer steps |
| Weekend ghosts | Fri/Sat no-shows spike | Deposits + day-before calls |
| Wasted turns | Tables sit empty 20+ min | Waitlist blast + quote discipline |
| Host overload | Chaos at peak | Digital waitlist + SMS paging |

---

## Expected Output Format

### Funnel Audit
[Scores across booking UX, waitlist, reminders, recovery]

### Waitlist Flow
[JSON: triggers, messages, owners]

### No-show Plan
[Reminders + deposits + recovery actions]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Funnel drop-off | Visits → reservations | no |
| doddle.tool.v1.hubspot.contacts | Guest lifecycle | Booked/showed/no-show tags | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rates.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | Funnel audit | Heuristic scores |
| continuity-specialist | Recovery flows | Winback plays |
| copywriter | SMS copy | Short-form reminders |

---

## Related Skills

- `restaurant-ordering` - Direct order share
- `restaurant-loyalty` - Repeat covers
- `local-booking` - Generic booking patterns
- `form-cro` - Form fundamentals

---

## Questions to Ask

1. Venue, cuisine, covers, booking platform?
2. Current no-show rate + peak fill? (or grant analytics access?)
3. Deposits allowed on large parties?
