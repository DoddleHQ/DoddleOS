# Doddle SaaS Skills

> SaaS-specific marketing skills for homepage, pricing, trial activation, retention/dunning, and expansion.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). 5 specialised SaaS skills covering visitor → trial → paid → expansion.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `saas-homepage` | Hero, proof, pricing teaser → trial/demo | `/saas:homepage` |
| `saas-pricing` | Tier design, metered vs seat, annual toggle | `/saas:pricing` |
| `saas-trial` | Signup → activation → PQL → sales handoff | `/saas:trial` |
| `saas-retention` | Dunning, save flow, winback | `/saas:retention` |
| `saas-expansion` | Seat/usage upsell, advocacy, referral | `/saas:expansion` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-saas-skills
/plugin install doddle-saas-skills@doddle-saas-skills
```

Manual: `cp -r doddle-saas-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### saas-homepage (Visitor → Trial)
- Hero (outcome + proof, <5s clarity)
- Social proof stack (logos, G2, numbers)
- Pricing teaser + trial/demo CTA hierarchy
- Template: hero variants, proof inventory

### saas-pricing (Evaluation → Choice)
- Good/better/best tiers, decoy, anchoring
- Seat vs metered vs hybrid value metric
- Monthly/annual toggle, discount framing
- Enterprise "contact us" fence

### saas-trial (Signup → Activated PQL)
- Signup friction audit (SSO, no card, sample data)
- Activation checklist + aha-moment instrumentation
- Trial email drip (day 0/3/7/13)
- PQL scoring + sales handoff SLA

### saas-retention (At-risk → Saved)
- Failed-payment dunning (day 0/3/7/14 + in-app)
- Cancellation save flow (reasons → offers)
- Winback sequences (30/60/90-day)
- Churn reason taxonomy

### saas-expansion (Paid → More $)
- Seat expansion triggers + admin nudges
- Usage-limit upsell moments
- Annual prepay + multi-year plays
- Advocacy → referral loop

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Homepage → trial conversion | `saas-homepage` |
| Plan mix + discount leakage | `saas-pricing` |
| Trial → paid rate + TTV | `saas-trial` |
| Logo/MRR churn + failed payments | `saas-retention` |
| NRR + expansion attach | `saas-expansion` |

## Dependencies

Core [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing) skills:
- `page-cro` - Landing page CRO
- `pricing-strategy` - Pricing fundamentals
- `signup-flow-cro`, `onboarding-cro` - Trial UX
- `paywall-upgrade-cro` - Upgrade moments
- `churn-prevention` - Churn fundamentals
- `product-led-growth` - PLG motions
- `referral-program` - Advocacy loop
- `email-sequence` - Trial/dunning/winback emails
- `revops` - PQL + handoff

## License

MIT License - Same as Doddle Marketing OS core
