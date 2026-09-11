---
description: Optimize restaurant online reputation and review profile for rating lift
argument-hint: [venue-name location]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `restaurant-reputation` (id `doddle.restaurant.reputation`), `seo-mastery`, `social-media` skills.

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

### Step 2: Ask Location

**Question:** "What is the venue location?"
**Header:** "Location"
**MultiSelect:** false

**Options:**
- **Enter location** - City / neighborhood
- **Multi-location** - Group with several venues
- **Skip** - Use generic location placeholder

---

### Step 3: Confirmation

**Display summary:**
- Venue: [venue_name]
- Location: [location]
- Skill: restaurant-reputation (`doddle.restaurant.reputation`)

**Question:** "Proceed with reputation optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `venue_name` + `location` from steps above.
2. **Run skill blueprint** - Execute `doddle-restaurant-skills/.claude/skills/restaurant-reputation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Reputation audit and rating-lift fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, reputation-management recommendations.
Save to: `./docs/restaurant/restaurant-reputation-[slug].md`
