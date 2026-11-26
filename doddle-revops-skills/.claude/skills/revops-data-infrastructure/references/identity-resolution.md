# Identity Resolution Reference

Identity resolution decides whether two records are the same customer. It is a data-contract
problem, not a clever-algorithm problem.

## The core problem

| Record | Source | Why it fails to join |
|--------|--------|---------------------|
| `crm_123` | CRM | CRM id, no shared key with product |
| `web_556` | Product signup | Anonymous email then a login on a shared domain |
| `acct_9f3` | Warehouse | The only record with a canonical id |

Without a mapping, every metric is wrong in a different way: customer counts inflated, revenue
split across duplicates, PQL assigned to nobody.

## Match methods, strongest first

| Method | Confidence | Notes |
|--------|-----------|-------|
| Deterministic (shared id, verified email) | 1.0 | Use when the key is contractual, not inferred |
| Verified email | high | Only with a verified email column |
| Fuzzy (name + domain + company) | medium | Always record the method and confidence |
| Manual override | varies | Highest priority, must be auditable |

## Rules

- A record without a canonical id is **unmapped**, not a duplicate and not a new customer.
- Confidence below `0.8` is reported as `low_confidence` and should be reviewed.
- Never merge on fuzzy signals alone inside an automated pipeline. Propose the merge; a human or
  a governed process decides.
- Store the method and confidence with every mapping. A mapping without a method is an
  assumption.

## Identity coverage metric

`identity_match_rate` = records with a canonical id ÷ total identity records.

Track it as a trend, not a number. A falling rate means new sources arrived without a mapping
rule — that is a data-contract incident, not a metric to report around.
