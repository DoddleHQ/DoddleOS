# Doddle Agency OS

> Agency-business skills: market the agency's own website, write winning proposals, price the work, onboard clients, and report results.

## Overview

Independent OS pack for [DoddleOS](https://github.com/DoddleHQ/DoddleOS). Provides 5 skills covering the agency client lifecycle — Market → Propose → Price → Onboard → Report — for marketing, software dev, AI, and consulting agencies. Installs and runs standalone; binds to peer packs only via blueprint `call` nodes where noted.

## Skills Included

| Skill | Purpose | Lifecycle stage |
|-------|---------|-----------------|
| `agency-marketing` | Market the agency's own website: positioning, services copy, case studies, proof | Win attention |
| `agency-proposals` | Winning proposals & SOWs: approach, scope, pricing presentation, terms | Win the deal |
| `agency-pricing` | Pricing models, rate cards, margin analysis, scenarios | Set the money model |
| `agency-client-onboarding` | Kickoff workflows, access checklists, cadence, first-30-days plan | Start clean |
| `agency-reporting` | Client reports, KPI rollups, ROI proof, QBR prep, renewal narratives | Prove & renew |

## Installation

### Option 1: Install as Plugin (Recommended)

```bash
# Add the monorepo as a marketplace
/plugin marketplace add DoddleHQ/DoddleOS
```

> Per-pack plugin install is planned; install single packs via manual copy below (Option 2).

### Option 2: Manual Installation

```bash
# Skills
cp -r doddle-agency-skills/.claude/skills/* your-project/.claude/skills/

# Agents (bundled, isolated)
cp -r doddle-agency-skills/.claude/agents/* your-project/.claude/agents/
```

## Agents (bundled)

Self-contained copies. No cross-pack agent refs: `researcher`, `planner`, `copywriter`, `conversion-optimizer`, `sales-enabler`, `continuity-specialist`.

## Optional bindings

Peer packs bind via blueprint `call` nodes (`type: call`, `ref: doddle.<domain>.<skill>`). No install dependency on any other pack. Kernel only: `doddle-core` spec v2 + `doddle.tool.v1` tools.

## Validate

```bash
python3 doddle-core/scripts/validate.py   # 0 errors target
```

## License

MIT License - Same as DoddleOS core
