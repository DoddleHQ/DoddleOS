# Harness Spec — CLI Tool Resolver (`doddle.tool.cli.*`)

Status: draft. Extends `harness.md` (Phase 1) and `harness-phase2.md` (gates, observability)
with a resolver for **CLI-backed tool nodes** — tool nodes whose implementation is a local
command instead of an MCP server.

First reference implementation: `doddle.tool.cli.drev` (Doddle RevOps OS), which backs all 12
`doddle-revops-skills` skills. Second: `doddle.tool.cli.dgtm` (Doddle GTM OS).

Related: `harness.md` §4.1, `harness-phase2.md` §2 (gates), `tool-namespace.md`,
`blueprint-schema.md`.

---

## 1. Why a CLI resolver

Some skills need **deterministic, offline computation** more than they need a live API. The
RevOps pack encodes revenue math — attribution allocation, NRR, usage rating, PQL scoring — as a
stdlib-only CLI (`drev`). Running it as a tool node gives the harness:

* reproducible numbers (same inputs → same envelope), verified by the pack's own tests;
* a hard boundary — no network, no credentials, no writes;
* a JSON envelope contract the runner can validate generically.

MCP servers stay the mechanism for live external data (`doddle.tool.v1.<server>.<tool>`).

---

## 2. Node contract

```yaml
- {id: route, type: tool, ref: doddle.tool.cli.drev,
   args: ["route-signals"],
   inputs: {events: $events, rules: $rules},
   needs: [survey], produces: [envelope]}
```

| Field | Required | Meaning |
|-------|----------|---------|
| `ref` | yes | `doddle.tool.cli.<cli>` — resolves via `registry/cli/<cli>.json` |
| `args` | no | Subcommand plus static flags, in order |
| `inputs` | no | Map of **flag → value** for dynamic arguments |
| `timeout_s` | no | Default 60s for CLI nodes |
| `idempotency` | no | Default `true` — same inputs reuse the cached envelope |

### 2.1 Flag binding rule

For each `inputs` key, the runner appends `--<key with `_`→`-`>` followed by the resolved value:

| `inputs` key | Emitted argv |
|--------------|--------------|
| `events` | `--events <value>` |
| `max_age_days` | `--max-age-days <value>` |
| `warehouse_export` | `--warehouse-export <value>` |

Rules:

* Values are resolved to **argv entries**, never shell strings. No interpolation, no quoting, no
  command substitution — a path with spaces is one argv entry.
* `$name` resolves to a run input, an upstream node output, or an artifact path (absolute).
* A literal (non-`$`) value is passed verbatim.
* Unknown keys, missing `$name` references, or a resolved value that is `null` → node fails with
  `input_binding_error` before the process starts.
* A required flag missing at the CLI level is caught by the CLI itself, which returns
  `ok: false` with `error.hint` — the runner relays it verbatim.

### 2.2 CLI registry

`doddle-core/registry/cli/<cli>.json`:

```json
{
  "name": "drev",
  "runtime": "python3",
  "path": "doddle-revops-skills/scripts/drev",
  "version": "1.0.0",
  "envelope": "doddle-revops-envelope-v1",
  "network": false,
  "writes": false
}
```

| Field | Meaning |
|-------|---------|
| `runtime` | Interpreter (`python3`, `node`) |
| `path` | Repo-relative executable |
| `envelope` | Envelope schema the runner validates against |
| `network` | `false` → runner runs with network disabled |
| `writes` | `false` → runner mounts the workspace read-only |

---

## 3. Execution contract

```
resolve inputs → build argv → run (no shell, timeout, rlimits) → parse stdout → validate envelope → map outputs
```

| Step | Rule |
|------|------|
| Invoke | `[runtime, <path>, *args, *bound_flags]`, `cwd` = pack root, `shell: false` |
| Sandbox | Read-only workspace except `./artifacts/<run_id>/`; no network for `network: false` CLIs; env allowlist only (`PATH`, `LANG`, `TZ`, plus declared `env` in the CLI registry) |
| Timeout | `timeout_s` (default 60). Kill the process group on expiry → node `failed` (`timeout`) |
| Stdout | Exactly one JSON object. Extra stdout output → `envelope_parse_error` |
| Exit code | `0` → parse and validate; `1` → the CLI's own error envelope is used; `>1` → `tool_error` with the exit code |
| Retry | Deterministic failures (exit 1, parse error, validation error) do **not** retry. Transient failures (OOM, SIGKILL, timeout) retry per `on_fail.retry` |

