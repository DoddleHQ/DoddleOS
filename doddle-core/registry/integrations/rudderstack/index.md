# RudderStack

> Official hosted MCP server — inspect and manage the customer-data pipeline.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.rudderstack.com/mcp` |
| Transport | Streamable HTTP |
| Auth | OAuth 2.0 with PKCE + dynamic client registration (browser sign-in) |
| Tools | ~62, grouped by access class |

```bash
claude mcp add --transport http rudderstack https://mcp.rudderstack.com/mcp
```

For stdio-only clients: `npx -y mcp-remote https://mcp.rudderstack.com/mcp`.

## Access classes

| Class | Examples | Effect |
|-------|----------|--------|
| Read | sources, destinations, transformations, event metrics, tracking plans, data catalog, audit logs, docs | Inspects without persisting changes |
| Sensitive execution | transformation tests, audience previews, reverse-ETL failed-record reads, activation planning | Executes code or submits temporary warehouse work without saving control-plane config |
| Write | create/update audiences, connect audiences to destinations, create rETL audience activations, **trigger audience-activation syncs**, create/update transformations, connect transformations to destinations | Persists control-plane changes |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.rudderstack.listSources` | read tools | read |
| `doddle.tool.v1.rudderstack.listDestinations` | read tools | read |
| `doddle.tool.v1.rudderstack.listEvents` | read tools | read |
| `doddle.tool.v1.rudderstack.getTrackingPlan` | read tools | read |
| `doddle.tool.v1.rudderstack.listReverseEtlSyncs` | read tools | read |
| `doddle.tool.v1.rudderstack.createAudience` | write tools | **write** |
| `doddle.tool.v1.rudderstack.triggerAudienceSync` | write tools | **write** |

**Write-gated.** Triggering a sync or creating an audience changes production data movement.
Gate both, and use sanitized sample events for transformation tests — transformation code can
make outbound requests even when the tool does not save configuration.

## Notes

- Workspace tools need `workspace_id` on every call; the endpoint is stateless.
- Sensitive fields in event payloads, delivery errors, and violations are redacted or hashed by
  the server, but live events and schemas can still contain sensitive information.
- Documentation tools can return inaccurate generated answers — verify against official docs.

## Used By

- `revops-pql-scoring`, `revops-data-infrastructure` (doddle-revops-skills)

## Verified notes (2026-11)

- 62 tools classified Read (50) / **Sensitive execution (5)** / Write (7). Docs warn against auto-approving sensitive-execution tools.
- **Best dry-run support in this registry:** `transformation_test_new` runs unsaved JS/Python against sample events without saving, `preview_audience` estimates row counts, and `plan_audience_activation` plans before creating.
- Headless variant: `Authorization: Bearer <token>` plus `X-Workspace-ID` at `https://mcp.rudderstack.com/bearer-auth-mcp`.
