# apollo

> Apollo prospecting and enrichment — official MCP server

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.apollo.io/mcp` |
| Transport | http |
| Auth | oauth-or-api-key |

## Upstream tools

`apollo_mixed_people_api_search`, `enrichment`, `sequence creation`, `one-off email`, `task creation`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.apollo.searchPeople` | `apollo_mixed_people_api_search` | read (no credits) |
| `doddle.tool.v1.apollo.enrichPeople` | `people enrichment` | write (consumes credits) |
| `doddle.tool.v1.apollo.createSequence` | `create/enroll sequence` | write |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Apollo account with access to the records you want
- Credits available for enrichment
- AI model training turned off in your client

### Notes

- OAuth 2.0 for interactive clients; headless clients send a MASTER key in the X-Api-Key header (scoped keys are rejected with 403 API_INACCESSIBLE).
- People search reads and consumes no credits; company search, enrichment, validation and research consume credits.
- Apollo prohibits AI model training on its data.
- Destructive bulk delete is not supported.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
