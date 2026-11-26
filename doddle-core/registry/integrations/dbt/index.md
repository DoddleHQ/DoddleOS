# dbt

> Official dbt Labs MCP server — model metadata, lineage, freshness, Semantic Layer, and docs.

## Connection

| Mode | Command | Use |
|------|---------|-----|
| Self-hosted | `uvx dbt-mcp` | Full access, including dbt platform CLI |
| Remote | dbt-hosted HTTP endpoint | Data consumption only (no CLI, no codegen) |

Requires Python 3.12–3.14 on the host (dbt-mcp's own supported range).

## Toolsets

| Toolset | Self-hosted | Remote | Needs |
|---------|:-----------:|:------:|-------|
| dbt platform CLI commands | ✅ | ❌ | `DBT_PROJECT_DIR`, `DBT_PATH` |
| Semantic Layer | ✅ | ✅ | `DBT_HOST`, `DBT_TOKEN`, `DBT_PROD_ENV_ID` |
| SQL execution | ✅ | ✅ | personal access token, `DBT_DEV_ENV_ID`, `DBT_USER_ID` |
| Metadata Discovery | ✅ | ✅ | `DBT_HOST`, `DBT_TOKEN`, `DBT_PROD_ENV_ID` |
| Administrative API | ✅ | ✅ | `DBT_HOST`, `DBT_TOKEN`, `DBT_ACCOUNT_ID` |
| Codegen | ✅ | ❌ | `DBT_PROJECT_DIR`, `DBT_PATH` |
| Product Docs / MCP Server Metadata | ✅ | ✅ | — |

Toolsets **auto-disable** when their env vars are missing rather than failing the server.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.dbt.getManifest` | project manifest / dbt v2 tools | read |
| `doddle.tool.v1.dbt.discover` | Metadata Discovery API — models, lineage, freshness | read |
| `doddle.tool.v1.dbt.semanticLayerQuery` | Semantic Layer queries | read |
| `doddle.tool.v1.dbt.getJobRun` | job run status and artifacts | read |

**Read-only by design.** The dbt CLI toolset (`dbt run`, `dbt build`, `dbt test`) mutates the
warehouse and is intentionally **not** bound. Promote it deliberately: add
`doddle.tool.v1.dbt.runCommand`, set `"writes": true` in `config.json`, and gate it in the
blueprint.

## Verified notes (2026-11)

- Remote (dbt-hosted) MCP endpoint: `https://cloud.getdbt.com/api/ai/v1/mcp/` (OAuth beta, or `Authorization: Bearer <PAT>` plus `x-dbt-prod-environment-id` / `x-dbt-dev-environment-id` / `x-dbt-user-id`).
- Write surface declared but **not bound** by any blueprint: `trigger_job_run`, `retry_job_run`, `cancel_job_run`, and the self-hosted dbt CLI (`run` / `build` / `test`).
- **Dry-run levers:** `execute_sql` is hard-enforced to a single read-only `SELECT`; `x-dbt-disable-tools` can disable job-run tools; `DISABLE_ADMIN_API` / `DBT_MCP_ENABLE_<TOOLSET>` give an allowlist; `compile` / `parse` never write to the warehouse.
## Setup

```bash
export DBT_PROJECT_DIR="/path/to/dbt/project"
export DBT_PATH="/path/to/dbt/executable"
export DBT_HOST="https://your-account.cloud.getdbt.com"
export DBT_TOKEN="<service token>"
```

## Used By

- `revops-data-infrastructure` (doddle-revops-skills, model/document/test coverage)
