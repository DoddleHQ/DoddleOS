---
description: Generate content ideas for niche and platform
argument-hint: [niche platform]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `creator-ideation` (id `doddle.creator.ideation`), `content-strategy`, `marketing-ideas` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Niche

**Question:** "What is the content niche?"
**Header:** "Niche"
**MultiSelect:** false

**Options:**
- **Enter niche** - I'll share the niche / topic area
- **Skip** - Use general creator placeholder

---

### Step 2: Ask Platform

**Question:** "Which platform is this for?"
**Header:** "Platform"
**MultiSelect:** false

**Options:**
- **YouTube** - Long-form video ideas
- **TikTok / Shorts / Reels** - Short-form video ideas
- **Other** - Blog, podcast, or multi-platform

---

### Step 3: Confirmation

**Display summary:**
- Niche: [niche]
- Platform: [platform]
- Skill: creator-ideation (`doddle.creator.ideation`)

**Question:** "Proceed with ideation?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, generate** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `niche` + `platform` from steps above.
2. **Run skill blueprint** - Execute `doddle-creator-skills/.claude/skills/creator-ideation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Idea pipeline with scored angles per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored ideas, prioritized angles, content recommendations.
Save to: `./docs/creator/creator-ideation-[slug].md`
