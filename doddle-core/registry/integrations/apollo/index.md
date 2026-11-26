# Apollo

> Official Apollo MCP server — people and company search, enrichment, validation, research.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.apollo.io/mcp` |
| Transport | Streamable HTTP |
| Auth | OAuth 2.0 (interactive) **or** `X-Api-Key` header with a MASTER key |
| Registry | `io.github.apolloio/apollo-mcp` v0.1.1 |

Headless clients must send a **MASTER** key in the `X-Api-Key` header — scoped keys are
rejected with `403 API_INACCESSIBLE`.

## Tools

| Upstream tool | Credits |
|---------------|---------|
| `apollo_mixed_people_api_search` | none (pure read) |
| company search | consumed |
| enrichment | consumed |
| validation | consumed |
| research | consumed |

Destructive bulk delete is **not** supported. Apollo prohibits AI model training on its data.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.apollo.searchPeople` | People search action (`apollo_mixed_people_api_search`) | read (no credits) |
| `doddle.tool.v1.apollo.searchCompanies` | company search | read (credits) |
| `doddle.tool.v1.apollo.enrichPeople` | enrichment | **write** (credits) |
| `doddle.tool.v1.apollo.validateRecords` | validation | read (credits) |
| `doddle.tool.v1.apollo.research` | research | read (credits) |

**Write-gated.** `enrichPeople` writes enriched fields onto the enriched records in Apollo and
burns credits, so a blueprint must place a `gate` node before it (for example
`approve_enrichment`), keep the tool `required: false` with `fallback: manual_review`, and
preview the target list first. Everything else in this entry is a read.

## Verified notes (2026-11)

- Apollo publishes **Actions, not fixed tool ids**. Pin behaviour to `tools/list` and re-connect after a rollout — an API-key connection gets no "new tools available" signal.
- **Dry-run:** create sequences inactive for review, draft email content before pushing, and set client approval to "Approval required" for credit-consuming actions.
## Setup

1. Apollo account.
2. Interactive: authorize the MCP client with OAuth 2.0.
   Headless: set `APOLLO_API_KEY` to a **MASTER** key (scoped keys fail with 403).
3. Keep a credit balance for company search, enrichment, validation and research.

```bash
export APOLLO_API_KEY="<MASTER key>"
```

## Used By

- `revops-ai-sdr` (doddle-revops-skills) — binds `doddle.tool.v1.apollo.searchPeople` and the gated
  `doddle.tool.v1.apollo.enrichPeople` (`approve_enrichment`)
- Candidate lane for `gtm-icp`, `gtm-abm`, `gtm-segmentation` (doddle-gtm-skills), which today
  bind the deprecated `doddle.tool.v1.clearbit.company` id
