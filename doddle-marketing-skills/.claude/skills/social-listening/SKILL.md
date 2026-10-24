---
name: social-listening
id: doddle.marketing.social-listening
version: 1.0.0
blueprint: ./blueprint.yaml
description: "Brand and competitor listening: mention tracking, sentiment monitoring, trend alerts, competitor comparison, share-of-voice tracking."
---
# Social: Listening
Social execution for listening and competitive intelligence — brand/competitor mention tracking, sentiment monitoring, trend alerts, competitor theme comparison. Cross-reference `social-media`; applies intelligence layer. See `AGENTS.md`: `regions` guides jurisdiction/localization; `local.gbp` and `local.reviews` feed local business reputation data; `b2b.proposals` / `b2b.qbr` feed national/procurement reputation tracking.

## When to Use This Skill
Apply for: competitive intelligence, brand health monitoring, trend detection, sentiment tracking, competitor campaign comparison. Always: never fabricate mention/sentiment data; state ⚠️ NOT AVAILABLE when listening server is unconfigured (`social-listening` uses `researcher` for assessment; no dedicated sentiment server in current registry — `social-analytics` feeds performance metrics, not listening data directly).

---

## Core Framework (Listening-Specific)
1. Confirm scope: brand + competitors + keywords + channels (`regions` guides jurisdiction and competitor selection — international requires multi-market competitors; local requires local-service competitor comparison per `local.gbp`).
2. Lock monitoring rules: mention volume, sentiment categories, trend definitions, competitor themes, share-of-voice calculation. Lock in `listening_summary`. Lock `trend_alert` for emerging topics. Lock `competitor_data` for comparison.
3. Lock cadence: daily/weekly trend review; monthly competitor comparison; quarterly strategic review (`agency-reporting` for QBR input; `measurement-plan` for KPI linkage; `social-crisis` for escalation triggers).
4. Apply `approve_content` gate before any `distribute` of listening outputs (reports shared externally — approval ensures accuracy and avoids sharing unverified competitor intelligence).

---

## Metrics & Benchmarks (Listening-Specific)
| Metric | Definition | Note |
|-----------|------------|--------|
| Mention Volume Trend | Brand mentions per period | Assumed unless configured; no stub server (`social-analytics` feeds performance, not listening volume) |
| Sentiment Ratio | Positive / Negative / Neutral mentions | Assumed unless configured; manual review required |
| Share of Voice (SOV) | Brand mentions / Competitor mentions | Requires competitor monitoring setup (manual or third-party until `listening-server` configured) |
| Trend Alert Count | Emerging competitor themes / brand mentions | Manual tracking until listening server live |

Note: All listening metrics depend on manual review or third-party listening tools (`social-analytics` for GA4/social traffic; `local.gbp` for local reputation; `b2b.proposals` for procurement reputation tracking). No sentiment server in `doddle-core/registry/integrations/_registry.md`. Never invent SOV, sentiment ratios, or competitor mention counts.

---

## Anti-Patterns (Listening-Specific)
| Anti-Pattern | Fix |
| Broadcast-only (ignoring listening) | Lock monitoring cadence; set `trend_alert` thresholds |
| No competitor comparison | Lock `competitor_data` in `listening_summary`; reference `b2b.proposals` / `b2b.rfp` for national/procurement competitor tracking |
| Fabricated SOV / sentiment | Never invent; label `assumed` or `⚠️ NOT AVAILABLE`; reference `AGENTS.md`: stub mechanism (`google-business-profile`, `stripe`, `sensortower` are stubs; no sentiment server registered) |
| Ignoring regional differences | Lock `regions` input; reference `local.gbp` (local reputation) and `b2b.proposals` (national competitor tracking) |

---

## Related Skills
- `social-media` — pillar framework; `social-listening` feeds content planning and crisis detection (`social-crisis`)
- `social-analytics` — performance metrics feed listening recommendations; `social-listening` feeds strategic adjustments
- `social-crisis` — escalation triggers feed `trend_alert` (negative sentiment spike triggers crisis response)
- `social-engagement` — community sentiment feeds `listening_summary` (response sentiment = engagement signal)
- `analytics-attribution` — UTM/social traffic attribution; `measurement-plan` — KPI linkage
- `creative-direction` — competitor themes feed concept revisions; `agency-marketing` — agency positioning feeds brand health tracking; `regions` applies to international listening scope
- `b2b.proposals` / `b2b.rfp` / `b2b.qbr` — national/procurement competitor/reputation tracking feeds listening recommendations
- `local.gbp` / `local.reviews` (local segment) — local reputation metrics feed listening; `local.booking` — booking conversion from local engagement
- `doddle.marketing.budget-allocator` — budget impact of competitor campaigns (reference only; no direct call node)

---

## Questions to Ask
1. Monitoring scope: brand mentions, competitor comparison, keywords, sentiment, channels?
2. Competitors and keywords defined? (If no: propose assumption list; flag in `listening_summary`.)
3. Cadence (daily/weekly/monthly)?
4. Listening server / MCP configured? (⚠️ NOT AVAILABLE — `social-analytics` + `social-listening` have no dedicated listening server in registry; rely on manual review or `social-analytics` performance data only. See `AGENTS.md`: stub mechanism.)
5. Regions (`regions` input): local / national / international? (Guides competitor selection: local competitors (`local.gbp`) vs national competitors (`b2b.proposals`) vs international competitors (region-localized tracking).)
