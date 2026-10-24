---
name: social-crisis
id: doddle.marketing.social-crisis
version: 1.0.0
blueprint: ./blueprint.yaml
description: "Social reputation and crisis response: trigger detection, response templates, escalation rules, brand-voice protection, recovery narrative framework."
---
# Social: Crisis
Social reputation/crisis response — trigger detection, response templates (public reply / DM / no-response criteria), escalation matrix (who approves what), timeline (acknowledge → investigate → respond → monitor → close/recover), recovery framework (acknowledgment + concrete action + outcome proof). Cross-reference `social-media`; applies reputation layer. See `AGENTS.md`: `regions` guides jurisdiction/compliance differences (local: owner-level; national: committee/procurement escalation; international: legal review timelines vary by jurisdiction).

## When to Use This Skill
Apply for: negative mention spikes, competitor attacks, product/service failures visible on social, PR incidents, regulatory/news events impacting brand, crisis-level sentiment drops (>20% negative spike), legal/compliance risks in public claims (`claims-review` applies — see below).

---

## Core Framework (Crisis-Specific)
1. Confirm severity and jurisdiction (`regions` input guides legal review timeline: international requires jurisdiction-specific escalation). If claims/regulatory risk: route through `claims-review` before any public response.
2. Lock triggers: category definitions (negative spike / competitor / PR / failure / regulatory). Per-category response templates: public reply format, DM format, no-response criteria, approval levels (`approvers: [owner]` gate applies; critical responses may require `manager-maria` / `brand-voice-guardian` escalation — see `AGENTS.md` reference patterns).
3. Lock response timeline: acknowledge (<1h critical, <4h standard), investigate (<4h), respond (<8h), monitor (<24h cycle), close/recover (with proof). Apply `approve_content` gate before ANY public response.
4. Recovery narrative framework: acknowledgment (without admission of liability unless legal approves), concrete action taken, outcome proof (number / timeline / verification), trust-rebuild steps. Lock in `recovery_narrative`.

---

## Metrics & Benchmarks (Crisis-Specific)
| Metric | Good | Excellent | Note |
|-----------|------|-----------|------|
| Response Time (critical) | <1h | <30min | Manual review; `regions` guides timeline |
| Sentiment Recovery | Growing | Growing | Manual review; `social-analytics` feeds sentiment data (⚠️ NOT AVAILABLE if analytics unconfigured) |
| Escalation Accuracy | Growing | Growing | Manual review |

Note: No stub analytics server for sentiment tracking; rely on manual review, native analytics (if configured), or `social-analytics` rollups. Never invent crisis response times or sentiment numbers.

---

## Anti-Patterns (Crisis-Specific)
| Anti-Pattern | Fix |
| No written escalation rules | Lock `escalation_matrix` with owners + thresholds (`approvers: [owner]` gate applies) |
| Delayed first response | Lock timeline (<1h critical / <4h standard) in `response_plan` |
| Defensive/generic templates | Lock category-specific templates (acknowledgment + concrete action + proof) in `recovery_narrative` |
| No legal/compliance review for regulated claims | Route through `claims-review` before any public response |

---

## Related Skills
- `social-media` — applies this reputation layer; crisis response is a specialized layer of the broader framework
- `social-analytics` — feeds sentiment/recovery data; `social-engagement` — feeds escalation triggers
- `social-listening` — mention/competitor tracking feeds crisis detection
- `claims-review` — MANDATORY for any crisis involving product/service claims (legal/compliance gate before public response)
- `brand-building` — brand voice rules guide recovery narrative tone; `social-crisis` applies the voice under pressure
- `doddle.marketing.copywriting` — response templates; `conversion-copywriting` — persuasive recovery messaging framework
- `doddle.local.*` (local segment) — local reputation events (`local.reviews` / `local.gbp` for local service businesses)
- `doddle.b2b.*` (national/procurement) — procurement-level reputation events (`b2b.qbr` / `b2b.proposals`) for committee-facing crises
- `doddle.agency.marketing` — agency positioning must align with crisis response tone; `regions` guides jurisdiction-specific rules

---

## Questions to Ask
1. Severity and type of crisis (negative spike / competitor / PR / product failure / regulatory)?
2. Jurisdiction / `regions` (local / national / international)? — guides escalation timeline and legal review (`claims-review`).
3. Stakeholders / approvers identified (`approvers: [owner]` gate applies — critical responses may need manager/brand-guardian escalation)?
4. Analytics/MCP status — sentiment/recovery tracking configured? (⚠️ NOT AVAILABLE if unconfigured; see `AGENTS.md`: `hubspot.contacts` / `google-business-profile` / `stripe` / `sensortower` are stubs; no sentiment server in registry. Never fabricate crisis metrics.)
