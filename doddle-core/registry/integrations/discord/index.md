# discord

> Discord community reads — official server is docs-only; message reads need a bot-token community server

## Connection

| Field | Value |
|-------|-------|
| Command | `npx -y mcp-discord` |
| Auth | bot token / access token |

## Upstream tools

`discord_read_messages`, `discord_search_messages`, `discord_send_message`

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.discord.readMessages` | `discord_read_messages` | read |
| `doddle.tool.v1.discord.searchMessages` | `discord_search_messages` | read |
| `doddle.tool.v1.discord.sendMessage` | `discord_send_message` | write |

**Write-gated.** Any tool marked *write* must sit behind a `gate` node in the blueprint (`approve_*`), and the write tool stays `required: false` with `fallback: manual_review`.

## Setup

- Discord application with a bot token
- Message Content privileged intent enabled (otherwise the Gateway closes with code 4014)
- Bot invited to the servers it may read

### Notes

- Discord has NO official MCP server that reads or sends messages. Its official MCP (https://docs.discord.com/mcp) only searches developer documentation.
- Message reads need a community server driven by a bot token — the maintained option is barryyip0625/mcp-discord (MIT). The npm `mcp-discord` build is older than the GitHub release.
- Reading history needs VIEW_CHANNEL + READ_MESSAGE_HISTORY; reading message text needs the Message Content intent.
- Discord native Search Guild Messages endpoint (2026-03-19) needs the same permissions; error 110000 means the guild is not yet indexed.
- Self-bot servers (account-token logins) violate Discord terms — not an option.

## Used By

- `doddle.revops.*` (doddle-revops-skills) where the skill binds it
