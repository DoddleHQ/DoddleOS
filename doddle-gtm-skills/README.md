# Doddle GTM OS (`doddle-gtm-skills`)

> Synced from the standalone source of truth: [`DoddleHQ/doddle-go-to-market-skills`](https://github.com/DoddleHQ/doddle-go-to-market-skills)
> (tag `v0.2.0`). This DoddleOS copy keeps pack name `doddle-gtm-skills` and commands
> `/gtm:*` for existing consumers; skill IDs are `doddle.gtm.<skill>`.

**Doddle Go-To-Market OS** — 32 agent-agnostic skills and 7 agents for taking a product to
market: positioning, ICP, segmentation, demand, pipeline, enablement, pricing, expansion,
measurement and international entry. **Default segment: SMB.**

The one claim this pack makes: **every number is reproducible from recorded inputs.** A
stdlib-only Python toolkit (`dgtm`) computes; the skills narrate and prioritize. Unlike a
website audit, the inputs here are often *assumptions* — so the pack always distinguishes a
**measured** (`live`) number from an **assumed** (`advisory`) one, and says which is which.

## Why it is different

- **Deterministic toolkit.** Funnel conversion, unit economics, pricing, market sizing, weighted
  scoring and pipeline audit are computed in Python, never in prose. Same inputs → same outputs.
- **Assumptions are labelled, not hidden.** ACV, churn, ICP weights and market-size inputs are
  the user's beliefs. The skills say so, every time.
- **Versioned.** Every envelope carries `toolkit_version`, `scoring_version` (`gtm-1`) and
  `data_version` (`gtm-frameworks-2026-10-2`). Reports always state them.
- **Frameworks are configuration.** The 30 named templates live in a versioned registry
  (`dgtm frameworks`), never paraphrased from memory.
- **Read-only.** No CRM writes, no sends, no ad spend. This pack reads and analyses.
- **Agent-agnostic.** Each skill is a `SKILL.md` readable by Claude Code, opencode, Cursor or
  Codex, plus a DoddleOS `blueprint.yaml`.

## Install

The pack is self-contained. Point your agent at `.claude/skills/` (skills) and
`.claude/agents/` (agents), or install the DoddleOS plugin from `.claude-plugin/plugin.json`.

```bash
python3 scripts/dgtm doctor          # check the environment
python3 scripts/dgtm version
```

Python 3.9+; no dependencies (stdlib only).

## The toolkit — `dgtm`

```
dgtm version
dgtm frameworks [--name SLUG] [--json]
dgtm funnel --stage name:count --stage name:count ... [--json]
dgtm unit-economics --cac C --arpa A --gross-margin G --churn R [--json]
dgtm pricing --price P --variable-cost V [--fixed-cost F] [--tier name:price:cost:mix ...] [--json]
dgtm size-market --accounts N --acv X [--sam-pct S --som-pct O] [--json]
dgtm score --criteria name:weight:score ... [--target T] [--json]
dgtm audit  <deals.json|csv> [--json]
dgtm report <deals.json|csv> [--out FILE] [--json]
dgtm doctor
```

Every command emits a JSON **evidence envelope**. Example:

```bash
python3 scripts/dgtm report tests/fixtures/deals.json --out GTM-PIPELINE.md
```

The pipeline audit reads a deals export (columns like `stage`, `amount`, `created_at`,
`closed_at`, `outcome`, `segment`; common aliases accepted) and scores data hygiene and pipeline
mechanics — **not** revenue outcomes.

## What is in the pack

**Skills (32)** grouped by the GTM motion (every skill ships a `## Sub-flows` table):

| Group | Skills |
|-------|--------|
| Strategy & positioning | gtm-strategy, gtm-positioning, gtm-messaging, gtm-icp, gtm-market-sizing, gtm-competitive, gtm-intl |
| Segments & accounts | gtm-segmentation, gtm-persona, gtm-abm |
| Demand & pipeline | gtm-demand-gen, gtm-lead-scoring, gtm-outbound, gtm-pipeline-analytics, gtm-forecasting, gtm-win-loss |
| Content & enablement | gtm-launch, gtm-sales-narrative, gtm-enablement, gtm-battlecards, gtm-case-study |
| Pricing & monetization | gtm-pricing, gtm-packaging, gtm-expansion |
| Channels & growth | gtm-partnerships, gtm-channel, gtm-plg, gtm-advocacy |
| Measurement & ops | gtm-metrics, gtm-reporting, gtm-experimentation, gtm-onboarding |

**Agents (7):** `gtm-strategist`, `positioning-strategist`, `demand-gen-strategist`,
`enablement-lead`, `revenue-analyst`, `revenue-operations`, `partner-manager`. Every skill has
exactly one owner; agents hand off via `## Escalation` sections.

Full inventory: [`skills-matrix.md`](skills-matrix.md). Authoring rules: [`AGENTS.md`](AGENTS.md).

## Slash commands

Every skill is reachable as `/gtm:<name>` (files under `.claude/commands/gtm/`):

| Command | Skill | Command | Skill |
|---------|-------|---------|-------|
| `/gtm:strategy` | gtm-strategy | `/gtm:market-sizing` | gtm-market-sizing |
| `/gtm:positioning` | gtm-positioning | `/gtm:competitive` | gtm-competitive |
| `/gtm:messaging` | gtm-messaging | `/gtm:playbook` | gtm-sales-narrative (legacy alias) |
| `/gtm:icp` | gtm-icp | `/gtm:enablement` | gtm-enablement |
| `/gtm:persona` | gtm-persona | `/gtm:battlecards` | gtm-battlecards |
| `/gtm:segmentation` | gtm-segmentation | `/gtm:case-study` | gtm-case-study |
| `/gtm:abm` | gtm-abm | `/gtm:onboarding` | gtm-onboarding |
| `/gtm:demand-gen` | gtm-demand-gen | `/gtm:pricing` | gtm-pricing |
| `/gtm:lead-scoring` | gtm-lead-scoring | `/gtm:packaging` | gtm-packaging |
| `/gtm:outbound` | gtm-outbound | `/gtm:expansion` | gtm-expansion |
| `/gtm:pipeline-analytics` | gtm-pipeline-analytics | `/gtm:partnerships` | gtm-partnerships |
| `/gtm:forecasting` | gtm-forecasting | `/gtm:channel` | gtm-channel |
| `/gtm:win-loss` | gtm-win-loss | `/gtm:plg` | gtm-plg |
| `/gtm:launch` | gtm-launch | `/gtm:advocacy` | gtm-advocacy |
| `/gtm:sales-narrative` | gtm-sales-narrative | `/gtm:intl` | gtm-intl |
| `/gtm:metrics` | gtm-metrics | `/gtm:reporting` | gtm-reporting |
| `/gtm:experimentation` | gtm-experimentation | | |

## Validation

```bash
python3 scripts/lint_pack.py && python3 -m pytest tests -q
python3 doddle-core/scripts/validate.py --strict   # from repo root
```
