# Blueprint Schema (DoddleOS v2)

Every skill = `SKILL.md` (human) + `blueprint.yaml` (machine). Full template: `spec/skill-template.md`.

## blueprint.yaml fields

| Field | Required | Shape |
|-------|----------|-------|
| `id` | yes | `doddle.<domain>.<skill>` — MUST equal SKILL.md frontmatter `id` |
| `version` | yes | semver, independent per skill |
| `kind` | yes | `skill` |
| `engine` | yes | `doddle-os>=1.0` |
| `description` | yes | Trigger text, mirrors frontmatter |
| `inputs` | yes | `[{name, type, required, description}]` — ask-if-missing contract |
| `outputs` | yes | `[{name, type, description}]` — engine deliverables |
| `tools` | yes | `[{id, required, fallback}]` — IDs per `tool-namespace.md` |
| `integrations` | yes | Names matching `registry/integrations/<name>/config.json` |
| `nodes` | yes | DAG: `[{id, type, ref, needs, produces}]` — type ∈ {agent, tool, call, gate} |
| `on_fail` | yes | `{retry, fallback}` — `manual_review` default |
| `domains` | no | `[strings]` for router disambiguation; empty = generic (see harness-phase2 §4) |
| `fallback_for` | no | `[skill ids]` this skill backs; entries MUST be known ids |

## Node types

| `type` | `ref` points to | Extra required fields | Example |
|--------|-----------------|----------------------|---------|
| `agent` | Agent name (any pack) | — | `conversion-optimizer`, `copywriter` |
| `tool` | `doddle.tool.v1.*` ID | — | `doddle.tool.v1.ga4.getReport` |
| `call` | Skill id (sub-graph) | `inputs:` map; no self-call; depth ≤3 | `doddle.local.reviews` |
| `gate` | — (human) | `approvers:`, `timeout_s` | approval before publish |

`needs` lists upstream node ids or `inputs`. `produces` names outputs.

## SKILL.md frontmatter (light)

```yaml
name: <dir-name>
id: <same as blueprint>
version: <semver>
blueprint: ./blueprint.yaml
description: <triggers>
```

## Validator rules (implemented)

* Node `type` ∈ {agent, tool, call, gate}; `call` refs and `fallback_for` entries MUST be known skill ids.
* Every declared output MUST appear in ≥1 `produces` (output coverage).
