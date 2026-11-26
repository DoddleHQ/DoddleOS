# Clearbit (deprecated)

> **DEPRECATED.** Clearbit was acquired by HubSpot (Dec 2023), rebranded **Breeze Intelligence**
> (Sept 2024), and that name was **retired in 2026** — the capability is now *data enrichment*
> built into HubSpot Smart CRM. **Clearbit has no MCP server of its own.**

## Connection

| Field | Value |
|-------|-------|
| Standalone endpoint | **none** — the `url` field in `config.json` is `null` on purpose |
| Served by | `hubspot` — https://mcp.hubspot.com (enrichment / buyer intent) |
| Intent alternative | `6sense` — https://api.6sense.com/mcp (read-only intent and account insight) |
| Status | deprecated — kept so existing `doddle.tool.v1.clearbit.company` bindings keep working |

## Tools

| Upstream tool | Source |
|---------------|--------|
| HubSpot data enrichment (firmographics) | HubSpot Smart CRM |
| HubSpot buyer intent (HubSpot Credits metered) | HubSpot Smart CRM |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.clearbit.company` | HubSpot enrichment / intent lookup | read — deprecated id, kept for compatibility |

**Read-only.** The mapped capability is a read; nothing here mutates data, so no approval gate
is required. Enabling intent signals is a HubSpot-side action, not this tool — it is metered in
HubSpot Credits (10 credits per company per month to enable / monitor intent signals, 50 credits
per month per custom signal). Data enrichment itself consumes no HubSpot Credits.

## Setup

There is no Clearbit setup — the product no longer exists standalone.

1. For enrichment: a paid HubSpot plan. Data enrichment is included and consumes no HubSpot
   Credits.
2. For buyer intent: prefer `6sense` (read-only intent, keyword and account insight), or use
   HubSpot buyer intent and accept the Credit metering.

## Used By

- `gtm-icp`, `gtm-abm`, `gtm-segmentation` (doddle-gtm-skills) — already bind
  `doddle.tool.v1.clearbit.company`; migrate them to `hubspot` / `6sense` / `apollo` /
  `zoominfo` enrichment ids
- `revops-ai-sdr` (doddle-revops-skills) — enrichment evidence lane
