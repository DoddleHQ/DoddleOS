---
name: gtm-messaging
id: doddle.gtm.gtm-messaging
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to turn positioning into messaging — a messaging house, value proposition pillars, or persona and stage messages. Use for 'build a messaging house', 'messaging framework', 'value proposition pillars', 'what is our core message', 'message by persona'. Uses only the agreed positioning and user-supplied inputs."
---

# Messaging House

Turn positioning into a messaging house the whole team can use — roof, pillars, proof, persona and stage.

## Deterministic Toolkit

```
dgtm frameworks --name messaging-house --json
```

Read `frameworks[0].sections` — the exact structure to fill:

1. Roof: core value proposition
2. Pillars (3)
3. Proof per pillar
4. Message by persona
5. Message by stage
6. Words to use / avoid

The framework supplies the **structure** (`deterministic`, from the registry); the agreed
positioning and the user's inputs supply the content (`advisory`). This skill runs no
calculator and invents no proof, metric or customer result — leave proof blank where none is
given and flag the gap.

## Workflow

1. Pull the structure with `dgtm frameworks --name messaging-house`.
2. Take the agreed positioning and elicit the three pillars and the proof behind each.
3. Write the roof and pillars from the positioning only.
4. Fill proof per pillar; leave it blank and flag it when no proof was supplied.
5. Map the message by persona (from `gtm-persona`) and by stage.
6. List the words to use and avoid; flag any pillar with no supporting proof.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `house-from-positioning` | Build the full messaging house from agreed positioning | `messaging-house` |
| `proof-gap-audit` | Audit an existing house for pillars with no supporting proof | `messaging-house` |
| `persona-stage-messages` | Only the message-by-persona and message-by-stage rows are needed | `messaging-house` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the roof proposition, tagged `advisory`.
2. **Key evidence.** The positioning and inputs used, each tagged `advisory`; the house structure
   tagged `deterministic` (from the registry).
3. **Artifact path.** Where the messaging house was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number, a proof point or a customer result; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Building messaging from a feature list | Start from the positioning and the pillars |
| Inventing proof for a pillar | Leave the proof blank and flag the gap |
| One message for every persona | Fill the message-by-persona row from real personas |
| Paraphrasing the house from memory | Read `frameworks[0].sections` from the command |
| Treating stage messages as static | Map a message to each funnel stage |

## Related Skills

- `gtm-positioning` — the input this skill turns into a house.
- `gtm-persona` — supplies the message-by-persona row.
- `gtm-competitive` — pressure-tests the pillars against alternatives.
- `gtm-sales-narrative` — delivers the house in the field.
- `gtm-enablement` — the house is an enablement asset.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| positioning | string | yes | The agreed positioning |
| personas | string | no | Personas to message to |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| messaging | markdown | Messaging house |
