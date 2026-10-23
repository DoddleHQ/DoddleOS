---
name: gtm-persona
id: doddle.gtm.gtm-persona
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to define buyer personas for a segment. Use for 'define buyer personas', 'who are our buyers', 'persona template', 'what does the buyer care about', 'message to the economic buyer'. Uses only inputs the user supplies and never invents quotes or metrics."
---

# Buyer Persona

Build buyer personas for a segment from the registry template and the user's inputs.

## Deterministic Toolkit

```
dgtm frameworks --name persona-template --json
```

Read `frameworks[0].sections` — the exact structure to fill:

1. Role & reporting line
2. Goals
3. Pains
4. Success metrics
5. Objections
6. Where they learn
7. Message that lands

The registry supplies the **structure** (`deterministic`); the user's inputs supply the content
(`advisory`). This skill runs no calculator. Never invent a buyer quote, a success metric or a
statistic — leave an unsupplied field blank and flag it as a gap.

## Workflow

1. Confirm the segment (default **SMB**) and the roles in the buying committee.
2. Pull the structure with `dgtm frameworks --name persona-template`.
3. For each role, fill goals, pains, success metrics and objections from the supplied inputs.
4. Write the message that lands, tied to the positioning; flag any proof blank.
5. Record where each persona learns, from supplied inputs only.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `full-committee` | Define every role in the buying committee for a segment | `persona-template` |
| `single-role` | Deepen one role (e.g. economic buyer) for a specific play | `persona-template` |
| `message-hook` | Only the message-that-lands field is needed, tied to positioning | `persona-template` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying how many personas were written and the segment,
   tagged `advisory`.
2. **Key evidence.** The user-supplied inputs used, each tagged `advisory`; the persona structure
   tagged `deterministic` (from the registry).
3. **Artifact path.** Where the personas were written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number or a quote; never do arithmetic; an unsupplied field is a gap,
not a guess; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Writing a buyer quote yourself | Use only a supplied quote, or leave it out |
| Inventing a success metric | Leave the field blank and flag the gap |
| One persona for the whole committee | Cover each role in the buying committee |
| Paraphrasing the template from memory | Read `frameworks[0].sections` from the command |
| Confusing persona (a role) with the ICP (an account) | The persona is role-level; the ICP is account-level |

## Related Skills

- `gtm-icp` — the account-level profile the persona sits inside.
- `gtm-messaging` — persona messaging feeds the messaging house.
- `gtm-positioning` — the message must trace to the positioning.
- `gtm-sales-narrative` — personas shape the story in the field.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| segment | string | yes | Segment the personas belong to |
| roles | string | no | Buying-committee roles |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| personas | markdown | Buyer personas |
