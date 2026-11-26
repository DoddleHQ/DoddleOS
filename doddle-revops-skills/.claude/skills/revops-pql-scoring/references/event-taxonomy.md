# Event Taxonomy Reference

Events are the raw material of PQL scoring. A sloppy taxonomy produces a model nobody trusts.

## Minimum event shape

```json
{
  "account_id": "acct_9f3",
  "event_name": "created_project",
  "event_at": "2026-11-20T10:00:00Z",
  "user_id": "u_42",
  "properties": {"workspace_id": "ws_7"}
}
```

| Field | Rule |
|-------|------|
| `account_id` | Required. Without it the event cannot be scored. |
| `event_name` | Required. Use a stable verb_object name (`created_project`). |
| `event_at` | Required, UTC. Local timestamps break window maths. |
| `user_id` | Optional. Needed for user-level activation, useless for account scoring. |
| `properties` | Optional. Keep small; wide properties slow every downstream query. |

## Naming rules

- Lowercase, snake_case, verb first: `created_project`, `invited_teammate`, `exported_report`.
- Never reuse a name for two meanings. `invited_teammate` must mean the same thing forever.
- Do not encode state in the name (`project_created_v2`). Version the schema, not the vocabulary.
- Keep the taxonomy small. Every event costs storage, pipeline time, and model complexity.

## Aha events

An aha event is the moment value is first realised. It must be:

1. **Actionable** — the user did something, not something happened to them.
2. **Correlated** with retention, verified from cohort data rather than opinion.
3. **Reachable** — a realistic fraction of users can hit it.

Choosing an aha event from "what would be nice" is the most common PQL failure. Calibrate it
against a retention cohort.

## Instrumentation checklist

- [ ] Event name follows the naming rule.
- [ ] `account_id` present and resolvable to a canonical account.
- [ ] Timestamp is UTC and not client-clock dependent where avoidable.
- [ ] Event is emitted server-side, not only in the browser.
- [ ] A test proves the event fires on the intended action and not others.
