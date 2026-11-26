# MCP Integrations Registry

> Central catalog of all MCP server integrations for agentic task execution

## Quick Reference

| Service | Category | Type | Tools | Status |
|---------|----------|------|-------|--------|
| [6sense](./6sense/) | Intent & Signals | Remote | 7 | ✅ Active |
| [apollo](./apollo/) | Enrichment & Outreach | Remote | 5 | ✅ Active (write-gated) |
| [asana](./asana/) | Existing (see table) | npm | 12 | ✅ Active |
| [bigquery](./bigquery/) | Warehouse | npm | 8 | ✅ Active |
| [clay](./clay/) | Enrichment & Outreach | Remote | 4 | ✅ Active (write-gated) |
| [clearbit](./clearbit/) | Enrichment & Outreach | Remote | 1 | ⚠️ Deprecated |
| [crosspost](./crosspost/) | Existing (see table) | npm | 3 | ✅ Active |
| [dataforseo](./dataforseo/) | Existing (see table) | npm | 50 | ✅ Active |
| [dbt](./dbt/) | Data Modeling | npm | 6 | ✅ Active |
| [discord](./discord/) | Community | npm | 3 | ⚪ Community |
| [fivetran-activations](./fivetran-activations/) | Reverse ETL | REST | 4 | ✅ Active (write-gated) |
| [gong](./gong/) | Conversation Intelligence | Remote | 9 | ✅ Active |
| [google-analytics](./google-analytics/) | Existing (see table) | npm | 6 | ✅ Active |
| [google-business-profile](./google-business-profile/) | Existing (see table) | custom | 4 | ✅ Active |
| [google-search-console](./google-search-console/) | Existing (see table) | npm | 6 | ✅ Active |
| [hightouch](./hightouch/) | Reverse ETL | Remote | 12 | ✅ Active (write-gated) |
| [hubspot](./hubspot/) | Existing (see table) | Remote | 15 | ✅ Active |
| [line](./line/) | Existing (see table) | npm | 5 | ✅ Active |
| [make](./make/) | Automation | Remote | 8 | ✅ Active (write-gated) |
| [meta-ads](./meta-ads/) | Existing (see table) | npm | 25 | ✅ Active |
| [notion](./notion/) | Existing (see table) | npm | 15 | ✅ Active (write-gated) |
| [rudderstack](./rudderstack/) | Customer Data | Remote | 10 | ✅ Active (write-gated) |
| [segment](./segment/) | Customer Data | npm | 6 | ✅ Active (write-gated) |
| [semrush](./semrush/) | Existing (see table) | Remote | 20 | ✅ Active |
| [sensortower](./sensortower/) | Existing (see table) | custom | 29 | ✅ Active |
| [slack](./slack/) | Existing (see table) | npm | 10 | ✅ Active (write-gated) |
| [snowflake](./snowflake/) | Warehouse | Remote | 6 | ✅ Active (write-gated) |
| [stripe](./stripe/) | Existing (see table) | Remote | 4 | ✅ Active (write-gated) |
| [tiktok](./tiktok/) | Existing (see table) | npm | 5 | ✅ Active |
| [twitter](./twitter/) | Existing (see table) | npm | 8 | ✅ Active |
| [zalo](./zalo/) | Existing (see table) | custom | 0 | ✅ Active |
| [zapier](./zapier/) | Automation | Remote | 5 | ✅ Active (write-gated) |
| [zoominfo](./zoominfo/) | Conversation Intelligence | Remote | 5 | ✅ Active |

---

## By Category

### Warehouse

- **[bigquery](./bigquery/)** — 8 tools · npm · auth: bot/token

- **[snowflake](./snowflake/)** (write-gated) — 6 tools · Remote · auth: oauth-or-pat


### Data Modeling

- **[dbt](./dbt/)** — 6 tools · npm · auth: bot/token


### Customer Data

- **[rudderstack](./rudderstack/)** (write-gated) — 10 tools · Remote · auth: oauth

- **[segment](./segment/)** (write-gated) — 6 tools · npm · auth: bot/token


### Intent & Signals

- **[6sense](./6sense/)** — 7 tools · Remote · auth: oauth


### Enrichment & Outreach

- **[apollo](./apollo/)** (write-gated) — 5 tools · Remote · auth: oauth-or-api-key

- **[clay](./clay/)** (write-gated) — 4 tools · Remote · auth: oauth-dcr

- **[clearbit](./clearbit/)** — 1 tools · Remote · auth: remote


### Conversation Intelligence

- **[gong](./gong/)** — 9 tools · Remote · auth: oauth

- **[zoominfo](./zoominfo/)** — 5 tools · Remote · auth: remote


### Reverse ETL

- **[fivetran-activations](./fivetran-activations/)** (write-gated) — 4 tools · REST · auth: rest

- **[hightouch](./hightouch/)** (write-gated) — 12 tools · Remote · auth: oauth (workspace, gated)


### Automation

- **[make](./make/)** (write-gated) — 8 tools · Remote · auth: oauth-or-api-key

- **[zapier](./zapier/)** (write-gated) — 5 tools · Remote · auth: oauth


### Community

- **[discord](./discord/)** — 3 tools · npm · auth: bot/token

---

## By Market

