# Cohort Analysis Reference

Cohort analysis answers "what happens to a group of customers after they arrive?" — the
question a funnel snapshot cannot answer.

## Structure

Rows are account-periods:

```csv
account_id,cohort_start,period_start,active,revenue
acct_1,2026-09-01,2026-09-01,1,100
acct_1,2026-09-01,2026-10-01,1,120
```

- `cohort_start` — when the account joined the cohort (usually the signup or first-value month).
- `period_start` — the month being measured.
- `active` — did the account do the defining activity in that period.
- `revenue` — revenue recognised in that period.

Period index = months since `cohort_start`. Period 0 is the joining month.

## Reading the matrix

| Pattern | Reading |
|---------|---------|
| High period 0, flat after | Stable base; growth must come from new cohorts or expansion |
| High period 0, cliff at period 1 | Onboarding or time-to-value failure |
| Low period 0 | Acquisition quality or activation failure — not a retention problem |
| Logo retention holds, revenue retention falls | Pricing, discounting, or expansion mix |
| Retention improves by cohort | A product change worked; date it and keep it |

## Rules

- Cohort size must be reported next to every rate. A 100% rate on 2 accounts is not a signal.
- Revenue retention needs a period-0 revenue base; without it the value is `null`, not zero.
- Segment cohorts (SMB vs enterprise, channel, plan) only when the cohort size supports it.
- Changes in the event definition break comparability — note the change date in the report.
