# PQL Model Reference

The model file is configuration. Change it deliberately and keep it versioned.

```json
{
  "aha_events": ["created_project", "invited_teammate"],
  "event_weights": {"created_project": 60, "invited_teammate": 40, "page_view": 2},
  "weights": {"fit": 0.4, "intent": 0.4, "recency": 0.2},
  "thresholds": {"pql": 70, "hot": 85},
  "window_days": 30,
  "min_aha_count": 1,
  "as_of": "2026-11-26T00:00:00Z"
}
```

## Scoring

| Component | Definition |
|-----------|------------|
| `fit` | `fit_score` from the account export (0–100). Advisory — it is a stated belief. |
| `intent` | Sum of `event_weights` for events inside the window, capped at 100. |
| `recency` | Linear decay from 100 at the last event to 0 at the window edge. |

`pql_score = (fit×w_fit + intent×w_intent + recency×w_recency) / Σweights`

## Tiers

| Tier | Rule |
|------|------|
| `hot` | score ≥ `thresholds.hot` **and** `aha_count` ≥ `min_aha_count` |
| `pql` | score ≥ `thresholds.pql` **and** `aha_count` ≥ `min_aha_count` |
| `nurture` | scored, but below threshold or missing the aha count |
| `insufficient_data` | no `fit_score` for the account |

## Calibration

- **Aha events never trigger.** The event is not in the taxonomy, or the threshold is too high.
- **Everything is hot.** Lower thresholds, or raise `min_aha_count`.
- **Everything is nurture.** Check the event weights and the window before moving thresholds.
- **Unknown accounts.** `metrics.unknown_account_events` counts events with no matching account —
  an identity problem, fixed in `revops-data-infrastructure`, not by rescoring.

## Rules

- Thresholds and weights are `advisory` assumptions; state them with every score.
- Never tune a threshold to match a number someone wants. Tune it to behaviour.
- Never treat a PQL as a revenue prediction.
