---
description: Optimize restaurant private events and group bookings for fill rate
argument-hint: [venue-name capacity]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `restaurant-events` (id `doddle.restaurant.events`), `page-cro`, `content-strategy` skills.

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

### Step 2: Ask Event Capacity

**Question:** "What is the private events capacity?"
**Header:** "Capacity"
**MultiSelect:** false

**Options:**
- **Under 30** - Small private room
- **30-100** - Mid-size events space
- **100+** - Large events venue

---

### Step 3: Confirmation

**Display summary:**
- Venue: [venue_name]
- Capacity: [capacity]
- Skill: restaurant-events (`doddle.restaurant.events`)

**Question:** "Proceed with events optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `venue_name` + `capacity` from steps above.
2. **Run skill blueprint** - Execute `doddle-restaurant-skills/.claude/skills/restaurant-events/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Events friction audit and fill-rate fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, events-flow recommendations.
Save to: `./docs/restaurant/restaurant-events-[slug].md`
