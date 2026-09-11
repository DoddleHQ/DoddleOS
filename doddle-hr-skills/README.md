# Doddle HR Skills

> People-ops skills for recruiting, screening, onboarding, culture, and employer brand.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). First non-marketing pack: same DoddleOS v2 scaffold (SKILL.md + blueprint.yaml, validator-gated).

Naming: pack dir `doddle-hr-skills`, skills `hr-*`, IDs `doddle.hr.*`, commands `/hr:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `hr-recruiting` | Job posts, sourcing, interview loops, offer close | `/hr:recruiting` |
| `hr-screening` | Triage, knockouts, scorecards, assessments | `/hr:screening` |
| `hr-onboarding` | Preboarding, 90-day plan, buddy, reviews | `/hr:onboarding` |
| `hr-culture` | Engagement pulses, rituals, recognition | `/hr:culture` |
| `hr-brand` | Careers page, review sites, employee advocacy | `/hr:brand` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-hr-skills
/plugin install doddle-hr-skills@doddle-hr-skills
```

Manual: `cp -r doddle-hr-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### hr-recruiting (Open Req → Signed Offer)
- Job post anatomy (outcomes + pay range, not laundry lists)
- Sourcing mix (referrals, outbound, boards, community)
- Interview loop design (max 4 touches, work-sample heavy)
- Offer close (comp bands, sell call, backchannel risk)

### hr-screening ( pile → Shortlist)
- Knockout questions (visa, location, comp, must-haves)
- Scorecards per role (skills weighted, no gut hires)
- Async assessments (paid trials > brainteasers)
- SLA: every applicant touches within 5 days

### hr-onboarding (Signed → Productive)
- Preboarding (laptop, accounts, day-one agenda before start)
- 30/60/90 plan with one measurable win per phase
- Buddy + manager cadence (weekly → biweekly)
- 30/60/90 reviews with written feedback

### hr-culture (Team → Engaged)
- Pulse surveys (quarterly, 5 questions, anonymous)
- Values rituals (weekly wins, demos, retros)
- Recognition systems (peer-nominated, specific)
- Retention drivers (growth paths, comp reviews, manager quality)

### hr-brand (Unknown → Talent Magnet)
- Careers page (team, mission, pay philosophy, process)
- Review-site hygiene (Glassdoor/AmbitionBox responses)
- Employee advocacy (LinkedIn prompts, referral bonus)
- Content: build-in-public engineering/life posts

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Time-to-hire + offer acceptance | `hr-recruiting` |
| Screen quality + interview load | `hr-screening` |
| 90-day ramp + early attrition | `hr-onboarding` |
| Engagement + regretted attrition | `hr-culture` |
| Inbound applicant share | `hr-brand` |

## Dependencies

Core skills (no new integration needed):
- `copywriting` - Job posts + employer content
- `email-sequence` - Candidate + onboarding comms
- `onboarding-cro` - Activation patterns (adapted to people)
- `brand-building` - Employer brand foundations
- `analytics-attribution` - Funnel measurement
- Integrations: `notion` (scorecards, plans), `asana` (hiring pipeline), `slack` (pulses, recognition)

## License

MIT License - Same as Doddle Marketing OS core
