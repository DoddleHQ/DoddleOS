# gong

> Gong call intelligence — find calls, read transcripts, AI-generated briefs (read-only server)

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.gong.io/mcp` |
| Transport | http |
| Auth | oauth |

## Upstream tools

`ask_account`, `ask_deal`, `generate_brief`, `search_conversations`, `get_transcript`, `research_conversations`, `get_session_context`, `search_crm_entities`, `search_person_entities`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.gong.getTranscript` | `get_transcript` | read |
| `doddle.tool.v1.gong.searchConversations` | `search_conversations` | read |
| `doddle.tool.v1.gong.generateBrief` | `generate_brief` | read (consumes credits) |
| `doddle.tool.v1.gong.researchConversations` | `research_conversations` | read (consumes credits) |

**Read-only.** No tool in this entry mutates external data, so it needs no approval gate.

## Setup

- Gong account with a paid seat
- Gong integration registered (automatic via marketplace/OAuth, or manual with client id + secret)
- Scopes mcp:read (and mcp:write if you enable it)

### Notes

- The Gong MCP server is read-only: it never creates, updates, or deletes data in Gong or the CRM.
- ask_account, ask_deal, generate_brief and research_conversations consume Gong credits; search_conversations, get_transcript, get_session_context and the entity searches do not.
- Some tools only work with personal-access authorization; shared access exposes fewer tools.
- Native API alternative: POST /v2/calls/transcript with scope api:calls:read:transcript.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
