---
description: Reduce SaaS churn and improve retention
argument-hint: [product churn-rate]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `saas-retention` (id `doddle.saas.retention`), `churn-prevention`, `email-sequence`, `analytics-attribution` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Product Context

**Question:** "What product should the retention plan cover?"
**Header:** "Product"
**MultiSelect:** false

**Options:**
- **Describe product** - I'll share product, plans, and users
- **Have docs** - I'll link product / help docs
- **Skip** - Use general SaaS retention patterns

---

### Step 2: Ask Churn Rate

**Question:** "What is your current churn rate / concern?"
**Header:** "Churn Rate"
**MultiSelect:** false

**Options:**
- **Know my rate** - I'll share logo / revenue churn %
- **High early churn** - Trial or first-90-day drop-off
- **Unknown** - No churn data, need baseline plan
- **Custom** - I'll describe segments and timing

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Retention Config

| Parameter | Value |
|-----------|-------|
| Product | [product description] |
| Churn Rate | [rate / concern] |
| Skill | saas-retention (`doddle.saas.retention`) |
```

**Question:** "Proceed with retention plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `product` + `churn_rate` from steps above.
2. **Run skill blueprint** - Execute `doddle-saas-skills/.claude/skills/saas-retention/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Risk segments, save plays, and lifecycle fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: churn risks, prioritized plays, lifecycle recommendations.
Save to: `./docs/saas/saas-retention-[slug].md`
