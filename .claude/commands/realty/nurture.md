---
description: Build buyer and seller nurture sequences for long-term follow-up
argument-hint: [segment database_size]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `realty-nurture` (id `doddle.realty.nurture`), `email-sequence`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Fair Housing**: Never use discriminatory language; comply with Fair Housing Act in all copy.

---

## Interactive Parameter Collection

### Step 1: Ask Segment

**Question:** "Which segment to nurture?"
**Header:** "Segment"
**MultiSelect:** false

**Options:**
- **Buyers** - Active / future home buyers
- **Sellers** - Current / future home sellers
- **Past clients / Sphere** - Referral and repeat base

---

### Step 2: Ask Database Size

**Question:** "What is the database size?"
**Header:** "Database Size"
**MultiSelect:** false

**Options:**
- **Enter size** - I'll share contact count / CRM size
- **Skip** - Use generic sizing assumptions

---

### Step 3: Confirmation

**Display summary:**
- Segment: [segment]
- Database size: [database_size]
- Skill: realty-nurture (`doddle.realty.nurture`)

**Question:** "Proceed with nurture sequence?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `segment` + `database_size` from steps above.
2. **Run skill blueprint** - Execute `doddle-real-estate-skills/.claude/skills/realty-nurture/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Nurture sequences and follow-up cadence per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, nurture-sequence recommendations.
Save to: `./docs/realty/realty-nurture-[slug].md`
