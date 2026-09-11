---
description: Optimize restaurant table reservations flow for booking rate
argument-hint: [venue-name covers]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `restaurant-reservations` (id `doddle.restaurant.reservations`), `page-cro`, `form-cro` skills.

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
- Skill: restaurant-reservations (`doddle.restaurant.reservations`)

**Question:** "Proceed with reservations optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `venue_name` + `covers` from steps above.
2. **Run skill blueprint** - Execute `doddle-restaurant-skills/.claude/skills/restaurant-reservations/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Reservation friction audit and booking-rate fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, reservations-flow recommendations.
Save to: `./docs/restaurant/restaurant-reservations-[slug].md`
