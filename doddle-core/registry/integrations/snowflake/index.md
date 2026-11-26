# Snowflake

> Snowflake-managed MCP server (GA since 2025-11-04) — governed data access, SQL execution,
> Cortex Analyst, Cortex Search, and Cortex Agents as tools.

## Connection

| Field | Value |
|-------|-------|
| Transport | Streamable HTTP |
| URL | `https://<account_url>/api/v2/databases/{database}/schemas/{schema}/mcp-servers/{name}` |
| Auth | Snowflake OAuth (recommended) or a Programmatic Access Token |
| MCP revision | 2025-11-25 |

> **Use hyphens, not underscores, in the account hostname.** `acme-marketing-account`
> works; `acme-marketing_account` fails to connect (often as a TLS error).

> **Streaming responses.** Since 2026-08-20, `tools/call` replies arrive as an SSE stream. Send
> `Accept: application/json, text/event-stream`. The server emits a keep-alive comment roughly
> every 5 seconds and the final `data:` event carries the JSON-RPC response.

## Tool types you can expose

| Type | What it does |
|------|--------------|
| `SYSTEM_EXECUTE_SQL` | Runs SQL directly |
| `CORTEX_ANALYST_MESSAGE` | Natural-language analysis over semantic views |
| `CORTEX_SEARCH_SERVICE_QUERY` | Cortex Search queries |
| `CORTEX_AGENT_RUN` | Orchestrates a governed Cortex Agent |
| `CODING_AGENT` | Coding agent with a code toolset |
| `GENERIC` | UDFs and stored procedures |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.snowflake.listSchemas` | catalog listing | read |
| `doddle.tool.v1.snowflake.listTables` | catalog listing | read |
| `doddle.tool.v1.snowflake.getTableInfo` | table metadata | read |
| `doddle.tool.v1.snowflake.executeSql` | `SYSTEM_EXECUTE_SQL` | **write-capable** |

**Write-gated.** `executeSql` can run DDL/DML. Any blueprint that binds it must gate it first
(`approve_query`) and scope the role to a least-privilege role. Read-only profiling should use
the catalog tools, not SQL.

## Setup

```bash
export SNOWFLAKE_ACCOUNT_URL="acme-marketing-account"
export SNOWFLAKE_DATABASE="DASH_MCP_DB"
export SNOWFLAKE_SCHEMA="DATA"
export SNOWFLAKE_MCP_SERVER="DASH_MCP_SERVER"
export SNOWFLAKE_PAT="<programmatic access token>"
```

## Used By

- `revops-data-infrastructure` (doddle-revops-skills, read + gated SQL)
