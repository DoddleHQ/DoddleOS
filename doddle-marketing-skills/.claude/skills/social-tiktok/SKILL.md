---
name: social-tiktok
id: doddle.marketing.social-tiktok
version: 1.0.0
blueprint: ./blueprint.yaml
description: "TikTok-specific execution: Gen-Z short-form video, trend/hook mechanics, sound-driven content, watch-time optimization."
---
# Social: TikTok
Social media execution for TikTok — awareness and reach for Gen-Z / younger millennials. Cross-reference `social-media` for broader framework; this applies the TikTok layer.

## When to Use This Skill
- Creating Gen-Z/short-form video content (1-3x/day)
- Trend/hook optimization (first 0.5 sec hook, trending sounds, duets/stitches)
- Watch-time / completion-rate optimization (>50% target)
- Building shares as primary growth signal

---

## Core Framework (TikTok-Specific)
1. Confirm goal fits TikTok (awareness, reach, Gen-Z). For B2B/procurement leads, redirect to `social-media` / `social-linkedin` / `b2b.proposals`.
2. Lock pillars: entertaining (30%) + educational (40%) + inspirational (20%) + promotional (10%). Lock ratio in `plan`.
3. Assets: hook script (first 0.5 sec), trend/sound reference, vertical format (9:16, <60s), caption + hashtags, CTA. Lock in `assets`. Apply `approve_content` gate before `distribute`.
4. Cadence: 1-3x/day; best times: Tue-Thu 7-9pm (local). Lock in `assets`.
5. Growth: collaboration/duets; trend participation (`tiktok.trending` — stub, requires setup, shows ⚠️ NOT AVAILABLE); paid amplification (`paid-advertising`) when organic exceeds threshold; cross-promotion (`email-marketing`, `content-strategy`). Apply gate.

## Metrics & Benchmarks
| Metric | Good | Excellent | Source |
| Engagement Rate (watch-time) | Growing | >50% completion | Native analytics |
| Share Rate | Growing | Growing | Native analytics |
| Follower Growth Rate | >5%/mo | >10%/mo | Native analytics |
| Trending Sound Alignment | Partial | Full | `tiktok.trending` (stub) |

## Anti-Patterns (TikTok-Specific)
| Anti-Pattern | Fix |
| Repurposed unchanged from YouTube/Instagram | Rewrite/reformat: vertical 9:16, under 60s, hook in 0.5s |
| Slow hook (miss first 0.5 sec) | Lock hook script in assets |
| No trending sound / no caption | Monitor trends (stub); always include captions |

## Related Skills
- `social-media` — broader framework; this applies the TikTok layer
- `social-analytics` — measurement; `social-engagement` — community response; `social-crisis` — reputation
- `video-marketing` — deeper production specs; `image` — thumbnail production
- `paid-advertising` — Spark Ads / paid amplification thresholds
- `analytics-attribution` — cross-channel attribution linking TikTok traffic
- Local: `local.gbp` / `local.reviews` (service-area proof videos); International: region-localized content (subtitles, region-trending sounds)

## Questions
1. Primary goal for TikTok (awareness, engagement, leads, community)?
2. Gen-Z/younger millennial audience confirmed?
3. Video assets available (`video-marketing`, `image`)?
4. Analytics/MCP (`tiktok.trending` stub — requires API key/config)?
5. Regions (`regions` input): local/national/international?
