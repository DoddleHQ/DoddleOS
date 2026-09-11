---
description: Optimize ecommerce PLP / category page for CTR to PDP
argument-hint: [page_url category_keyword]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `ecommerce-plp` (id `doddle.ecommerce.plp` v1.5.1, pack `doddle-ecommerce-skills`), `page-cro`, `copywriting`, `seo-mastery` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**NOTE**: Replaces legacy routing via `/cro:*` and `/pricing:strategy`.

---

## Interactive Parameter Collection

### Step 1: Ask Page URL

**Question:** "What is the PLP / category page URL?"
**Header:** "Page URL"
**MultiSelect:** false

**Options:**
- **Enter URL** - I'll share the PLP link
- **Skip** - Audit from description only

---

### Step 2: Ask Category Keyword

**Question:** "What is the target category keyword?"
**Header:** "Category Keyword"
**MultiSelect:** false

**Options:**
- **Enter keyword** - I'll share the primary keyword
- **Skip** - Infer from page content

---

### Step 3: Confirmation

**Display summary:**
- Page URL: [page_url]
- Category keyword: [category_keyword]
- Skill: ecommerce-plp (`doddle.ecommerce.plp`)

**Question:** "Proceed with PLP optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `page_url` + `category_keyword` from steps above.
2. **Run skill blueprint** - Execute `doddle-ecommerce-skills/.claude/skills/ecommerce-plp/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - PLP CTR audit and PDP click-through fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, PLP-to-PDP recommendations.
Save to: `./docs/ecom/ecommerce-plp-[slug].md`
