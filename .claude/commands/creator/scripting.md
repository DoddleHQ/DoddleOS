---
description: Write creator script for topic and format
argument-hint: [topic format]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `creator-scripting` (id `doddle.creator.scripting`), `copywriting`, `video-marketing` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Topic

**Question:** "What is the video topic?"
**Header:** "Topic"
**MultiSelect:** false

**Options:**
- **Enter topic** - I'll share the topic / title idea
- **Skip** - Use generic topic placeholder

---

### Step 2: Ask Format

**Question:** "Which script format?"
**Header:** "Format"
**MultiSelect:** false

**Options:**
- **Long-form** - YouTube deep-dive script
- **Short-form** - TikTok / Shorts / Reels script
- **Other** - Podcast, tutorial, or custom format

---

### Step 3: Confirmation

**Display summary:**
- Topic: [topic]
- Format: [format]
- Skill: creator-scripting (`doddle.creator.scripting`)

**Question:** "Proceed with scripting?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, write script** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `topic` + `format` from steps above.
2. **Run skill blueprint** - Execute `doddle-creator-skills/.claude/skills/creator-scripting/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Full script with hooks and retention beats per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored script, hook options, retention recommendations.
Save to: `./docs/creator/creator-scripting-[slug].md`
