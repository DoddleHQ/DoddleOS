---
name: revops-qbr
id: doddle.revops.revops-qbr
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants the quarterly business review prepared — KPI scoreboard, ROI proof, risks, the ask, and a CSM deck outline. Use for 'QBR', 'quarterly review', 'business review', 'customer review', 'ROI proof', 'renewal deck', 'CSM slides'."
---

# RevOps Automated QBR

Assemble the review from recorded numbers, then state plainly what is missing. The deck is an
**outline for a human to present** — this skill does not send or schedule anything.

## Deterministic Toolkit

```
drev qbr --account <account.json> [--out <qbr.md>]
```

Read the JSON envelope:

- `rows[]` — `kind: kpi` rows (`metric`, `target`, `actual`, `delta`, `status`) and `kind: slide`
  rows (`id`, `title`, `bullets`).
- `metrics.on_track` / `at_risk` / `off_track` / `not_measured`.
- `metrics.roi` — `(revenue − investment) / investment`; `null` when either input is missing.
- `completeness.missing` — `roi_inputs` and `kpi_actuals` when the data was not supplied.

Status rules: `on_track` when actual ≥ target, `at_risk` when the ratio is ≥ 0.80, `off_track`
below that, and `not_measured` when a target or actual is missing. Deck slides: value delivered,
scorecard, risks, the ask.

## Workflow

1. Confirm the segment (default **SMB**), the period, and who presents.
2. Collect the account payload: KPIs with targets and actuals, outcomes, risks, asks, and the
   investment/revenue figures for ROI.
3. Run `drev qbr …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Write the review in the order: scoreboard first, then value, then risks, then **one** ask.
6. Mark every missing input as `NOT AVAILABLE`. Never fill a gap with a plausible number.
7. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `qbr-default` | Default: full review pack | `drev qbr` → `rows[]` |
| `scoreboard-only` | Only the KPI view is wanted | `rows[]` (`kind: kpi`) |
| `roi-proof` | The renewal hinges on ROI | `metrics.roi` + `completeness.missing` |
| `renewal-deck` | A renewal deck is needed | `rows[]` (`kind: slide`) |
| `gap-audit` | The review keeps stalling on missing data | `completeness.missing` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying the scorecard state and the verdict.
2. **Key evidence.** KPI rows tagged `deterministic` (computed) or `live` (read from the
   payload); ROI inputs tagged `advisory`.
3. **Artifact path.** Where the QBR pack was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a KPI, an outcome, or a risk; `null` is not measured, not zero; never do
arithmetic; missing sections are stated as missing; on `ok: false` relay `error.message` +
`error.hint`. Full block: `common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Leading with a status readout | Scoreboard first, then value, then the ask |
| Five asks instead of one | A review with five asks has none |
| Quietly dropping an off-track KPI | Show it with the mitigation |
| ROI without investment and revenue | It reads NOT AVAILABLE |
| Inventing a risk to fill the slide | Say no risks were supplied |

## Related Skills

- `doddle.revops.revops-retention` — NRR, health, and renewal risk feeding the review.
- `doddle.revops.revops-call-intelligence` — customer quotes as value evidence.
- `doddle.b2b.b2b-qbr` — QBR narrative and expansion plays.
- `doddle.agency.agency-reporting` — reporting cadence and KPI rollup discipline.
- `doddle.gtm.gtm-reporting` — presentation layer over a pipeline audit.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| account | file | yes | Account JSON with kpis, outcomes, risks, asks |
| period | string | no | Review period, e.g. 2026-Q4 |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | QBR pack: scoreboard, ROI, outcomes, risks, the ask |
| deck | json | CSM deck outline |
| envelope | json | Deterministic QBR envelope |
