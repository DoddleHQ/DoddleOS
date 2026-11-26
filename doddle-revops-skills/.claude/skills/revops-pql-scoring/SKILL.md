---
name: revops-pql-scoring
id: doddle.revops.revops-pql-scoring
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants to score product-qualified leads from product events — fit, intent, recency, aha thresholds, and account tiers. Use for 'PQL model', 'product qualified leads', 'aha moment', 'which accounts are sales ready', 'activation threshold', 'lead scoring for PLG'."
---

# RevOps PQL Scoring

Score accounts from product telemetry with a deterministic, versioned model. This replaces
MQL points with evidence about real usage.

## Deterministic Toolkit

```
drev pql --events <file.jsonl|csv> --accounts <file.csv|json> --model <model.json>
```

Read the JSON envelope:

- `metrics.tiers` — counts per `hot`, `pql`, `nurture`, `insufficient_data`.
- `metrics.average_pql_score` — average across scored accounts only.
- `metrics.unknown_account_events` — events that matched no known account (identity gaps).
- `rows[]` — per account: `fit_score`, `intent_score`, `recency_score`, `aha_count`,
  `event_count`, `last_event_at`, `pql_score`, `tier`.
- `completeness.missing` — accounts with no fit score.

The model file is configuration, not prose:

```json
{
  "aha_events": ["created_project", "invited_teammate"],
  "event_weights": {"created_project": 60, "invited_teammate": 40, "page_view": 2},
  "weights": {"fit": 0.4, "intent": 0.4, "recency": 0.2},
  "thresholds": {"pql": 70, "hot": 85},
  "window_days": 30,
  "min_aha_count": 1
}
```

Score = `(fit×w_fit + intent×w_intent + recency×w_recency) / Σweights`, where intent is the
capped sum of `event_weights` in the window and recency decays linearly to zero at the window
edge. Tiers require both the score threshold **and** `min_aha_count` aha events.

## Workflow

1. Confirm the segment (default **SMB**), the window, and the owner of the model.
2. Collect the event export, the account list with `fit_score`, and the model. If a fit score is
   missing for an account, it is reported as `insufficient_data` — never as a zero.
3. Run `drev pql …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report the tier distribution, then the accounts that crossed a threshold, with the evidence
   that moved them (`aha_count`, `event_count`, `last_event_at`).
6. Name the calibration gaps: unknown accounts, accounts with no fit score, aha thresholds that
   never trigger.
7. Propose alert and routing rules as a **dry-run plan** — this skill sends nothing.
8. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `pql-triage` | Default: tier the account base | `drev pql` → `metrics.tiers` |
| `aha-calibration` | The aha event or threshold is disputed | model `aha_events` + `rows[].aha_count` |
| `threshold-review` | Sales says the PQL list is wrong | model `thresholds` vs `rows[].pql_score` |
| `identity-gap` | Events exist for unknown accounts | `metrics.unknown_account_events` |
| `slack-alert-draft` | A routed alert is wanted | `rows[]` → proposed Slack payload (not sent) |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the tier distribution and the verdict. If
   `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** Tier counts and the driving accounts, each tagged `deterministic` (computed)
   or `live` (read from the export); model assumptions tagged `advisory`.
3. **Artifact path.** Where the JSON or report was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent an event, aha moment, or score; `null` is not measured, not zero; never
do arithmetic; model weights and thresholds are the user's assumptions and are labelled
`advisory`; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Treating an account with no fit score as a zero-fit account | It is `insufficient_data` |
| Calling a PQL a revenue prediction | It ranks readiness; it does not forecast |
| Hardcoding a benchmark aha event | Define it in the model, sourced from the product |
| Ignoring unknown-account events | Report them; they are identity gaps |
| Auto-sending alerts from this skill | Read-only — deliver the payload, the owner sends it |

## Related Skills

- `doddle.revops.revops-data-infrastructure` — validate the event table and identity map first.
- `doddle.revops.revops-attribution` — revenue outcomes for the same accounts.
- `doddle.saas.analytics` — PQL guidance and measurement audit.
- `doddle.gtm.gtm-plg` — activation funnel design and loop structure.
- `doddle.gtm.gtm-lead-scoring` — fit-and-intent scoring for marketing-sourced leads.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| events | file | yes | Product event export (JSONL/CSV) |
| accounts | file | no | Account export with `account_id` and `fit_score` |
| model | file | yes | PQL model (JSON) |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Tier summary, leading accounts, calibration actions |
| envelope | json | Deterministic PQL scoring envelope |
