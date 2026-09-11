---
description: Plan creator monetization by audience size
argument-hint: [audience-size niche]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `creator-monetization` (id `doddle.creator.monetization`), `pricing-strategy`, `offers` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Audience Size

**Question:** "What is the current audience size?"
**Header:** "Audience Size"
**MultiSelect:** false

**Options:**
- **Starting out** - Under 1k followers / subs
- **Growing** - 1k to 100k followers / subs
- **Established** - 100k+ followers / subs

---

### Step 2: Ask Niche

**Question:** "What is the content niche?"
**Header:** "Niche"
**MultiSelect:** false

**Options:**
- **Enter niche** - I'll share the niche / topic area
- **Skip** - Use general creator placeholder

---

### Step 3: Confirmation

**Display summary:**
- Audience size: [audience_size]
- Niche: [niche]
- Skill: creator-monetization (`doddle.creator.monetization`)

**Question:** "Proceed with monetization plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan it** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `audience_size` + `niche` from steps above.
2. **Run skill blueprint** - Execute `doddle-creator-skills/.claude/skills/creator-monetization/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Monetization roadmap with revenue streams per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored revenue streams, prioritized offers, monetization recommendations.
Save to: `./docs/creator/creator-monetization-[slug].md`
