---
name: social-youtube
id: doddle.marketing.social-youtube
version: 1.0.0
blueprint: ./blueprint.yaml
description: "YouTube-specific execution: long-form education/authority, retention optimization, playlists, subscriber growth, session-time."
---
# Social: YouTube
Social media execution for YouTube — long-form educational/authority content with retention >50%, playlists, thumbnails/CTR, subscriber growth. Cross-reference `social-media`; applies YouTube layer.

## When to Use This Skill
- Creating long-form educational/how-to video content (2-5 min)
- Building subscriber growth and session-time (playlists, end screens)
- Optimizing thumbnails/CTR and retention curves

---

## Core Framework (YouTube-Specific)
1. Confirm goal fits YouTube (education, authority, retention). For quick awareness → redirect to `social-tiktok` or `social-instagram`; for B2B/procurement → redirect to `social-linkedin`.
2. Lock pillars: educational (long-form dominant) + entertaining/retention-optimized + promotional (end-screen/CTA only, capped at 10%). Lock in `plan`.
3. Assets: script/hook (first 3 sec), chapters, thumbnail specs, end screens, playlist links. Lock in `assets`. Apply `approve_content` gate before `distribute`.
4. Cadence: 1-2x/week; lock schedule. Apply gate.
5. Growth: playlists for session time; end screens (subscribe + CTA); collaboration accounts; paid promotion (`paid-advertising`); cross-promotion (`email-marketing`, `content-strategy`). Apply gate.

## Metrics & Benchmarks
| Metric | Good | Excellent | Source |
|-----------|------|-----------|--------|
| Watch Time / Retention | Growing | >50% | Native analytics (no stub tool in registry — assume ⚠️ NOT AVAILABLE unless custom server configured) |
| Subscriber Growth Rate | Growing | Growing | Native analytics (⚠️ NOT AVAILABLE — requires YouTube data access) |
| Click-Through Rate (thumbnail) | Growing | Growing | Native analytics |

Note: YouTube native analytics (`youtube-analytics`) is NOT in the current `doddle-core/registry/integrations/_registry.md`. Any YouTube metric reported without a configured server must be labeled `assumed` or `⚠️ NOT AVAILABLE`, never fabricated. Cross-reference `social-analytics` for dashboard structure; reference `analytics-attribution` only for GA4-linked traffic (not native YouTube retention/subscribers).

## Anti-Patterns (YouTube-Specific)
| Anti-Pattern | Fix |
| Repurposing TikTok/Instagram without format adaptation | Adapt to long-form (2-5 min), chapters, playlists |
| No hook in first 3 seconds | Lock script hook in `assets` |
| No playlists / no session-time optimization | Include playlists and end screens in `assets` |
| No chapters / missing accessibility | Add chapters; captions always |

## Related Skills
- `social-media` — broader framework; applies YouTube layer
- `social-analytics` — measurement/reporting for retention/subscriber metrics (⚠️ NOT AVAILABLE without YouTube server)
- `social-engagement` — comment/DM response cadence for video audience
- `social-crisis` — reputation/crisis response for channel-level events
- `social-listening` — competitor/theme tracking feeds content planning
- `video-marketing` — deeper production specs, thumbnail testing, script framework
- `image` — thumbnail graphic production
- `content-strategy` — editorial calendar feeding cadence
- `paid-advertising` — paid promotion rules (`youtube-ads` not in registry; reference `paid-advertising` for paid amplification thresholds, not YouTube-specific targeting)
- `analytics-attribution` — cross-channel attribution linking YouTube traffic to conversions (GA4 only; native YouTube analytics separate)
- `agency-marketing` — case-study videos feed authority content; `regions` guides localization (subtitles, region-relevant examples)
- `doddle.local.gbp` / `doddle.local.reviews` (local services use YouTube for how-to/service tutorials) — local service businesses may use YouTube differently than B2B/procurement; `regions` applies

## Questions
1. Primary goal (education/authority/retention/subscribers/traffic/community)?
2. Audience fit confirmed (long-form vs quick awareness)?
3. Assets available (`video-marketing`, `image`)?
4. Analytics configured — or ⚠️ NOT AVAILABLE? (State setup steps; note `youtube-analytics` not in registry.)
5. Regions (`regions`): local/national/international? (Guides subtitle/localization and proof selection.)
