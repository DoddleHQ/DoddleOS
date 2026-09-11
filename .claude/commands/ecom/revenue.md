---
description: Grow ecommerce revenue via AOV and repeat purchase levers
argument-hint: [store_url aov_current]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `ecommerce-revenue` (id `doddle.ecommerce.revenue` v1.5.1, pack `doddle-ecommerce-skills`), `page-cro`, `form-cro`, `pricing-strategy` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**NOTE**: Replaces legacy routing via `/cro:*` and `/pricing:strategy`.

---

## Interactive Parameter Collection

### Step 1: Ask Store URL

**Question:** "What is the store URL?"
**Header:** "Store URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the store link
- **Skip** - Audit from description only

---

### Step 2: Ask Current AOV

**Question:** "What is the current AOV?"
**Header:** "Current AOV"
**MultiSelect:** false

**Options:**
- **Enter AOV** - I'll share the current order value
- **Skip** - Benchmark without baseline

---

### Step 3: Confirmation

**Display summary:**
- Store URL: [store_url]
- Current AOV: [aov_current]
- Skill: ecommerce-revenue (`doddle.ecommerce.revenue`)

**Question:** "Proceed with revenue optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `store_url` + `aov_current` from steps above.
2. **Run skill blueprint** - Execute `doddle-ecommerce-skills/.claude/skills/ecommerce-revenue/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Revenue audit and AOV / repeat-purchase fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, revenue-growth recommendations.
Save to: `./docs/ecom/ecommerce-revenue-[slug].md`
