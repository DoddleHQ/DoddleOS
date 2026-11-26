# Warehouse Readiness Checklist

Read every item before trusting a number that came out of a warehouse.

## Ownership

- [ ] Every table has a named owner (a team, not a person who left).
- [ ] Every table has a primary key declared.
- [ ] Exactly one table is authoritative per business metric. Two authoritative tables are a
      contradiction, not redundancy.

## Freshness

- [ ] Each table records when it last refreshed (`updated_at`).
- [ ] The freshness threshold is agreed per table class (facts hourly, dims daily).
- [ ] Stale tables are flagged, not silently excluded from a report.

## Grain

- [ ] The table grain is stated (one row per opportunity, per event, per account-month).
- [ ] Duplicate keys are counted, not assumed absent.
- [ ] Soft deletes and status flags are part of the contract.

## Semantics

- [ ] Currency and timezone are declared per monetary or time column.
- [ ] `null` has a documented meaning in every metric column.
- [ ] Derived metrics live in the model layer, not in ad-hoc spreadsheet logic.

## Access

- [ ] The agent's role can read the tables it needs and no more.
- [ ] Row-level security or masking is applied to PII columns.
- [ ] No credential is stored in the pack, a config file, or a prompt.

## What to do with a gap

Do not fill it with a guess. Mark the metric `NOT AVAILABLE`, name the missing artefact, and
propose the fix with an owner and a verification query.
