---
description: Build home valuation funnel and seller lead capture for real estate
argument-hint: [market brokerage]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `realty-valuation` (id `doddle.realty.valuation`), `form-cro`, `page-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Fair Housing**: Never use discriminatory language; comply with Fair Housing Act in all copy.

---

## Interactive Parameter Collection

### Step 1: Ask Market

**Question:** "What is the target market?"
**Header:** "Market"
**MultiSelect:** false

**Options:**
- **Enter market** - I'll share city / service area
- **Skip** - Use generic market placeholder

---

### Step 2: Ask Brokerage

**Question:** "What is the brokerage name?"
**Header:** "Brokerage"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the brokerage brand
- **Skip** - Use generic brokerage placeholder

---

### Step 3: Confirmation

**Display summary:**
- Market: [market]
- Brokerage: [brokerage]
- Skill: realty-valuation (`doddle.realty.valuation`)

**Question:** "Proceed with valuation funnel?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `market` + `brokerage` from steps above.
2. **Run skill blueprint** - Execute `doddle-real-estate-skills/.claude/skills/realty-valuation/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Valuation funnel audit and seller-lead fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, valuation-funnel recommendations.
Save to: `./docs/realty/realty-valuation-[slug].md`
