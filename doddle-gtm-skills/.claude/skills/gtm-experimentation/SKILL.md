---
name: gtm-experimentation
id: doddle.gtm.gtm-experimentation
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants to design a test before it runs — a hypothesis, metric and decision rule over a baseline funnel. Use for 'design an experiment', 'A/B test brief', 'what should we test', 'experimentation brief', 'set up a funnel test before we spend'. Baseline funnel counts are inputs."
---

# Experimentation

Design a test before it runs — from the baseline funnel, with a decision rule up front.

## Deterministic Toolkit

```
dgtm funnel --stage name:count [--stage name:count …] [--json]
```

Read `metrics` from the envelope:

- `overall_conversion` — last stage ÷ first.
- `metrics.steps[]` — per-step `conversion` and `dropoff`, plus the `worst_step`.
- `notes` — names any stage with a zero or missing count (a zero stage yields `null` conversions).

The baseline funnel counts are the user's **assumption** — label them `advisory`. Read the brief
structure from the registry:

```
dgtm frameworks --name experimentation-brief --json
```

Fill `frameworks[0].sections`: Hypothesis, Metric & guardrails, Population, Variants, Sample &
duration, Decision rule, Result & learning. Use `doddle.tool.v1.ga4.getReport` for a measured
baseline (tag `live`) where configured; otherwise use the counts the user provides.

## Workflow

1. Confirm the funnel stages and counts; label them `advisory` (or `live` if pulled from GA4).
2. Run `dgtm funnel …` and read `metrics.steps[]` to locate the worst step.
3. Pull the `experimentation-brief` structure with `dgtm frameworks --name experimentation-brief`.
4. Write the hypothesis, the primary metric and guardrails, the population, variants, sample and
   duration, and the decision rule **before** any result.
5. Leave the Result & learning section blank — the test has not run.
6. State `scoring_version`, `data_version` and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `worst-step-test` | `metrics.steps[]` names the drop-off to attack and the brief targets it | `dgtm funnel`, `dgtm frameworks --name experimentation-brief` |
| `pre-spend-gate` | Budget is about to be committed to a channel or campaign that is unproven | `dgtm frameworks --name experimentation-brief` |
| `message-test` | Two value propositions compete and no evidence says which lands | `dgtm frameworks --name messaging-house`, `dgtm frameworks --name experimentation-brief` |
| `baseline-refresh` | The baseline counts are stale or purely assumed and need a measured read | `doddle.tool.v1.ga4.getReport` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence naming the target step and the hypothesis. If
   `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** The baseline step conversions tagged `deterministic`, the given counts tagged
   `advisory` (assumed) or `live` (measured), and the framework structure tagged `deterministic`.
3. **Artifact path.** Where the brief was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic;
assumptions are labelled; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Writing the result before the test runs | Leave Result & learning blank |
| Inventing baseline counts | Use the user's counts; label them `advisory` |
| No decision rule up front | Define the threshold that ends the test |
| Treating a zero stage as a zero rate | Its conversion is `null`; name the reason |
| Paraphrasing the framework from memory | Read sections from `dgtm frameworks` |

## Related Skills

- `gtm-demand-gen` — experimentation refines the demand plan.
- `gtm-metrics` — the funnel steps feed the KPI scorecard.
- `gtm-plg` — product loops are prime test territory.
- `gtm-channel` — test the assumptions behind channel economics.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| hypothesis | string | yes | The hypothesis to test |
| funnel | string | yes | Baseline funnel counts (`name:count`) |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| brief | markdown | Experiment brief |
| envelope | json | Funnel envelope |
