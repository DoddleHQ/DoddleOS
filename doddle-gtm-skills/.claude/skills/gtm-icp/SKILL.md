---
name: gtm-icp
id: doddle.gtm.gtm-icp
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to define or score an ideal customer profile. Use for 'define our ICP', 'ideal customer profile', 'who should we target', 'score these accounts', 'qualify our best-fit customers'. Weights and 0-100 scores are the user's assumptions; this skill never presents them as facts."
---

# ICP Definition

Define a scored ideal customer profile from weighted criteria the user supplies.

## Deterministic Toolkit

```
dgtm score --criteria name:weight:score [--criteria name:weight:score ...] [--target T] [--json]
dgtm frameworks --name icp-template --json
```

Read the JSON envelope:

- `metrics.composite` — the weighted score (0-100) over the criteria that were scored.
- `metrics.coverage` — the share of total weight that was actually scored.
- `criteria[]` — `name`, `weight`, `score`, `contribution` per criterion.
- `notes[]` — criteria that were not measured.

Every `weight` and `score` is a user **assumption** (`advisory`); the `composite` and `coverage`
are computed (`deterministic`). `coverage` below 1 means some criteria were not scored — report
it as not measured, never as zero. Read `frameworks[0].sections` for the ICP structure. Enrich
target accounts with `doddle.tool.v1.clearbit.company` (read-only); if unavailable, ask for the
account list and print `NOT AVAILABLE — configure doddle.tool.v1.clearbit.company`.

## Workflow

1. Elicit the qualifying criteria, each with a weight and a 0-100 score (or leave the score blank).
2. Run `dgtm score --criteria …` and read `metrics`, `criteria` and `notes`.
3. Read the `icp-template` structure with `dgtm frameworks --name icp-template`.
4. Fill firmographics, technographics, triggers, buying committee and disqualifiers from the inputs.
5. Optionally enrich the target accounts via `doddle.tool.v1.clearbit.company`.
6. Narrate the composite and coverage; label every weight and score `advisory`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `definition-only` | Define the ICP before any account list exists | `icp-template` |
| `account-scoring` | Score a supplied account list against the ICP | `dgtm score` |
| `refinement` | Re-weight criteria after new win/loss evidence | `dgtm score`, `icp-template` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the composite and coverage together, tagged with the
   assumption that the weights are the user's. If any criterion is unscored, say so here.
2. **Key evidence.** The criteria and their contributions, tagged `deterministic`; the weights and
   scores tagged `advisory` (assumptions).
3. **Artifact path.** Where the ICP was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Presenting weights as measured facts | Label every weight and score `advisory` |
| Reading `coverage` below 1 as a zero score | It means some criteria were not scored |
| Confusing the ICP (an account) with a persona (a role) | The ICP is account-level; personas are roles |
| Recomputing the weighted mean by hand | Read `metrics.composite` from the envelope |
| Guessing firmographics instead of enriching | Use clearbit, or ask for the account list |

## Related Skills

- `gtm-segmentation` — group accounts into segments before profiling.
- `gtm-persona` — the role-level view inside the ICP.
- `gtm-abm` — tier accounts against the ICP.
- `gtm-market-sizing` — size the market the ICP defines.
- `gtm-lead-scoring` — apply the same criteria to inbound leads.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| criteria | string | yes | Weighted qualifying criteria for the ICP |
| accounts | file | no | Optional account list to score against the ICP |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| icp | markdown | ICP definition |
| envelope | json | Weighted score envelope |
