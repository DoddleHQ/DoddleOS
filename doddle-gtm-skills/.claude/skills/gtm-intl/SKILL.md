---
name: gtm-intl
id: doddle.gtm.gtm-intl
version: 0.2.0
blueprint: ./blueprint.yaml
description: "Rank candidate international markets and design a minimum launch pack for the winners. Use when the user asks about going international, localization, geo expansion or which country to enter next."
---

# International Expansion

Rank candidate markets on recorded fit criteria and define the minimum pack needed to enter
the winner — never a full local build-out by default.

## Advisory (no toolkit)

The toolkit has no market-data source, so every ranking input is user-supplied and labelled
`advisory`: candidate list, demand signals, competitor presence, localization effort,
readiness. Do not fetch or invent country statistics; if the user has none, report the ranking
as blocked on inputs.

## Sub-flows

| Sub-flow | When to use | Output focus |
|----------|-------------|--------------|
| `market-ranking` | Choosing between 2+ candidate countries | Weighted ranking table |
| `minimum-launch-pack` | A market is chosen; define smallest viable entry | Localized asset list |
| `localization-scope` | Deciding what must be translated vs adapted | Scope matrix |
| `geo-hold` | Deferring entry; what to monitor instead | Trigger watchlist |

## Workflow

1. Collect the candidate markets and the ranking axes (fit, effort, readiness). Default axes
   if the user has none: ICP presence, competition, localization effort, sales readiness.
2. Collect each market's input values from the user; tag every one `advisory`. Never fill a
   blank with a remembered statistic.
3. Build the ranking table (weights × scores are the user's; state them, do not silently
   normalize).
4. For the winning market, pull the minimum launch pack: which assets localize, which channel
   enters first, which proof transfers.
5. Define triggers for revisiting (evidence that would change the ranking).

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the top-ranked market and score if computed, tagged
   `advisory`; if inputs are missing, say the ranking is blocked.
2. **Key evidence.** Every input per market, each tagged `advisory` with its source (user
   statement / supplied file).
3. **Artifact path.** Where the ranking was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent country statistics, demand data or competitor facts; never do
arithmetic the user did not authorize — state the weights and scores and let them stand as
recorded inputs; if a market input is missing, mark it `NOT AVAILABLE`. Full block:
`common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Quoting remembered market sizes | Every market number is user-supplied `advisory` |
| Full localization up front | Default to the minimum launch pack; expand on evidence |
| Ranking without weights | Make the weights explicit and recorded |
| Ignoring readiness | Rank on readiness, not just demand |

## Related Skills

`gtm-strategy`, `gtm-launch`, `gtm-segmentation`, `gtm-messaging`, `gtm-pricing`

## Inputs

| Input | Required | Type | Notes |
|-------|----------|------|-------|
| markets | yes | string | Candidate markets to rank |
| criteria | no | string | Ranking axes; defaults to fit / effort / readiness |

## Outputs

| Output | Type | Notes |
|--------|------|-------|
| plan | markdown | Locale ranking and minimum launch pack |
