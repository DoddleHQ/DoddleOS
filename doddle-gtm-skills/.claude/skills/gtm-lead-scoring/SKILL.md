---
name: gtm-lead-scoring
id: doddle.gtm.gtm-lead-scoring
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to build or audit weighted fit-and-intent lead scoring. Use for 'lead scoring model', 'score our leads', 'fit and intent weights', 'which leads should sales work', 'weight these criteria'. Weights and scores are the user's assumptions."
---

# Lead Scoring

Build a weighted fit-and-intent scoring model from the user's criteria — reproducibly.

## Deterministic Toolkit

```
dgtm score --criteria name:weight:score [--criteria name:weight:score ...] [--target NAME] [--json]
dgtm frameworks --name icp-template --json
```

Read the JSON envelope — every figure comes from it:

- `metrics.composite` — weighted mean of the 0-100 criterion scores, normalised over measured
  criteria.
- `metrics.coverage` — share of total weight that was actually scored.
- `criteria[]` — per-criterion `name`, `weight`, `score`, `contribution`.
- `notes[]` — criteria that were unmeasured (`null`); a missing criterion lowers `coverage`, not
  the score.
- `frameworks[0].sections` — ICP structure: Firmographics, Technographics, Trigger events,
  Buying committee, Qualifying criteria + weights, Disqualifiers.

**Weights and scores are `advisory`** — the user's beliefs about what matters. The toolkit
computes reproducibly with them; it does not make them true. Use `doddle.tool.v1.hubspot.deals`
for live deal history and tag it `live`; otherwise ask for the export.

## Workflow

1. Confirm the segment (default **SMB**) and whether you are scoring leads or accounts.
2. Elicit fit criteria (firmographic/technographic) and intent criteria, each with a weight and a
   0-100 score.
3. Pull the `icp-template` structure to name the criteria consistently.
4. Run `dgtm score --criteria …` and read `metrics` and `criteria`.
5. If `ok: false`, relay `error.message` and `error.hint`; stop.
6. Present the model, composite and coverage; label every weight and score `advisory`.
7. State `scoring_version`, `data_version` and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `model-build` | Create a new fit-and-intent scoring model from scratch | `dgtm score`, `icp-template` |
| `batch-scoring` | Score a supplied leads file against an existing model | `dgtm score` |
| `weight-audit` | Re-check criteria weights after live deal history arrives | `dgtm score` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the composite and coverage together, stated as an
   assumption-based score. If `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** The criteria, weights and scores, each tagged `advisory`, with the computed
   composite and coverage marked `deterministic`.
3. **Artifact path.** Where the model was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Presenting weights as objective truth | Label every weight and score `advisory` |
| Letting a missing criterion read as zero | `coverage` drops; the score excludes it (`null`) |
| Re-deriving the weighted mean by hand | Read `metrics.composite` from the envelope |
| Calling the score a revenue prediction | It ranks fit and intent; it does not forecast |
| Writing scores back to the CRM | This pack is read-only; it never updates records |

## Related Skills

- `gtm-icp` — the profile the criteria are drawn from.
- `gtm-segmentation` — tier accounts before scoring them.
- `gtm-demand-gen` — score the leads the funnel produces.
- `gtm-abm` — route high-fit accounts into plays.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| criteria | string | yes | Weighted fit and intent criteria as name:weight:score |
| leads | file | no | Optional leads to score |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| model | markdown | Lead-scoring model |
| envelope | json | Score envelope |
