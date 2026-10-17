# MCP Integration Guide & Tool Registry

Skills may reference external data only through tool IDs on this registry. **Never invent a
tool ID.** The toolkit CLI (`doddle.tool.v1.cli.dseo`) covers everything deterministic; MCP tools
cover live, property-specific data.

## Registry

| Tool ID | Provides | Typical skills | Required |
|---------|----------|----------------|----------|
| `doddle.tool.v1.cli.dseo` | Deterministic citability/technical/schema/robots/llms.txt evidence | geo-*, seo-audit, seo-technical | yes (bundled) |
| `doddle.tool.v1.gsc.query` | Search Console performance: queries, pages, CTR, position, indexation | seo-reporting, seo-audit, seo-onpage | no |
| `doddle.tool.v1.ga4.getReport` | Analytics: sessions, conversions, AI-referral traffic | geo-monitor, seo-reporting, analytics | no |
| `doddle.tool.v1.semrush.domain` | Keyword volume/difficulty, domain overview | seo-keyword-research, seo-competitor | no |
| `doddle.tool.v1.dataforseo.serp` | SERP features, PAA, live rankings | seo-sxo, seo-competitor, seo-keyword-research | no |
| `doddle.tool.v1.ahrefs.backlinks` | Backlink profile, referring domains, anchors | seo-backlinks, seo-digital-pr | no |
| `doddle.tool.v1.hubspot.contacts` | CRM segments and lifecycle stage | seo-strategy, reporting | no |
| `doddle.tool.v1.notion.pages` | Planning docs, briefs, roadmaps | seo-strategy, seo-content-brief | no |

## Rules

1. **Deterministic first.** If `dseo` can compute it, do not ask an MCP tool for it.
2. **Optional tools are optional.** Every MCP tool in a blueprint is `required: false` with
   `fallback: manual_review`. Their absence degrades the report, it does not fail the skill.
3. **Unavailable ⇒ say so.** Print `⚠️ NOT AVAILABLE — configure <tool>` and name the setup.
   Never estimate a substitute.
4. **Live numbers are `live` class.** Tag them. They are not part of the deterministic score.
5. **Never put API keys on a command line** or in the conversation. Read them from the
   environment or the harness's secret store.

## Fallback behaviour by tool

| Tool missing | What to do |
|--------------|------------|
| `gsc.query` | Report organic performance as NOT AVAILABLE; do not substitute third-party estimates |
| `ga4.getReport` | Report sessions/conversions as NOT AVAILABLE; still run deterministic audit |
| `semrush.domain` | Ask the user for target keywords; do not invent search volume |
| `dataforseo.serp` | Use the deterministic audit; note SERP-feature checks were skipped |
| `ahrefs.backlinks` | Run `dseo` technical audit; mark backlink section NOT AVAILABLE |
