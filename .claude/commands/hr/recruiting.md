---
description: Create job posting and sourcing plan for open role
argument-hint: [role company]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `hr-recruiting` (id `doddle.hr.recruiting`), `copywriting`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Role

**Question:** "What role are you hiring for?"
**Header:** "Role"
**MultiSelect:** false

**Options:**
- **Enter role** - I'll share the job title + level
- **Skip** - Use generic role placeholder

---

### Step 2: Ask Company

**Question:** "What is the company name?"
**Header:** "Company"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the company name
- **Skip** - Use generic company placeholder

---

### Step 3: Confirmation

**Display summary:**
- Role: [role]
- Company: [company]
- Skill: hr-recruiting (`doddle.hr.recruiting`)

**Question:** "Proceed with recruiting plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, create plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `role` + `company` from steps above.
2. **Run skill blueprint** - Execute `doddle-hr-skills/.claude/skills/hr-recruiting/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Job posting and sourcing plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, recruiting recommendations.
Save to: `./docs/hr/hr-recruiting-[slug].md`
