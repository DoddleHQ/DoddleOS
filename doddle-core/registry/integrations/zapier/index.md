# zapier

> Zapier MCP — 9,000+ apps and 40,000+ actions through agentic or managed servers

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.zapier.com` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`discover_zapier_actions`, `enable_zapier_action`, `manage_zapier_connections`, `auto_provision_mcp`, `managed-mode action tools`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.zapier.listActions` | `discover_zapier_actions` | read |
| `doddle.tool.v1.zapier.runAction` | `an enabled action` | write (mutates the connected app) |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Zapier Team or Enterprise plan
- App connections in the Zapier account

### Notes

- One server per named MCP client; sharing a server needs Team or Enterprise.
- Streamable HTTP only — SSE is not supported.
- Agentic mode exposes meta-tools (discover_zapier_actions, enable_zapier_action, manage_zapier_connections, auto_provision_mcp); managed mode exposes one tool per action.
- Actions run against existing app connections and CAN mutate those apps. Tool calls consume plan tasks; failed calls are free.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
