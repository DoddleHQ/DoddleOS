# Stripe

> Billing data and write access — subscriptions, invoices, usage meters, customers, analytics.

## Current server (verified 2026-11)

Stripe hosts an **official remote MCP server**:

| Field | Value |
|-------|-------|
| Endpoint | `https://mcp.stripe.com` (streamable HTTP) |
| Registry | `com.stripe/mcp` — official, active |
| Auth | OAuth (interactive) or **agent API key** (autonomous) |
| Docs | https://docs.stripe.com/mcp |

> The local npm packages `@stripe/mcp` and `@stripe/agent-toolkit` were **deprecated on
> 2026-11-04** and receive no further updates or security fixes. Any config that starts Stripe
> with `npx @stripe/mcp` should be migrated to the hosted server.
>
> From **2027-01-11** Stripe MCP no longer accepts full-access secret keys or non-agent
> restricted keys — use an agent API key or OAuth.

## Upstream tools exposed

| Upstream tool | Use |
|----------------|-----|
| `stripe_api_read` | Any Stripe API `GET` method |
| `stripe_api_write` | Any Stripe API `POST`/`PATCH`/`PUT`/`DELETE` method |
| `stripe_api_search` / `stripe_api_details` | Find API methods and their parameters |
| `stripe_analytics` | Billing analytics, reports, natural-language SQL |
| `get_stripe_account_info` | Account details |
| `search_stripe_documentation` | Stripe knowledge base |

## DoddleOS tool IDs

DoddleOS binds **semantic** tool IDs that map onto the upstream tools above.

| Tool ID | Maps to | Type |
|---------|---------|------|
| `doddle.tool.v1.stripe.getSubscriptions` | `stripe_api_read` on subscription list | read |
| `doddle.tool.v1.stripe.listInvoices` | `stripe_api_read` on invoice list | read |
| `doddle.tool.v1.stripe.getCustomers` | `stripe_api_read` on customer list | read |
| `doddle.tool.v1.stripe.getMrr` | `stripe_analytics` / subscription read | read |
| `doddle.tool.v1.stripe.recordMeterEvent` | `stripe_api_write` → `POST /v1/billing/meter_events` | **write** |
| `doddle.tool.v1.stripe.updateSubscription` | `stripe_api_write` → subscription item update | **write** |

## Write tools (usage-based billing)

`recordMeterEvent` writes to Stripe Billing meters — the payload must carry the customer and the
value, and `event_id` makes the write idempotent on retry. `updateSubscription` changes what a
customer is charged.

**Write-gated.** Both write tools mutate billing. A blueprint must place a `gate` node before the
write, and it must preview first — see `doddle.revops.revops-usage-monetization`, which previews
with `drev meter` and only then records. Meter-event payloads reuse the preview's `event_id` so a
retry never double-counts.

## Verified notes (2026-11)

- **Metered billing must target `POST /v1/billing/meter_events`** — the legacy `subscription_items/{id}/usage_records` endpoint was removed in API version `2025-03-31.basil`.
- **Dry-run:** Stripe MCP has a first-class human-confirmation flow (approval in the Dashboard returns a 24h approval token). Combine it with a sandbox account and a restricted agent key.
- From **2027-01-11** Stripe MCP stops accepting full-access secret keys and non-agent restricted keys — agent API key or OAuth only.
## Setup

```bash
export STRIPE_AGENT_API_KEY="sk_xxx"   # agent API key from the Dashboard
```

## Used By

- `saas-retention`, `saas-expansion` (doddle-saas-skills)
- `revops-usage-monetization` (doddle-revops-skills, gated write)
