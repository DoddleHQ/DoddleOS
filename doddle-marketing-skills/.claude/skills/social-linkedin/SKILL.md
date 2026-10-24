---
name: social-linkedin
id: doddle.marketing.social-linkedin
version: 1.0.0
blueprint: ./blueprint.yaml
description: LinkedIn-specific strategy, content creation, and optimization for B2B/professional audiences.
---
# Social: LinkedIn
When creating B2B/professional content — document/carousel posts, thought leadership, lead-generation, or authority building — on LinkedIn specifically. See `social-media` for broader cross-platform strategy.

## When to Use
Apply when the client's goal (leads, authority, B2B awareness) matches LinkedIn's strengths (professional decision-makers, document/carousel dwell time, sponsored lead-gen). Confirm via `social-media` matrix. If the client's audience isn't professional/B2B, redirect to `social-media` for platform selection.

## Core Framework (LinkedIn-Specific)
5. **Regions (`regions` input)**: `local` guides local proof (`local.gbp`, `local.reviews`, `local.pages`); `national` guides national/procurement proof (`b2b.proposals`, `b2b.rfp`, `b2b.qbr`); `international` guides region-localized metrics/content (`regions` normalization per `AGENTS.md`). Flag as assumption if unstated.

### 1. Lock Professional Pillars: Educational (document/carousel) + Thought Leadership (long-form) + Promotional (10% max, with proof). Ratio: 50% educational / 30% thought leadership / 10% promotional / 10% entertaining/inspirational.
### 2. Create Native Assets: Document/carousel for dwell time; native video (under 60s) preferred over links; no outbound links in post body; CTAs in comments.
### 3. Cadence: Post 3-5x/week (Tue-Thu best: 8-10am, 12pm). Lock schedule in `assets`. Apply `approve_content` gate before `crosspost.publish`.

## Metrics & Benchmarks
| Metric | Good | Excellent | Source |
|-----------|------|-----------|--------|
| Engagement Rate | 2-3% | 3%+ | Native analytics |
| Profile Views | Growing | Growing | Native analytics |
| Document Dwell Time | Growing | Growing | Native analytics |
| Sponsored CTR | >2% | >3% | Ad + GA |

## Anti-Patterns (LinkedIn-Specific)
| Mistake | Fix |
|---------|-----|
| Same promotional content everywhere | Lock pillar ratio in `plan` (value-heavy) |
| No hook / first line in document/post | Lock hook line per asset |
| Outbound links in body (penalized by algorithm) | Put links in comments; native document preferred |
| Broadcasting without conversation | Respond to comments within 1 hour (`social-engagement`) |

## Related Skills
- `social-media` — broader strategy; this applies the LinkedIn layer
- `social-analytics` — measurement & dashboards for these metrics
- `social-engagement` — daily response cadence
- `doddle.b2b.proposals` — proposal links shared in threads for credibility
- `doddle.agency.marketing` — agency positioning feeds thought leadership themes
- `doddle.local.gbp` — not directly; national/procurement context applies (`doddle.b2b.rfp`), local uses different proof stack

## Questions
1. Primary goal for LinkedIn (awareness, leads, authority, community)?
2. B2B/professional audience confirmed?
3. Assets available (documents, carousels, video)?
4. Analytics configured — or ⚠️ NOT AVAILABLE?
5. Regions: local (service-area authority), national (committee/procurement awareness), international (localized thought leadership)?
