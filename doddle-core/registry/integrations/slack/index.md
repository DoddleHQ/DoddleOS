# Slack

> Official Slack MCP server — hosted at `https://mcp.slack.com/mcp`. Read and write messages,
> files, channels, users, canvases and lists.

## Connection

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.slack.com/mcp` |
| Transport | Streamable HTTP (JSON-RPC 2.0) — **no SSE, no DCR** |
| Auth | OAuth 2.0 (Slack app Client ID + secret); workspace admin approves each MCP client |
| Env | `SLACK_CLIENT_ID`, `SLACK_CLIENT_SECRET`, `SLACK_BOT_TOKEN` |

> **There is no official npm package.** `@slack/mcp-server` does not exist on npm (404). Use the
> hosted endpoint above.

> **Security — CVE-2025-34072 (CVSS 9.3).** The reference server
> `@modelcontextprotocol/server-slack` is archived and npm-deprecated: its post/reply paths leave
> link unfurling enabled, so a prompt injection can exfiltrate a `.env` file or private message
> through a URL the agent posts. Do not use it. Revoke any `xoxb-` tokens it touched.

Slack documents **capabilities** rather than a fixed tool list, and tool names vary per client —
pin behaviour to `tools/list` instead of hardcoded names.

## Upstream capabilities

Search messages/files/users/channels · retrieve and send messages · schedule messages · manage
canvases · manage users · upload files · lists.

## DoddleOS tool IDs

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.slack.messages` | search messages / read channel history | read |
| `doddle.tool.v1.slack.sendMessage` | send a message or blocks | **write** |
| `doddle.tool.v1.slack.scheduleMessage` | schedule a message | **write** |
| `doddle.tool.v1.slack.uploadFile` | upload a file to a channel | **write** |

**Write-gated.** Sending, scheduling and uploading change the workspace. A blueprint must place a
`gate` node immediately before the write (`approve_alert` for signal alerts, `approve_share` for
the QBR share) and keep the tool `required: false` with `fallback: manual_review`.

## Setup

1. Slack workspace.
2. Create a Slack app (Client ID + secret); add the MCP integration in your AI client.
3. Workspace admin approves the MCP client integration.
4. A bot token is needed for message actions — scopes `chat:write`, `channels:read`,
   `users:read`, `files:write`.

## Used By

- `revops-signal-routing` (doddle-revops-skills) — `slack.sendMessage` behind `approve_alert`
- `revops-qbr` (doddle-revops-skills) — `slack.sendMessage` behind `approve_share`
- `gtm-outbound`, `gtm-abm`, `gtm-icp` (doddle-gtm-skills) — optional reads
