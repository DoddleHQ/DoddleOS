---
name: social-analytics
id: doddle.marketing.social-analytics
version: 1.0.0
blueprint: ./blueprint.yaml
description: "Social measurement and reporting: platform-specific engagement rate, follower growth, share/saves, CTR, UTM attribution, competitor SOV, monthly dashboards, QBR prep."
---
# Social: Analytics
Social measurement and reporting — platform-specific KPIs, UTM attribution, competitor SOV, monthly dashboards, QBR prep. Uses MCP (GA4, HubSpot — stub integrations; `⚠️ NOT AVAILABLE` if unconfigured) or asks when missing. Cross-reference `social-media` for pillar framework; applies measurement layer.

## When to Use This Skill
Apply when a client/report requires social performance measurement — monthly reporting, QBR data, ROI proof for retainer reviews (`agency-reporting`), or performance comparison against competitors (`social-listening`). Use `measurement-plan` for KPI definitions; this executes them.

---

## Core Framework (Social Analytics-Specific)
1. **Data Gather**: Pull actuals per platform (GA4 for social traffic; native analytics for platform metrics; HubSpot for lead/deal attribution). If unavailable: ⚠️ NOT AVAILABLE + setup instructions (see `AGENTS.md`: stub mechanism for GA4 requires setup; `hubspot.contacts` requires CRM access; native analytics APIs not currently registered — rely on GA4 for traffic/conversion; never invent metrics). List unavailable sources at end.
2. **Scorecard Build**: Per KPI from `measurement-plan`: metric, definition, target, actual, delta, status, source. One primary KPI per engagement; guardrails (CAC ceiling, unsubscribe rate) tracked separately. Status: 🟢 on_track / 🟡 at_risk / 🔴 off_target. Never hide red.
3. **Report Format**: Client-ready report (`report`) with scoreboard-first (green/yellow/red table), brief narrative (what moved + why + causal read — correlation labeled honestly), blockers, recommendations (`recommendations`) with impact estimates.
4. **Recommendations**: 3-5 prioritized actions for next period. Each: recommendation, expected impact (range + basis), which KPI it moves, resource needed (`budget-allocator` for cost; `media-reallocator` for budget shifts), timeline. Tie to `social-engagement` (cadence), `social-crisis` (if crisis-related), and `agency-reporting` (QBR format).

---

## Metrics & Benchmarks (Social-Specific)
| Metric | Good | Excellent | Source / Note |
|-----------|------|-----------|---------------|
| Engagement Rate | 1-3% | 3%+ | Per-platform native (no stub server in registry; assume ⚠️ NOT AVAILABLE unless custom configured) |
| Follower Growth Rate | 2-5%/mo | 5%+/mo | Per-platform native |
| Share / Save Rate | Growing | Growing | Per-platform native |
| CTR (Social Traffic → Landing) | >1% | >3% | GA4 (`doddle.tool.v1.ga4.getReport` — requires setup) |
| Cost per Click (Paid) | <$1 | <$0.50 | Ad platforms (`paid-advertising`; meta-ads/stub) |
| Return on Ad Spend | >2x | >3x | GA4 + HubSpot (`hubspot.contacts` — stub; requires setup) |
| Share of Voice | Growing | Growing | `social-listening` (manual / third-party listening until `listening-server` configured) |
| UTM Attribution Accuracy | Tagged 100% | Tagged 100% + event mapping verified | `measurement-plan` taxonomy + `analytics-attribution` |

Note: Metrics that depend on stub integrations (`hubspot.contacts`, `meta-ads`, native analytics APIs not in registry) must be labeled `assumed` or `⚠️ NOT AVAILABLE` — never invented. See `AGENTS.md` for stub mechanism documentation.

---

## Anti-Patterns (Social Analytics-Specific)
| Anti-Pattern | Fix |
| All promotional metrics only | Lock scoreboard-first format (metrics + status); recommendations must reference value metrics |
| No UTM tags / attribution gaps | Apply `measurement-plan` taxonomy; verify UTM mapping before reporting |
| Invented benchmarks | Use stated targets from `measurement-plan` or industry ranges labeled `assumed` |

---

## Related Skills
- `social-media` — pillar framework feeding metrics; `social-analytics` executes measurement layer
- `measurement-plan` — KPI definitions, UTM taxonomy, decision rules this executes
- `media-reallocator` — uses `social-analytics` scorecard to trigger budget moves
- `agency-reporting` — QBR/report structure; `social-analytics` feeds data layer
- `analytics-attribution` — deeper cross-channel attribution (GA4-based)
- `doddle.local.gbp` / `doddle.local.reviews` (local segment) — local service business metrics (GBP insights, review velocity, call tracking) complement platform analytics
- `doddle.b2b.proposals` / `doddle.b2b.qbr` (national/procurement segment) — proposal proof + QBR metrics require analytics documentation
- `doddle.marketing.budget-allocator` — budget split feeds paid social cost calculations
- `social-engagement` — daily cadence feeds engagement metrics; `social-crisis` — crisis metrics (sentiment, response time) feed analytics
- `social-listening` — SOV/competitor data feeds analytics recommendations

---

## Questions to Ask
1. KPIs defined (`measurement-plan`)? If not: set targets from brief assumptions and flag.
2. Reporting period and cadence (weekly/monthly/QBR)?
3. Analytics/MCP configured — or assume ⚠️ NOT AVAILABLE? (State `ga4.getReport`, `hubspot.contacts` setup instructions; note stub integrations: `tiktok.trending`, `crosspost.publish`, `stripe`, `google-business-profile`, `sensortower` — see `AGENTS.md` and `_registry.md`.)
4. Regions (`regions` input): local/national/international? (Affects proof selection: local uses `local.gbp`/reviews; national uses `b2b.proposals`; international uses region-localized metrics with normalization.)
