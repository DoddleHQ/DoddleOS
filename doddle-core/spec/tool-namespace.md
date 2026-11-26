# Tool Namespace

All executable tools are addressed as:

```
doddle.tool.v1.<server>.<tool>     # live MCP server
doddle.tool.cli.<cli>              # deterministic local CLI
```

## Rules

1. `<server>` MUST equal an integration name in `registry/integrations/<server>/config.json`.
2. `<tool>` is the **DoddleOS semantic tool name** for that server. Where a vendor exposes a
   differently named tool, the registry's `index.md` documents the mapping
   (for example `doddle.tool.v1.stripe.recordMeterEvent` → Stripe's generic
   `stripe_api_write` against `POST /v1/billing/meter_events`).
3. `<cli>` MUST equal a CLI registry entry in `registry/cli/<cli>.json` (currently `drev`, `dgtm`).
4. Blueprints bind tools with `required: true|false` + `fallback:` (usually `manual_review`).
5. Missing/unconfigured tools surface as ⚠️ NOT AVAILABLE per data-reliability rules. Never
   fabricate.
6. New servers land as **stubs** first — see `registry/integrations/_registry.md` promotion path.
7. **Write tools are gated.** Any server whose `config.json` sets `"writes": true` exposes a
   `writeTools` list. A blueprint that binds a listed tool MUST place a `gate` node immediately
   before the write node. The runner refuses to schedule an ungated write
   (`write_without_gate` — see `harness-cli-resolver.md` §6).

## Examples

| ID | Server | Data |
|----|--------|------|
| `doddle.tool.v1.ga4.getReport` | google-analytics | Sessions, funnels |
| `doddle.tool.v1.gsc.getSearchAnalytics` | google-search-console | Queries, CTR |
| `doddle.tool.v1.gbp.listReviews` | google-business-profile (stub) | Reviews |
| `doddle.tool.v1.stripe.getMrr` | stripe | MRR movement |
| `doddle.tool.v1.stripe.recordMeterEvent` | stripe | Usage meter event (**write — gated**) |
| `doddle.tool.v1.snowflake.getTableInfo` | snowflake | Warehouse table metadata |
| `doddle.tool.v1.dbt.discover` | dbt | Model metadata and lineage |
| `doddle.tool.v1.bigquery.executeSqlReadonly` | bigquery | Read-only SQL |
| `doddle.tool.v1.rudderstack.listEvents` | rudderstack | Event stream and metrics |
| `doddle.tool.v1.gong.getTranscript` | gong | Call transcript (read-only server) |
| `doddle.tool.cli.drev` | cli registry | Revenue-data toolkit (15 commands) |
| `doddle.tool.cli.dgtm` | cli registry | GTM toolkit (10 commands) |
