---
description: Optimize restaurant online ordering flow for order conversion
argument-hint: [venue-name order-mix]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `restaurant-ordering` (id `doddle.restaurant.ordering`), `page-cro`, `form-cro` skills.

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

### Step 2: Ask Order Mix

**Question:** "What is the primary order mix?"
**Header:** "Order Mix"
**MultiSelect:** false

**Options:**
- **Dine-in heavy** - Mostly on-premise covers
- **Takeaway / Delivery** - Mostly off-premise orders
- **Balanced** - Roughly even split

---

### Step 3: Confirmation

**Display summary:**
- Venue: [venue_name]
- Order mix: [order_mix]
- Skill: restaurant-ordering (`doddle.restaurant.ordering`)

**Question:** "Proceed with ordering optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `venue_name` + `order_mix` from steps above.
2. **Run skill blueprint** - Execute `doddle-restaurant-skills/.claude/skills/restaurant-ordering/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Ordering friction audit and order-conversion fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, ordering-flow recommendations.
Save to: `./docs/restaurant/restaurant-ordering-[slug].md`
