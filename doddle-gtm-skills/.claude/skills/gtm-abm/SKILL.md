---
name: gtm-abm
id: doddle.gtm.gtm-abm
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to tier target accounts and run account-based plays — Tier 1/2/3, effort matched to value, owners and a success metric. Use for 'ABM tiers', 'tier our target accounts', 'account-based plan', 'which accounts get 1:1', 'score our target list'. Tiering criteria are user assumptions."
---

# ABM

Tier target accounts by weighted criteria and match effort to value — reproducibly.

## Deterministic Toolkit

```
dgtm score --criteria name:weight:score [--criteria …] [--target <account>] [--json]
dgtm frameworks --name abm-tiering --json
```

Read the `score` envelope: `metrics.composite`, `metrics.coverage`, `criteria[]` (each with
`weight`, `score`, `contribution`) and `notes[]`. `coverage` is the share of criteria that
received a score; a missing score is `null`, not zero. Every criterion, weight and score is an
**assumption** the user supplies — label it `advisory`. Then read `frameworks[0].sections` from
`abm-tiering` — the structure the tiers are written into:

1. Tier 1 (1:1)
2. Tier 2 (1:few)
3. Tier 3 (1:many)
4. Account criteria
5. Play per tier
6. Owners
7. Success metric

Use `doddle.tool.v1.clearbit.company` for firmographic enrichment and
`doddle.tool.v1.hubspot.deals` for open deals; if either is unavailable, print
`⚠️ NOT AVAILABLE — configure <tool>` and ask for the account list and firmographics instead.

## Workflow

1. Pull the tiering structure with `dgtm frameworks --name abm-tiering`.
2. Take the weighted criteria from the user; confirm the weights sum to 1.
3. Run `dgtm score --criteria name:weight:score …` for each account and read the envelope.
4. Rank by `metrics.composite` and cut the tiers using the account criteria.
5. Assign a play, an owner and a success metric to each tier.
6. Enrich accounts with `clearbit.company` / `hubspot.deals` if available; never estimate a
   missing firmographic. State that all criteria are assumptions.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `tier-1-one-to-one` | A handful of top-scoring accounts get bespoke, rep-owned plays | `dgtm frameworks --name abm-tiering` |
| `tier-2-few` | A cluster of similar mid-tier accounts shares one semi-custom play | `dgtm frameworks --name abm-tiering` |
| `tier-3-many` | The long tail is handled by scaled, campaign-led touches | `dgtm frameworks --name demand-gen-plan` |
| `enrichment-pass` | The account list lacks firmographics needed to score criteria | `dgtm score`, `doddle.tool.v1.clearbit.company` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the composite for the scored account(s) and the tier cut,
   and that the criteria are assumptions. If `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** The `criteria[]` contributions tagged `deterministic`; every criterion,
   weight and score tagged `advisory` (an assumption); enriched firmographics tagged `live`; the
   tier structure tagged `deterministic` (from the registry).
3. **Artifact path.** Where the JSON/report was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; a `null` criterion score is not measured, not zero; never do
arithmetic; criteria are assumptions and must be labelled; on `ok: false` relay `error.message` +
`error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Presenting the tiering criteria as facts | Label every criterion, weight and score `advisory` |
| Re-adding the weighted contributions by hand | Read `metrics.composite` from the envelope |
| Treating a missing score as zero | It is `null`; check `metrics.coverage` and `notes[]` |
| Defaulting weights when the user did not give them | Ask; do not substitute a default |
| Skipping the play/owner/success metric per tier | Fill the abm-tiering sections or flag the gap |

## Related Skills

- `gtm-icp` — define the profile the account criteria test.
- `gtm-segmentation` — group accounts before tiering them.
- `gtm-demand-gen` — the channels the plays run through.
- `gtm-outbound` — the direct touch for Tier 1 accounts.
- `gtm-lead-scoring` — scoring inbound leads (distinct from account tiering).

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| accounts | file | yes | Target account list |
| criteria | string | yes | Weighted tiering criteria |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| program | markdown | ABM tiers and plays |
| envelope | json | Account score envelope |
