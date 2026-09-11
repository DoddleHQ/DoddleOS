---
description: Optimize education enrollment funnel for application rate
argument-hint: [institution program]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `edu-enrollment` (id `doddle.edu.enrollment`), `signup-flow-cro`, `form-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Student privacy**: Never request or store student PII; use de-identified examples only.

---

## Interactive Parameter Collection

### Step 1: Ask Institution

**Question:** "What is the institution name?"
**Header:** "Institution"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the institution name
- **Skip** - Use generic institution placeholder

---

### Step 2: Ask Program

**Question:** "Which program to optimize enrollment for?"
**Header:** "Program"
**MultiSelect:** false

**Options:**
- **Undergraduate** - Bachelor / associate degrees
- **Graduate** - Master / MBA / doctorate
- **Certificate / Other** - Short courses, bootcamps

---

### Step 3: Confirmation

**Display summary:**
- Institution: [institution]
- Program: [program]
- Skill: edu-enrollment (`doddle.edu.enrollment`)

**Question:** "Proceed with enrollment optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `institution` + `program` from steps above.
2. **Run skill blueprint** - Execute `doddle-education-skills/.claude/skills/edu-enrollment/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Enrollment friction audit and application-rate fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, enrollment-funnel recommendations.
Save to: `./docs/edu/edu-enrollment-[slug].md`
