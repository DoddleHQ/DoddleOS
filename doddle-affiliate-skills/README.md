# Doddle Affiliate OS

> Affiliate-site marketing: niche → keywords → content → links → revenue. Turns search demand into EPC without thin content or spam links.

## Overview

Independent OS pack for [DoddleOS](https://github.com/DoddleHQ/DoddleOS). Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted. Covers niche affiliate sites and programmatic comparison portfolios.

Naming: pack dir `doddle-affiliate-skills`, skills `affiliate-*`, IDs `doddle.affiliate.*`, commands `/affiliate:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `affiliate-niche` | Demand vs difficulty vs monetization scoring | `/affiliate:niche` |
| `affiliate-keywords` | Portfolio + programmatic templates | `/affiliate:keywords` |
| `affiliate-content` | Reviews/vs/best-X briefs + E-E-A-T QA | `/affiliate:content` |
| `affiliate-links` | Gap + outreach without spam | `/affiliate:links` |
| `affiliate-revenue` | Leakage + CRO plan for EPC | `/affiliate:revenue` |

## Installation

```bash
/plugin marketplace add doddleOS/doddleOS-marketing
/plugin install doddle-affiliate-skills@doddleOS-marketing
```

Manual: `cp -r doddle-affiliate-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### affiliate-niche (Idea → Go/No-go)
- Buyer-intent share, SERP difficulty, commission stability
- Output: niche_audit + shortlist, no invented volumes

### affiliate-keywords (Niche → Portfolio)
- Best-X / vs / alternatives clustering, template per pattern
- Cannibalization guard, hub internal links

### affiliate-content (Cluster → Brief)
- Tested angle, entities, FAQ, Review/ItemList schema
- Disclosure above fold + near CTA, cons included

### affiliate-links (Page → Authority)
- RD gap vs competitors, HARO + digital PR angles
- Internal equity first, outreach second

### affiliate-revenue (Traffic → EPC)
- Table above fold, single CTA, speed, network mix
- One-variable tests ordered by impact

## Optional bindings (peer packs, no install dependency)

- `doddle.marketing.programmatic-seo` - Template scale depth
- `doddle.marketing.schema-markup` - Review/FAQ structured data
- `doddle.marketing.page-cro` - Money-page CRO depth
- `doddle.marketing.digital-pr` - Linkable assets

## Validate

```bash
python3 doddle-core/scripts/validate.py   # 0 errors target
```

## License

MIT License - Same as DoddleOS core
