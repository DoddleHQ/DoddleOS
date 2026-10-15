# Doddle SaaS OS

> SaaS-specific marketing skills for homepage, pricing, trial activation, retention/dunning, and expansion.

## Overview

Independent OS pack for [DoddleOS](https://github.com/DoddleHQ/DoddleOS). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. 14 specialised SaaS skills covering visitor → trial → paid → expansion.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `saas-homepage` | Hero, proof, pricing teaser → trial/demo | `/saas:homepage` |
| `saas-pricing` | Tier design, metered vs seat, annual toggle | `/saas:pricing` |
| `saas-trial` | Signup → activation → PQL → sales handoff | `/saas:trial` |
| `saas-retention` | Dunning, save flow, winback | `/saas:retention` |
| `saas-expansion` | Seat/usage upsell, advocacy, referral | `/saas:expansion` |
| `saas-onboarding` | Signup + onboarding CRO + aha instrumentation (calls signup-flow-cro, onboarding-cro) | `/saas:onboarding` |
| `saas-paywall` | Paywall + upgrade-moment CRO (calls paywall-upgrade-cro) | `/saas:paywall` |
| `saas-emails` | Lifecycle drip: trial/activation/dunning/winback (calls email-sequence) | `/saas:emails` |
| `saas-analytics` | PQL scoring, TTV, funnel diagnosis (calls analytics-attribution) | `/saas:analytics` |
| `saas-dunning` | Failed-payment recovery + save/winback (calls churn-prevention, stripe stub) | `/saas:dunning` |
| `saas-comparison` | Vs/alternatives pages (calls competitor-alternatives) | `/saas:comparison` |
| `saas-reviews` | G2/Capterra flywheel | `/saas:reviews` |
| `saas-security` | Trust center + questionnaire kit | `/saas:security` |
| `saas-docs` | Help-center SEO (calls onboarding-cro) | `/saas:docs` |

## Installation

```bash
/plugin marketplace add DoddleHQ/DoddleOS
```

> Per-pack plugin install is planned; install single packs via manual copy below.

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

## Optional bindings (peer packs, no install dependency)

Core [Doddle Marketing OS](https://github.com/DoddleHQ/DoddleOS) skills:
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

MIT License - Same as DoddleOS core
