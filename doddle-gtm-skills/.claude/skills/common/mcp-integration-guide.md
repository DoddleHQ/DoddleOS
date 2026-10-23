# MCP Integration Guide & Tool Registry

Skills may reference external data only through tool IDs on this registry. **Never invent a
tool ID.** The toolkit CLI (`doddle.tool.cli.dgtm`) covers everything deterministic; MCP tools
cover live, account-specific data.

## Registry

| Tool ID | Provides | Typical skills | Required |
|---------|----------|----------------|----------|
| `doddle.tool.cli.dgtm` | Funnel math, unit economics, pricing, market sizing, weighted scoring, pipeline audit, frameworks | all `gtm-*` | yes (bundled) |
| `doddle.tool.v1.hubspot.deals` | Deals, stages, amounts, close dates | gtm-pipeline-analytics, gtm-forecasting, gtm-win-loss, gtm-expansion | no |
| `doddle.tool.v1.salesforce.opportunities` | Opportunities and stage history (alt CRM) | gtm-pipeline-analytics, gtm-forecasting | no |
| `doddle.tool.v1.gong.calls` | Recorded calls, transcripts, talk ratios | gtm-win-loss, gtm-battlecards, gtm-sales-narrative | no |
| `doddle.tool.v1.clearbit.company` | Firmographic enrichment for target accounts | gtm-icp, gtm-abm, gtm-segmentation | no |
| `doddle.tool.v1.ga4.getReport` | Site traffic and conversion by source | gtm-demand-gen, gtm-plg, gtm-reporting | no |
| `doddle.tool.v1.linkedin.ads` | LinkedIn ad account: campaigns, spend, results | gtm-demand-gen, gtm-outbound | no |
| `doddle.tool.v1.notion.pages` | Planning docs, briefs, GTM plans | gtm-strategy, gtm-launch, gtm-enablement | no |

CRM exports (HubSpot, Salesforce, Pipedrive) are ingested through `dgtm audit` as a file — no
MCP tool needed, and no scraping.

## Rules

1. **Deterministic first.** If `dgtm` can compute it, do not ask an MCP tool for it.
2. **Optional tools are optional.** Every MCP tool in a blueprint is `required: false` with
   `fallback: manual_review`. Their absence degrades the report, it does not fail the skill.
3. **Unavailable ⇒ say so.** Print `⚠️ NOT AVAILABLE — configure <tool>` and name the setup.
   Never estimate a substitute.
4. **Live numbers are `live` class.** Tag them. They are not part of the deterministic score.
5. **Never put API keys on a command line** or in the conversation. Read them from the
   environment or the harness's secret store.
6. **Read-only.** No skill writes to the CRM or sends anything.

## Fallback behaviour by tool

| Tool missing | What to do |
|--------------|------------|
| `hubspot.deals` / `salesforce.opportunities` | Ask the user for a deal export file; audit that instead |
| `gong.calls` | Use win/loss interviews and notes the user supplies; do not invent call data |
| `clearbit.company` | Ask the user for the account list and firmographics |
| `ga4.getReport` | Report site conversions as NOT AVAILABLE; still proceed with the rest |
| `linkedin.ads` | Report ad performance as NOT AVAILABLE; plan from strategy only |
| `notion.pages` | Keep planning output inline |
