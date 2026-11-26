# Gong

> Official Gong MCP server — calls, transcripts, AI briefs, CRM entity search.
> **Read-only**: it never creates, updates or deletes Gong or CRM data.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.gong.io/mcp` |
| Transport | HTTP (remote MCP) |
| Auth | OAuth — scope `mcp:read`, `mcp:write`, or both |
| Registration | Automatic (marketplace / OAuth) or manual (Gong issues client id + secret) |

## Tools

`ask_account`, `ask_deal`, `generate_brief`, `search_conversations`, `get_transcript`,
`research_conversations`, `get_session_context`, `search_crm_entities`, `search_person_entities`

| Upstream tool | Gong credits |
|---------------|--------------|
| `ask_account`, `ask_deal`, `generate_brief`, `research_conversations` | consumed |
| `search_conversations`, `get_transcript`, `get_session_context`, `search_crm_entities`, `search_person_entities` | none |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.gong.calls` | `search_conversations` | read |
| `doddle.tool.v1.gong.searchConversations` | `search_conversations` | read (same upstream tool as `calls`) |
| `doddle.tool.v1.gong.getTranscript` | `get_transcript` | read |
| `doddle.tool.v1.gong.askAccount` | `ask_account` | read (credits) |
| `doddle.tool.v1.gong.askDeal` | `ask_deal` | read (credits) |
| `doddle.tool.v1.gong.generateBrief` | `generate_brief` | read (credits) |
| `doddle.tool.v1.gong.researchConversations` | `research_conversations` | read (credits) |
| `doddle.tool.v1.gong.getSessionContext` | `get_session_context` | read |
| `doddle.tool.v1.gong.searchCrmEntities` | `search_crm_entities` | read |
| `doddle.tool.v1.gong.searchPersonEntities` | `search_person_entities` | read |

Two ids resolve to `search_conversations` because two packs bind it: `gong.calls` (doddle-gtm-skills)
and `gong.searchConversations` (doddle-revops-skills). Keep both pointing at the same upstream
tool so existing blueprints stay valid.

**Read-only.** No tool in this entry mutates Gong or CRM data, so no approval gate is needed.
The only cost is Gong credits, so keep `ask_*`, `generate_brief` and `research_conversations`
deliberate and few.

## Setup

1. Paid Gong seat.
2. Register the MCP client — automatic via the marketplace / OAuth flow, or manual (Gong issues
   client id + secret).
3. Authorize with `mcp:read` (add `mcp:write` only if you really need it).
4. Some tools only work with personal-access authorization — a shared grant exposes fewer tools.

Native API alternative: `POST /v2/calls/transcript` with scope `api:calls:read:transcript`.

## Used By

- `gtm-win-loss`, `gtm-battlecards`, `gtm-sales-narrative`, `gtm-outbound`, `gtm-enablement`
  (doddle-gtm-skills) — bind `doddle.tool.v1.gong.calls`
- `revops-call-intelligence` (doddle-revops-skills) — binds `doddle.tool.v1.gong.searchConversations`
  and `doddle.tool.v1.gong.getTranscript`
