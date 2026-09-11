---
description: Plan and promote education open house event for attendance
argument-hint: [institution event-date]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `edu-openhouse` (id `doddle.edu.openhouse`), `page-cro`, `email-sequence` skills.

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

### Step 2: Ask Event Date

**Question:** "When is the open house event?"
**Header:** "Event Date"
**MultiSelect:** false

**Options:**
- **Enter date** - I'll share the event date
- **TBD** - Plan without fixed date

---

### Step 3: Confirmation

**Display summary:**
- Institution: [institution]
- Event date: [event_date]
- Skill: edu-openhouse (`doddle.edu.openhouse`)

**Question:** "Proceed with open house planning?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `institution` + `event_date` from steps above.
2. **Run skill blueprint** - Execute `doddle-education-skills/.claude/skills/edu-openhouse/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Event promo plan and attendance drivers per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, open-house promo recommendations.
Save to: `./docs/edu/edu-openhouse-[slug].md`
