---
description: Optimize SaaS pricing page for plan selection and ARPA
argument-hint: [pricing-url arpa]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `saas-pricing` (id `doddle.saas.pricing`), `page-cro`, `pricing-strategy`, `marketing-psychology` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Pricing URL

**Question:** "What is the pricing page URL to optimize?"
**Header:** "Pricing URL"
**MultiSelect:** false

**Options:**
- **Paste URL** - I'll share the live pricing link
- **Describe tiers** - No URL, I'll paste plans and prices
- **Skip** - Use general pricing best practices

---

### Step 2: Ask ARPA Context

**Question:** "What is your current ARPA / pricing concern?"
**Header:** "ARPA"
**MultiSelect:** false

**Options:**
- **Low ARPA** - Need to push higher tiers (know current ARPA)
- **High churn on tiers** - Wrong plan mix, downgrades
- **Unknown / new pricing** - No ARPA data yet
- **Custom** - I'll share ARPA and tier mix

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Pricing Optimization Config

| Parameter | Value |
|-----------|-------|
| Pricing URL | [url / tier description] |
| ARPA | [arpa context] |
| Skill | saas-pricing (`doddle.saas.pricing`) |
```

**Question:** "Proceed with pricing optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `pricing_url` + `arpa` from steps above.
2. **Run skill blueprint** - Execute `doddle-saas-skills/.claude/skills/saas-pricing/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Tier structure, anchoring, and CTA fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, packaging recommendations.
Save to: `./docs/saas/saas-pricing-[slug].md`
