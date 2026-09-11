---
description: Screen applicants and rank candidates for open role
argument-hint: [role applicants]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `hr-screening` (id `doddle.hr.screening`), `analytics-attribution`, `problem-solving` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Role

**Question:** "What role are you screening for?"
**Header:** "Role"
**MultiSelect:** false

**Options:**
- **Enter role** - I'll share the job title + level
- **Skip** - Use generic role placeholder

---

### Step 2: Ask Applicants

**Question:** "How will you provide applicant info?"
**Header:** "Applicants"
**MultiSelect:** false

**Options:**
- **Paste summaries** - I'll paste resumes / summaries
- **Describe pool** - I'll describe count + background mix

---

### Step 3: Confirmation

**Display summary:**
- Role: [role]
- Applicants: [applicants]
- Skill: hr-screening (`doddle.hr.screening`)

**Question:** "Proceed with candidate screening?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, screen** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `role` + `applicants` from steps above.
2. **Run skill blueprint** - Execute `doddle-hr-skills/.claude/skills/hr-screening/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Ranked shortlist with screening rationale per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, screening recommendations.
Save to: `./docs/hr/hr-screening-[slug].md`
