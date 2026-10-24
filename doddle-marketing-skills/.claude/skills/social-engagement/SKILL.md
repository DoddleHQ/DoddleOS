---
name: social-engagement
id: doddle.marketing.social-engagement
version: 1.0.0
blueprint: ./blueprint.yaml
description: "Daily social community management: response cadence, moderation guides, conversation playbooks, UGC spotlight, escalation rules."
---
# Social: Engagement
Social execution for daily community management — responding within 1 hour, moderating UGC, spotlighting community, managing reputation risk. Cross-reference `social-media` (broader framework); this applies the execution layer. See `AGENTS.md` for region-specific cadence differences (local: faster/owner-level; national: multi-stakeholder escalation; international: timezone windows).

## When to Use This Skill
Apply for: daily comment/DM response cadence, moderation rules for UGC, community spotlight planning, escalation rules for negative mentions or competitor attacks, response templates per tone.

---

## Core Framework (Engagement-Specific)
1. Confirm cadence fits segment (`regions` input guides timezone/escalation rules per `AGENTS.md`).
2. Lock response rules: 1-hour comment response; 4-hour DM response (national/procurement: committee-level escalation; local: owner-level direct; international: async timezone windows).
3. Lock moderation rules: approve/reject/escalate criteria; brand-safety guidelines; UGC spotlight criteria; escalation matrix (`social-crisis` for crisis-level events).
4. Lock engagement growth: collaboration accounts, trend-participation rules, cross-promotion (`email-marketing`, `content-strategy`), paid amplification (`paid-advertising`) thresholds.

---

## Metrics & Benchmarks
| Metric | Good | Excellent | Note |
|-----------|------|-----------|------|
| Response Rate | Growing | Growing | Manual review |
| Moderation Throughput | Growing | Growing | Manual review |
| UGC Spotlight Rate | Growing | Growing | Manual review |

Note: No stub tool available for community metrics; rely on manual review or native analytics (`social-analytics`). Never fabricate response/moderation rates.

---

## Anti-Patterns (Engagement-Specific)
| Mistake | Fix |
| No response cadence | Lock cadence in `plan`; apply gate before distribution of engagement actions |
| No moderation rules | Lock approve/reject/escalate criteria; reference `social-crisis` for escalation |
| All promotional responses | Lock tone rules (value-first; promotional capped at 10%) in `plan` |
| Buying followers / fake comments | Organic only; paid amplification only for best organic content (`paid-advertising`) |

---

## Related Skills
- `social-media` — broader framework; applies execution layer
- `social-analytics` — measurement; `social-crisis` — reputation/crisis escalation; `social-listening` — competitor/brand tracking feeds moderation rules
- `social-engagement` works with ALL platform skills (`social-linkedin`, `social-instagram`, etc.) — daily execution applies regardless of platform
- `agency-marketing` — community tone rules; `regions` dimension applies (local/national/international cadence differences)
- `doddle.local.gbp` / `doddle.local.reviews` (local segment) — review response is part of engagement cadence; `doddle.b2b.qbr` (national/procurement) — QBR engagement rules apply

---

## Questions to Ask
1. Audience tone and response goals? 2. Moderation rules (approve/reject/escalate thresholds)? 3. Cadence (local/national/international via `regions`)? 4. Analytics/MCP status (manual review or `social-analytics`)?
