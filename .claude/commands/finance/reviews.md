---
description: Build trust with finance reviews and reputation system
argument-hint: [firm-name location]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `finance-reviews` (id `doddle.finance.reviews`), `page-cro`, `social-media` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Compliance**: No guaranteed returns; all messaging must be compliant, no misleading claims.

---

## Interactive Parameter Collection

### Step 1: Ask Firm Name

**Question:** "What is the firm name?"
**Header:** "Firm Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the firm name
- **Skip** - Use generic firm placeholder

---

### Step 2: Ask Location

**Question:** "What is the firm location?"
**Header:** "Location"
**MultiSelect:** false

**Options:**
- **Single branch** - One office / city
- **Multi-branch** - Several locations
- **Online-only** - No physical branch

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Location: [location]
- Skill: finance-reviews (`doddle.finance.reviews`)

**Question:** "Proceed with reviews setup?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `location` from steps above.
2. **Run skill blueprint** - Execute `doddle-finance-skills/.claude/skills/finance-reviews/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Review generation playbook and reputation fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, reviews recommendations.
Save to: `./docs/finance/finance-reviews-[slug].md`