### 3.1 Envelope validation

Required fields: `ok` (bool), `command` (str), `metrics` (object), `rows` (array),
`evidence.stamp` (str), `completeness.missing` (array).

| Condition | Outcome |
|-----------|---------|
| `ok: false` | Node `failed` with `error.message` + `error.hint` from the envelope; no retry |
| `evidence.stamp != "CURRENT"` | Node `succeeded`, run flagged `stale_evidence`; the flag must appear in the node's narrative output |
| `completeness.missing` non-empty | Node `succeeded`; missing inputs are reported, never substituted with zero |

This is the machine-enforced half of the data-reliability rule.

---

## 4. Output mapping

| `produces` name | Source |
|-----------------|--------|
| `envelope` | The whole envelope object (serialized as JSON artifact) |
| `report` | The node's narrative artifact, produced by the downstream agent node |
| `deck` | Envelope rows filtered by `kind` (e.g. `kind: slide`) |

A tool node never produces prose. Narrative is always an agent node downstream, so the numbers
and the words stay separable — the same rule the packs' authoring contracts require.

---

## 5. Determinism and idempotency

* Time-dependent commands accept `--now` (ISO-8601). A node may declare
  `deterministic_time: true`, and the runner injects the run's frozen reference time so two runs
  of the same inputs produce identical envelopes.
* Idempotency key = `(cli, args_hash, inputs_hash)`. A repeat within the run TTL (15 min,
  matching `harness.md` §4.1) reuses the cached envelope instead of re-executing.
* The same `(skill_version, inputs)` therefore replays byte-identical envelopes.

---

## 6. Gates and write safety

CLI nodes are read-only by construction (`network: false`, `writes: false`). Write-capable
actions live behind MCP write tools, and those carry the Phase 2 gate rule:

> **Preflight rule `write_without_gate`:** a node whose tool can mutate an external system
> (`registry/integrations/<server>/config.json` → `writes: true`) MUST have an upstream `gate`
> node whose decision is `approved`. The runner refuses to schedule such a node without that
> record — the run parks as `waiting_input` with `reason: approval_required`.

Concretely for the RevOps pack:

| Action | Tool | Gate |
|---------|------|------|
| Send a Slack alert | `doddle.tool.v1.slack.messages` | `approve_alert` |
| Record a usage/meter event | `doddle.tool.v1.stripe.*` (write) | `approve_billing` |
| Trigger a reverse-ETL sync | `doddle.tool.v1.hightouch.*` (write) | `approve_sync` |
| Publish a teardown | `doddle.tool.v1.notion.pages` (write) | `approve_publish` |

The `drev` CLI never performs any of these. It produces the payload, the preview, or the plan;
the write is a separate, gated node.

---

## 7. Ledger

```json
{"id": "route", "type": "tool", "status": "succeeded",
 "cli": "drev", "argv_hash": "sha256:…", "inputs_hash": "sha256:…",
 "envelope_hash": "sha256:…", "artifacts": ["sha256:…"], "ms": 84,
 "flags": ["stale_evidence"]}
```

The ledger stores hashes, not raw argument values, because CLI inputs can contain file paths
and, in future, PII. Raw values live in artifacts under the retention policy in `harness.md`
§3.3.

---

## 8. Conformance checklist (harness implementer)

- [ ] CLI registry lookup; missing entry → `unavailable` (stub path), node follows `fallback`
- [ ] Argv construction from `args` + `inputs`, no shell, no interpolation
- [ ] Input resolution (`$name` → input / node output / artifact path)
- [ ] Read-only sandbox, network off for `network: false`, env allowlist
- [ ] Timeout + process-group kill; transient-vs-deterministic retry split
- [ ] Single-JSON stdout parse; exit-code mapping
- [ ] Envelope validation (`ok`, `evidence.stamp`, `completeness.missing`)
- [ ] `stale_evidence` and missing-input propagation to the narrative node
- [ ] Output mapping (`envelope`, filtered `rows`)
- [ ] Idempotency cache keyed by `(cli, args_hash, inputs_hash)`
- [ ] Preflight `write_without_gate` check before scheduling write nodes
- [ ] Ledger entries with hashes only

---

## 9. Phases

| Phase | Scope |
|-------|-------|
| **1** | CLI resolver only: registry, argv binding, sandbox, envelope validation, ledger |
| **2** | Gate preflight (`write_without_gate`), Slack approval transport, idempotency cache |
| **3** | MCP write tools behind gates, approval records in the ledger, rollback artifacts |
