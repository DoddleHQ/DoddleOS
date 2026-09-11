---
description: Build healthcare review and reputation growth system
argument-hint: [practice-name location]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `healthcare-reputation` (id `doddle.health.reputation`), `social-media`, `brand-building`, `email-sequence` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**HIPAA**: Never request or store PHI; never incentivize reviews tied to care outcomes.

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

### Step 2: Ask Location

**Question:** "What is the practice location (city / area)?"
**Header:** "Location"
**MultiSelect:** false

**Options:**
- **Enter location** - I'll share city / service area
- **Multi-location** - More than one site
- **Skip** - Use general local-SEO guidance

---

### Step 3: Confirmation

**Display summary:**
- Practice: [practice_name]
- Location: [location]
- Skill: healthcare-reputation (`doddle.health.reputation`)

**Question:** "Proceed with reputation plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `practice_name` + `location` from steps above.
2. **Run skill blueprint** - Execute `doddle-healthcare-skills/.claude/skills/healthcare-reputation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Review-request flow, response templates, and rating-growth plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: review assets, request timing, response playbook, growth recommendations.
Save to: `./docs/health/healthcare-reputation-[slug].md`
