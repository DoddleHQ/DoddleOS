# BigQuery

> BigQuery over MCP, two ways: the open-source **MCP Toolbox for Databases** (self-hosted) or
> Google's **fully managed remote BigQuery MCP server** (preview, January 2026).

## Option A — MCP Toolbox for Databases (recommended)

| Field | Value |
|-------|-------|
| Command | `npx -y @toolbox-sdk/server --prebuilt bigquery --stdio` |
| Binary | `https://storage.googleapis.com/mcp-toolbox-for-databases/VERSION/<os>/<arch>/toolbox` (v0.7.0+) |
| Auth | Application Default Credentials |

Prebuilt BigQuery tools: `list_dataset_ids`, `get_dataset_info`, `list_table_ids`,
`get_table_info`, `execute_sql`, `forecast`, `analyze_contribution`, `search_catalog`,
`ask_data_insights`.

The same toolbox also serves **Snowflake**, Postgres, MySQL, Oracle, MongoDB, ClickHouse and
more — a single server for a whole data estate.

## Option B — managed remote BigQuery MCP server

| Field | Value |
|-------|-------|
| Endpoint | `https://bigquery.googleapis.com/mcp` |
| Auth | Google OAuth |
| Tools | `list_dataset_ids`, `get_dataset_info`, `list_table_ids`, `get_table_info`, `execute_sql_readonly`, `execute_sql`, `get_query_results`, `cancel_job`, `get_job` |

Enable it with `gcloud beta services mcp enable bigquery.googleapis.com --project=${BIGQUERY_PROJECT}`.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.bigquery.listDatasets` | `list_dataset_ids` | read |
| `doddle.tool.v1.bigquery.listTables` | `list_table_ids` | read |
| `doddle.tool.v1.bigquery.getTableInfo` | `get_table_info` | read |
| `doddle.tool.v1.bigquery.executeSqlReadonly` | `execute_sql_readonly` / read-only `execute_sql` | read |

**Read-only by design.** `execute_sql` (managed server) can run `INSERT`/`UPDATE`/`DELETE` and is
intentionally unbound. Use `execute_sql_readonly` for analysis, and prefer in-warehouse
computation (`AI.FORECAST`, `AI.KEY_DRIVERS`, `ML.PREDICT`) over exporting rows locally.

## Setup

```bash
export BIGQUERY_PROJECT="your-gcp-project-id"
export BIGQUERY_LOCATION="US"
export BIGQUERY_READONLY="true"
```

## Used By

- `revops-data-infrastructure` (doddle-revops-skills)
- `revops-attribution` (cohort SQL templates)
