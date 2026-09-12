# Doddle GTM OS

> Go-to-market orchestration: ICP → message → channel → launch → sales → expansion. Sequences execution packs into one plan.

## Overview

Independent OS pack for [DoddleOS](https://github.com/doddleOS/doddleOS-marketing). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. Orchestration layer over marketing, sales, and vertical packs.

Naming: pack dir `doddle-gtm-skills`, skills `gtm-*`, IDs `doddle.gtm.*`, commands `/gtm:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `gtm-strategy` | ICP, TAM tiering, message, channel mix, launch gates | `/gtm:strategy` |
| `gtm-abm` | Account select, personalize, orchestrate plays | `/gtm:abm` |
| `gtm-win-loss` | Battlecards, loss analysis, competitive traps | `/gtm:win-loss` |
| `gtm-sales-playbook` | MEDDIC, demo, RFP, discount guardrails | `/gtm:playbook` |
| `gtm-channel` | Reseller, co-sell, affiliate design + ops | `/gtm:channel` |
| `gtm-advocacy` | References, reviews flywheel, community proof | `/gtm:advocacy` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-gtm-skills
/plugin install doddle-gtm-skills@doddle-gtm-skills
```

Manual: `cp -r doddle-gtm-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### gtm-strategy (TAM → Launch Plan)
- ICP + TAM sizing + A/B/C tiering
- Positioning → message house → channel mix
- Launch gates (product, marketing, sales, CS ready)
- Calls peer packs: `doddle.marketing.*`, `doddle.sales.*`

### gtm-abm (Accounts → Pipeline)
- Account selection + scoring (fit + intent)
- Personalization tiers (1:1, 1:few, 1:many)
- Plays: warm-up, exec outreach, direct mail, ads
- SDR/AE orchestration + meeting bar

### gtm-win-loss (Deals → Learning)
- Battlecard per competitor (traps, landmines, proof)
- Loss interview script + coding taxonomy
- Win reasons → message + product feedback loop

### gtm-sales-playbook (Hire → Quota)
- MEDDIC-lite qualification + exit criteria
- Demo script (situation → click → value)
- RFP response kit + discount approval matrix
- New-rep ramp (certification, shadow, first deals)

### gtm-channel (Partner → Sourced Pipeline)
- Partner tiers (referral, reseller, co-sell)
- Enablement kit + deal registration
- Co-marketing plays + sourced-pipeline share

### gtm-advocacy (Customers → Proof)
- Reference recruitment + review flywheel
- Case pipeline (ask → draft → approve → publish)
- Community signals → expansion triggers

## Optional bindings (peer packs, no install dependency)

Orchestrates (via `call`):
- `doddle.marketing.product-marketing` - Positioning input
- `doddle.sales.prospecting` - Outbound execution
- `doddle.sales.enablement` - Asset production

## License

MIT License - Same as DoddleOS core
