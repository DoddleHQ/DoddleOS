# clay

> Clay enrichment and custom functions — official MCP server plus Public API routines

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://api.clay.com/v3/mcp` |
| Transport | http |
| Auth | oauth-dcr |

## Upstream tools

`list_subroutines`, `run subroutine by id`, `search/find-and-enrich tools`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.clay.searchPeople` | `find-and-enrich search tools` | read |
| `doddle.tool.v1.clay.runSubroutine` | `run a routine/function by id` | write (consumes credits) |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Clay workspace
- OAuth client registered via dynamic client registration (PKCE mandatory) or a public API key

### Notes

- MCP endpoint: https://api.clay.com/v3/mcp; metadata at https://api.clay.com/.well-known/oauth-authorization-server.
- Public API alternative: POST https://api.clay.com/public/v0/routines/{routine_id}/run with header clay-api-key, then GET .../routines/run/{routine_run_id}/results (202 while processing, 200 complete).
- Running a function needs MCP access enabled on that function; API access alone is not enough. Use list_subroutines to find callable functions.
- Admins control which clients are allowed and set per-user/role credit budgets. Tools consume workspace credits at the in-app rate.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
