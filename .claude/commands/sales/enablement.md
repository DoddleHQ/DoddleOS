---
description: Create sales enablement collateral and playbooks
argument-hint: [product audience]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `sales-enablement` (id `doddle.sales.enablement`).

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Product

**Question:** "What product is this for?"
**Header:** "Product"
**MultiSelect:** false

**Options:**
- **Enter product** - I'll share name + key value props
- **Skip** - Use generic product placeholder

---

### Step 2: Ask Audience

**Question:** "Who is the sales audience?"
**Header:** "Audience"
**MultiSelect:** false

**Options:**
- **AEs / SDRs** - New business prospecting + closing
- **AMs / CS** - Expansion / renewal team
- **Partners** - Channel / reseller sellers

---

### Step 3: Confirmation

**Display summary:**
- Product: [product]
- Audience: [audience]
- Skill: sales-enablement (`doddle.sales.enablement`)

**Question:** "Proceed with enablement kit?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `product` + `audience` from steps above.
2. **Run skill blueprint** - Execute `doddle-sales-skills/.claude/skills/sales-enablement/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Enablement kit and talk tracks per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored assets, prioritized collateral, enablement recommendations.
Save to: `./docs/sales/sales-enablement-[slug].md`
