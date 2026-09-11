---
description: Promote open house events to drive attendance and offers
argument-hint: [listing_address event_date]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `realty-openhouse` (id `doddle.realty.openhouse`), `social-media`, `email-sequence` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Fair Housing**: Never use discriminatory language; comply with Fair Housing Act in all copy.

---

## Interactive Parameter Collection

### Step 1: Ask Listing Address

**Question:** "What is the listing address?"
**Header:** "Listing Address"
**MultiSelect:** false

**Options:**
- **Enter address** - I'll share the property address
- **Skip** - Use generic address placeholder

---

### Step 2: Ask Event Date

**Question:** "What is the open house date?"
**Header:** "Event Date"
**MultiSelect:** false

**Options:**
- **Enter date** - I'll share date / time window
- **Skip** - Use TBD placeholder

---

### Step 3: Confirmation

**Display summary:**
- Listing address: [listing_address]
- Event date: [event_date]
- Skill: realty-openhouse (`doddle.realty.openhouse`)

**Question:** "Proceed with open house promotion?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `listing_address` + `event_date` from steps above.
2. **Run skill blueprint** - Execute `doddle-real-estate-skills/.claude/skills/realty-openhouse/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Event promo plan and attendance drivers per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, open-house promo recommendations.
Save to: `./docs/realty/realty-openhouse-[slug].md`
