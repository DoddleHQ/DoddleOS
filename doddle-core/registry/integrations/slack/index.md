# Slack Integration

> Team messaging, notifications, and workflow automation

## Overview

Send messages, notifications, and interact with Slack channels. Essential for marketing team communication and alerts.

## Capabilities

| Tool | Description |
|------|-------------|
| `send_message` | Send message to channel/user |
| `list_channels` | Get workspace channels |
| `get_channel_history` | Read channel messages |
| `post_blocks` | Send rich formatted messages |
| `upload_file` | Share files to channels |

## Authentication

```bash
export SLACK_BOT_TOKEN="xoxb-xxx-xxx-xxx"
export SLACK_TEAM_ID="T0123456789"
```

### Setup Slack App
1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Create New App → From Scratch
3. Add Bot Token Scopes: `chat:write`, `channels:read`, `files:write`
4. Install to Workspace
5. Copy Bot User OAuth Token

## Use Cases

### 1. Campaign Alerts
```
Notify team about campaign launch
→ send_message(channel="#marketing", text="🚀 Q1 campaign is now live!")
```

### 2. Report Delivery
```
Send weekly report to channel
→ post_blocks(channel="#marketing-reports", blocks=[...report_blocks])
```

### 3. Lead Notifications
```
Alert sales about hot lead
→ send_message(channel="#sales-leads", text="🔥 New MQL: Company X - $50K opportunity")
```

## Integration with Marketing

- `/report:weekly` → Auto-send to Slack
- `/campaign:analyze` → Alert on performance changes
- `/leads:qualify` → Notify sales team

## DoddleOS Tool IDs

| Tool ID | Action | Type |
|---------|--------|------|
| `doddle.tool.v1.slack.messages` | Read channel history / list channels | read |
| `doddle.tool.v1.slack.sendMessage` | Post a message or blocks to a channel | **write** |

**Write-gated.** `slack.sendMessage` mutates a workspace. Any blueprint that calls it must place
a `gate` node (`approvers` + `timeout_s`) immediately before the write node — see
`doddle-core/spec/harness-phase2.md` §2.1 and `harness-cli-resolver.md` §6. Without an approved
gate record the runner refuses to schedule the node (`write_without_gate`).

## Related
- [Discord](../discord/) - Alternative notification channel
- [HubSpot](../hubspot/) - CRM lead source
