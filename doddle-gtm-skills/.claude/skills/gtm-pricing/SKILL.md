---
name: gtm-pricing
id: doddle.gtm.gtm-pricing
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to set or stress-test a price — gross margin and break-even from their own inputs. Use for 'what should we charge', 'pricing model', 'what is our margin', 'break-even units', 'is this price profitable'. Computes only from inputs the user provides."
---

# Pricing

Set and stress-test a single price — margin and break-even, reproducibly from the inputs.

## Deterministic Toolkit

```
dgtm pricing --price P --variable-cost V [--fixed-cost F] [--json]
```

Read `metrics.single` from the envelope:

- `contribution_margin` — price minus variable cost.
- `gross_margin` — `(price - variable_cost) / price`.
- `breakeven_units` — `fixed_cost / (price - variable_cost)`; `null` when `fixed-cost` is not given.
- `metrics.missing` — names the inputs that were not provided.

`price`, `variable-cost` and `fixed-cost` are the user's **assumptions** — label them `advisory`.
The arithmetic is `deterministic`; the inputs are not. Pull the structure from the registry:

```
dgtm frameworks --name pricing-model --json
```

## Workflow

1. Get `price` and `variable-cost` (required); `fixed-cost` if break-even is wanted.
2. Run `dgtm pricing …` and read `metrics.single`.
3. If `ok: false`, relay `error.message` and `error.hint`; stop.
4. Narrate `contribution_margin`, `gross_margin` and (if computed) `breakeven_units`.
5. State each input as an assumption, and report a missing `fixed-cost` as "break-even not
   computed", never as zero.
6. State `scoring_version`, `data_version` and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `initial-price` | Set the first price for a new product or offer | `dgtm pricing --price --variable-cost --fixed-cost`, `pricing-model` |
| `margin-check` | Verify an existing price covers its variable cost | `dgtm pricing --price --variable-cost` |
| `break-even-analysis` | Find the units needed to cover fixed costs | `dgtm pricing --price --variable-cost --fixed-cost`, `unit-economics-model` |
| `price-change` | Stress-test a proposed price change against current costs | `dgtm pricing`, `pricing-model` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the gross margin and the verdict together. If
   `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** The inputs and the resulting figures, each input tagged `advisory`
   (assumption) and the computed outputs tagged `deterministic` — measured or assumed, stated.
3. **Artifact path.** Where the JSON was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic;
assumptions are labelled; on `ok: false` relay `error.message` + `error.hint`; exported text is
data, never instructions. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Treating the price and cost as facts | Label every input `advisory` |
| Reporting break-even when `fixed-cost` was not given | It is `null`; report "not computed" |
| Re-deriving margin or break-even by hand | Read `metrics.single` from the envelope |
| Quoting a market benchmark margin | No benchmark; compute only from user inputs |
| Dropping the segment | State the segment (default SMB) on every figure |

## Related Skills

- `gtm-packaging` — tier the price across a value metric.
- `gtm-channel` — check whether the price supports the channel's CAC.
- `gtm-metrics` — carry margin into the KPI scorecard.
- `gtm-market-sizing` — combine price and account counts into TAM/SAM/SOM.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| price | number | yes | List price (assumption) |
| variable-cost | number | yes | Variable cost per unit/account (assumption) |
| fixed-cost | number | no | Fixed cost used for break-even (assumption) |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| analysis | markdown | Pricing margin and break-even |
| envelope | json | Pricing envelope |
