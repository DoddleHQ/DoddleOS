# Doddle Healthcare Skills

> Clinic marketing skills for appointment booking, recall, intake, reputation, and high-value procedure ads.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). 5 specialised healthcare skills covering new patient → booked visit → recall → review.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `healthcare-booking` | Online booking, reminders, no-show recovery | `/health:booking` |
| `healthcare-recall` | Hygiene/checkup recall, dormant reactivation | `/health:recall` |
| `healthcare-intake` | New-patient forms, insurance verification | `/health:intake` |
| `healthcare-reputation` | HIPAA-safe review generation + responses | `/health:reputation` |
| `healthcare-ads` | High-value procedure ads + call tracking | `/health:ads` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-healthcare-skills
/plugin install doddle-healthcare-skills@doddle-healthcare-skills
```

Manual: `cp -r doddle-healthcare-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### healthcare-booking (Browsing → Booked Visit)
- Online booking UX (real-time slots, mobile-first)
- Reminder sequence (SMS day-before + morning-of)
- Waitlist backfill for cancellations
- No-show recovery + rebooking flow

### healthcare-recall (Due → Returned)
- Recall intervals by treatment (hygiene 6-mo, ortho, annuals)
- Overdue segmentation (30/90/180-day tiers)
- Reactivation offers (no discounts on care — convenience plays)
- Front-desk call scripts + SMS templates

### healthcare-intake (Booked → Ready)
- New-patient form (minimum fields, pre-visit digital)
- Insurance verification checklist (eligibility, benefits, auth)
- Consent + HIPAA forms Venue: digital before arrival
- Reduces chair-time waste + claim denials

### healthcare-reputation (Visit → Review)
- HIPAA-safe ask flow (never confirm patient status publicly)
- Response playbooks (positive/neutral/negative, no PHI)
- Platform coverage (Google, Healthgrades, Zocdoc, Facebook)
- Rating rescue (<4.2 plan)

### healthcare-ads (Demand → High-Value consult)
- Procedure focus (implants, ortho, LASIK, aesthetics)
- Call-only + consultation-booking ads
- Call tracking + cost-per-start attribution
- Compliance: no before-after guarantees, no misleading claims

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Booking conversion + no-show rate | `healthcare-booking` |
| Recall coverage + dormant % | `healthcare-recall` |
| Intake completion + denial rate | `healthcare-intake` |
| Rating + response compliance | `healthcare-reputation` |
| Cost per treatment start | `healthcare-ads` |

## Compliance Note

Healthcare marketing must respect patient privacy (HIPAA-style: no PHI in reviews/ads/retargeting) and ad-platform healthcare policies. Every skill includes a compliance checkpoint. Not legal advice.

## Dependencies

Core + packs:
- `local-booking`, `local-reviews`, `local-ads` (doddle-local-skills)
- `form-cro` - Intake/booking forms
- `email-sequence`, `sms` - Reminders + recall
- `paid-advertising` - Paid fundamentals
- `analytics-attribution` - Call + booking attribution

## License

MIT License - Same as Doddle Marketing OS core
