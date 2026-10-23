---
name: gtm-market-sizing
id: doddle.gtm.gtm-market-sizing
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to size a market — TAM, SAM, SOM — bottom-up from their own inputs. Use for 'how big is this market', 'TAM/SAM/SOM', 'how many accounts could we sell to', 'size the SMB opportunity'. Computes only from inputs the user provides."
---

# Market Sizing

Bottom-up TAM/SAM/SOM from the user's own inputs — never from a look-up.

## Deterministic Toolkit

```
dgtm size-market --accounts N --acv X [--sam-pct S --som-pct O] [--json]
dgtm size-market --units N --unit-price P [--sam-pct S --som-pct O] [--json]
```

Formulas (all from the inputs you pass):

- `TAM = accounts x ACV` (or `units x unit_price`)
- `SAM = TAM x sam_pct`
- `SOM = SAM x som_pct`

Read the envelope: `metrics.tam/sam/som`, `inputs`, and `notes` for what is still missing. Every
input is an **assumption** the user supplies — label it as such. Never look up a market size or
import a third-party figure.

## Workflow

1. Get the bottom-up inputs: number of target accounts and ACV (or units and unit price).
2. Get `sam_pct` and `som_pct` if the user wants SAM/SOM; otherwise report TAM only.
3. Run `dgtm size-market …` and read `metrics`.
4. Narrate TAM/SAM/SOM, and state each input as an assumption with its value.
5. If a required input is missing, say so — do not substitute a default.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `bottom-up` | User has a target account count and an ACV assumption | `dgtm size-market --accounts N --acv X` |
| `unit-based` | Sizing from units (seats, locations, shipments) instead of accounts | `dgtm size-market --units N --unit-price P` |
| `sam-som` | User wants the serviceable/obtainable layers, not just TAM | `dgtm size-market --sam-pct S --som-pct O` |
| `sanity-check` | User already has a market-size claim and wants it tested against their own inputs | `dgtm size-market` (claim tagged `advisory`) |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying TAM (and SAM/SOM if computed). If any input is an
   assumption, say so here.
2. **Key evidence.** The inputs and the resulting figures, tagged `advisory` (assumptions) with
   the computed outputs marked `deterministic`.
3. **Artifact path.** Where the JSON was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Quoting a market size from memory or the web | Compute only from user inputs |
| Presenting an assumed ACV as a fact | Label every input `advisory` |
| Reporting SOM without `som_pct` | It is `null`; ask for the assumption or stop at SAM |
| Mixing units (units vs accounts) | Match the metric: accounts↔ACV, units↔unit price |

## Related Skills

- `gtm-segmentation` — size each segment, not just the whole market.
- `gtm-icp` — sharpen who counts as an account before sizing.
- `gtm-metrics` — carry the sizing into the KPI set.
- `gtm-strategy` — the sizing feeds the plan.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| accounts | number | no | Total addressable accounts (bottom-up) |
| acv | number | no | Annual contract value assumption |
| sam-pct | number | no | Serviceable share of TAM (assumption) |
| som-pct | number | no | Obtainable share of SAM (assumption) |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| sizing | markdown | TAM/SAM/SOM from the given inputs |
| envelope | json | Sizing envelope |
