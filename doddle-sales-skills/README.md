# Doddle Sales Skills

> B2B sales-execution skills for prospecting, discovery, negotiation, forecasting, and enablement.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). Sits between marketing and revenue: turns pipeline into forecastable closes.

Naming: pack dir `doddle-sales-skills`, skills `sales-*`, IDs `doddle.sales.*`. Commands extend the EXISTING `/sales:*` category (outreach, pitch, battlecard, qualify already live) — no new namespace.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `sales-prospecting` | ICP lists, triggers, sequencing, AE handoff | `/sales:prospecting` |
| `sales-discovery` | Qualification, call plans, stakeholder maps | `/sales:discovery` |
| `sales-negotiation` | Objections, discount guardrails, give-gets | `/sales:negotiation` |
| `sales-forecasting` | Pipeline hygiene, stages, inspection cadence | `/sales:forecasting` |
| `sales-enablement` | Decks, one-pagers, battlecards, rep onboarding | `/sales:enablement` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-sales-skills
/plugin install doddle-sales-skills@doddle-sales-skills
```

Manual: `cp -r doddle-sales-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### sales-prospecting (TAM → Worked Accounts)
- ICP → account tiers (A/B/C effort split)
- Trigger monitoring (hiring, funding, tech, intent)
- Sequencing (email + phone + social touches)
- AE/SDR handoff + meeting quality bar

### sales-discovery (Meeting → Qualified Opp)
- MEDDIC-lite qualification (metrics, decision, paper process)
- Call plan per meeting (objectives, questions, landmines)
- Stakeholder mapping (champion, blocker, econ buyer)
- No-go discipline (disqualify fast, recycle with reason)

### sales-negotiation (Proposal → Signed)
- Objection library (price, timing, incumbent, status quo)
- Discount guardrails (floor, approval matrix, give-gets)
- Multi-threading (never single-threaded over $X)
- Close plans with dated mutual actions

### sales-forecasting (Pipeline → Predictable Number)
- Stage definitions with exit criteria (no vibes)
- Commit/best-case/pipeline categorization
- Inspection cadence (weekly deal review format)
- Slippage forensics (why deals slip, stage-0 honesty)

### sales-enablement (Product → Rep-Ready)
- Asset gap audit (what reps actually send)
- Deck/one-pager/battlecard production from one brief
- Demo asset library (click paths, datasets, stories)
- New-rep onboarding (certification, shadow, first deals)

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Top-of-funnel coverage + meeting quality | `sales-prospecting` |
| Qualification rigor + stakeholder spread | `sales-discovery` |
| Win rate + discount leakage | `sales-negotiation` |
| Forecast accuracy + stage hygiene | `sales-forecasting` |
| Asset usage + ramp time | `sales-enablement` |

## Dependencies

Core + packs (no new integration needed):
- `cold-email`, `customer-research` - Prospecting
- `revops` - Stages, routing, SLA
- `pricing-strategy`, `offers` - Negotiation levers
- `analytics-attribution` - Source-to-close
- `product-marketing` - Enablement source of truth
- `b2b-outbound`, `b2b-proposals` (doddle-b2b-skills) - Agency-flavored siblings
- Integrations: `hubspot` (pipeline), `slack` (alerts), `notion` (assets), `semrush` (account intel)

## License

MIT License - Same as Doddle Marketing OS core
