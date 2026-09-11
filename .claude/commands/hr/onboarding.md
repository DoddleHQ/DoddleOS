---
description: Build onboarding plan for new hire by start date
argument-hint: [role start-date]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `hr-onboarding` (id `doddle.hr.onboarding`), `content-strategy`, `copywriting` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Role

**Question:** "What role is the new hire starting in?"
**Header:** "Role"
**MultiSelect:** false

**Options:**
- **Enter role** - I'll share the job title + level
- **Skip** - Use generic role placeholder

---

### Step 2: Ask Start Date

**Question:** "What is the start date?"
**Header:** "Start Date"
**MultiSelect:** false

**Options:**
- **Enter date** - I'll share the start date
- **ASAP** - Starting immediately, plan from day one

---

### Step 3: Confirmation

**Display summary:**
- Role: [role]
- Start date: [start_date]
- Skill: hr-onboarding (`doddle.hr.onboarding`)

**Question:** "Proceed with onboarding plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `role` + `start_date` from steps above.
2. **Run skill blueprint** - Execute `doddle-hr-skills/.claude/skills/hr-onboarding/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Onboarding timeline and checklist per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, onboarding recommendations.
Save to: `./docs/hr/hr-onboarding-[slug].md`
