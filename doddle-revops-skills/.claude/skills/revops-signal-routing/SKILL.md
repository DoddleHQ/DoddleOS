---
name: revops-signal-routing
id: doddle.revops.revops-signal-routing
version: 1.1.0
blueprint: ./blueprint.yaml
description: "When the user wants to route buyer-intent signals to owners — recency windows, priority ladders, and ready-to-send alerts without sending them. Use for 'signal routing', 'buyer intent', 'intent alerts', 'when is someone in-market', 'webhook to Slack', 'route events to reps'."
---

# RevOps Signal Routing

Turn raw signal events into owned, prioritized next actions. This skill **routes**; it never
sends. Alert payloads are drafted and handed to the owner.

## Deterministic Toolkit

```
drev route-signals --events <events.jsonl|csv> --rules <rules.json> [--now <ISO-8601>]
```

Read the JSON envelope:

- `metrics.signals_routed` / `signals_unrouted` / `accounts_routed`.
- `rows[]` — one entry per routed signal: `signal`, `age_days`, `channel`, `owner`, `priority`,
  and a `slack_payload` marked `delivery: dry-run — not sent`.
- `completeness.missing[]` — signal types that no rule matched. These are gaps in the rules, not
  noise to ignore.
- `metrics.window_days` — the recency window that was applied.

Signals outside the window are dropped by the tool, not by judgement. Rules are configuration:

```json
{
  "recency_window_days": 14,
  "routes": [
    {"signal": "pricing_page_view", "channel": "email", "owner": "sdr", "priority": 1, "action": "send_1to1_offer"},
    {"signal": "job_posting", "channel": "linkedin", "owner": "ae", "priority": 3, "action": "review_account"}
  ]
}
```

### Write path (gated)

Routing is read-only. Posting an alert is a **write**, so the blueprint gates it:

```yaml
- {id: approve_alert, type: gate, needs: [route], produces: [decision],
   approvers: [owner], timeout_s: 3600, on_approve: proceed, on_reject: revise}
- {id: send_alert, type: tool, ref: doddle.tool.v1.slack.sendMessage,
   needs: [approve_alert], produces: [alert_receipt]}
```

`approve_alert` is a hard stop: without an approved decision nothing is sent, and the report
still shows the plan. If Slack is not configured the node degrades to `manual_review` and the
report states that the alert was not delivered.

## Workflow

1. Confirm the segment (default **SMB**) and the recency window that fits the buying cycle.
2. Collect the events and the rules. If a signal type has no rule, say so — it becomes a rules
   gap, not an unroutable event.
3. Run `drev route-signals …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report what routed, to whom, and at what priority. Name the unmatched signal types.
6. Draft the alert payloads from `rows[].slack_payload`. **Do not send.** Hand them to the owner.
7. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `route-default` | Default: route recent signals to owners | `drev route-signals` → `rows[]` |
| `window-review` | Signals arrive but nothing routes | `metrics.window_days`, `metrics.signals_unrouted` |
| `rules-gap` | A new signal type needs a route | `completeness.missing[]` → propose the rule |
| `priority-tuning` | Everything is priority 1 | `rows[].priority` ladder in the rules file |
| `alert-draft` | A Slack alert is wanted | `rows[].slack_payload` (draft only) |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying routed accounts, signals, and the verdict.
2. **Key evidence.** Routed rows tagged `deterministic` (computed) or `live` (read from the
   export); rules and window tagged `advisory`.
3. **Artifact path.** Where the JSON or report was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a signal, an account, or an owner; `null` is not measured, not zero;
never do arithmetic; on `ok: false` relay `error.message` + `error.hint`. Full block:
`common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Sending an alert without approval | `approve_alert` is a hard stop — unapproved alerts are never sent |
| Ignoring unrouted signal types | They are a rules gap; report them |
| Routing stale signals | The window is applied by the tool; widen it deliberately or not at all |
| Guessing an account from an email | Anonymous is anonymous — do not deanonymize by inference |
| One channel for every signal | The ladder exists to separate now from later |

## Related Skills

- `doddle.revops.revops-ai-sdr` — turn a routed signal into evidence-backed outreach.
- `doddle.revops.revops-data-infrastructure` — validate the event table before trusting routing.
- `doddle.gtm.gtm-outbound` — outbound sequence design and copy.
- `doddle.gtm.gtm-lead-scoring` — weighted fit and intent scoring.
- `doddle.marketing.revops` — lifecycle and handoff design.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| events | file | yes | Signal events (JSONL/CSV) |
| rules | file | yes | Routing rules (JSON) |
| segment | string | no | Segment filter; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Routed signals, unrouted types, alert plan |
| envelope | json | Deterministic routing envelope |
