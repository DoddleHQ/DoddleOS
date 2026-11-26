# Reverse ETL Reference

Reverse ETL copies operational data **out** of a system of record (CRM, billing, support) into
the warehouse, so analysis has one copy instead of five live queries.

## Shape of a sync

```json
{
  "name": "crm_deals_to_warehouse",
  "source": "crm.opportunities",
  "destination": "fct_opportunities",
  "enabled": true,
  "sync_mode": "incremental",
  "cursor": "updated_at",
  "schedule": "hourly",
  "owner": "revops",
  "verification": "row count delta + checksum"
}
```

## Checks that matter

| Check | Failure it prevents |
|-------|--------------------|
| Destination named | A sync that writes nowhere, or writes to the wrong model |
| Cursor column exists and is indexed | Full reloads, missed rows, silent gaps |
| Primary key present at the destination | Duplicates and update storms |
| Row-count delta within tolerance | A broken filter that drops most rows |
| Idempotent write | Re-runs duplicating revenue |
| Owner assigned | Nobody fixes it when it drifts |
| Verification query written | Nobody can prove the sync is correct |

## Drift between source and destination

When CRM and warehouse disagree, check in this order:

1. **Sync health** — is the sync running, and did the last run succeed?
2. **Cursor lag** — is the newest source row missing because the cursor stopped?
3. **Filter drift** — is a filter on the sync excluding rows the report expects?
4. **Mapping drift** — did a source field change shape (a renamed column, a new stage value)?
5. **Identity drift** — are the two sides joined on different keys?

## Rules

- Reverse ETL never becomes the source of truth. The operational system owns the record.
- Read-only skill: propose the sync change, run it in dry-run, verify, then hand off to the
  owner for execution.
- A sync without a verification query is not finished.
