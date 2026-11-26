# zoominfo

> ZoomInfo GTM.AI MCP — verified B2B intelligence; Conversation Intelligence (formerly Chorus)

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.zoominfo.com/mcp` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`account/contact search`, `buying signal lookup`, `conversation insights`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.zoominfo.getConversationInsights` | `Conversation Intelligence (Chorus) insights` | read |
| `doddle.tool.v1.zoominfo.searchAccounts` | `verified account/contact search` | read |

**Read-only.** No tool in this entry mutates external data, so it needs no approval gate.

## Setup

- ZoomInfo account with GTM.AI / Conversation Intelligence access

### Notes

- ZoomInfo operates an official MCP server exposing verified B2B intelligence (500M+ contacts, 100M+ companies), buying signals, and the GTM Context Graph.
- Chorus is now ZoomInfo Conversation Intelligence (calls, meetings, emails, winning behaviors, deal momentum, churn risk) — a ZoomInfo product, not a separate vendor.
- ZoomInfo is the data provider behind HubSpot Breeze Prospecting Agent (public beta); Breeze Intelligence itself has no MCP server.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
