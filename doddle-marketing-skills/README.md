# Doddle Marketing OS

> Independent marketing OS pack: 49 skills covering CRO, copy, SEO, growth, content, and analytics.

## Overview

Independent OS pack for [DoddleOS](https://github.com/doddleOS/doddleOS-marketing). Installs and runs standalone. One of 14 peer packs (marketing + 13 vertical OS packs). Cross-pack binding only via blueprint `call` nodes where noted.

## Skills Included

| Group | Skills |
|-------|--------|
| Core | `marketing-fundamentals`, `marketing-psychology`, `marketing-ideas`, `seo-mastery`, `social-media`, `email-marketing`, `paid-advertising`, `content-strategy`, `analytics-attribution`, `brand-building`, `problem-solving` |
| CRO | `page-cro`, `form-cro`, `popup-cro`, `signup-flow-cro`, `onboarding-cro`, `paywall-upgrade-cro`, `ab-test-setup` |
| Content & Copy | `copywriting`, `copy-editing`, `email-sequence`, `conversion-copywriting` |
| SEO & Growth | `programmatic-seo`, `schema-markup`, `competitor-alternatives`, `launch-strategy`, `pricing-strategy`, `referral-program`, `free-tool-strategy` |
| Specialized | `ai-seo`, `aso`, `churn-prevention`, `cold-email`, `community-building`, `customer-research`, `directory-submissions`, `events`, `image`, `influencer-marketing`, `lead-magnets`, `marketing-loops`, `offers`, `partnerships`, `product-led-growth`, `product-marketing`, `public-relations`, `revops`, `sms`, `video-marketing`, `document-skills` |

## Installation

```bash
/plugin marketplace add doddleOS/doddleOS-marketing
/plugin install doddle-marketing-skills@doddleOS-marketing
```

Manual: `cp -r doddle-marketing-skills/.claude/skills/* your-project/.claude/skills/`
Agents (bundled, isolated): `cp -r doddle-marketing-skills/.claude/agents/* your-project/.claude/agents/`

## Agents (bundled)

Self-contained copies. No cross-pack agent refs: `brainstormer`, `brand-voice-guardian`, `continuity-specialist`, `conversion-optimizer`, `copywriter`, `email-wizard`, `planner`, `project-manager`, `researcher`, `sales-enabler`, `seo-specialist`.

## Optional bindings

Peer packs bind via blueprint `call` nodes (`type: call`, `ref: doddle.<domain>.<skill>`). No install dependency on any other pack. Kernel only: `doddle-core` spec v2 + `doddle.tool.v1` tools.

## Validate

```bash
python3 doddle-core/scripts/validate.py   # 0 errors target
```

## License

MIT License - Same as DoddleOS core
