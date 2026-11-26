---
name: revops-revenue-portfolio
id: doddle.revops.revops-revenue-portfolio
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants a public teardown or pricing comparison portfolio — normalized pricing models, dated evidence, confidence grading, and a publishable outline. Use for 'teardown', 'pricing comparison', 'benchmark analysis', 'public writing', 'revenue portfolio', 'competitive pricing'."
---

# RevOps Revenue Portfolio

Compare what competitors publish, grade how fresh and complete the evidence is, and outline the
teardown. Public claims need a source and a date — otherwise they are `NOT AVAILABLE`.

## Deterministic Toolkit

```
drev portfolio --companies <companies.json> --observations <observations.csv|json>
```

Read the JSON envelope:

- `rows[]` — `kind: company` rows: `pricing_model` (normalized to `seat`, `metered`, `hybrid`,
  `flat`, `free`, or `unknown`), `value_metric`, `price`, `observations`,
  `latest_observed_at`, `observation_age_days`, `confidence` (`low` / `medium` / `high`), and
  `url`; plus `kind: outline` rows with the six teardown sections.
- `metrics.comparable` — `true` only when every company shares one pricing model.
- `metrics.price_min` / `price_max` / `price_median` — populated **only** when comparable.
- `metrics.low_confidence_companies`.

If the pricing models differ, the comparison is withheld and the envelope says why. Comparing a
per-seat price against a usage price is not a benchmark.

## Workflow

1. Confirm the segment (default **SMB**), the scope, and whether this is internal analysis or
   published work.
2. Collect the company list and dated observations. Capture the source URL with every
   observation.
3. Run `drev portfolio …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report the normalized models, the evidence confidence per company, and the comparison only if
   `metrics.comparable` is `true`. Otherwise say the comparison was withheld and why.
6. Fill the six-section teardown outline using the supplied observations only. Mark every
   unsupported cell `NOT AVAILABLE`.
7. Flag anything that needs legal or competitive-intel review before it is published.
8. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `portfolio-default` | Default: normalize and grade the set | `drev portfolio` → `rows[]` |
| `like-for-like` | A price benchmark is requested | `metrics.comparable`, `metrics.price_median` |
| `evidence-freshness` | Old captures may be stale | `observation_age_days`, `confidence` |
| `teardown-outline` | A public write-up is planned | `rows[]` (`kind: outline`) |
| `pricing-psychology` | Pricing design is the question | `doddle.marketing.marketing-psychology` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying what is comparable, the evidence quality, and the
   verdict.
2. **Key evidence.** Company rows tagged `deterministic` (normalized) or `live` (observed, dated);
   comparison figures tagged `advisory` when the models differ.
3. **Artifact path.** Where the JSON or the outline was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a competitor price, claim, or observation; never compare prices across
different pricing models; `null` is not measured, not zero; never do arithmetic; on `ok: false`
relay `error.message` + `error.hint`. Full block: `common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Comparing a seat price to a usage price | The tool withholds it — use like-for-like only |
| Publishing a price with no capture date | Every claim needs a source and a date |
| Treating low-confidence data as a benchmark | Report the confidence level next to the number |
| Filling the outline from memory | Only supplied observations enter it |
| Presenting the outline as publish-ready | It needs human review before it ships |

## Related Skills

- `doddle.marketing.marketing-psychology` — pricing psychology and persuasion structures.
- `doddle.gtm.gtm-competitive` — competitive teardown structure and evidence discipline.
- `doddle.gtm.gtm-case-study` — proof assets and storytelling.
- `doddle.gtm.gtm-pricing` — margin and break-even on your own prices.
- `doddle.revops.revops-usage-monetization` — your own metered pricing mechanics.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| companies | file | yes | Companies JSON with pricing model and price |
| observations | file | yes | Dated observations with source URLs |
| segment | string | no | Segment focus; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Normalized comparison, confidence, teardown outline |
| envelope | json | Deterministic portfolio envelope |
