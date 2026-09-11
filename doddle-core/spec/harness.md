# Harness Spec — Phase 1 (DoddleOS execution)

Status: draft. Makes one blueprint execute end-to-end: runner + I/O schema + resolvers + ledger.
Backward compatible with v2 blueprints (defaults fill new fields). Out of scope: human gates
mechanism, traces/cost, `call` nodes, router, lockfiles, evals, memory (Phase 2/3).

Related: `blueprint-schema.md`, `tool-namespace.md`.

---

## 1. Run lifecycle

```
create → validate → schedule → execute → complete | failed | waiting_input
```

| Transition | Rule |
|------------|------|
| `create` | Caller supplies `skill_id + inputs`. Harness assigns `run_id` (ulid). |
| `validate` | Blueprint shape (existing validator) + input schema check (§3). Fail → `failed`, no nodes run. |
| `schedule` | Topological order from `needs`. Nodes with all deps met run; independent nodes may run in parallel up to `max_parallel` (default 4). |
| `execute` | Each node runs to a terminal state before dependents start (join policy §2). |
| `complete` | All sink-node outputs validate against output schemas. Artifacts sealed. |
| `failed` | Node exhausted retries and `on_fail.fallback` is not actionable (Phase 1: `manual_review` parks run as `waiting_input` with reason). |

Idempotency: `(skill_id, inputs_hash)` reuses a `complete` run within TTL (default 24h) unless `force: true`.

---

## 2. Runner semantics

### 2.1 Node states

`pending → running → succeeded | failed | skipped`

### 2.2 Dependencies (`needs`)

* `needs: [inputs]` — runs at wave 0 after input validation.
* `needs: [node_a, node_b]` — runs when **all** listed nodes `succeeded` (join policy `all`; the only Phase-1 policy).
* If any dep `failed`/`skipped` → node is `skipped`, run continues to nodes whose deps still satisfiable; run `failed` at end if any required output missing.

### 2.3 Timeouts and retries

| Field (node-level, optional) | Default |
|------------------------------|---------|
| `timeout_s` | 300 (agent), 60 (tool) |
| `retry` | from skill `on_fail.retry` (default 1) |

Retry applies to timeouts + transient tool errors only (5xx, rate-limit, DNS). Deterministic errors (4xx, schema fail, auth) do not retry. Backoff: 2s × attempt.

### 2.4 Failure propagation

Node exhausts retries → `failed` → dependents `skipped` → at run end:
* If all declared `outputs` producible from succeeded nodes → `complete` (partial noted in ledger).
* Else apply skill `on_fail.fallback`: Phase 1 supports `manual_review` only → run parks as `waiting_input` with `reason + node_id + partial_artifacts`.

### 2.5 Determinism notes

Same `(skill version, inputs)` replays same node order. Tool nodes SHOULD set idempotency keys where the server supports them. Agent nodes are inherently non-deterministic; ledger records model + prompt hash for audit.

---

## 3. I/O schema

### 3.1 Inputs

Each blueprint `inputs[]` entry gains optional `schema` (JSON Schema draft 2020-12). Minimal form stays valid:

```yaml
- {name: page_url, type: string, required: true, description: "..."}
# full form:
- name: monthly_budget
  type: number
  required: false
  default: 1000
  schema: {type: number, minimum: 0}
```

Rules:
* `required: true` missing → run fails at `validate` with `missing_input` (Phase 2 adds interactive `waiting_input` ask).
* Unknown input keys → rejected at `validate` (strict mode; warns otherwise).
* Types map: `string | number | boolean | url | markdown | json`. `url` = string + format uri. `markdown/json` may exceed inline limits → stored as artifacts (§3.3), referenced by id.

### 3.2 Outputs

Each `outputs[]` entry gains optional `schema`. Node `produces` names MUST match declared outputs (validator extension). At `complete`, each output validates; failure → run `failed` with `output_schema_error`.

### 3.3 Artifact store

```
./artifacts/<run_id>/<output_name>.<md|json|txt>
```

* Values >4KB or of type markdown/json are written to the store; ledger references artifact ids.
* Content-addressed manifest (`manifest.json`: sha256 per artifact) sealed at `complete`.
* Retention default 90 days. Stubs/tools returning NOT AVAILABLE produce explicit `unavailable` markers, never empty files (data-reliability rule, machine-enforced).

---

## 4. Resolver contracts

### 4.1 Tool resolver

`doddle.tool.v1.<server>.<tool>` resolves via `registry/integrations/<server>/config.json`:

| Step | Contract |
|------|----------|
| Lookup | server dir MUST exist; else `unavailable` (stub path). |
| Auth | env vars from `config.json:env` injected from vault; missing creds → `unavailable`, no retry. |
| Invoke | MCP client call with node `timeout_s`; maps result to declared output type. |
| Cache | GET-like reads cached by `(tool, args_hash)` TTL 15 min unless `cache: false`. |
| Limits | per-server concurrency 4, rate-limit backoff honors `Retry-After`. |

Stub servers (no live MCP): resolver short-circuits to `unavailable` → node follows `fallback` (Phase 1: downstream continues with `manual_review` note; see §2.4).

### 4.2 Agent resolver

Agent `ref: <name>` resolves:

1. File: first match in `<pack>/.claude/agents/<name>.md`, else core `.claude/agents/<name>.md`; missing → run `failed` (`unknown_agent`).
2. Model pin: optional node field `model:` (default from harness config; Phase 1 default recorded in ledger, no per-skill requirement).
3. Prompt assembly: `SKILL.md` relevant sections + node inputs + prior artifact refs. Exact template TBD Phase 2; Phase 1 records `prompt_hash` only.

---

## 5. Run ledger (minimal record)

```json
{
  "run_id": "ulid",
  "skill_id": "doddle.local.gbp",
  "skill_version": "1.0.0",
  "status": "complete",
  "inputs_hash": "sha256",
  "nodes": [{"id": "assess", "type": "agent", "status": "succeeded",
             "attempts": 1, "model": "…", "prompt_hash": "…",
             "artifacts": ["…"], "ms": 1234}],
  "artifacts_manifest": "artifacts/<run_id>/manifest.json",
  "error": null
}
```

Ledger is append-only (JSONL per run). Phase 1 has no query API beyond files.

---

## 6. v2 → v2.1 migration (non-breaking)

Existing blueprints stay valid. New optional fields: node `timeout_s`, `model`, `cache`; input/output `schema`, `default`. Validator gains: `produces` ⊆ declared outputs (error), unknown `ref` targets (warning until agent registry lands).

## 7. Conformance checklist (harness implementer)

- [ ] Topological schedule + join-all + max_parallel
- [ ] Input/output JSON-Schema validation at validate/complete boundaries
- [ ] Artifact store + manifest sealing
- [ ] Tool resolver (lookup/auth/invoke/cache/limits) incl. stub short-circuit
- [ ] Agent resolver (file + model record + prompt hash)
- [ ] Ledger JSONL + idempotent re-dispatch
- [ ] `waiting_input` parking for `manual_review`
