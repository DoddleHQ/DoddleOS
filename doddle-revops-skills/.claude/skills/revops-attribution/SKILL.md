---
name: revops-attribution
id: doddle.revops.revops-attribution
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants multi-touch attribution and cohort retention — allocate won revenue across touchpoints, report channel ROI, and build logo/revenue retention matrices. Use for 'attribution model', 'multi touch', 'which channel drove revenue', 'cohort analysis', 'retention curve', 'funnel leakage'."
---

# RevOps Attribution

Allocate revenue deterministically across touchpoints and read retention by cohort. Every
allocation is reproducible from the supplied rows.

## Deterministic Toolkit

```
drev attribution \
  --touchpoints <file.csv|json> \
  --deals <file.csv|json> \
  [--model linear|time-decay|position-based] \
  [--window-days 90] \
  [--half-life-days 7]

drev cohorts <file.csv|json> [--max-periods 12]
```

Read the JSON envelopes:

- `metrics.attributed_revenue`, `unattributed_revenue`, `attribution_coverage`.
- `metrics.attributed_deals` vs `won_deals`.
- `rows[]` with `kind: allocation` (per touchpoint) and `kind: channel` (per channel/campaign,
  with `attributed_revenue`, `cost`, `roi`).
- `metrics.cohorts`, `metrics.accounts` and `rows[]` with `logo_retention` and
  `revenue_retention` per cohort period.

Models:

| Model | Rule |
|-------|------|
| `linear` | Equal credit to every eligible touchpoint |
| `time-decay` | Exponential decay on days before close (`--half-life-days`) |
| `position-based` | 40% first, 40% last, 20% spread across the middle |

A touchpoint is eligible when it occurs on or before close and inside `--window-days`. Deals
join on `deal_id` first, then `contact_id`. Only **won** deals carry revenue.

## Workflow

1. Confirm the segment (default **SMB**), the attribution window, and the model.
2. Collect the touchpoint and deal exports. Confirm the join keys exist before running.
3. Run `drev attribution …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report attributed revenue by channel, then coverage and unattributed revenue — unattributed
   revenue is a data gap, not a modelling artefact to hide.
6. If cohort input is available, run `drev cohorts …` and report logo and revenue retention
   per cohort period.
7. Flag leakage risks named in the cohort matrix (a period-0 drop) and propose a fix.
8. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `mta-default` | Default: linear allocation of won revenue | `drev attribution --model linear` |
| `long-cycle` | A long sales cycle flattens linear credit | `--model time-decay` |
| `roi-review` | Channel ROI is disputed | `rows[]` (`kind: channel`) `cost` / `roi` |
| `leakage-audit` | Revenue is attributed but the funnel still leaks | `drev cohorts` + `references/sql/` |
| `coverage-gap` | A large share of revenue is unattributed | `metrics.attribution_coverage` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying attributed revenue, coverage, and the verdict. If
   `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** Channel rows and cohort rows, each tagged `deterministic` (computed) or
   `live` (read from the export); model choice and window tagged `advisory`.
3. **Artifact path.** Where the JSON or report was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a touchpoint, deal, or revenue figure; `null` is not measured, not zero;
never do arithmetic; the model and window are assumptions and are labelled `advisory`; on
`ok: false` relay `error.message` + `error.hint`. Full block:
`common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Attributing open or lost-deal revenue | Only won deals carry revenue |
| Hiding unattributed revenue in a footnote | It is a headline coverage gap |
| Comparing ROI across models without stating the model | State model and window on every figure |
| Treating a period-0 retention drop as a campaign failure | Read the cohort matrix before blaming channels |
| Running raw SQL against production from this skill | Use the exported files and `references/sql/` templates |

## Related Skills

- `doddle.revops.revops-data-infrastructure` — validate touchpoint and deal tables first.
- `doddle.revops.revops-pql-scoring` — product usage signals for the same accounts.
- `doddle.marketing.analytics-attribution` — attribution model selection and ROI reporting.
- `doddle.gtm.gtm-pipeline-analytics` — pipeline hygiene audit over a deals export.
- `doddle.gtm.gtm-reporting` — presentation layer over a pipeline audit.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| touchpoints | file | yes | Touchpoint export with channel and timestamp |
| deals | file | yes | Deals export with amount, close date, outcome |
| model | string | no | `linear` \| `time-decay` \| `position-based`; default `linear` |
| window_days | number | no | Attribution window; default 90 |
| cohorts | file | no | Cohort input for retention matrices |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Attribution summary, channel ROI, cohort retention |
| attribution_envelope | json | Deterministic attribution envelope |
| cohort_envelope | json | Deterministic cohort envelope |
