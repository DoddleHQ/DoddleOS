---
name: gtm-outbound
id: doddle.gtm.gtm-outbound
version: 0.2.0
blueprint: ./blueprint.yaml
description: "When the user wants an outbound sequence and copy — cadence, channels and messaging for a target profile. Use for 'outbound sequence', 'cold email sequence', 'LinkedIn outreach plan', 'write our outbound cadence', 'prospecting copy'. The plan and copy are advisory."
---

# Outbound

Design an outbound sequence and copy from the user's ICP and offer — the plan is advisory.

## Deterministic Toolkit

```
dgtm frameworks --name demand-gen-plan --json
```

Read `frameworks[0].sections` — the structure the sequence plan fills: Pipeline target,
Funnel math, Source mix, Content & offers, Cadence, Budget assumptions, Measurement.

The framework supplies the **structure** only. The sequence, the copy, and every reply, meeting
or win rate you estimate are `advisory`. Do not invent send volumes, response rates or booked
meetings. Use `doddle.tool.v1.linkedin.ads` for live campaign results and
`doddle.tool.v1.gong.calls` for live call evidence, and tag them `live`; if a tool is absent say
`⚠️ NOT AVAILABLE — configure <tool>`.

## Workflow

1. Confirm the segment (default **SMB**), the ICP, and the offer to lead with.
2. Pull the structure with `dgtm frameworks --name demand-gen-plan`.
3. Choose channels and a cadence; draft the ordered sequence steps.
4. Write the copy — subject, opener, value, ask — strictly from the ICP and offer given.
5. Tag every expected rate and volume `advisory`; do not fabricate any benchmark.
6. Cite live tool numbers as `live` when available; never substitute an estimate.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `smb-multichannel` | Default SMB segment with a volume-led cadence across email and LinkedIn | `dgtm frameworks --name demand-gen-plan` |
| `tier-1-one-to-one` | A short list of named enterprise accounts that each need researched, individual copy | `dgtm frameworks --name abm-tiering` |
| `trigger-based` | A live signal (funding, hiring, tech change) starts a short, urgent sequence | `dgtm frameworks --name demand-gen-plan` |
| `sequence-teardown` | A cadence already exists and needs critique against real call evidence | `doddle.tool.v1.gong.calls` |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence naming the sequence shape (channels and number of touches),
   tagged `advisory`. If `evidence.stamp` is not `CURRENT`, say so here.
2. **Key evidence.** The ICP, offer and framework structure used, tagging the structure
   `deterministic` (from the registry) and every rate or target `advisory`.
3. **Artifact path.** Where the sequence was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a number or a benchmark; never do arithmetic; on `ok: false` relay
`error.message` + `error.hint`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Inventing response or meeting rates | Tag all rates `advisory` or omit them |
| Quoting a benchmark open rate from memory | Use only user-supplied or live tool numbers |
| Sending the sequence or scheduling email | This pack is read-only; it drafts, it never sends |
| Building copy from generic features | Start from the ICP pain and the offer |
| Ignoring call evidence | Read `gong.calls` when configured for real objections |

## Related Skills

- `gtm-demand-gen` — the broader plan this sequence serves.
- `gtm-sales-narrative` — the story the copy draws on.
- `gtm-messaging` — the vocabulary behind the copy.
- `gtm-icp` — the profile the sequence targets.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| icp | string | yes | Target profile |
| offer | string | yes | Value proposition to lead with |
| channels | string | no | Outbound channels to consider |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| sequences | markdown | Outbound sequence plan and copy |
