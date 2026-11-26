# Integration-Led Growth Checklist

`drev integration-audit --catalog <integrations.json>` scores each integration against six
checks. The score says what is missing — the decision is yours.

## The six checks

| Check | Meaning | Typical failure |
|-------|---------|-----------------|
| `owner_assigned` | A named owner exists | Integration shipped, nobody maintains it |
| `has_oauth_scopes` | Scopes are declared (native and partner types excepted) | Consent screen ships without scopes |
| `has_webhook_coverage` | The integration emits webhooks or events | Sync works one way only |
| `listing_complete` | Listing status and URL exist | Unlistable in the marketplace |
| `co_sell_fields_present` | Co-selling attribution fields defined | Partner pipeline cannot be attributed |
| `documented` | A docs URL exists | Support burden lands on the founder |

Readiness score = satisfied checks ÷ total checks × 100.

## Co-selling motion

1. **Register** the partner or listing in the motion.
2. **Enable** — a sales playbook for both sides.
3. **Attribute** — which pipeline came through the integration.
4. **Review** — a cadence to fix what the data shows.

## Marketplace listing basics

- Name, category, and one-line value proposition.
- Screenshots or a short capture of the real flow.
- Scopes listed plainly, with why each is needed.
- A docs page and a support path.

## Rules

- Audit the whole catalog. A missing integration cannot be scored.
- A score of 100 means the checklist passed, not that the integration is worth building.
- Deployment is out of scope: propose the work and name the owner.
- OAuth scopes are a privacy decision as well as a technical one — request the minimum.
