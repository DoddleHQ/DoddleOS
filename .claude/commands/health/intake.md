---
description: Optimize healthcare patient intake flow for completion rate
argument-hint: [practice-name specialty]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `healthcare-intake` (id `doddle.health.intake`), `form-cro`, `onboarding-cro`, `copy-editing` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**HIPAA**: Never request or store PHI; review form structure only, no patient data.

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
- **Dental** - New-patient intake forms
- **Medical** - Registration / history intake
- **Aesthetic / Physio / Other** - Consult intake

---

### Step 3: Confirmation

**Display summary:**
- Practice: [practice_name]
- Specialty: [specialty]
- Skill: healthcare-intake (`doddle.health.intake`)

**Question:** "Proceed with intake optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_name` + `specialty` from steps above.
2. **Run skill blueprint** - Execute `doddle-healthcare-skills/.claude/skills/healthcare-intake/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Intake friction audit and completion-rate fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, intake-flow recommendations.
Save to: `./docs/health/healthcare-intake-[slug].md`
