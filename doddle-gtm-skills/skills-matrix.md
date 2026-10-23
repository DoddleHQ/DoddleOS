# Skills Matrix

32 skills, 7 agents. Default segment: **SMB** unless stated otherwise. Every `id` is
`doddle.gtm.<dir-name>`. Toolkit: `dgtm`. Framework slugs are read from `dgtm frameworks`
(30 registered, `gtm-frameworks-2026-10-2`). Every skill carries a `## Sub-flows` table.

## Strategy & positioning (7)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-strategy` | gtm-strategist | unit-economics, funnel, frameworks | Assemble the whole go-to-market plan |
| `gtm-positioning` | positioning-strategist | frameworks (positioning-canvas) | Who you serve, the alternative, the differentiated value |
| `gtm-messaging` | positioning-strategist | frameworks (messaging-house) | Turn positioning into a messaging house |
| `gtm-icp` | positioning-strategist | score, frameworks (icp-template) | Scored ideal customer profile |
| `gtm-market-sizing` | revenue-analyst | size-market | Bottom-up TAM/SAM/SOM from inputs |
| `gtm-competitive` | positioning-strategist | frameworks (competitive-teardown, battlecard) | Competitive landscape and gaps |
| `gtm-intl` | gtm-strategist | advisory only | Market ranking + minimum launch pack |

## Segments & accounts (3)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-segmentation` | gtm-strategist | size-market, frameworks | Segment definitions and priority |
| `gtm-persona` | positioning-strategist | frameworks (persona-template) | Buyer personas |
| `gtm-abm` | demand-gen-strategist | score, frameworks (abm-tiering) | ABM tiers and plays |

## Demand & pipeline (6)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-demand-gen` | demand-gen-strategist | funnel, frameworks (demand-gen-plan) | Demand plan against a pipeline target |
| `gtm-lead-scoring` | demand-gen-strategist | score | Weighted fit + intent lead model |
| `gtm-outbound` | demand-gen-strategist | frameworks | Outbound sequence plan and copy |
| `gtm-pipeline-analytics` | revenue-analyst | audit, report | Audit a deals export |
| `gtm-forecasting` | revenue-operations | audit, frameworks (forecast-model) | Forecast from recorded pipeline |
| `gtm-win-loss` | revenue-operations | audit, frameworks (win-loss-interview) | Win/loss analysis |

## Content & enablement (5)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-launch` | gtm-strategist | frameworks (launch-checklist) | Cross-functional launch plan |
| `gtm-sales-narrative` | enablement-lead | frameworks (sales-narrative) | Sales narrative |
| `gtm-enablement` | enablement-lead | frameworks | Enablement program |
| `gtm-battlecards` | enablement-lead | frameworks (battlecard) | Competitive battlecard |
| `gtm-case-study` | enablement-lead | advisory only | Customer proof story |

## Pricing & monetization (3)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-pricing` | gtm-strategist | pricing, frameworks (pricing-model) | Margin and break-even |
| `gtm-packaging` | gtm-strategist | pricing (tiers) | Packaging on a value metric |
| `gtm-expansion` | revenue-operations | audit | Upsell/cross-sell/renewal plan |

## Channels & growth (4)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-partnerships` | partner-manager | frameworks (partnership-model) | Partnership model |
| `gtm-channel` | partner-manager | unit-economics | Channel economics comparison |
| `gtm-plg` | demand-gen-strategist | funnel, frameworks (plg-loop) | Product-led growth loop |
| `gtm-advocacy` | partner-manager | report, frameworks (case-study-brief) | References, reviews, referral flywheel |

## Measurement & ops (4)

| Skill | Agent | Toolkit | Purpose |
|-------|-------|---------|---------|
| `gtm-metrics` | revenue-analyst | unit-economics, funnel | KPI scorecard |
| `gtm-reporting` | revenue-analyst | report | Presentation layer over the audit |
| `gtm-experimentation` | demand-gen-strategist | funnel, frameworks (experimentation-brief) | Test designed before it runs |
| `gtm-onboarding` | enablement-lead | advisory only, frameworks (onboarding-plan) | Customer onboarding / time-to-value |

## Agents

| Agent | Owns (count) | Owns |
|-------|--------------|------|
| `gtm-strategist` | 6 | The end-to-end plan: strategy, segmentation, launch, pricing, packaging, intl |
| `positioning-strategist` | 5 | Positioning, messaging, ICP, personas, competitive |
| `demand-gen-strategist` | 6 | Demand gen, outbound, ABM, lead scoring, PLG, experimentation |
| `enablement-lead` | 5 | Narrative, enablement, battlecards, case studies, onboarding |
| `revenue-analyst` | 4 | Market sizing, pipeline analytics, metrics, reporting |
| `revenue-operations` | 3 | Forecasting, win/loss, expansion |
| `partner-manager` | 3 | Partnerships, channel, advocacy |

Every skill has exactly one owner agent; agents hand off via their `## Escalation` section.
