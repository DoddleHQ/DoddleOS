---
name: gtm-partnerships
id: doddle.gtm.gtm-partnerships
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to design a partnership or channel alliance with clear mutual value. Use for 'partnership model', 'partner strategy', 'should we partner with X', 'co-marketing / reseller / integration partner', 'alliance plan'. Advisory work backed by the partnership-model framework."
---

# Partnerships

Design a partnership with explicit mutual value — a structured, advisory model.

## Deterministic Toolkit

```
dgtm frameworks --name partnership-model --json
```

Read `frameworks[0].sections` — the exact structure to fill:

1. Partner type
2. Mutual value
3. Integrated motion
4. Commercial terms
5. Enablement
6. Attribution
7. Review cadence

The framework supplies the **structure**; the user supplies the content. This is `advisory`
work — no market figures, no invented metrics. Use `doddle.tool.v1.notion.pages` to read planning
docs or prior partner briefs (tag any figure from them `live`); if it is unavailable, keep the
model inline.

## Workflow

1. Pull the `partnership-model` structure with `dgtm frameworks --name partnership-model`.
2. Elicit the objective and candidate partners from the user.
3. Complete each section from those inputs — state specifically what each side gives and gets.
4. Where a term needs a number (revenue share, targets) and none is supplied, leave it blank and
   flag it; never estimate.
5. Flag any one-sided value as a gap in the model.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `partner-fit` | User asks "should we partner with X?" — evaluate a named candidate | `partnership-model` (Mutual value, Integrated motion) |
| `new-alliance-design` | Designing a partnership from scratch against a stated objective | `partnership-model` |
| `terms-review` | Commercial terms (revenue share, targets) need scrutiny before signing | `partnership-model` (Commercial terms) |
| `cadence-review` | An existing partnership is due its attribution/review checkpoint | `partnership-model` (Attribution, Review cadence) |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the recommended partner type and the mutual-value
   proposition, tagged `advisory`.
2. **Key evidence.** The user-supplied inputs tagged `advisory` (assumed) and the framework
   structure tagged `deterministic` (from the registry); Notion figures tagged `live`.
3. **Artifact path.** Where the model was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic;
assumptions are labelled; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Describing only what you get | Fill Mutual value from both sides |
| Inventing revenue-share or target numbers | Leave blank and flag it; use only supplied inputs |
| Paraphrasing the framework from memory | Read sections from `dgtm frameworks` |
| Treating a partner's public claims as measured facts | Tag them `live` or leave them out |
| Writing to Notion or the CRM | Read-only; keep output inline or as a file |

## Related Skills

- `gtm-strategy` — partnerships sit inside the overall plan.
- `gtm-channel` — compare partner-led economics with direct channels.
- `gtm-demand-gen` — co-marketing feeds the demand plan.
- `gtm-positioning` — partner value must fit the position.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| objective | string | yes | What the partnership must achieve |
| candidates | string | no | Candidate partners |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| model | markdown | Partnership model with mutual value |
