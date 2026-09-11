---
description: Create education content plan for programs and market
argument-hint: [programs market]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `edu-content` (id `doddle.edu.content`), `content-strategy`, `seo-mastery` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Student privacy**: Never request or store student PII; use de-identified examples only.

---

## Interactive Parameter Collection

### Step 1: Ask Programs

**Question:** "Which programs to create content for?"
**Header:** "Programs"
**MultiSelect:** true

**Options:**
- **Undergraduate** - Bachelor / associate programs
- **Graduate** - Master / MBA / doctorate
- **Certificate** - Short courses, bootcamps

---

### Step 2: Ask Market

**Question:** "What is the target market?"
**Header:** "Market"
**MultiSelect:** false

**Options:**
- **Domestic** - Local / national students
- **International** - Overseas recruitment
- **Working adults** - Part-time / online learners

---

### Step 3: Confirmation

**Display summary:**
- Programs: [programs]
- Market: [market]
- Skill: edu-content (`doddle.edu.content`)

**Question:** "Proceed with content planning?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, create plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `programs` + `market` from steps above.
2. **Run skill blueprint** - Execute `doddle-education-skills/.claude/skills/edu-content/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Content pillars and editorial plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, content-plan recommendations.
Save to: `./docs/edu/edu-content-[slug].md`
