# Doddle Education OS

> School/course marketing skills for enrollment, open-house events, program content, nurture, and alumni referrals.

## Overview

Independent OS pack for [DoddleOS](https://github.com/doddleOS/doddleOS-marketing). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. Turns inquiries into enrolled students: capture fast, nurture long cycles, yield admits, activate alumni.

Naming: pack dir `doddle-education-skills`, skills `edu-*`, IDs `doddle.edu.*`, commands `/edu:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `edu-enrollment` | Inquiry → application → enrolled funnel | `/edu:enrollment` |
| `edu-openhouse` | Open days, tours, admissions webinars | `/edu:openhouse` |
| `edu-content` | Program pages + guides that rank | `/edu:content` |
| `edu-nurture` | Parent/student long-cycle drip + yield | `/edu:nurture` |
| `edu-alumni` | Alumni referrals, ambassadors, proof | `/edu:alumni` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-education-skills
/plugin install doddle-education-skills@doddle-education-skills
```

Manual: `cp -r doddle-education-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### edu-enrollment (Inquiry → Enrolled)
- Application funnel audit (inquiry, visit, apply, admit, yield)
- Speed-to-lead (<5 min on high-intent inquiries)
- Parent vs student track split (different pains, same CRM)
- Deadline + document chase sequences

### edu-openhouse (Browsing → Visited)
- Open-day promo calendar (portal, schools, social, signage)
- RSVP capture + family reminders
- Tour script (student guides, proof points per stop)
- 48h followup (visit recap + application nudge)

### edu-content (Searching → Applying)
- Program pages (outcomes, faculty, fees, FAQs)
- Parent-query guides (costs, admissions odds, careers)
- Local + course intent SEO (city + course pages)
- Application CTA on every content page

### edu-nurture (Lead → Enrolled over Terms)
- Segment tracks (parent/student, grade/course, intake term)
- Deadline-driven drip (early bird, regular, clearing)
- Yield plays (admitted → deposited → arrived)
- Re-engagement (deferred, waitlisted, melt prevention)

### edu-alumni (Graduate → Advocate)
- Ambassador program (parent + alumni volunteers)
- Testimonial + outcome-story capture (with consent)
- Referral asks (sibling priority, friend invites)
- Reunion + giving-lite touches (engagement first)

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Inquiry-to-enrolled + melt rate | `edu-enrollment` |
| Open-day turnout + application lift | `edu-openhouse` |
| Program content traffic + apply rate | `edu-content` |
| Database engagement + yield | `edu-nurture` |
| Alumni referral share | `edu-alumni` |

## Compliance Note

Education marketing must respect student privacy (no minor data in ads/retargeting without consent), honest outcome claims (no guaranteed placements/salaries), and platform education-ad policies. Every skill includes a checkpoint. Not legal advice.

## Optional bindings (peer packs, no install dependency)

Core + packs (no new integration needed):
- `form-cro`, `lead-qualifier` - Inquiry + application
- `events` - Open days + webinars
- `seo-mastery`, `programmatic-seo`, `copywriting` - Program content
- `email-sequence`, `sms` - Nurture + reminders
- `referral-program` - Alumni engine
- Integrations: `hubspot` (admissions CRM), `google-analytics`, `google-search-console`, `semrush`, `meta-ads`

## License

MIT License - Same as DoddleOS core
