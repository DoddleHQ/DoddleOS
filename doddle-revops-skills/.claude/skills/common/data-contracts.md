# Data Contracts

Shared shapes for the inputs this pack reads. Field names are matched case-insensitively.

## Warehouse table profile (`warehouse_export`)

```json
{
  "snapshot_at": "2026-11-25T00:00:00Z",
  "tables": [
    {
      "name": "fct_opportunities",
      "row_count": 128400,
      "columns": ["account_id", "stage", "amount", "created_at", "closed_at"],
      "owner": "revops",
      "primary_key": "opportunity_id",
      "authoritative": true,
      "updated_at": "2026-11-25T06:00:00Z",
      "destinations": ["crm.opportunities"]
    }
  ]
}
```

- `authoritative` marks the source of truth for a metric. Missing owner, primary key, or
  `authoritative` keeps the table in `incomplete` status.
- `destinations` lists reverse-ETL targets.

## dbt manifest (`dbt_manifest`)

A standard `manifest.json`. The profiler reads `nodes`, `sources`, and `tests`, and lists models
without a `description` as undocumented.

## Identity map (`identity_map`)

```csv
source_id,canonical_id,match_method,confidence
crm_123,acct_9f3,deterministic,1.0
web_556,acct_9f3,fuzzy,0.74
```

- A record without `canonical_id` is **unmapped**, not a duplicate.
- Confidence below `0.8` is counted as `low_confidence`.

## Reverse-ETL config (`reverse_etl_config`)

```json
{
  "syncs": [
    {"name": "crm_deals_to_warehouse", "source": "crm.opportunities", "destination": "fct_opportunities", "enabled": true},
    {"name": "trial_signups", "source": "app.trials", "enabled": true}
  ]
}
```

An enabled sync without a `destination` (or `model`) is **unconfigured** and blocks readiness.

## Event export (`events`)

```json
{"account_id": "acct_9f3", "event_name": "created_project", "event_at": "2026-11-20T10:00:00Z"}
```

Required: `account_id`, `event_name`, `event_at`. Optional: `user_id`, `properties`.

## Accounts (`accounts`)

Required: `account_id`. Optional: `fit_score` (0–100), `segment`, `owner`. A missing
`fit_score` produces the `insufficient_data` tier — never a zero.

## Touchpoints (`touchpoints`)

Required: `contact_id` or `deal_id`, `channel`, `occurred_at`. Optional: `campaign`, `cost`.

## Deals (`deals`)

Required: `amount`, `closed_at`, `outcome` (`won` / `lost` / `open`). Optional: `deal_id`,
`contact_id`. Only won deals carry revenue.

## Cohort input (`cohorts`)

Required: `account_id`, `cohort_start`, `period_start`. Optional: `active`, `revenue`.
