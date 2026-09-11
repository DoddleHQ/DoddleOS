---
description: Plan publishing schedule across channels
argument-hint: [channels cadence]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `creator-publishing` (id `doddle.creator.publishing`), `content-strategy`, `social-media` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Channels

**Question:** "Which channels are you publishing to?"
**Header:** "Channels"
**MultiSelect:** true

**Options:**
- **YouTube** - Long-form publishing
- **TikTok / Shorts / Reels** - Short-form distribution
- **Other** - Newsletter, podcast, or blog

---

### Step 2: Ask Cadence

**Question:** "What is the publishing cadence?"
**Header:** "Cadence"
**MultiSelect:** false

**Options:**
- **Weekly** - Steady sustainable pace
- **Multi-weekly** - 2-3x per week growth pace
- **Daily** - High-volume output pace

---

### Step 3: Confirmation

**Display summary:**
- Channels: [channels]
- Cadence: [cadence]
- Skill: creator-publishing (`doddle.creator.publishing`)

**Question:** "Proceed with publishing plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan it** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `channels` + `cadence` from steps above.
2. **Run skill blueprint** - Execute `doddle-creator-skills/.claude/skills/creator-publishing/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Publishing calendar and distribution plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored schedule, prioritized actions, distribution recommendations.
Save to: `./docs/creator/creator-publishing-[slug].md`
