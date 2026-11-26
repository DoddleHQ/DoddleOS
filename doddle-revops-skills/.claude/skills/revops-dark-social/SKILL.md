---
name: revops-dark-social
id: doddle.revops.revops-dark-social
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants to know what community and word-of-mouth actually drove — survey-modelled attribution, influenced revenue, confidence, and consent discipline. Use for 'dark social', 'community attribution', 'word of mouth', 'survey attribution', 'Discord', 'Slack community', 'influenced pipeline'."
---

# RevOps Dark Social & Community Attribution

Community advocacy and community **attribution** are different problems. This skill measures
the second one: how much revenue traces to conversations the CRM cannot see.

## Deterministic Toolkit

```
drev community-attribution --community <community.csv|json> \
  --surveys <surveys.csv|json> --deals <deals.csv|json> [--min-sample 30]
```

Read the JSON envelope:

- `rows[]` — `kind: source` rows with `basis` (`self_reported` or `modeled`), `source`, `count`;
  and `kind: member` rows with activity counts.
- `metrics.influenced_revenue` and `community_won_deals` — won deals whose `person_id` appears in
  community activity.
- `metrics.confidence` — `low` below `min_sample` (default 30), `medium` below 3× that, `high`
  above.
- `metrics.consent_recorded` / `consent_missing` — survey rows without usable consent.

Two bases, never merged into one number: **self-reported** (`heard_from`) and **modelled**
(`other_source` when the primary answer was empty).

## Workflow

1. Confirm the segment (default **SMB**), the window, and the privacy constraints.
2. Collect the community activity, the survey responses, and the deals. Use hashed `person_id`
   values; never copy raw identities into a prompt.
3. Run `drev community-attribution …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report the two attribution bases separately, then the influenced revenue, then the confidence
   level and what it is based on.
6. Name the consent gaps. Missing consent is a blocker for using a record in any external
   artifact.
7. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `attribution-default` | Default: self-reported vs modelled sources | `rows[]` (`kind: source`) |
| `influenced-revenue` | What did community conversations influence | `metrics.influenced_revenue` |
| `sample-check` | A small survey is being over-read | `metrics.confidence` + `min_sample` |
| `consent-cleanup` | Some records lack consent | `metrics.consent_missing` |
| `community-ops` | The community itself needs a program | `doddle.gtm.gtm-advocacy` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying influenced revenue, confidence, and the verdict.
2. **Key evidence.** The source counts and member activity tagged `deterministic` (computed) or
   `live` (read from the exports); confidence tagged with its basis.
3. **Artifact path.** Where the JSON or the summary was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a survey response, a community member, or a source; never report a
modelled attribution as a measured one; `null` is not measured, not zero; never do arithmetic;
on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Reporting modelled sources as if people said them | Keep the `basis` label |
| Quoting a revenue number from a 6-response survey | Report confidence `low` and the sample size |
| Using a record without consent | Flag it; it is blocked for external use |
| Treating community activity as attribution | Activity is a signal, attribution needs a survey or a link |
| Naming individual community members | Use hashed ids and aggregate results |

## Related Skills

- `doddle.gtm.gtm-advocacy` — designing the advocacy and community program itself.
- `doddle.revops.revops-attribution` — tracked multi-touch attribution for comparison.
- `doddle.marketing.community-building` — community strategy and health.
- `doddle.revops.revops-signal-routing` — routing community-originated signals to owners.
- `doddle.gtm.gtm-metrics` — the KPI scorecard that carries these numbers.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| community | file | yes | Community activity rows |
| surveys | file | no | Survey responses with consent |
| deals | file | no | Deals linking person_id to revenue |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Attribution bases, influenced revenue, confidence, consent gaps |
| envelope | json | Deterministic community-attribution envelope |
