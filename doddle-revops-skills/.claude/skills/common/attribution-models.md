# Attribution & Cohort Reference

## Attribution models

| Model | Rule | Use when |
|-------|------|----------|
| `linear` | Equal credit across eligible touchpoints | Short cycles, even contribution |
| `time-decay` | `0.5 ^ (days_before_close / half_life)` | Long cycles, recency matters |
| `position-based` | 40% first, 40% last, 20% across the middle | Discovery plus closing touches |

Eligibility: touchpoint occurred on or before close and within `--window-days` (default 90).
Join order: `deal_id`, then `contact_id`. Only **won** deals carry revenue.

## Reading coverage

| Metric | Meaning |
|--------|---------|
| `attribution_coverage` | Attributed revenue ÷ won revenue |
| `unattributed_revenue` | Won revenue with no eligible touchpoint — a tracking gap |
| `attributed_deals` vs `won_deals` | Deals with at least one touchpoint |

Unattributed revenue is a **data quality finding**, not a modelling artefact. Report it in the
headline.

## Cohort metrics

| Metric | Definition |
|--------|------------|
| `cohort_size` | Distinct accounts first seen in the cohort month |
| `logo_retention` | Active accounts in a period ÷ cohort size |
| `revenue_retention` | Revenue in a period ÷ period-0 revenue |

Period index is months since `cohort_start`. A period-0 value of `null` revenue retention means
revenue was not recorded for the cohort base — it is not zero.

## Leakage reading

- Period 0 low → acquisition or activation problem, not a retention problem.
- Period 1 cliff → onboarding or time-to-value gap.
- Flat after period 2 → a stable base; growth must come from new cohorts.
- Revenue retention below logo retention → pricing or expansion mix problem.

## Rules

- The model and window are `advisory`; state them on every figure.
- Never compare ROI across different models without saying so.
- Never run raw SQL against production from this pack — use exports and `references/sql/`.
