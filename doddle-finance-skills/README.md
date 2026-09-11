# Doddle Finance Skills

> Advisor/finance marketing skills for lead-gen calculators, compliant onboarding, reviews, cross-sell, and COI referrals.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). Turns searches into AUM/premiums: capture with calculators, onboard cleanly, grow share-of-wallet.

Naming: pack dir `doddle-finance-skills`, skills `finance-*`, IDs `doddle.finance.*`, commands `/finance:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `finance-leads` | Calculator magnets, quote flows, speed-to-lead | `/finance:leads` |
| `finance-onboarding` | KYC-friendly onboarding, funding the account | `/finance:onboarding` |
| `finance-reviews` | Compliant review generation + responses | `/finance:reviews` |
| `finance-crosssell` | Annual reviews, life-event triggers, attach | `/finance:crosssell` |
| `finance-referrals` | COI network (CPA/attorney), client intros | `/finance:referrals` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-finance-skills
/plugin install doddle-finance-skills@doddle-finance-skills
```

Manual: `cp -r doddle-finance-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### finance-leads (Search → Appointment)
- Calculator magnets (retirement gap, fee drag, mortgage, insurance need)
- Quote/estimate flows with honest ranges
- Speed-to-lead (<5 min, licensed rep only where required)
- Seminar/webinar funnel for high-trust niches

### finance-onboarding (Signed → Funded)
- Document checklist (ID, statements, beneficiaries)
- KYC/AML-friendly steps (no shortcuts, clear status)
- First-90-day touch plan (welcome, funding, review)
- Drop-off rescue (stalled applications)

### finance-reviews (Client → Proof)
- Compliant ask flow (post-review-meeting, never incentivized)
- Testimonial rules (disclosures, no cherry-picked returns)
- Response playbooks (no specific performance claims)
- Platform coverage (Google, Yelp, industry directories)

### finance-crosssell (One Product → Household)
- Annual review as cross-sell engine
- Life-event triggers (job change, baby, home, inheritance)
- Next-best-product matrix per segment
- Advisor task prompts on signals

### finance-referrals (Client → Introductions)
- COI network (CPAs, attorneys, realtors) with reciprocity
- Client introduction asks (post-win moments)
- Educational events as referral engines
- Introducer tracking + thank-you discipline

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Lead volume + contact rate | `finance-leads` |
| Application completion + funding rate | `finance-onboarding` |
| Rating + response compliance | `finance-reviews` |
| Products per household + review coverage | `finance-crosssell` |
| Referral/COI share of new business | `finance-referrals` |

## Compliance Note

Finance marketing is regulated: no guaranteed returns, risk disclosures where required, testimonial/endorsement disclosure rules, licensed-activity boundaries for unlicensed staff. Every skill includes a compliance checkpoint. Not legal advice — have counsel/compliance review.

## Dependencies

Core + packs (no new integration needed):
- `lead-magnets`, `form-cro` - Calculators + flows
- `signup-flow-cro`, `onboarding-cro` - Onboarding patterns
- `local-reviews` - Reputation mechanics
- `email-sequence`, `sms` - Followup + reviews
- `referral-program`, `partnerships` - COI network
- Integrations: `hubspot` (pipeline), `google-analytics`, `google-search-console`, `semrush`

## License

MIT License - Same as Doddle Marketing OS core
