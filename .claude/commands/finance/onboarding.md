---
description: Optimize finance client onboarding and activation flow
argument-hint: [firm-name product]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `finance-onboarding` (id `doddle.finance.onboarding`), `signup-flow-cro`, `onboarding-cro` skills.

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

### Step 2: Ask Product

**Question:** "What is the core product?"
**Header:** "Product"
**MultiSelect:** false

**Options:**
- **Advisory / Planning** - Wealth, retirement plans
- **Lending / Accounts** - Loans, deposits, cards
- **Insurance / Other** - Policies, claims onboarding

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Product: [product]
- Skill: finance-onboarding (`doddle.finance.onboarding`)

**Question:** "Proceed with onboarding optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `product` from steps above.
2. **Run skill blueprint** - Execute `doddle-finance-skills/.claude/skills/finance-onboarding/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Onboarding friction audit and activation fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, onboarding recommendations.
Save to: `./docs/finance/finance-onboarding-[slug].md`
