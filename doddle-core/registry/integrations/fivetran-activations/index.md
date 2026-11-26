# Fivetran Activations

> Census was acquired by Fivetran and is now **Fivetran Activations** — Census is no longer a
> standalone product. **No Activations-native MCP server exists**: the reverse-ETL sync path
> runs on the Activations REST API or the Terraform provider today.

## Connection

| Field | Value |
|-------|-------|
| MCP endpoint | none — Activations has no MCP server (the `url` field in `config.json` is `null` on purpose) |
| Activations surfaces | REST API, Terraform provider, Management API, Connect Links |
| Fivetran platform MCP | "Agent Context MCP server" — semantic definitions + READ-ONLY warehouse SQL (not Activations-specific) |
| Self-hosted platform MCP | published by Fivetran in its own GitHub org for platform operations (not Activations-specific) |

## Tools

| Upstream tool | Surface |
|---------------|---------|
| semantic definitions | Agent Context MCP |
| read-only warehouse SQL | Agent Context MCP |
| audiences (Audience Hub) | Activations REST API |
| reverse-ETL sync (200+ destinations) | Activations REST API / Terraform provider |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.fivetran-activations.getSemanticDefinitions` | Agent Context MCP — semantic definitions | read |
| `doddle.tool.v1.fivetran-activations.queryWarehouse` | Agent Context MCP — read-only warehouse SQL | read |
| `doddle.tool.v1.fivetran-activations.listAudiences` | Activations REST API — Audience Hub segments | read |
| `doddle.tool.v1.fivetran-activations.triggerSync` | Activations REST API / Terraform provider — reverse-ETL sync | **write** |

These ids are **not** MCP tool calls today — the first two map to Fivetran's platform MCP and
the last two to the Activations REST API / Terraform provider. That split is deliberate: it
keeps the skill bindings stable while the sync path stays on the supported API.

**Write-gated.** `triggerSync` starts data movement from the warehouse to a destination. A
blueprint must place a `gate` node immediately before it (for example `approve_sync`), keep the
tool `required: false` with `fallback: manual_review`, and show the source model, destination
and audience before asking for approval.

## Setup

1. Fivetran account with Activations enabled.
2. Activations REST API or Terraform provider credentials for the sync path.
3. Warehouse model and destination connection (200+ destinations supported).
4. Audience Hub for governed segments.

## Used By

- `revops-data-infrastructure` (doddle-revops-skills) — reverse-ETL readiness audit
- Candidate lane for `gtm-segmentation` (doddle-gtm-skills) via Audience Hub — not yet bound
