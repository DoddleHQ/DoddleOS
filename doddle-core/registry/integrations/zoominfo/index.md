# ZoomInfo

> Official ZoomInfo MCP server for the **GTM.AI layer** — verified B2B intelligence, buying
> signals and the GTM Context Graph. Chorus is now **ZoomInfo Conversation Intelligence**.

## Connection

| Field | Value |
|-------|-------|
| Transport | HTTP (remote MCP) |
| Endpoint | issued per ZoomInfo account — not published in this registry (`url` is `null` on purpose) |
| Auth | per account |
| Coverage | 500M+ verified contacts, 100M+ verified companies |

## Tools

| Upstream tool | Provides |
|---------------|----------|
| verified contact search | 500M+ B2B contacts |
| verified company search | 100M+ B2B companies |
| buying signals | intent / trigger signals |
| GTM Context Graph | connected account context |
| Conversation Intelligence (formerly Chorus) | call, meeting and email capture; winning behaviors; deal momentum; churn risk |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.zoominfo.searchContacts` | verified contact search | read |
| `doddle.tool.v1.zoominfo.searchCompanies` | verified company search | read |
| `doddle.tool.v1.zoominfo.getBuyingSignals` | buying signals | read |
| `doddle.tool.v1.zoominfo.getContextGraph` | GTM Context Graph | read |
| `doddle.tool.v1.zoominfo.getConversationInsights` | Conversation Intelligence (formerly Chorus) | read |

**Read-only.** The registered surface is intelligence retrieval — no mutating tool is bound, so
no approval gate is required.

## Setup

1. ZoomInfo account with GTM.AI access.
2. Conversation Intelligence access for call / meeting / email insight.
3. Obtain the MCP endpoint URL and credentials from ZoomInfo for your account.

## Used By

- `revops-call-intelligence` (doddle-revops-skills) — binds
  `doddle.tool.v1.zoominfo.getConversationInsights`
- Candidate lane for `gtm-icp`, `gtm-abm`, `gtm-outbound` (doddle-gtm-skills) — external
  intelligence replacement for the deprecated `doddle.tool.v1.clearbit.company` — not yet bound
- Feeds HubSpot's Breeze Prospecting Agent (public beta) as a third-party data provider
