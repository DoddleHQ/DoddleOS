---
description: Build applicant nurture sequence for segment and cycle
argument-hint: [segment cycle]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `edu-nurture` (id `doddle.edu.nurture`), `email-sequence`, `marketing-psychology` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Student privacy**: Never request or store student PII; use de-identified examples only.

---

## Interactive Parameter Collection

### Step 1: Ask Segment

**Question:** "Which applicant segment to nurture?"
**Header:** "Segment"
**MultiSelect:** false

**Options:**
- **Inquiries** - New leads, info requests
- **Applicants** - Started but not submitted
- **Admitted** - Accepted, yield stage

---

### Step 2: Ask Cycle

**Question:** "Which admissions cycle?"
**Header:** "Cycle"
**MultiSelect:** false

**Options:**
- **Fall intake** - Main enrollment cycle
- **Spring intake** - Secondary cycle
- **Rolling** - Continuous admissions

---

### Step 3: Confirmation

**Display summary:**
- Segment: [segment]
- Cycle: [cycle]
- Skill: edu-nurture (`doddle.edu.nurture`)

**Question:** "Proceed with nurture sequence?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `segment` + `cycle` from steps above.
2. **Run skill blueprint** - Execute `doddle-education-skills/.claude/skills/edu-nurture/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Nurture sequence and conversion plays per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, nurture-sequence recommendations.
Save to: `./docs/edu/edu-nurture-[slug].md`
