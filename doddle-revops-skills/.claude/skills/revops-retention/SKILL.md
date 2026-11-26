---
name: revops-retention
id: doddle.revops.revops-retention
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants revenue retention math and churn risk — NRR, GRR, usage-based health, renewal risk, and expansion signals from recorded data. Use for 'NRR', 'net revenue retention', 'churn risk', 'health score', 'renewal risk', 'expansion signals', 'usage drop off'."
---

# RevOps Retention

Compute the retention numbers, then read the usage signals behind them. The health score is a
**deterministic usage signal**, not a predictive churn model.

## Deterministic Toolkit

```
drev retention --customers <customers.csv|json> --usage <usage.csv|json> \
  [--renewal-window-days 90] [--dropoff-threshold 0.20]
```

Read the JSON envelope:

- `metrics.nrr` — `(starting_arr + expansion_arr − contraction_arr − churned_arr) / starting_arr`
- `metrics.grr` — `(starting_arr − contraction_arr − churned_arr) / starting_arr`
- `metrics.average_health_score`, `renewal_risk_count`, `expansion_candidates`.
- `rows[]` — per customer: ARR components, `usage_dropoff`, `usage_growth`, `health_score`,
  `health_penalties`, `days_to_renewal`, and `flags`.

Health starts at 100. It loses 30 when the account is inactive in the latest period, and up to
40 points when the usage drop exceeds the threshold. Flags:

| Flag | Condition |
|------|-----------|
| `renewal_risk` | Renewal inside the window **and** (usage drop over threshold, or churn, or contraction, or inactive) |
| `expansion_candidate` | Usage growth over the threshold **and** `expansion_arr` is 0 |

## Workflow

1. Confirm the segment (default **SMB**), the cohort period, and the renewal window.
2. Collect the customer export (ARR components are the user's stated beliefs) and the usage
   export (measured).
3. Run `drev retention …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report NRR and GRR with the ARR inputs labelled `advisory` and the usage signals `live`.
6. List the renewal-risk accounts with their reason (`health_penalties`, `flags`), then the
   expansion candidates with the usage growth that triggered them.
7. Propose the save/expand play for each account — as a proposal for the CSM.
8. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `nrr-review` | Default: NRR/GRR with the driver accounts | `metrics.nrr`, `metrics.grr` |
| `renewal-watch` | A renewal is approaching | `rows[].flags` → `renewal_risk` |
| `usage-drop` | Usage fell and nobody noticed | `rows[].usage_dropoff`, `health_penalties` |
| `expansion-scout` | Find accounts ready to grow | `flags` → `expansion_candidate` |
| `cohort-read` | Retention by cohort rather than a snapshot | `drev cohorts` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying NRR, GRR, and the verdict.
2. **Key evidence.** The flagged accounts tagged `deterministic` (computed) or `live` (usage);
   ARR inputs tagged `advisory`.
3. **Artifact path.** Where the JSON or the play was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent ARR, churn, or usage; `null` is not measured, not zero; never do
arithmetic; the health score is not a churn probability; on `ok: false` relay `error.message` +
`error.hint`. Full block: `common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Presenting ARR inputs as measured facts | They are the user's beliefs — label them `advisory` |
| Calling the health score a churn prediction | It is a deterministic usage signal |
| Flagging churn risk without a renewal date | The flag needs the renewal inside the window |
| Reporting an expansion candidate as expansion revenue | It is a signal, not booked revenue |
| Ignoring accounts with no usage history | Health is `null` — no usage data, not a low score |

## Related Skills

- `doddle.revops.revops-attribution` — where the revenue actually came from.
- `doddle.revops.revops-call-intelligence` — what the customer said before the risk appeared.
- `doddle.revops.revops-qbr` — turn the risk into the customer conversation.
- `doddle.saas.saas-retention` — dunning, save flows, and winback playbooks.
- `doddle.gtm.gtm-expansion` — upsell, cross-sell, and renewal planning.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| customers | file | yes | Customer export with ARR components |
| usage | file | yes | Usage export with period and usage_value |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | NRR/GRR, health, renewal risk, expansion candidates |
| envelope | json | Deterministic retention envelope |
