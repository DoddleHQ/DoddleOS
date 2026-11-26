# clearbit

> DEPRECATED — Clearbit is now HubSpot data enrichment; use hubspot (enrichment/intent) or 6sense

## Connection

| Field | Value |
|-------|-------|
| Status | **Deprecated** — no server endpoint exists |

## Upstream tools

`HubSpot data enrichment`, `HubSpot buyer intent`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.clearbit.company` | `HubSpot enrichment/intent lookup` | read (HubSpot) — DEPRECATED id, kept for compatibility |

**Read-only.** No tool in this entry mutates external data, so it needs no approval gate.

## Setup

_No setup — this entry is a pointer to another integration._

### Notes

- Clearbit was acquired by HubSpot (Dec 2023), became Breeze Intelligence (Sept 2024), and the Breeze Intelligence name was retired in 2026 — the capability is now data enrichment inside HubSpot Smart CRM.
- Standalone Clearbit subscriptions stopped (April 2025); free Clearbit tools sunset 2025-04-30; the free Logo API sunset 2025-12-01.
- Clearbit has no MCP server of its own. Map doddle.tool.v1.clearbit.company onto HubSpot data enrichment + buyer intent (HubSpot Credits metered: 10 credits per company per month for intent signals).
- For predictive buying stage and keyword intent use 6sense instead.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
