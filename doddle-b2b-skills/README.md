# Doddle B2B OS

> Agency/services marketing skills for outbound, proposals, case studies, retainers, and partnerships.

## Overview

Independent OS pack for [DoddleOS](https://github.com/doddleOS/doddleOS-marketing). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. 5 specialised B2B skills covering pipeline → proposal → proof → recurring revenue.

Naming: pack dir `doddle-b2b-skills`, skills `b2b-*`, IDs `doddle.b2b.*`, commands `/b2b:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `b2b-outbound` | ICP, cold email + LinkedIn, deliverability | `/b2b:outbound` |
| `b2b-proposals` | Scoping, pricing, SoW, followup | `/b2b:proposals` |
| `b2b-cases` | Case study interview → approval → distribution | `/b2b:cases` |
| `b2b-retainers` | Retainer packaging, QBRs, churn defense | `/b2b:retainers` |
| `b2b-partnerships` | Referral partners, co-marketing, channel | `/b2b:partnerships` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-b2b-skills
/plugin install doddle-b2b-skills@doddle-b2b-skills
```

Manual: `cp -r doddle-b2b-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### b2b-outbound (ICP → Meeting)
- ICP + trigger list building (hiring, funding, tech)
- Cold email deliverability (SPF/DKIM/DMARC, warmup, volume caps)
- Personalization at scale (account → persona → hook)
- LinkedIn touch pattern + call bridge
- Positive-reply routing + SLA

### b2b-proposals (Opp → Signed)
- Discovery-to-scope traceability (every line item earned)
- Good/better/best packaging + decoy
- SoW essentials (scope, exclusions, timeline, payment)
- Followup cadence + objection handling (price, timing, incumbent)

### b2b-cases (Win → Proof Asset)
- Client interview guide (before → after → numbers)
- Permission + logo approval workflow
- One-page + deck + web + social cuts from one interview
- Distribution: outbound proof, proposal inserts, ads

### b2b-retainers (Project → MRR)
- Productized tiers vs custom scope
- QBR format (wins, metrics, roadmap, upsell)
- Utilization + scope-creep guardrails
- At-risk saves + downgrade paths (vs churn)

### b2b-partnerships (Alone → Ecosystem)
- Partner tiers (referral, co-sell, co-market, tech)
- Outreach + enablement kit (one-pager, deck, commission)
- Co-marketing plays (webinar, report, integration)
- Partner-sourced pipeline attribution

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Outbound reply + meeting rate | `b2b-outbound` |
| Proposal win rate + cycle length | `b2b-proposals` |
| Proof coverage per offer | `b2b-cases` |
| Retainer MRR + logo retention | `b2b-retainers` |
| Partner-sourced pipeline share | `b2b-partnerships` |

## Optional bindings (peer packs, no install dependency)

Core skills (no new integration needed):
- `cold-email` - Outbound fundamentals
- `customer-research` - ICP development
- `pricing-strategy`, `offers` - Packaging
- `churn-prevention` - Retainer defense
- `partnerships`, `referral-program` - Ecosystem
- `revops` - Pipeline + handoff
- `email-sequence` - Followup automation

## License

MIT License - Same as DoddleOS core
