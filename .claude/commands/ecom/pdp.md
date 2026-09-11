---
description: Optimize ecommerce PDP for add-to-cart conversion
argument-hint: [page_url product_id]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `ecommerce-pdp` (id `doddle.ecommerce.pdp` v1.5.1, pack `doddle-ecommerce-skills`), `page-cro`, `copywriting`, `form-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**NOTE**: Replaces legacy routing via `/cro:*` and `/pricing:strategy`.

---

## Interactive Parameter Collection

### Step 1: Ask Page URL

**Question:** "What is the PDP / product page URL?"
**Header:** "Page URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the PDP link
- **Skip** - Audit from description only

---

### Step 2: Ask Product ID

**Question:** "What is the product ID or SKU?"
**Header:** "Product ID"
**MultiSelect:** false

**Options:**
- **Enter ID** - I'll share the product ID / SKU
- **Skip** - Use page URL only

---

### Step 3: Confirmation

**Display summary:**
- Page URL: [page_url]
- Product ID: [product_id]
- Skill: ecommerce-pdp (`doddle.ecommerce.pdp`)

**Question:** "Proceed with PDP optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `page_url` + `product_id` from steps above.
2. **Run skill blueprint** - Execute `doddle-ecommerce-skills/.claude/skills/ecommerce-pdp/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - PDP conversion audit and add-to-cart fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, PDP conversion recommendations.
Save to: `./docs/ecom/ecommerce-pdp-[slug].md`
