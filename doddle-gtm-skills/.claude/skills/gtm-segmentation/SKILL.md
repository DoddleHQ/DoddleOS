---
name: gtm-segmentation
id: doddle.gtm.gtm-segmentation
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to define and prioritize market segments. Use for 'segment the market', 'segmentation', 'which segment first', 'prioritize segments', 'split the market into segments'. Sizes each segment only from inputs the user provides and defaults to SMB-first."
---

# Segmentation

Define and prioritize segments — SMB-first — sizing each only from inputs the user provides.

## Deterministic Toolkit

```
dgtm size-market --accounts N --acv X [--sam-pct S --som-pct O] [--json]
dgtm size-market --units N --unit-price P [--sam-pct S --som-pct O] [--json]
dgtm frameworks --json
```

Run `size-market` once per segment. Read the envelope: `metrics.tam/sam/som`, `inputs` and
`notes`.

- `TAM = accounts x ACV` (or `units x unit_price`)
- `SAM = TAM x sam_pct`
- `SOM = SAM x som_pct`

Every input (accounts/units, ACV/unit price, `sam_pct`, `som_pct`) is an **assumption**
(`advisory`); the computed sizes are `deterministic`. A missing `sam_pct` or `som_pct` yields
`null` — ask for the assumption, never default it to zero. Read segment definitions from the
user; read `frameworks` for the named templates. Enrich segments with
`doddle.tool.v1.clearbit.company` (read-only); if unavailable, ask for the account list and print
`NOT AVAILABLE — configure doddle.tool.v1.clearbit.company`.

## Workflow

1. Choose the segmentation axes (size, vertical, geography, motion).
2. Define the candidate segments; default priority is **SMB-first**.
3. For each segment, collect the bottom-up inputs and run `dgtm size-market …`.
4. Read `metrics` and `notes`; label each size input `advisory`.
5. Read the framework list with `dgtm frameworks`.
6. Prioritize the segments from the sizes plus the axes; state which inputs are assumptions.
7. Enrich the segments with clearbit where configured.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `account-sizing` | Size segments measured as accounts and ACV | `dgtm size-market --accounts` |
| `unit-sizing` | Size segments measured as units and unit price | `dgtm size-market --units` |
| `segment-prioritization` | Rank already-sized segments to pick which one goes first | `dgtm size-market` per segment, `icp-template` |
| `new-vertical` | Evaluate a new vertical or geography as a candidate segment | `dgtm size-market`, `persona-template` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying how many segments were sized and the recommended
   first segment, with TAM where computed. State that sizes rest on assumptions.
2. **Key evidence.** The inputs and resulting sizes, tagged `advisory` (assumptions) with the
   computed outputs marked `deterministic`.
3. **Artifact path.** Where the segmentation was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Quoting a market size from memory or the web | Compute only from user inputs |
| Presenting an assumed ACV as a fact | Label every input `advisory` |
| Defaulting SOM to zero when `som_pct` is missing | It is `null`; ask for the assumption |
| Prioritizing by gut instead of the sizes | Rank from the computed sizes and the axes |
| Mixing units (units vs accounts) | Match the metric: accounts with ACV, units with unit price |

## Related Skills

- `gtm-market-sizing` — size the whole market this skill divides.
- `gtm-icp` — the account-level profile within a segment.
- `gtm-persona` — the roles inside each segment.
- `gtm-strategy` — the plan the segment priority feeds.
- `gtm-abm` — tier accounts once segments are chosen.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| market | string | yes | Market to segment |
| criteria | string | no | Segmentation axes |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| segments | markdown | Segment definitions and priority |
| envelope | json | Sizing envelope |
