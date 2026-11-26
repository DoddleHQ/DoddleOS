# fivetran-activations

> Fivetran Activations (formerly Census) reverse ETL — REST/Terraform today; Fivetran platform MCP covers context and read-only SQL

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.fivetran.com/mcp` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`Agent Context MCP (read-only SQL + semantics)`, `Activations REST API`, `Activations Terraform provider`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.fivetran-activations.queryWarehouse` | `Agent Context MCP read-only SQL` | read |
| `doddle.tool.v1.fivetran-activations.listActivations` | `Activations REST API (out of MCP)` | read (REST) |

**Read-only.** No tool in this entry mutates external data, so it needs no approval gate.

## Setup

- Fivetran account (Activations lives inside the Fivetran platform)

### Notes

- Census was acquired by Fivetran and is now Fivetran Activations — Census is no longer a standalone product.
- Fivetran hosts an Agent Context MCP exposing semantic definitions and read-only warehouse SQL, plus a self-hosted MCP repo for platform operations; neither is Activations-specific.
- There is NO Activations-native MCP server: create and manage reverse-ETL syncs through the Activations REST API or the Terraform provider.
- Activations syncs warehouse models to 200+ destinations; Audience Hub provides governed segments.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
