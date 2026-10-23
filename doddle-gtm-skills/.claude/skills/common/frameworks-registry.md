# Framework Registry

Named templates live in `scripts/doddle_gtm/frameworks.py`, versioned as one unit
(`gtm-frameworks-2026-10-2`). A framework is a **structure**, not a market figure — it carries no
statistics, so it never goes stale the way a benchmark does.

Always read a framework's sections from the toolkit:

```
dgtm frameworks                 # list all
dgtm frameworks --name battlecard
```

Never paraphrase a framework's structure from memory; quote it from the command.

## Registered frameworks

| Slug | Name | Purpose |
|------|------|---------|
| `positioning-canvas` | Positioning Canvas | Who you serve, the alternative, the differentiated value, the proof |
| `messaging-house` | Messaging House | Core proposition, pillars, proof, message by persona and stage |
| `icp-template` | ICP Definition | Scored ideal-customer profile plus disqualifiers |
| `persona-template` | Buyer Persona | Role-level goals, pains, objections and the message that lands |
| `launch-checklist` | GTM Launch Checklist | Cross-functional launch plan and readiness gate |
| `battlecard` | Competitive Battlecard | Arm sellers against a specific competitor |
| `sales-narrative` | Sales Narrative | A pitch structured as a story from problem to proof |
| `pipeline-review` | Pipeline Review Agenda | A forecast-honest pipeline meeting |
| `unit-economics-model` | Unit Economics Model | Assemble CAC, LTV, payback inputs |
| `pricing-model` | Pricing & Packaging Model | Value metric, tiers, margins, migration |
| `abm-tiering` | ABM Tiering | Tier target accounts and match effort to value |
| `win-loss-interview` | Win/Loss Interview | Structured interview script for closed deals |
| `onboarding-plan` | Customer Onboarding Plan | Time-to-value for a new customer |
| `partnership-model` | Partnership Model | Design an alliance with clear mutual value |
| `plg-loop` | Product-Led Growth Loop | Acquisition and expansion through the product |
| `demand-gen-plan` | Demand Generation Plan | Plan channels against a pipeline target |
| `experimentation-brief` | Experimentation Brief | A test designed before it runs |
| `forecast-model` | Forecast Model | Build a forecast from recorded pipeline |
| `competitive-teardown` | Competitive Teardown | Structured read of a competitor's GTM |
| `case-study-brief` | Case Study Brief | Turn a customer win into proof |
| `jtbd-interview` | Jobs-to-be-Done Interview | The job the buyer hired the product to do |
| `buying-committee-map` | Buying Committee Map | Every role in a B2B deal and how to reach each |
| `aarrr-metrics` | AARRR Metrics Framework | Acquisition to revenue, bottleneck first |
| `territory-plan` | Sales Territory Plan | Accounts, quota and capacity per territory |
| `sales-capacity-model` | Sales Capacity Model | Reps, win rate, coverage → required pipeline |
| `partnership-scorecard` | Partnership Scorecard | Score a partner on recorded evidence |
| `channel-fit-matrix` | Channel Fit Matrix | Score channels on fit before spending |
| `win-loss-program` | Win/Loss Program | Continuous interview program and coding scheme |
| `nrr-waterfall` | Net Revenue Retention Waterfall | Expansion, contraction, churn, new ARR |
| `launch-readiness-gate` | Launch Readiness Gate | Go / no-go scored before launch day |

## Rules

1. **Structure from the registry, content from inputs.** A framework tells you *which sections
   to fill*; the user's data and the skills' analysis fill them.
2. **Never invent a framework.** If a slug is not registered, say so and offer the closest one.
3. **Bump `data_version`** when frameworks are added or their sections change.
