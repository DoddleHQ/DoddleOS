# Make

> Official Make-hosted MCP server — run scenarios and manage the automation workspace.
> Stateless Streamable HTTP.

## Connection

| Field | Value |
|-------|-------|
| OAuth URL | `https://mcp.make.com/v2` |
| API-key URL | `https://<MAKE_ZONE>/mcp/u/<API_KEY>/v2` (zone e.g. `eu2.make.com`) |
| Transport | Stateless Streamable HTTP |
| Optional parameter | `?maxToolNameLength=` — 32–160, default 56 |
| Scopes | control which tools are exposed (e.g. `scenarios:read` to fetch outputs after a timeout) |
| Timeouts | scenario run 25s (OAuth) / 40s (API key); management 30s / 60s |
| Plan | management tools need a paid plan |

## Tools

| Upstream tool | Effect |
|---------------|--------|
| run active/on-demand scenario | executes the automation |
| view scenario | reads a scenario |
| modify scenario | changes a scenario |
| view/modify connection | reads or changes app connections |
| view/modify webhook | reads or changes webhooks |
| view/modify data store | reads or changes data stores |
| view/modify team | reads or changes teams |
| view/modify organization | reads or changes organizations |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.make.listScenarios` | view scenario | read |
| `doddle.tool.v1.make.getScenarioOutputs` | scenario outputs (needs `scenarios:read`) | read |
| `doddle.tool.v1.make.runScenario` | run active/on-demand scenario | **write** |
| `doddle.tool.v1.make.updateScenario` | modify scenario | **write** |
| `doddle.tool.v1.make.manageConnections` | view/modify connection | **write** |
| `doddle.tool.v1.make.manageWebhooks` | view/modify webhook | **write** |
| `doddle.tool.v1.make.manageDataStores` | view/modify data store | **write** |
| `doddle.tool.v1.make.manageTeams` | view/modify team and organization | **write** |

**Write-gated.** Running a scenario executes live automation — it can post, send, sync or
delete. The management tools rewrite the automation workspace. A blueprint must place a `gate`
node immediately before any of them (for example `approve_run`), keep the tool
`required: false` with `fallback: manual_review`, and name the scenario and its destination
before asking for approval.

**Timeouts are not failures.** After a timeout the scenario keeps running for up to 40 minutes
— keep the returned `executionId` and fetch the result later with the outputs tool instead of
re-running the scenario.

## Setup

1. Make account.
2. OAuth: use `https://mcp.make.com/v2`.
   API key: use `https://<MAKE_ZONE>/mcp/u/<API_KEY>/v2` with your zone.

```bash
export MAKE_API_KEY="<api key>"
export MAKE_ZONE="eu2.make.com"
```

3. Grant scopes for the tools you intend to bind — scope `scenarios:read` if you need outputs
   after a timeout.
4. Management tools require a paid plan.

## Used By

- `revops-integration-growth` (doddle-revops-skills) — binds `doddle.tool.v1.make.listScenarios`
- `marketing-loops` (doddle-marketing-skills) — listed as an automation lane for content, SEO
  and review loops (not yet bound to a tool id)
