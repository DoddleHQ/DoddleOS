# Segment

> Segment (Twilio) customer-data platform — **no first-party MCP server**. Read this before
> connecting anything.

## Status

As of **2026-10** Segment has not published an official MCP server, and no Twilio-published MCP
package exists for it. Repos claiming to be an "official Segment MCP" do not exist.

| Option | Hosting | Auth | Notes |
|--------|---------|------|-------|
| `mcp-segment` (npm, community, April 2026) | Self-hosted | Your Segment workspace token | Lists sources/destinations, schemas, volumes, audiences, tracking plans. Cannot trigger syncs or create audiences. |
| Composio / StackOne / Pipedream / Activepieces | Hosted | OAuth | Segment as one connector among many; vendor-managed auth and audit trail |
| Wrap Segment's Tracking API yourself | Self-hosted | Source write key / workspace token | `POST /v1/track`, `POST /v1/identify` — full control, you own the server |

> **Verify the publisher** before handing a workspace token to a community server. These servers
> can read and change your Segment data.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.segment.listSources` | source listing | read |
| `doddle.tool.v1.segment.listDestinations` | destination listing | read |
| `doddle.tool.v1.segment.getSchemas` | event schema/property definitions | read |
| `doddle.tool.v1.segment.getVolumes` | data volume by source/destination/event | read |
| `doddle.tool.v1.segment.trackEvent` | server-side `track` | **write** |
| `doddle.tool.v1.segment.identifyUser` | server-side `identify` | **write** |

**Write-gated.** `trackEvent` and `identifyUser` write into your customer data. Gate them, and
never use them to inject events you did not earn.

## Setup

```bash
export SEGMENT_ACCESS_TOKEN="<workspace access token>"
export SEGMENT_WORKSPACE_SLUG="your-workspace"
```

## Used By

- `revops-pql-scoring` (doddle-revops-skills) — prefer RudderStack or Segment's own export for
  product events; the write tools are for backfills, not live scoring.
