# Signal Taxonomy

A signal is a recorded event that says something about buying intent. This file defines what
counts, how to name it, and how to route it.

## Signal definition

| Field | Rule |
|-------|------|
| `account_id` | Required. A signal without an account cannot be routed. |
| `signal` | Required. One stable name per meaning, forever. |
| `occurred_at` | Required, UTC. Recency is the routing input. |
| `contact_id` | Optional. Useful for one-to-one outreach, not for routing. |
| `source` | Optional. Where the signal came from. |

## Naming rules

- Lowercase, snake_case, verb first: `pricing_page_view`, `job_posting`, `docs_search`.
- One meaning per name. `invited_teammate` must mean the same thing in every system.
- Never version inside the name (`project_created_v2`). Version the schema, not the vocabulary.
- Do not encode state in the name (`trial_expired`). Emit two signals instead.

## Good and weak signals

| Signal | Strength | Why |
|--------|----------|-----|
| `pricing_page_view` | strong | Near-purchase behaviour |
| `job_posting` | medium | Timing signal, not intent to buy from you |
| `docs_search` | weak | Research, often pre-purchase but long tail |
| `page_view` | weak | Rarely actionable on its own |

## Recency windows

| Buying motion | Suggested window |
|---------------|------------------|
| Self-serve / trial | 3–7 days |
| Sales-assisted mid-market | 14–30 days |
| Enterprise | 30–90 days |

The window is a rule, not a habit. Set it once, in the rules file, and report it with every
signal result.

## Priority ladder

| Priority | Meaning | Response |
|----------|---------|----------|
| 1 | In-market now | Same-day 1:1 outreach |
| 2 | Actively evaluating | Sequence + content |
| 3 | Researching | Nurture, no interrupt |

Keep the ladder short. If everything is priority 1, nothing is.

## Routing

Each rule names a channel, an owner, and an action. An unrouted signal type is a **rules gap** —
report it, then add the rule deliberately.

## What this skill does not do

- It does not send. Payloads are drafted for a human.
- It does not deanonymize. An anonymous visit stays anonymous until a legitimate identifier
  links it — never guess from email domain, fingerprint, or inference.
- It does not scrape. Signals come from supplied exports.
- It does not learn. The rules file is configuration; changing it is a human decision.
