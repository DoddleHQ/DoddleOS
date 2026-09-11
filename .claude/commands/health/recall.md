---
description: Build healthcare patient recall and reactivation campaign
argument-hint: [practice-name specialty]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `healthcare-recall` (id `doddle.health.recall`), `email-sequence`, `sms`, `email-marketing` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**HIPAA**: Never request or store PHI; use de-identified segments only.

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
- **Dental** - Hygiene / treatment recall
- **Medical** - Follow-up / annual recall
- **Aesthetic / Physio / Other** - Repeat-visit recall

---

### Step 3: Confirmation

**Display summary:**
- Practice: [practice_name]
- Specialty: [specialty]
- Skill: healthcare-recall (`doddle.health.recall`)

**Question:** "Proceed with recall campaign?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_name` + `specialty` from steps above.
2. **Run skill blueprint** - Execute `doddle-healthcare-skills/.claude/skills/healthcare-recall/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Recall segments, message sequence, and reactivation plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: segments, sequence drafts, send cadence, reactivation recommendations.
Save to: `./docs/health/healthcare-recall-[slug].md`
