# Discord

> Discord has **no official MCP server** that reads or sends messages in your servers or DMs.
> The official MCP (`https://docs.discord.com/mcp`) only searches developer documentation —
> message history needs a bot-token community server.

## Connection

| Field | Value |
|-------|-------|
| Official MCP | `https://docs.discord.com/mcp` — 3 read-only doc tools, no message access |
| Message reads | community server `barryyip0625/mcp-discord` (MIT), driven by a DISCORD bot token |
| Registered command | `npx -y github:barryyip0625/mcp-discord` — stdio by default, optional HTTP |
| Stale build | npm `mcp-discord` is v1.3.4 (22 tools); the GitHub build is v1.5.1 (46 tools) — use the GitHub build |

## Tools

| Upstream tool | Needs |
|---------------|-------|
| message history read (community server) | `VIEW_CHANNEL` + `READ_MESSAGE_HISTORY`, Message Content intent |
| Search Guild Messages (native Discord endpoint, 2026-03-19) | `READ_MESSAGE_HISTORY` + `MESSAGE_CONTENT` |
| official docs MCP — 3 read-only documentation search tools | none |

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.discord.readMessages` | message history read (community server) | read |
| `doddle.tool.v1.discord.searchMessages` | Search Guild Messages (native Discord endpoint) | read |
| `doddle.tool.v1.discord.searchDocs` | official docs MCP — documentation search | read |
| `doddle.tool.v1.discord.sendMessage` | community server — send a message | **write** |
| `doddle.tool.v1.discord.createChannel` | community server — create a channel | **write** |
| `doddle.tool.v1.discord.manageRole` | community server — role management | **write** |
| `doddle.tool.v1.discord.moderate` | community server — moderation actions | **write** |

**Read-only.** This entry binds reads only — Discord's official MCP cannot send messages, and
no send tool is registered here, so no approval gate is required. To post to a server, use the
bot / Discord API directly, outside the MCP registry.

## Verified notes (2026-11)

- **No official Discord action server exists.** The only Discord-operated MCP is the docs server (`https://docs.discord.com/mcp`, live, 3 tools). Several public MCP catalogs list `npx @discord/mcp-server` — that package does not exist on npm (404); treat those catalogs as unreliable.
- Community servers can write (messages, channels, roles, moderation). **Dry-run:** `@discord-mcp/core` exposes `MCP_WRITE_MODE=preview` (blocks all mutations) and `MCP_DRY_RUN`, plus per-guild allow-lists.
- The npm `mcp-discord` build lags the GitHub release — npm is 1.3.4 (22 tools), the repo ships 1.5.1 (46 tools). Prefer a pinned GitHub spec.
## Setup

1. Create a Discord application and a bot token.
2. Invite the bot to the servers it may read and grant `VIEW_CHANNEL` +
   `READ_MESSAGE_HISTORY`.
3. Enable the **Message Content** privileged intent — without it the Gateway closes with code
   **4014** and message text is unreadable.
4. Export the token into the environment (never onto a command line):

```bash
export DISCORD_BOT_TOKEN="<bot token>"
```

5. Native search: `Search Guild Messages` (2026-03-19) needs `READ_MESSAGE_HISTORY` +
   `MESSAGE_CONTENT`; error **110000** means the guild is not yet indexed.

## Used By

- `revops-dark-social` (doddle-revops-skills) — binds `doddle.tool.v1.discord.readMessages` and
  `doddle.tool.v1.discord.searchMessages`
- `community-building` (doddle-marketing-skills) — Discord community analysis lane
- Not supported: self-bot servers (account-token logins) violate Discord's terms of service
