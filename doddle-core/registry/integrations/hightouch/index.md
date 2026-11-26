# Hightouch

> Official Hightouch MCP server for the marketing stack — **gated**: Hightouch must enable it
> for your workspace. Reads schema/data/performance, and takes actions on audiences, journeys,
> creatives and syncs.

## Connection

| Field | Value |
|-------|-------|
| Workspace MCP | Gated — enabled by Hightouch per workspace (endpoint URL not published) |
| Public docs MCP | `https://docs.hightouch.com/mcp` — Search / Read pages / Submit feedback, no auth |
| Signed-in docs MCP | `https://docs.hightouch.com/authed/mcp` |
| Public Agent API MCP | `https://hightouch.com/agent-api/mcp` — read-only search + fetch |
| Agent API metadata | `https://hightouch.com/agent-api/v1/info`, `https://hightouch.com/agent-api/openapi.json` |
| Transport | HTTP (remote MCP) |
| Auth | Workspace OAuth for the workspace server; none for the public docs MCP |
| Cost | No extra charge for MCP access |

The registered `url` in `config.json` is the public docs MCP — it is the only Hightouch
endpoint published in this registry. The workspace server (which carries the write tools) must
be enabled by Hightouch for your workspace.

## Tools

| Upstream tool | Effect |
|---------------|--------|
| schema inspection | reads the workspace schema |
| data access | reads data |
| performance analysis | reads sync / flow performance |
| audience create/save | creates or saves an audience |
| journey design | designs a journey |
| email/SMS creative generation | generates creatives, saved as drafts |
| ad creative generation | generates ad creatives |
| sync management | manages syncs |
| sync creation from templates | creates a sync from a template |
| Agent API `search` / `fetch` | read-only public product docs |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.hightouch.getSchema` | schema inspection | read |
| `doddle.tool.v1.hightouch.getData` | data access | read |
| `doddle.tool.v1.hightouch.analyzePerformance` | performance analysis | read |
| `doddle.tool.v1.hightouch.listSyncs` | sync management — list | read |
| `doddle.tool.v1.hightouch.createAudience` | audience create/save | **write** |
| `doddle.tool.v1.hightouch.designJourney` | journey design | **write** |
| `doddle.tool.v1.hightouch.generateEmailCreative` | email/SMS creative generation (drafts) | **write** |
| `doddle.tool.v1.hightouch.generateAdCreative` | ad creative generation | **write** |
| `doddle.tool.v1.hightouch.manageSyncs` | sync management — update | **write** |
| `doddle.tool.v1.hightouch.createSync` | sync creation (from a template) | **write** |
| `doddle.tool.v1.hightouch.agentApiSearch` | Agent API `search` | read |
| `doddle.tool.v1.hightouch.agentApiFetch` | Agent API `fetch` | read |

**Write-gated.** Every `**write**` row changes production marketing data or starts data
movement. A blueprint must place a `gate` node immediately before it — `approve_sync` for the
sync tools (see `doddle-core/spec/harness-cli-resolver.md` §6), `approve_publish` for audience,
journey and creative tools — keep the tool `required: false` with `fallback: manual_review`,
and preview the audience / sync / creative before asking for approval. All operations are
scoped to the authenticated workspace and respect its RBAC.

## Verified notes (2026-11)

- REST fallback for everything the gated MCP cannot do: `https://api.hightouch.com` with a bearer key (`HIGTOUCH_API_KEY`).
- The workspace OAuth metadata is live at `https://mcp-auth.hightouch.com/oauth2/{authorize,token,register,device_authorization}`, so a client can be built before the endpoint URL is disclosed.
## Setup

1. Hightouch workspace.
2. Ask Hightouch to enable the MCP server for the workspace — it is gated, not self-serve.
3. Authorize with a role that allows the actions you intend to bind.
4. Optional: use the public docs MCP (`https://docs.hightouch.com/mcp`) or the read-only Agent
   API MCP (`https://hightouch.com/agent-api/mcp`) for documentation lookups.

## Used By

- `revops-data-infrastructure` (doddle-revops-skills) — binds `hightouch.listSyncs` and the gated
  `hightouch.createSync` (`approve_sync`)
- `revops-integration-growth` (doddle-revops-skills) — binds `hightouch.listSyncs`
