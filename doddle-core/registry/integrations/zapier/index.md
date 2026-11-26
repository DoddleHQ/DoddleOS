# Zapier

> Official Zapier MCP (GA) — **agentic** mode with fixed meta-tools, or **managed** mode with one
> tool per action. Actions run against your existing app connections.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.zapier.com` |
| Transport | Streamable HTTP only — **SSE is not supported** |
| Plan | Team or Enterprise |
| Topology | one server per named MCP client (sharing needs Team/Enterprise) |
| Compliance | SOC 2 Type II |
| Quota | tool calls consume Zapier tasks from the plan quota; failed calls are free |

## Tools

### Agentic mode (default)

| Upstream tool | Effect |
|---------------|--------|
| `discover_zapier_actions` | lists available actions |
| `enable_zapier_action` | enables an action for use |
| `manage_zapier_connections` | manages app connections |
| `auto_provision_mcp` | provisions the MCP setup |

### Managed mode

One tool per action, configured in Zapier.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.zapier.listActions` | `discover_zapier_actions` | read |
| `doddle.tool.v1.zapier.enableAction` | `enable_zapier_action` | **write** |
| `doddle.tool.v1.zapier.manageConnections` | `manage_zapier_connections` | **write** |
| `doddle.tool.v1.zapier.autoProvisionMcp` | `auto_provision_mcp` | **write** |
| `doddle.tool.v1.zapier.runAction` | managed-mode action tool (one per action) | **write** (mutates the connected app) |

**Write-gated.** `runAction` executes against the user's live app connections and **can mutate
those apps** — a CRM record, a sheet row, a sent message. `enableAction`,
`manageConnections` and `autoProvisionMcp` change the Zapier-side setup. A blueprint must place
a `gate` node immediately before any of them (for example `approve_publish`), keep the tool
`required: false` with `fallback: manual_review`, and name the app and action before asking for
approval. Watch the workspace task quota — every call costs a task.

## Verified notes (2026-11)

- Programmatic clients connect with a **connection token** against a server you create; OAuth-from-the-client attaches the user to their default server.
- Agentic mode ships 14 meta-tools for discovering and enabling actions mid-conversation; managed mode exposes one tool per enabled action, with names derived from Zapier action names.
- **Dry-run:** managed mode with a single app and one enabled action.
## Setup

1. Zapier Team or Enterprise plan.
2. Create the MCP server for the named client — one server per client.
3. Connect the apps you want the actions to run against.
4. Choose a mode: agentic (default) or managed (one tool per action, configured in Zapier).

## Used By

- `revops-integration-growth` (doddle-revops-skills) — binds `doddle.tool.v1.zapier.listActions`
- `marketing-loops` (doddle-marketing-skills) — automation lane for content, SEO and review loops