### 🇺🇸 US Market
| Platform | Integration | Priority |
|----------|-------------|----------|
| Google Analytics | ✅ Ready | High |
| Google Search Console | ✅ Ready | High |
| Meta Ads | ✅ Ready | High |
| HubSpot | ✅ Ready | High |
| Semrush | ✅ Ready | High |
| Twitter/X | ✅ Ready | Medium |
| Slack | ✅ Ready | Medium |

### 🇻🇳 Vietnam Market
| Platform | Integration | Priority |
|----------|-------------|----------|
| Zalo | ⚠️ Need Custom | Critical |
| Facebook (Meta Ads) | ✅ Ready | High |
| TikTok | ✅ Ready | High |
| Google | ✅ Ready | High |

### 🇯🇵 Japan Market
| Platform | Integration | Priority |
|----------|-------------|----------|
| LINE | ✅ Ready | Critical |
| Twitter/X | ✅ Ready | High |
| TikTok | ✅ Ready | Medium |

---

## Environment Variables

```bash
# App Intelligence
export SENSOR_TOWER_API_TOKEN="xxx"

# SEO
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export SEMRUSH_API_KEY="xxx"
export DATAFORSEO_LOGIN="xxx"
export DATAFORSEO_PASSWORD="xxx"

# Analytics
export GA4_PROPERTY_ID="properties/xxx"

# Advertising
export META_ACCESS_TOKEN="xxx"

# CRM
export HUBSPOT_ACCESS_TOKEN="pat-xxx"

# Communication
export SLACK_BOT_TOKEN="xoxb-xxx"

# Project Management
export NOTION_API_KEY="secret_xxx"
export ASANA_ACCESS_TOKEN="xxx"

# Social Media
export TWITTER_API_KEY="xxx"
export TWITTER_API_SECRET="xxx"
export TWITTER_ACCESS_TOKEN="xxx"
export TWITTER_ACCESS_SECRET="xxx"

# Regional
export LINE_CHANNEL_ACCESS_TOKEN="xxx"
export ZALO_OA_ACCESS_TOKEN="xxx"

# Local & Billing (stubs - MCP servers pending)
export GBP_ACCESS_TOKEN="xxx"
export GBP_ACCOUNT_ID="accounts/xxx"
export STRIPE_SECRET_KEY="sk_xxx"
```

---

## Write-capable servers

Servers whose `config.json` sets `"writes": true` can mutate an external system. Any blueprint
that calls them **must** place a `gate` node immediately before the write node — the runner
refuses to schedule a write without an approved decision (`write_without_gate`, see
`doddle-core/spec/harness-cli-resolver.md` §6).

| Server | Write tool IDs | Gate used by |
|--------|----------------|--------------|
| `slack` | `doddle.tool.v1.slack.sendMessage` | `approve_alert`, `approve_share` |
| `stripe` | `doddle.tool.v1.stripe.recordMeterEvent`, `doddle.tool.v1.stripe.updateSubscription` | `approve_billing` |
| `notion` | `doddle.tool.v1.notion.createPage` | `approve_publish` |

Read-only servers (analytics, CRM reads, ad platforms, registries) need no gate.

---

## CLI registry

Deterministic offline toolkits are registered separately, in `doddle-core/registry/cli/`, and
resolved through `doddle.tool.cli.<cli>` nodes (see
`doddle-core/spec/harness-cli-resolver.md`).

| CLI | Path | Runtime | Pack | Backs |
|-----|------|---------|------|-------|
| `drev` | `doddle-revops-skills/scripts/drev` | python3 | `doddle.revops.*` | 12 revenue-data skills |
| `dgtm` | `doddle-gtm-skills/scripts/dgtm` | python3 | `doddle.gtm.*` | 32 GTM skills |

---

## Adding New Integration

1. Create folder: `integrations/[service-name]/`
2. Add `index.md` - docs, use cases, examples
3. Add `config.json` - MCP server config (set `"writes": true` if it can mutate)
4. Update this `_registry.md`
5. Add to `.mcp.json`

---

## Stub → Live Promotion Path

New integrations land as **stubs** (config reserved, MCP server pending). Skills bind stub tool IDs (`doddle.tool.v1.<server>.*`, `required: false`, `fallback: manual_review`) and show ⚠️ NOT AVAILABLE until live.

Promote stub → ✅ Active when ALL hold:
1. MCP server exists (npm package or remote endpoint reachable)
2. `config.json` validated (command/args/env smoke-tested)
3. At least 1 skill blueprint exercises each tool without fallback
4. `index.md` updated (remove stub notice, document auth + quotas)
5. `scripts/validate-skills.py` passes + registry row flipped to ✅ Active

Current stubs: `google-business-profile`, `sensortower`. `stripe` now points at the hosted Stripe MCP server (`https://mcp.stripe.com`) and only needs an agent API key or OAuth.

### config.json Template

```json
{
  "name": "service-name",
  "description": "Service description",
  "type": "npm|custom|remote",
  "command": "npx",
  "args": ["-y", "package-name"],
  "env": {
    "API_KEY": "${SERVICE_API_KEY}"
  },
  "capabilities": {
    "tools": 10,
    "categories": ["category1", "category2"]
  },
  "source": {
    "npm": "https://npmjs.com/package/xxx",
    "github": "https://github.com/xxx"
  }
}
```
