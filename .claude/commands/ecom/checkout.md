---
description: Optimize ecommerce checkout flow for completion rate
argument-hint: [checkout_url cart_type]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `ecommerce-checkout` (id `doddle.ecommerce.checkout` v1.5.1, pack `doddle-ecommerce-skills`), `form-cro`, `page-cro`, `signup-flow-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**NOTE**: Replaces legacy routing via `/cro:*` and `/pricing:strategy`.

---

## Interactive Parameter Collection

### Step 1: Ask Checkout URL

**Question:** "What is the checkout URL?"
**Header:** "Checkout URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the checkout link
- **Skip** - Audit from description only

---

### Step 2: Ask Cart Type

**Question:** "What is the cart type?"
**Header:** "Cart Type"
**MultiSelect:** false

**Options:**
- **Guest checkout** - No account required
- **Registered / One-click** - Account, express, or BNPL flow

---

### Step 3: Confirmation

**Display summary:**
- Checkout URL: [checkout_url]
- Cart type: [cart_type]
- Skill: ecommerce-checkout (`doddle.ecommerce.checkout`)

**Question:** "Proceed with checkout optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `checkout_url` + `cart_type` from steps above.
2. **Run skill blueprint** - Execute `doddle-ecommerce-skills/.claude/skills/ecommerce-checkout/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Checkout friction audit and completion fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, checkout completion recommendations.
Save to: `./docs/ecom/ecommerce-checkout-[slug].md`
