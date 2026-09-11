# Google Business Profile

> Listings, reviews, posts, and insights for local service businesses. **Status: stub** - config reserved, MCP server pending. Skills using `doddle.tool.v1.gbp.*` fall back to `manual_review` until live.

## Tools (planned)

| Tool ID | Data |
|---------|------|
| `doddle.tool.v1.gbp.getBusinessProfile` | Categories, hours, attributes, completeness |
| `doddle.tool.v1.gbp.listReviews` | Rating, review text, response status |
| `doddle.tool.v1.gbp.getInsights` | Calls, direction requests, impressions, bookings |
| `doddle.tool.v1.gbp.createPost` | Publish offers/events/updates |

## Setup (when live)

```bash
export GBP_ACCESS_TOKEN="xxx"
export GBP_ACCOUNT_ID="accounts/xxx"
```

## Used By

- `local-gbp`, `local-reviews` (doddle-local-skills)
