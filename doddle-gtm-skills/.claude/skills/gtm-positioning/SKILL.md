---
name: gtm-positioning
id: doddle.gtm.gtm-positioning
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to define or sharpen positioning — who you serve, the alternative, the differentiated value and the proof. Use for 'positioning statement', 'how should we position', 'positioning canvas', 'why are we different', 'category narrative'."
---

# Positioning

Define who the product is for and why it is the better choice — as a canvas, then a statement.

## Deterministic Toolkit

```
dgtm frameworks --name positioning-canvas --json
```

Read `frameworks[0].sections` — the exact structure to fill:

1. Target segment
2. Category / frame of reference
3. Alternative & status quo
4. Unique differentiated value
5. Reasons to believe
6. Positioning statement

The framework supplies the **structure**; the user's inputs supply the content. This is
`advisory` work — no market figures, no competitor statistics.

## Workflow

1. Pull the canvas structure with `dgtm frameworks --name positioning-canvas`.
2. Elicit the inputs: product, the alternative buyers use today, and the differentiators.
3. Complete each section from those inputs — do not invent proof.
4. Write a one-sentence positioning statement from the filled canvas.
5. Flag any claim that lacks a reason to believe as a gap.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `first-positioning` | Define positioning for a product that has none yet | `positioning-canvas` |
| `repositioning` | Sharpen positioning when the alternative or status quo has changed | `positioning-canvas`, `competitive-teardown` |
| `competitor-response` | Test positioning against a specific named competitor | `positioning-canvas`, `battlecard` |
| `segment-refocus` | Re-aim positioning at a different target segment | `positioning-canvas`, `icp-template` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the positioning statement, tagged `advisory`.
2. **Key evidence.** The inputs used, each tagged `advisory`; the canvas structure tagged
   `deterministic` (from the registry).
3. **Artifact path.** Where the canvas was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number or a customer result; never do arithmetic; on `ok: false`
relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Positioning from a feature list | Start from the alternative and the differentiated value |
| Inventing proof points | Leave the reason-to-believe blank and flag the gap |
| Nesting too broad a segment | Name the segment; default SMB unless told otherwise |
| Paraphrasing the canvas from memory | Read sections from `dgtm frameworks` |

## Related Skills

- `gtm-messaging` — turn positioning into a messaging house.
- `gtm-icp` — define the account profile the positioning targets.
- `gtm-competitive` — test positioning against alternatives.
- `gtm-sales-narrative` — deliver the story in the field.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| product | string | yes | The product being positioned |
| alternative | string | yes | What buyers use today instead |
| differentiators | string | no | Why you are meaningfully better |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| positioning | markdown | Positioning canvas and statement |
