---
name: gtm-channel
id: doddle.gtm.gtm-channel
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to compare acquisition channels on unit economics — CAC, LTV:CAC and payback. Use for 'which channel is best', 'compare channels', 'channel economics', 'paid vs organic vs partner', 'where should we spend'. Inputs are assumptions the user supplies."
---

# Channel Economics

Compare channels on the same unit economics — reproducibly from each channel's inputs.

## Deterministic Toolkit

```
dgtm unit-economics --cac C --arpa A --gross-margin G --churn R [--json]
```

Run it once per channel and read `metrics` from each envelope:

- `ltv` — `arpa x gross_margin / churn`.
- `ltv_cac` — `ltv / cac`.
- `cac_payback_months` — `cac / (arpa x gross_margin)`.
- `monthly_gross_profit` — `arpa x gross_margin`.
- `inputs` and `notes` — the exact values used and any missing input.

CAC, ARPA, gross margin and churn are the user's **assumptions** — label them `advisory`. A
churn of `0` yields `ltv` of `null` (undefined, not infinite). Compare channels **only** on inputs
from the same period and segment.

## Workflow

1. List the channels to compare and the segment (default **SMB**).
2. Collect `cac`, `arpa`, `gross-margin` and `churn` per channel; label each `advisory`.
3. Run `dgtm unit-economics …` once per channel and read each `metrics` block.
4. Narrate the relative economics — payback and LTV:CAC — without recomputing them.
5. Flag any channel missing an input as not comparable, not as zero.
6. State `scoring_version`, `data_version` and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `channel-compare` | Default: rank two or more channels on one window and segment | `dgtm unit-economics` per channel |
| `single-channel-check` | Viability of one channel ("should we keep paid search?") | `dgtm unit-economics` |
| `budget-shift` | Deciding where the next increment of spend should go | `dgtm unit-economics` per channel, `demand-gen-plan` |
| `partner-vs-direct` | Comparing a partner-led motion against direct acquisition | `dgtm unit-economics` per channel, `partnership-model` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence naming the leading channel and its payback or LTV:CAC. If
   `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** Per-channel figures tagged `deterministic` (computed) and their inputs
   tagged `advisory` (assumed) — measured or assumed, stated.
3. **Artifact path.** Where the JSON was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic;
assumptions are labelled; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Presenting assumed CAC as measured | Label every input `advisory` |
| Comparing channels from different windows | Use one period and one segment |
| Treating zero churn as infinite LTV | `ltv` is `null`; it is undefined |
| Re-deriving payback by hand | Read `metrics.cac_payback_months` |
| Ranking a channel with a missing input | Mark it not comparable, not worst |

## Related Skills

- `gtm-demand-gen` — turn the winning channels into a plan.
- `gtm-pricing` — price and margin set the channel ceiling.
- `gtm-plg` — the product loop is one channel to compare.
- `gtm-metrics` — track channel economics in the scorecard.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| cac | number | yes | Channel acquisition cost (assumption) |
| arpa | number | yes | Average revenue per account, monthly (assumption) |
| gross-margin | number | no | Gross margin fraction (assumption) |
| churn | number | no | Monthly churn rate (assumption) |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| analysis | markdown | Channel economics comparison |
| envelope | json | Unit-economics envelope |
