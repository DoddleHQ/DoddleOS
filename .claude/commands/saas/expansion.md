---
description: Grow SaaS revenue via expansion and upsell
argument-hint: [product nrr]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `saas-expansion` (id `doddle.saas.expansion`), `paywall-upgrade-cro`, `pricing-strategy`, `product-led-growth` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Product Context

**Question:** "What product should the expansion plan cover?"
**Header:** "Product"
**MultiSelect:** false

**Options:**
- **Describe product** - I'll share product, plans, and add-ons
- **Have pricing** - I'll link pricing / packaging page
- **Skip** - Use general expansion patterns

---

### Step 2: Ask NRR Context

**Question:** "What is your current NRR / expansion goal?"
**Header:** "NRR"
**MultiSelect:** false

**Options:**
- **Know my NRR** - I'll share NRR and expansion mix
- **Low expansion** - Upsell / cross-sell underperforming
- **Unknown** - No NRR data, need baseline plan
- **Custom** - I'll describe goals and constraints

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Expansion Config

| Parameter | Value |
|-----------|-------|
| Product | [product description] |
| NRR | [nrr / goal] |
| Skill | saas-expansion (`doddle.saas.expansion`) |
```

**Question:** "Proceed with expansion plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `product` + `nrr` from steps above.
2. **Run skill blueprint** - Execute `doddle-saas-skills/.claude/skills/saas-expansion/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Expansion triggers, upsell surfaces, and packaging fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: expansion opportunities, prioritized plays, packaging recommendations.
Save to: `./docs/saas/saas-expansion-[slug].md`
