# Health Scoring and Retention Math

## The numbers

| Metric | Formula |
|--------|---------|
| NRR | `(starting_arr + expansion_arr − contraction_arr − churned_arr) / starting_arr` |
| GRR | `(starting_arr − contraction_arr − churned_arr) / starting_arr` |

ARR components come from the customer export. They are the **user's beliefs** (`advisory`);
usage signals are measured (`live`).

## Health score

Starts at 100 and is reduced by:

| Condition | Penalty |
|-----------|---------|
| Inactive in the latest usage period | −30 |
| Usage drop over the threshold (default 20%) | −min(40, drop %) |
| No usage history at all | score is `null` (not a low score) |

`health_score` is a deterministic usage signal. It is **not** a churn probability, and it must
never be presented as one.

## Flags

| Flag | Condition |
|------|-----------|
| `renewal_risk` | Renewal inside the window (default 90 days) **and** (usage drop over threshold, or `churned_arr > 0`, or `contraction_arr > 0`, or inactive) |
| `expansion_candidate` | Usage growth over the threshold **and** `expansion_arr` is 0 |

`health_penalties` records which rule fired, so a reviewer can challenge it.

## Reading it

- Health down, no renewal date → a watch item, not a risk.
- Health down, renewal close → the save play starts now.
- Expansion candidate with no expansion booked → the strongest expansion signal available, and
  still only a signal.
- One customer dominating the ARR base → NRR moves on that account alone. Report the
  concentration.

## Rules

- Never present ARR inputs as measured facts.
- Never convert a health score into a "churn probability".
- Never book expansion revenue from an expansion candidate.
- Save plays and expansion plays are proposals for the CSM; the pack never contacts the customer.
