# make

> Make MCP — run scenarios and manage the automation workspace

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.make.com/v2` |
| Transport | http |
| Auth | oauth-or-api-key |

## Upstream tools

`run active/on-demand scenario`, `view/modify scenario`, `view/modify connection`, `view/modify webhook`, `view/modify data store`, `view/modify team/org`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.make.listScenarios` | `view scenarios` | read |
| `doddle.tool.v1.make.runScenario` | `run a scenario` | write (executes automation) |
| `doddle.tool.v1.make.updateScenario` | `modify a scenario` | write |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Make account
- OAuth, or an API key plus your zone (e.g. eu2.make.com)

### Notes

- Stateless Streamable HTTP. API-key URL form: https://<MAKE_ZONE>/mcp/u/<API_KEY>/v2.
- Scenario run tools are on every plan; management tools need a paid plan. Scopes control what is exposed (e.g. scenarios:read to fetch outputs after a timeout).
- Timeouts: scenario run 25s (OAuth) / 40s (API key); management 30s / 60s. After a timeout the scenario keeps running up to 40 minutes — fetch the result with the returned executionId.
- Optional ?maxToolNameLength= parameter (32-160, default 56).

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
