---
description: Package video with titles thumbnails and hooks
argument-hint: [video-topic niche]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `creator-packaging` (id `doddle.creator.packaging`), `copywriting`, `marketing-psychology` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Video Topic

**Question:** "What is the video topic?"
**Header:** "Video Topic"
**MultiSelect:** false

**Options:**
- **Enter topic** - I'll share the video topic / draft title
- **Skip** - Use generic topic placeholder

---

### Step 2: Ask Niche

**Question:** "What is the channel niche?"
**Header:** "Niche"
**MultiSelect:** false

**Options:**
- **Enter niche** - I'll share the niche / audience area
- **Skip** - Use general creator placeholder

---

### Step 3: Confirmation

**Display summary:**
- Video topic: [video_topic]
- Niche: [niche]
- Skill: creator-packaging (`doddle.creator.packaging`)

**Question:** "Proceed with packaging?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, package** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `video_topic` + `niche` from steps above.
2. **Run skill blueprint** - Execute `doddle-creator-skills/.claude/skills/creator-packaging/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Title, thumbnail, and hook package per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored package options, prioritized picks, CTR recommendations.
Save to: `./docs/creator/creator-packaging-[slug].md`
