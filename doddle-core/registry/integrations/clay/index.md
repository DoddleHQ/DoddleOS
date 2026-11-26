# Clay

> Official Clay MCP server — subroutines, custom functions and enrichment, with a Public API
> alternative for routine runs.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://api.clay.com/v3/mcp` |
| Transport | HTTP (remote MCP) |
| Auth | OAuth 2.0 + Dynamic Client Registration (RFC 7591) — PKCE mandatory, scope `mcp` |
| Client registration | `https://api.clay.com/oauth/register` |
| Token lifetime | access token 1h; refresh tokens rotate |

| OAuth endpoint | URL |
|-----------------|-----|
| Authorization | `https://app.clay.com/oauth/authorize` |
| Token | `https://api.clay.com/oauth/token` |
| Revoke | `https://api.clay.com/oauth/revoke` |
| Server metadata | `https://api.clay.com/.well-known/oauth-authorization-server` |
| Resource metadata | `https://api.clay.com/.well-known/oauth-protected-resource/v3/mcp` |

## Tools

| Upstream tool | What it does |
|---------------|--------------|
| `list_subroutines` | lists callable subroutines / functions |
| run a function by id | executes that function (its MCP access must be enabled in Clay settings) |
| Public API routine run | `POST /public/v0/routines/{routine_id}/run` (header `clay-api-key`) |
| Public API routine results | `GET .../routines/run/{routine_run_id}/results` — 202 while processing, 200 when complete, per-item status |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.clay.searchPeople` | find-and-enrich people search (via routine / function run or the Public API) | read |
| `doddle.tool.v1.clay.listSubroutines` | `list_subroutines` | read |
| `doddle.tool.v1.clay.runSubroutine` | run a function by id | **write** (consumes credits) |
| `doddle.tool.v1.clay.getRoutineResults` | Public API `GET .../routines/run/{routine_run_id}/results` | read |

**Write-gated.** `runSubroutine` executes a Clay routine — it burns credits and can change
workspace state, so a blueprint must place a `gate` node immediately before it (for example
`approve_enrichment`), keep the tool `required: false` with `fallback: manual_review`, and
show the routine id + intended source list before asking for approval.

## Setup

1. Clay workspace with the functions you intend to call.
2. Enable MCP access on each function you want to run (API access alone is not enough).
3. An MCP client that supports dynamic client registration with PKCE.
4. Clay admins control the "Allowed MCP clients" list and set per-user / per-role credit
   budgets; MCP work consumes credits at the same rate as in-app work.

Public API alternative (same functions): `POST https://api.clay.com/public/v0/routines/{routine_id}/run`
with header `clay-api-key`, then poll `GET .../routines/run/{routine_run_id}/results`.

## Used By

- `revops-ai-sdr` (doddle-revops-skills) — binds `doddle.tool.v1.clay.searchPeople`
