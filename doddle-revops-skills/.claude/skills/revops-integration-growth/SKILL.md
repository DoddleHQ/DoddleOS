---
name: revops-integration-growth
id: doddle.revops.revops-integration-growth
version: 1.0.0
blueprint: ./blueprint.yaml
description: "When the user wants integration-led growth — readiness of native integrations, marketplace listings, OAuth scopes, webhook coverage, and co-selling motions. Use for 'ecosystem GTM', 'integration marketplace', 'Zapier app', 'OAuth scopes', 'co-selling', 'native integration'."
---

# RevOps Integration Growth

Integration-led growth is a checklist before it is a strategy. This skill audits whether each
integration is actually shippable and sellable — it never deploys anything.

## Deterministic Toolkit

```
drev integration-audit --catalog <integrations.json>
```

Read the JSON envelope:

- `metrics.integrations` / `ready` / `not_ready` / `average_readiness`.
- `rows[]` — per integration: `readiness_score`, the six `checks`, and the failing `failures`.

The six checks:

| Check | What it means |
|-------|---------------|
| `owner_assigned` | Someone owns the integration |
| `has_oauth_scopes` | Scopes are declared (native and partner types excepted) |
| `has_webhook_coverage` | The integration emits webhooks or events |
| `listing_complete` | A listing status and URL exist |
| `co_sell_fields_present` | Co-selling attribution fields are defined |
| `documented` | A docs URL exists |

A readiness score is a **checklist result**, not a go/no-go decision. It says what is missing,
not what the business should do.

## Workflow

1. Confirm the segment (default **SMB**) and the growth motion: native integration, app
   marketplace, automation platform, or partner.
2. Collect the catalog. Include every integration you claim to have — an integration that is
   absent cannot be scored.
3. Run `drev integration-audit …` and read the envelope.
4. If `ok: false`, relay `error.message` and `error.hint`, then stop.
5. Report the least-ready integrations first, with their failed checks named.
6. For each, propose the smallest fix and the owner — scope, tokens, webhooks, listing, co-sell
   fields, docs.
7. State `scoring_version`, `data_version`, and `evidence.stamp`.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `readiness-audit` | Default: score the whole catalog | `drev integration-audit` → `rows[]` |
| `marketplace-listing` | An app marketplace submission is planned | `listing_complete` + `documented` |
| `scope-review` | A token/consent problem blocks launch | `has_oauth_scopes` |
| `co-sell-plan` | A partner motion needs attribution | `co_sell_fields_present` |
| `build-order` | Several integrations need work | `rows[]` sorted by readiness |

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence carrying how many integrations are ready and the verdict.
2. **Key evidence.** The per-integration scores and failed checks tagged `deterministic`
   (computed) or `live` (read from the catalog).
3. **Artifact path.** Where the JSON or the plan was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent an integration, scope, or listing; `null` is not measured, not zero;
never do arithmetic; readiness is not a business decision; on `ok: false` relay `error.message` +
`error.hint`. Full block: `common/evidence-envelope.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Scoring only the integrations you like | Audit the whole catalog |
| Treating a score of 100 as a go decision | It only means the checklist passed |
| Forgetting webhook coverage until launch | It is a check, not an afterthought |
| Leaving co-sell attribution undefined | Then the partner motion cannot be measured |
| Deploying the integration from this skill | Read-only — propose the work, the owner ships it |

## Related Skills

- `doddle.gtm.gtm-partnerships` — the mutual-value model behind a partner motion.
- `doddle.gtm.gtm-channel` — partner-led versus direct channel economics.
- `doddle.b2b.b2b-partnerships` — partnership discovery and enablement.
- `doddle.revops.revops-data-infrastructure` — validate the tables that integrations sync.
- `doddle.gtm.gtm-advocacy` — community and referral proof that integrations amplify.

## Inputs

| Name | Type | Required | Description |
|------|------|----------|-------------|
| catalog | file | yes | Integration catalog (JSON) |
| segment | string | no | Segment focus; defaults to SMB |

## Outputs

| Name | Type | Description |
|------|------|-------------|
| report | markdown | Readiness scores, failed checks, build order |
| envelope | json | Deterministic integration-readiness envelope |
