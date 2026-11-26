# 6sense

> Official 6sense MCP server — account insights, 6QA trends, keyword and ad performance,
> website activity, segments, people insights. **Read-only**: it cannot modify data.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://api.6sense.com/mcp` |
| Transport | HTTP (remote MCP) |
| Auth | OAuth using existing 6sense credentials — per-user authorization |
| Access control | Honours license + role; RBAC and AI settings control what is exposed |
| Credit limits | Daily / weekly / monthly, per user and per role |

## Tools

| Capability | Covers |
|------------|--------|
| account insights | account-level buying and engagement insight |
| 6QA trend analysis | 6sense Question Answer trends |
| keyword performance | keyword performance and intent |
| ad campaign performance | paid campaign results |
| website activity | website visitor activity |
| account filtering / segments | filtering accounts and building segment views |
| sales account and people insights | account and people insights for sellers |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.6sense.getAccountInsights` | account insights | read |
| `doddle.tool.v1.6sense.getTrendAnalysis` | 6QA trend analysis | read |
| `doddle.tool.v1.6sense.getKeywordIntent` | keyword performance / intent | read |
| `doddle.tool.v1.6sense.getAdCampaignPerformance` | ad campaign performance | read |
| `doddle.tool.v1.6sense.getWebsiteActivity` | website activity | read |
| `doddle.tool.v1.6sense.filterAccounts` | account filtering / segments | read |
| `doddle.tool.v1.6sense.getSalesInsights` | sales account + people insights | read |

**Read-only.** Every operation in this entry reads; nothing mutates 6sense data, so no
approval gate is required. Watch the per-user / per-role credit limits instead — the Keyword
Intent Data API charges 3 credits per newly discovered account (non-matches are free), while
People Search and Lead Scoring consume no credits.

## Verified notes (2026-11)

- OAuth 2.1 with code + PKCE, DCR, per-user consent, single scope `mcp:use`. Protected-resource metadata: `https://api.6sense.com/.well-known/oauth-protected-resource/mcp`.
- Upstream tool names are **not published** — `tools/list` is OAuth-gated (401). Our tool ids are capability-shaped on purpose; pin to the live tool list.
## Setup

1. 6sense account and credentials whose license + role allow MCP access.
2. Each user authorizes individually with their own 6sense credentials.
3. Confirm RBAC and AI settings expose the tools you need, and check the daily / weekly /
   monthly credit limits for the role.

## Used By

- `revops-signal-routing` (doddle-revops-skills) — binds `doddle.tool.v1.6sense.getAccountInsights`
  and `doddle.tool.v1.6sense.getKeywordIntent`
- Candidate lane for `gtm-lead-scoring`, `gtm-segmentation` (doddle-gtm-skills) — not yet bound
