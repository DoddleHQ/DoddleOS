# Tool Namespace

All executable tools are addressed as:

```
doddle.tool.v1.<server>.<tool>
```

## Rules

1. `<server>` MUST equal an integration name in `registry/integrations/<server>/config.json`.
2. `<tool>` is the MCP server's tool name (camelCase preserved, e.g. `getSearchAnalytics`).
3. Blueprints bind tools with `required: true|false` + `fallback:` (usually `manual_review`).
4. Missing/unconfigured tools surface as ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate.
5. New servers land as **stubs** first — see `registry/integrations/_registry.md` promotion path.

## Examples

| ID | Server | Data |
|----|--------|------|
| `doddle.tool.v1.ga4.getReport` | google-analytics | Sessions, funnels |
| `doddle.tool.v1.gsc.getSearchAnalytics` | google-search-console | Queries, CTR |
| `doddle.tool.v1.gbp.listReviews` | google-business-profile (stub) | Reviews |
| `doddle.tool.v1.stripe.getMrr` | stripe (stub) | MRR movement |
