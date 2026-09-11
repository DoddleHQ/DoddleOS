---
description: Optimize healthcare appointment booking flow for show rate
argument-hint: [practice-name specialty]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `healthcare-booking` (id `doddle.health.booking`), `page-cro`, `form-cro`, `signup-flow-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**HIPAA**: Never request or store PHI; use de-identified examples only.

---

## Interactive Parameter Collection

### Step 1: Ask Practice Name

**Question:** "What is the practice name?"
**Header:** "Practice Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the practice name
- **Skip** - Use generic practice placeholder

---

### Step 2: Ask Specialty

**Question:** "What is the practice specialty?"
**Header:** "Specialty"
**MultiSelect:** false

**Options:**
- **Dental** - General / cosmetic / ortho
- **Medical** - Primary care / specialty clinic
- **Aesthetic / Physio / Other** - Elective or allied health

---

### Step 3: Confirmation

**Display summary:**
- Practice: [practice_name]
- Specialty: [specialty]
- Skill: healthcare-booking (`doddle.health.booking`)

**Question:** "Proceed with booking optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_name` + `specialty` from steps above.
2. **Run skill blueprint** - Execute `doddle-healthcare-skills/.claude/skills/healthcare-booking/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Booking friction audit and show-rate fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, booking-flow recommendations.
Save to: `./docs/health/healthcare-booking-[slug].md`
