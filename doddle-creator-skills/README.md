# Doddle Creator Skills

> Creator-economy skills for ideation, scripting, packaging, publishing, and monetization.

## Overview

Add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). Turns posting into a system: position → script → package → publish → get paid.

Naming: pack dir `doddle-creator-skills`, skills `creator-*`, IDs `doddle.creator.*`, commands `/creator:*`.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `creator-ideation` | Niche, pillars, hooks bank, format fit | `/creator:ideation` |
| `creator-scripting` | Retention scripts, open loops, CTAs | `/creator:scripting` |
| `creator-packaging` | Thumbnails + titles, CTR testing | `/creator:packaging` |
| `creator-publishing` | Cadence, cross-post, repurpose SOP | `/creator:publishing` |
| `creator-monetization` | Sponsors, affiliates, products, media kit | `/creator:monetization` |

## Installation

```bash
/plugin marketplace add doddleOS/doddle-creator-skills
/plugin install doddle-creator-skills@doddle-creator-skills
```

Manual: `cp -r doddle-creator-skills/.claude/skills/* your-project/.claude/skills/`

## What Each Skill Covers

### creator-ideation (Noise → Position)
- Niche down to ownable angle (topic × audience × format)
- 3-5 content pillars with proof of demand
- Hooks bank (100+ angles per pillar)
- Format-market fit (long vs short vs live per platform)

### creator-scripting (Idea → Retention)
- Hook-first structure (payoff promised <3s)
- Open loops + re-hooks every 20-30s
- CTA placement (subscribe, comment bait, next video)
- Short-form vs long-form script templates

### creator-packaging (Video → Click)
- Thumbnail anatomy (3 elements max, face + emotion + contrast)
- Title formulas (curiosity + specificity, <60 chars)
- CTR testing cadence (2-3 variants, 48h reads)
- Outlier analysis (own + competitor 10x videos)

### creator-publishing (One Video → Everywhere)
- Cadence by platform (volume vs quality math)
- Cross-post matrix (YT → Shorts/Reels/TikTok/X/Newsletter)
- Repurpose SOP (long → clips → carousels → threads)
- Scheduling + analytics review ritual

### creator-monetization (Audience → Income)
- Revenue stack (ads, sponsors, affiliates, products)
- Rate card + media kit (CPM by niche, deliverables)
- Sponsor outreach + negotiation (usage rights, renewals)
- Digital product ladder (freebie → $29 → $299 → cohort)

## Audit Coverage

| Audit Requirement | Skill |
|-------------------|-------|
| Positioning clarity + pillar demand | `creator-ideation` |
| Retention + avg view duration | `creator-scripting` |
| CTR + outlier rate | `creator-packaging` |
| Output volume + repurpose ratio | `creator-publishing` |
| RPM + sponsor pipeline | `creator-monetization` |

## Dependencies

Core skills (no new integration needed):
- `video-marketing` - Video fundamentals
- `social-media` - Platform distribution
- `content-strategy` - Pillars + calendar
- `copywriting`, `conversion-copywriting` - Hooks + titles
- `image` - Thumbnail production
- `ab-test-setup` - CTR testing
- `offers`, `pricing-strategy` - Monetization stack
- `partnerships` - Sponsor deals
- Integrations: `tiktok` (trends), `crosspost` (publish), `semrush` (keyword demand), `notion` (banks, calendars)

## License

MIT License - Same as Doddle Marketing OS core
