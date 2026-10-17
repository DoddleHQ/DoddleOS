# Skills Matrix

30 skills, 5 agents. Every skill is `<name>` at `.claude/skills/<name>/` with `SKILL.md` +
`blueprint.yaml`; `id: doddle.seo.<name>`. "Toolkit" lists the `dseo` commands the skill runs;
"advisory" means no deterministic script and the skill states its inputs.

## GEO / AI search (10)

| Skill | Toolkit / basis | Agent | Purpose |
|-------|-----------------|-------|---------|
| `geo-audit` | `dseo audit` | geo-specialist | Whole-site GEO score, ranked + sequenced fixes |
| `geo-citability` | `dseo score`, `dseo citability` | geo-specialist | One page's quotability for AI answers |
| `geo-crawlers` | `dseo robots` | geo-specialist | AI-crawler access: search vs training vs user |
| `geo-llmstxt` | `dseo llmstxt [--generate]` | geo-specialist | Validate or draft `/llms.txt` |
| `geo-schema` | `dseo schema` | schema-architect | Entity markup for AI (Organization/sameAs/Article) |
| `geo-report` | `dseo report` | geo-specialist | Client-ready GEO deliverable |
| `geo-brand-entity` | `dseo schema` + manual checklist | entity-strategist | Entity resolution and `sameAs` |
| `geo-platform` | `dseo score` + `dseo robots` | geo-specialist | Per-engine optimisation (ChatGPT, Perplexity, AIO, Copilot, Claude, Gemini) |
| `geo-monitor` | live `ga4.getReport` + advisory sampling | geo-specialist | AI-referral traffic and cited pages |
| `geo-content` | `dseo citability` + editorial | geo-specialist | Rewrite for quotability |

## SEO (20)

| Skill | Toolkit / basis | Agent | Purpose |
|-------|-----------------|-------|---------|
| `seo-audit` | `dseo audit` | technical-auditor | Full classic SEO audit |
| `seo-technical` | `dseo technical`, `dseo audit` | technical-auditor | Indexability, canonical, rendering, hygiene |
| `seo-onpage` | `dseo technical`, `dseo score` | seo-strategist | Intent, titles, metas, headings |
| `seo-schema` | `dseo schema` | schema-architect | Rich-result structured data |
| `seo-internal-linking` | `dseo audit` + advisory | technical-auditor | Hub-spoke architecture, anchors, orphans |
| `seo-hreflang` | `dseo technical` + advisory | technical-auditor | International / hreflang |
| `seo-keyword-research` | live `semrush.domain`, `dataforseo.serp` | seo-strategist | Intent, clustering, URL decisions |
| `seo-topical-map` | advisory | seo-strategist | Clusters and topical authority |
| `seo-content-brief` | advisory + live SERP | seo-strategist | Ready-to-write briefs |
| `seo-competitor` | `dseo audit` + live tools | seo-strategist | Gap analysis and comparison pages |
| `seo-backlinks` | live `ahrefs.backlinks` | seo-strategist | Profile health and prospecting |
| `seo-digital-pr` | advisory | seo-strategist | Linkable assets and earned coverage |
| `seo-local` | `dseo schema` + advisory | seo-strategist | GBP, NAP, local intent |
| `seo-ecommerce` | `dseo schema`, `dseo audit` | seo-strategist | Category/PDP, facets, variants |
| `seo-strategy` | advisory + notion/hubspot | seo-strategist | Roadmap and prioritisation |
| `seo-reporting` | live `gsc.query`, `ga4.getReport` | seo-strategist | Deltas, winners/losers, forecasts |
| `seo-sxo` | live `dataforseo.serp` + `dseo score` | seo-strategist | SERP features and CTR |
| `seo-programmatic` | `dseo audit` + advisory | technical-auditor | Pages at scale, quality gates |
| `seo-migration` | `dseo technical`/`audit` + advisory | technical-auditor | Redirects and post-launch checks |
| `seo-geo-fundamentals` | shared reference | geo-specialist | Orientation and navigation |

## Agents

| Agent | Focus |
|-------|-------|
| `geo-specialist` | GEO/AEO: citability, crawlers, entities, platforms, llms.txt |
| `seo-strategist` | Intent, clusters, briefs, prioritisation, reporting |
| `technical-auditor` | Crawl, rendering, indexability, architecture, migration |
| `schema-architect` | JSON-LD design, validation, entity graphs |
| `entity-strategist` | Brand/entity authority and `sameAs` |

## Shared references (`.claude/skills/common/`)

`response-contract.md`, `data-reliability.md`, `fundamentals.md`, `scoring-methodology.md`,
`mcp-integration-guide.md`.
