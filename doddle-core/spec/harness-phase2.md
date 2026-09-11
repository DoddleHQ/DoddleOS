# Harness Spec — Phase 2 (DoddleOS execution)

Status: draft. Builds on `harness.md` Phase 1 (runner, I/O, resolvers, ledger).
Adds: human gates mechanism, observability, composition (`call`), router.
Backward compatible: all new fields optional.

---

## 1. Composition — `call` nodes

Skills invoke skills as sub-graphs (kills reviews×5 / booking×3 duplication pressure).

```yaml
nodes:
  - {id: rep_check, type: call, ref: doddle.local.reviews,
     needs: [assess], produces: [review_data],
     inputs: {business_name: $business_name, location: $location}}
```

| Rule | Detail |
|------|--------|
| `ref` | MUST be a known skill id (validator: error otherwise). No self-reference (error). Max depth 3 (error at schedule). |
| `inputs` | Map caller values (`$name` = caller input/artifact) to callee required inputs. Missing callee required input → schedule-time `failed`. |
| `produces` | Subset of caller-declared outputs, filled from callee outputs. |
| Ledger | Sub-run nested under caller node (`sub_run_id`), full ledger rules apply. |
| Cost/latency | Roll up to caller node. |

## 2. Human gates — `gate` nodes + input asks

### 2.1 Gate node

```yaml
- {id: approve_copy, type: gate, needs: [recommend], produces: [decision],
   approvers: [owner], timeout_s: 86400,
   on_approve: proceed, on_reject: revise}
```

| Field | Required | Detail |
|-------|----------|--------|
| `approvers` | yes | Roles/users. Phase 2 transport = queue record (no UI specified). |
| `timeout_s` | yes | Expiry → `on_timeout` (default: `escalate`). |
| `on_approve` / `on_reject` | yes/no | `proceed` (default), `revise` (re-run upstream node once), `abort`. |

Gate pending → run status `waiting_input` with `gate: {node_id, approvers, expires_at, artifact_refs}`.
Phase 2 defines the queue record only; transports (Slack/email/dashboard) are integrations.

### 2.2 Missing required inputs → ask (replaces Phase-1 fail)

`validate` with missing required input parks run as `waiting_input` with `needed: [{name, type, description}]`
instead of `failed`, unless `strict_inputs: true` set on the call.

### 2.3 `manual_review` fallback (now mechanistic)

`on_fail.fallback: manual_review` creates a gate record: approvers `[owner]`, timeout 7d,
`on_approve: proceed-with-partial`, `on_reject: abort`. Same queue as §2.1.

## 3. Observability — traces, cost, audit

Ledger node entry extends (§5 of harness.md) with a span:

```json
{"id": "assess", "span": {"started_at": "…", "ended_ms": 1234,
 "tokens_in": 1200, "tokens_out": 300, "est_cost_usd": 0.0042,
 "tool_calls": [{"tool": "doddle.tool.v1.ga4.getReport", "ms": 210, "cached": true}],
 "artifacts": ["sha256:…"]}}
```

| Rule | Detail |
|------|--------|
| Cost | `tokens × model price table` (harness config, versioned). Tool calls: per-call price if server declares one, else latency only. |
| Run rollup | Total ms + cost on run record. Budget: optional call field `budget_usd` → exceed → park `waiting_input` (never silent-kill paid work mid-node; finish node, then park). |
| Audit | Compliance packs (health/legal/finance/edu) REQUIRE per-run: model id, prompt hash, tool args hash (never raw PHI/PII), approver id on gates. Raw PII stays in artifacts with retention policy; ledger holds hashes. |

## 4. Router — skill selection

Harness picks skill from user intent using ratified blueprint fields:

```yaml
domains: [restaurant, local]        # optional; empty = generic
fallback_for: []                    # optional; ids this skill is generic fallback for (none normally)
```

### 4.1 Routing rules

1. Parse trigger keywords from all skill descriptions (existing behavior, now explicit).
2. Prefer skills whose `domains` intersect detected domain tokens; generic (empty `domains`) skills rank below domain matches.
3. `fallback_for` declares reverse mapping (e.g. `local-reviews` lists nothing; router config maps unclaimed review intents → generic by category, not by skill claim).
4. Confidence < threshold (default 0.6) → `waiting_input` with top-3 candidates (ask, don't guess).
5. Exact skill id or command (`/health:booking`) bypasses routing entirely.

### 4.2 Validator rules (implemented)

* `domains`: free-form strings, no check.
* `fallback_for` entries MUST be known skill ids (error). Self-reference (error).
* `call` refs MUST be known skill ids, no self-call, depth checked at schedule.
* `gate` nodes MUST declare `approvers` + `timeout_s` (error).
* Node `type` ∈ {agent, tool, call, gate} (error).
* Every declared output MUST appear in ≥1 `produces` (error — output coverage).

## 5. Conformance checklist (Phase 2 delta)

- [ ] Sub-run execution for `call` (depth cap, ledger nesting, cost rollup)
- [ ] Gate queue records + approve/reject/revise flows + timeouts
- [ ] Missing-input ask (`waiting_input` + `needed`) unless strict
- [ ] Span emission (latency/tokens/cost/tool calls) + run rollup + budget park
- [ ] Audit fields for compliance packs (hashes, no raw PII in ledger)
- [ ] Router with domains/fallback, confidence threshold, top-3 ask
