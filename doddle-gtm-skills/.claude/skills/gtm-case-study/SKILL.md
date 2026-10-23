---
name: gtm-case-study
id: doddle.gtm.gtm-case-study
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to turn a customer win into proof — a case study, a customer story, a reference narrative. Use for 'write a case study', 'customer story', 'success story', 'turn this win into proof'. Uses only user-supplied, verified results."
---

# Case Study

Turn a customer win into a proof asset — from the customer's own verified results.

## Advisory (no toolkit)

This is a pure judgement skill: it produces narrative. It runs **no** calculator. Every input
comes from the user, and the standard is strict:

- The customer, the problem and the solution come from the user.
- **Every result must be user-supplied and verified.** If a number is not given, leave it out
  and mark it `NOT AVAILABLE` — never estimate or round up a customer outcome.
- Pull the structure from the registry:

```
dgtm frameworks --name case-study-brief --json
```

Read `frameworks[0].sections`: Customer & context, Problem, Evaluation, Solution, Quantified
result, Quote, Approvals.

## Workflow

1. Pull the `case-study-brief` structure.
2. Gather inputs: customer, context, problem, evaluation, solution, quantified result, quote.
3. For each section, write from the inputs only. Omit unsupplied numbers; flag them.
4. Draft the story with the result in the headline; keep claims tied to the given evidence.
5. Mark anything needing legal/customer approval.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `full-story` | Writing the complete case study end to end | `frameworks --name case-study-brief` |
| `quote-pull` | Another asset needs one verified pull-quote | `case-study-brief` (quote section) |
| `approvals-check` | Draft exists; confirm what needs customer/legal sign-off | `case-study-brief` (approvals section) |
| `result-gap` | Win is compelling but has no verified numbers yet | `case-study-brief` (quantified result) |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the customer and the headline outcome if supplied,
   tagged `advisory`; if no result was given, say the result is `NOT AVAILABLE`.
2. **Key evidence.** The user-supplied facts used, each tagged `advisory`.
3. **Artifact path.** Where the draft was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; never do arithmetic; if a result is missing, mark it
`NOT AVAILABLE` rather than describing it qualitatively as if measured. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Inventing or "estimating" a result | Omit it; mark `NOT AVAILABLE` |
| Writing the customer's quote | Use the supplied quote verbatim |
| Presenting the story as impartial analysis | Tag it `advisory` (it is advocacy) |
| Publishing before approval | Flag sections needing customer/legal sign-off |

## Related Skills

- `gtm-sales-narrative` — the general pitch the case study illustrates.
- `gtm-win-loss` — where the win's evidence often originates.
- `gtm-battlecards` — proof points feed battlecards.
- `gtm-enablement` — case studies are enablement assets.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| customer | string | yes | Customer the story is about |
| results | string | yes | User-supplied, verified results |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| case_study | markdown | Case study |
