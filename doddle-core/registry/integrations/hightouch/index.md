# hightouch

> Hightouch reverse ETL and audiences — official MCP server (workspace-gated)

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.hightouch.com/mcp` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`schema inspection`, `audience create/save`, `journey design`, `sync management`, `creative generation`, `performance analysis`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.hightouch.listSyncs` | `sync management` | read |
| `doddle.tool.v1.hightouch.createSync` | `create a sync from a template` | write |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Hightouch workspace
- MCP enabled for the workspace by Hightouch (not self-serve)

### Notes

- The workspace MCP server is gated: Hightouch must enable it for your account.
- Operations are scoped to the authenticated workspace and respect its role-based access controls.
- A public read-only docs MCP exists at https://docs.hightouch.com/mcp; a read-only Agent API MCP at https://hightouch.com/agent-api/mcp serves public product docs.
- MCP access carries no extra charge; underlying product and agent usage still applies.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
