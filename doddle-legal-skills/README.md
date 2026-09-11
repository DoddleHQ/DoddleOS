# Doddle Legal Skills

> Law-firm marketing skills for intake, guides SEO, consults, reputation, and referrals.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). Turns searches into signed matters: qualify fast, consult well, prove trust, earn referrals.

Naming: pack dir `doddle-legal-skills`, skills `legal-*`, IDs `doddle.legal.*`, commands `/legal:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `legal-intake` | Qualification, conflict check, speed-to-lead | `/legal:intake` |
| `legal-guides` | Practice-area guides that rank + convert | `/legal:guides` |
| `legal-consults` | Booking→show, prep, fee transparency | `/legal:consults` |
| `legal-reputation` | Reviews, case results within rules | `/legal:reputation` |
| `legal-referrals` | Past-client + attorney-to-attorney | `/legal:referrals` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-legal-skills
/plugin install doddle-legal-skills@doddle-legal-skills
```

Manual: `cp -r doddle-legal-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### legal-intake (Inquiry → Qualified Matter)
- Practice-area fit + case-value triage
- Conflict check before deep dives
- 5-minute speed-to-lead (call + text)
- Decline fast with referral out (goodwill + reciprocity)

### legal-guides (Search → Consult)
- One practice area = one hub (PI, family, DUI, estate...)
- Cost/timeline/process content (what clients actually ask)
- Local intent pages (city + practice area)
- Consult CTA on every guide (not just contact page)

### legal-consults (Booked → Showed → Signed)
- Prep sequence (what to bring, what happens, fee ranges)
- Show-rate plays (confirm-reply, day-before call)
- Fee transparency (ranges early, surprises kill trust)
- 24h followup (summary + next step + deadline)

### legal-reputation (Matter → Review)
- Ask flow (post-win, post-closing, never during)
- Bar-safe responses (no case details, no outcome promises)
- Platform coverage (Google, Avvo, Yelp, Facebook)
- Case results pages (with disclaimers, anonymized where required)

### legal-referrals (Client → Next Matter)
- Past-client touches (law changes, check-ins, anniversaries)
- Attorney-to-attorney network (conflict + niche overflow)
- Referral fee rules (check jurisdiction — many ban non-lawyer splits)
- COI and community presence plays

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Inquiry-to-qualified rate + speed | `legal-intake` |
| Guide traffic + consult rate | `legal-guides` |
| Show rate + sign rate | `legal-consults` |
| Rating + response compliance | `legal-reputation` |
| Referral share of matters | `legal-referrals` |

## Compliance Note

Law-firm marketing is regulated: no guaranteed outcomes, no "specialist/expert" claims unless certified, testimonial disclaimers where required, no misleading dramatizations. Every skill includes a bar-rules checkpoint. Not legal advice — have counsel review.

## Dependencies

Core + packs (no new integration needed):
- `form-cro`, `lead-qualifier` - Intake + triage
- `seo-mastery`, `programmatic-seo`, `copywriting` - Guides
- `local-booking`, `local-reviews` - Consults + reputation
- `email-sequence`, `sms` - Followup + reminders
- `referral-program`, `partnerships` - Referral network
- Integrations: `hubspot` (matters), `google-analytics`, `google-search-console`, `semrush`

## License

MIT License - Same as Doddle Marketing OS core
