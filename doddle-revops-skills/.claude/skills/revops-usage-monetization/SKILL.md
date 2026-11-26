---
name: revops-usage-monetization
id: doddle.revops.revops-usage-monetization
version: 1.1.0
blueprint: ./blueprint.yaml
description: "When the user wants usage-based pricing or monetisation math — rated usage, credit consumption, overage, and an invoice preview. Use for 'usage based pricing', 'metered billing', 'credits', 'overage', 'value metric', 'invoice preview', 'Stripe metered'."
---

# RevOps Usage & Monetization

Rate what customers actually used, consume the credits they were granted, and preview the
invoice. Nothing here writes to a billing system.

## Deterministic Toolkit

```
drev meter --usage <usage.jsonl|csv> --plan <plan.json>
```

Read the JSON envelope:

- `rows[]` — per account and period: `quantity`, `credits_available`, `credits_used`,
  `included_units`, `billable_units`, `base_amount`, `overage_amount`, `total_amount`,
  `currency`.
- `metrics.total_billed` / `total_overage_amount` / `credits_used`.
- `metrics.unrated_usage_rows` — usage that matched no tier. These are a **data gap**: they are
  excluded from the invoice and must be resolved, not absorbed.

Order of operations in the tool: credits are consumed first (1 credit per unit), then the
included units, then the remainder bills at `unit_price`.

```json
{
  "currency": "USD",
  "tiers": [
    {"name": "Pro", "price": 99, "included_units": 1000, "unit_price": 0.05, "credits": 100}
  ]
}
```

### Write path (gated)

The preview is read-only. Recording metered usage is a **write**, so the blueprint gates it:

```yaml
- {id: approve_billing, type: gate, needs: [meter], produces: [decision],
   approvers: [owner], timeout_s: 3600, on_approve: proceed, on_reject: revise}
- {id: record_meter_event, type: tool, ref: doddle.tool.v1.stripe.recordMeterEvent,
   needs: [approve_billing], produces: [meter_receipt]}
```

Order is fixed: **preview → approve → record**. The meter-event payload reuses the preview's
`event_id`, so a retry never double-counts. Without approval the usage is priced but not
recorded, and the report says so.

## Workflow

1. Confirm the segment (default **SMB**), the billing period, and the plan version.
2. Collect the usage rows and the plan. Every usage row must resolve to a tier — either declared
   on the row or mapped in the plan.
3. Run `drev meter …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report the invoice preview: base, overage, credits used, total. Flag any account whose total
   moved more than the agreed threshold — bill shock is a churn risk, not a revenue win.
6. Name the unrouted usage rows and the accounts they belong to.
7. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `invoice-preview` | Default: rate usage and preview the invoice | `drev meter` → `rows[]` |
| `credit-burn` | Credits are exhausted earlier than expected | `rows[].credits_used` vs `credits_available` |
| `bill-shock-review` | A large overage appeared | `rows[].overage_amount` vs `base_amount` |
| `value-metric-check` | The metered unit may not track value | `rows[].quantity` per account |
| `unrated-usage` | Usage exists with no tier | `metrics.unrated_usage_rows` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying total billed and the verdict.
2. **Key evidence.** The rated rows tagged `deterministic` (computed) or `live` (read from the
   export); plan prices and units tagged `advisory`.
3. **Artifact path.** Where the JSON or the preview was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent usage, prices, or credits; `null` is not measured, not zero; never do
arithmetic; the preview creates no billing object; on `ok: false` relay `error.message` +
`error.hint`. Full block: `common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Recording meter events without approval | `approve_billing` is a hard stop — preview, approve, then record |
| Ignoring unrouted usage rows | They are excluded from the total — resolve them |
| Pricing on a unit that does not scale with value | Re-check the value metric first |
| Hiding bill shock in a total | Report the accounts whose total moved sharply |
| Assuming credits and included units are the same thing | Credits burn first, then included units |

## Related Skills

- `doddle.revops.revops-retention` — NRR, health, and expansion on the same accounts.
- `doddle.saas.saas-pricing` — value-metric and tier framing guidance.
- `doddle.gtm.gtm-pricing` — margin, break-even, and tier mix.
- `doddle.saas.saas-dunning` — recovering failed payments after a price change.
- `doddle.revops.revops-data-infrastructure` — validate the usage table before billing on it.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| usage | file | yes | Usage rows (JSONL/CSV) |
| plan | file | yes | Plan definition (JSON) with tiers |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Rated usage, credit burn, overage, invoice preview |
| envelope | json | Deterministic metering envelope |
