---
name: social-instagram
id: doddle.marketing.social-instagram
version: 1.0.0
blueprint: ./blueprint.yaml
description: "Instagram-specific execution: Reels (3-7x/week), Stories (daily), carousel education, saves/shares tracking, visual engagement for millennial/Gen-Z audiences."
---
# Social: Instagram

When executing visual brand content on Instagram specifically — awareness through Reels, saves/shares as high-intent signals, Stories for daily engagement, carousel posts for education. Cross-reference `social-media` for broader pillar framework; this applies the Instagram layer.

## When to Use This Skill
- Creating Instagram Reels, Stories, carousels for brand/lifestyle/products
- Building saves/shares as high-intent signals
- Measuring Instagram-specific metrics (Reels completion >50%, save rate >5%)
- Responding to visual content needs for millennial/Gen-Z audiences

---

## Initial Assessment
1. **Platform fit**: Does the client's goal (awareness, engagement, leads) align with Instagram's strengths (visual, lifestyle, Reels, saves)? Check `social-media` matrix.
2. **Content inventory**: Assets from `social-media`, `content-strategy`, `video-marketing`, `image`? What must be created?
3. **Performance state**: Analytics/MCP configured (Instagram native analytics not in current registry — assume ⚠️ NOT AVAILABLE unless configured separately)? Use `social-analytics` for deeper reporting.
4. **Regions**: `regions` input guides proof/cadence (local/national/international per `AGENTS.md` guidance).

---

## Inputs/Outputs
Inputs: `brief` (required), `channel` (optional — Instagram), `budget` (optional — paid boost/Reels ads), `regions` (optional — local | national | international).
Outputs: `plan` (markdown: strategy, cadence, format mix) + `assets` (json: copy, Reels script, carousel slides, schedule, CTA).

---

## Core Framework (Instagram-Specific)
5. **Regions (`regions` input)**: `local` guides local proof (`local.gbp`, `local.reviews`, `local.pages`); `national` guides national/procurement proof (`b2b.proposals`, `b2b.rfp`, `b2b.qbr`); `international` guides region-localized metrics/content (`regions` normalization per `AGENTS.md`). Flag as assumption if unstated.

### 1. Confirm Platform-Goal Fit: Instagram excels at awareness + saves. For procurement/committee leads → redirect to `social-media` (LinkedIn) or `b2b.proposals`.
### 2. Lock Native Pillars: Educational (carousel/post) 40% + Entertaining/Inspirational (Reels) 50% + Promotional 10%. Lock in `plan`.
### 3. Create Native Assets: Reels (hook 0.5s, vertical, captions, trending sounds); carousel (hook slide 1, value slides 2-8, CTA final); Stories (polls, questions, swipe-ups); static (high-quality, minimal text, save-worthy info). Lock in `assets`.
### 4. Cadence: Reels 3-7x/week; Stories daily; carousel 1-2x/week. Best windows: Mon-Fri 11am, 2pm, 7pm (local time). Lock schedule in `assets`. Apply `approve_content` gate before `distribute`.
### 5. Growth/Engagement Rules: Respond to comments within 1 hour; feature UGC/community; collaboration accounts for reach; boost only when organic saves/engagement exceeds 2%. Apply gate.

---

## Metrics & Benchmarks
| Metric | Good | Excellent | Note |
| Engagement Rate | 1-3% | 3%+ | Native analytics |
| Save Rate | 2-5% | 5%+ | High-intent signal; track in `social-analytics` |
| Reels Completion | Growing | >50% | Watch-time critical; reference `social-analytics` |
| Reach Growth | Growing | Growing | `social-listening` (trend tracking) feeds growth |

---

## Anti-Patterns (Instagram-Specific)
| Anti-Pattern | Fix |
| Same content copied unchanged | Rewrite/reformat per native specs (carousel/Reels/Stories) |
| No hook / first-second hook missing | Lock hook in Reels script (`assets`) |
| All promotional content | Lock pillar ratio (value-heavy) in `plan` |
| No saves / missing save-worthy info | Design carousel content for saves (`assets`) |

---

## Related Skills (Cross-Pack)
- `social-media` — broader pillar framework; this applies Instagram layer
- `social-analytics` — measurement (`plan` feeds dashboard)
- `social-engagement` — response cadence; community management rules apply here
- `social-crisis` — reputation/crisis response (`regions` input guides jurisdiction)
- `social-listening` — trend/competitor tracking feeds `plan`
- `video-marketing` — deeper video specs; Reels production specs
- `image` — graphic/carousel design production
- `content-strategy` — editorial calendar feeding cadence
- `paid-advertising` — paid amplification rules (`budget` input feeds thresholds)
- `analytics-attribution` — UTM attribution linking Instagram traffic
- `agency-marketing` — agency positioning feeds visual brand themes; `regions` dimension applies
- `b2b.proposals` / `b2b.rfp` (national/procurement) — awareness only; formal sales use `b2b` skills
- `local.gbp` / `local.reviews` (local segment) — GBP optimization/review flows complement Instagram local presence

---

## Questions
1. Goal (awareness, engagement, leads, traffic, community)?
2. Platform fit confirmed? (If B2B/procurement → redirect to `social-media`/LinkedIn/`b2b.proposals`).
3. Assets available (`social-media`, `content-strategy`, `video-marketing`, `image`)?
4. Analytics/MCP configured — or assume ⚠️ NOT AVAILABLE (`tiktok.trending` stub if used; `crosspost.publish` requires config; `ga4.getReport` requires GA4 setup)?
5. Regions (`regions`): local/national/international?
