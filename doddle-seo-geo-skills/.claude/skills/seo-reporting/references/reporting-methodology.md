# Reporting methodology

Depth for `seo-reporting`. These are definitions and rules for reading live Search Console and
GA4 data. Nothing here is measured by `dseo`; every figure still comes from a live tool.

## Windows are mandatory

Every delta is stated as **current window vs comparison window** (e.g. "last 28 days vs the
previous 28 days"). A number without a window and a base is not a finding. Search Console lags
by a day or two and omits very low-volume queries, so say which window the tool returned.

## Winners and losers

- **Winner** — a query or page whose clicks or impressions rose between the windows.
- **Loser** — one that fell.

Report the largest movers in each direction with the query/URL and both window values. An
impression rise with a flat CTR is a visibility change; a click fall with flat impressions is a
CTR or SERP change. State which, and do not compute the split by hand if the tool already
provides it.

## CTR anomalies (position ≤ 5)

A query ranking in the top five with a CTR well below its peers is a **snippet** problem: the
title or meta description is not earning the click the rank deserves. This skill flags it and
hands the fix to `seo-sxo`/`seo-onpage`. A low CTR at position 20+ is normal and is not an
anomaly.

## Striking distance (position 8–20)

Queries and pages sitting around positions 8–20 already have some relevance and authority; a
small improvement (on-page, internal links, freshness) can move them to page one. Rank the
striking-distance list by impressions × proximity to page one. This is usually the cheapest
visible win in the account.

## Cannibalisation

Cannibalisation is when two or more URLs receive impressions for the same query or intent, so
neither ranks as well as one consolidated page would. Detect it by grouping pages by the query
they rank for:

- same query, multiple URLs → consolidate or differentiate;
- near-duplicate intents across URLs → hand to `seo-strategy` and `seo-topical-map`.

Label each flagged pair with the URLs and the shared query, and the recommended action.

## Forecasting

Only forecast from the observed live series:

1. State the window the series covers.
2. State the trend or level the forecast extrapolates.
3. State every assumption (no seasonality change, no algorithm shift, no new content).
4. Label the result `advisory`.

Never invent a growth rate or a market figure. If Search Console is unavailable, there is no
series and therefore no forecast — say so.
