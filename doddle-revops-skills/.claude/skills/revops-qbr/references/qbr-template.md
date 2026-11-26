# QBR Template

`drev qbr --account <account.json>` builds the scoreboard, the ROI line, and the deck outline.
This file is the shape of a review that lands.

## Scoreboard

| Metric | Target | Actual | Delta | Status |
|--------|--------|--------|-------|--------|
| expansion_arr | 18000 | 18000 | 0 | on_track |

Status rules:

| Status | Condition |
|--------|-----------|
| `on_track` | actual ≥ target |
| `at_risk` | actual ÷ target ≥ 0.80 |
| `off_track` | actual ÷ target < 0.80 |
| `not_measured` | target or actual was not supplied |

## ROI

`ROI = (revenue − investment) / investment`

When either input is missing the line reads **NOT AVAILABLE** and the envelope lists
`roi_inputs` in `completeness.missing`. Never estimate investment to fill it.

## Deck outline

| Slide | Content |
|-------|---------|
| `value-delivered` | Outcomes the customer recognises — in their language |
| `scorecard` | The KPI table, honest about misses |
| `risks` | Named risks with mitigations |
| `ask` | **One** ask, dated next step |

## Order of the conversation

1. Scorecard — where we stand.
2. Value — what changed for the customer.
3. Risks — what we know is not right.
4. The ask — what we need from them, with a date.

## Rules

- A review with five asks has none. One ask.
- Do not bury an off-track KPI; show it with the mitigation.
- Missing outcomes, risks, or asks are stated as missing, never invented.
- The pack prepares the review; the CSM presents it. Nothing is scheduled or sent here.
