# Stripe

> Subscriptions, invoices, dunning, and MRR metrics for SaaS. **Status: stub** - config reserved, MCP server pending. Skills using `doddle.tool.v1.stripe.*` fall back to `manual_review` until live.

## Tools (planned)

| Tool ID | Data |
|---------|------|
| `doddle.tool.v1.stripe.getSubscriptions` | Plan mix, trial status, cancellations |
| `doddle.tool.v1.stripe.listInvoices` | Failed payments, dunning state |
| `doddle.tool.v1.stripe.getCustomers` | LTV, tenure, expansion signals |
| `doddle.tool.v1.stripe.getMrr` | MRR movement, churn rate |

## Setup (when live)

```bash
export STRIPE_SECRET_KEY="sk_xxx"
```

## Used By

- `saas-retention`, `saas-expansion` (doddle-saas-skills, planned)
