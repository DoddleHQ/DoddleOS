# 6sense

> 6sense intent, buying stage, and account intelligence — official MCP server (read-only)

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://api.6sense.com/mcp` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`account insights`, `6QA trends`, `keyword performance`, `ad campaign performance`, `website activity`, `segment discovery`, `sales account/people insights`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.6sense.getAccountInsights` | `account insights / buying stage` | read |
| `doddle.tool.v1.6sense.getKeywordIntent` | `keyword intent performance` | read |

**Read-only.** No tool in this entry mutates external data, so it needs no approval gate.

## Setup

- 6sense account with Revenue Marketing access
- Per-user OAuth authorization (each user authorizes individually)

### Notes

- All MCP operations are read-only: it cannot modify data, settings, or configurations.
- Keyword Intent Data API (v1, OAuth 2.0) costs 3 credits per newly discovered account; non-matches are free.
- People Search API and Lead Scoring API consume no credits. Company Identification API v3 uses an API token.
- Admins can set MCP access controls and daily/weekly/monthly credit limits per user or role.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
