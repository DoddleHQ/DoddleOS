---
name: gtm-plg
id: doddle.gtm.gtm-plg
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants a product-led growth loop from activation funnel counts — signup, activation, habit, monetization and referral. Use for 'product led growth', 'PLG loop', 'activation funnel', 'freemium conversion', 'self-serve growth plan'. Funnel counts are the user's inputs."
---

# Product-Led Growth

Model a product-led growth loop from activation funnel counts.

## Deterministic Toolkit

```
dgtm funnel --stage name:count [--stage name:count ...] [--json]
dgtm frameworks --name plg-loop --json
```

Read the JSON envelope — every figure comes from it:

- `metrics.overall_conversion` — last stage ÷ first stage for the activation funnel.
- `metrics.steps[]` — per-step `from`, `to`, `conversion`, `dropoff`.
- `notes[]` — zero or missing stage counts; a zero-in stage yields `null` conversion, not zero.
- `frameworks[0].sections` — PLG Loop structure: Entry point, Activation moment, Habit,
  Loop mechanic, Monetization, Referral / virality, Guardrail metrics.

The funnel counts are **`advisory`** inputs the user gives; the conversion is reproducible with
them, not measured. Use `doddle.tool.v1.ga4.getReport` for live traffic and conversion by source
and tag it `live`; if it is not configured say `⚠️ NOT AVAILABLE — configure
doddle.tool.v1.ga4.getReport`.

## Workflow

1. Confirm the segment (default **SMB**) and the product's entry point (signup, trial, freemium).
2. Collect the ordered activation funnel counts (visit, signup, activate, habit, paid).
3. Run `dgtm funnel --stage …` and read `metrics`.
4. Pull the structure with `dgtm frameworks --name plg-loop`.
5. Map the counts to the loop sections; label every rate `advisory` and name the weakest step
   from `metrics.steps[]`.
6. Cite `ga4.getReport` as `live` when configured; never invent a traffic or conversion number.
7. State `scoring_version`, `data_version` and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `activation-repair` | `metrics.steps[]` names a weak step and activation, not traffic, is the problem | `dgtm funnel`, `dgtm frameworks --name plg-loop` |
| `freemium-monetization` | A free tier exists and the open question is paid conversion, not signup volume | `dgtm frameworks --name plg-loop`, `dgtm frameworks --name pricing-model` |
| `referral-loop-design` | Counts include a referred-visit stage and virality is the intended lever | `dgtm frameworks --name plg-loop` |
| `traffic-source-mix` | Entry-point traffic, rather than any funnel step, is what needs diagnosing | `doddle.tool.v1.ga4.getReport` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the overall activation conversion and the weakest
   step, with the input counts tagged `advisory`. If `evidence.stamp` is not `CURRENT`, say so
   here.
2. **Key evidence.** The step conversions, each tagged `deterministic` (computed) or `advisory`
   (assumed counts), and any GA4 figures tagged `live`.
3. **Artifact path.** Where the loop was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number; `null` is not measured, not zero; never do arithmetic; on
`ok: false` relay `error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Inventing activation or viral coefficients | Use only supplied counts; label the rest `NOT AVAILABLE` |
| Treating a zero stage as a 0% conversion | It is `null`; name the reason from `notes[]` |
| Assuming a viral loop exists | Mark referral/virality unknown unless the counts show it |
| Re-deriving step conversion by hand | Read `metrics.steps[]` from the envelope |
| Reporting GA4 traffic without the tool | Say `⚠️ NOT AVAILABLE — configure doddle.tool.v1.ga4.getReport` |

## Related Skills

- `gtm-demand-gen` — the paid and marketing-led side of the funnel.
- `gtm-onboarding` — time-to-first-value for new signups.
- `gtm-experimentation` — test activation changes before scaling them.
- `gtm-metrics` — carry activation rates into the KPI set.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| product | string | yes | The product and its entry point |
| funnel | string | yes | Activation funnel counts as name:count |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| loop | markdown | Product-led growth loop |
| envelope | json | Funnel envelope |
