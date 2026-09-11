---
description: Optimize restaurant loyalty program for repeat visit rate
argument-hint: [venue-name covers]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `restaurant-loyalty` (id `doddle.restaurant.loyalty`), `email-sequence`, `content-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Venue Name

**Question:** "What is the venue name?"
**Header:** "Venue Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the venue name
- **Skip** - Use generic venue placeholder

---

### Step 2: Ask Covers

**Question:** "What is the average weekly covers volume?"
**Header:** "Covers"
**MultiSelect:** false

**Options:**
- **Under 200** - Small / intimate venue
- **200-500** - Mid-size restaurant
- **500+** - High-volume venue

---

### Step 3: Confirmation

**Display summary:**
- Venue: [venue_name]
- Covers: [covers]
- Skill: restaurant-loyalty (`doddle.restaurant.loyalty`)

**Question:** "Proceed with loyalty optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `venue_name` + `covers` from steps above.
2. **Run skill blueprint** - Execute `doddle-restaurant-skills/.claude/skills/restaurant-loyalty/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Loyalty audit and repeat-visit fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, loyalty-program recommendations.
Save to: `./docs/restaurant/restaurant-loyalty-[slug].md`
