---
description: Optimize SaaS homepage for signup conversion
argument-hint: [page-url audience]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `saas-homepage` (id `doddle.saas.homepage`), `page-cro`, `copywriting`, `marketing-psychology` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Page URL

**Question:** "What is the homepage URL to optimize?"
**Header:** "Page URL"
**MultiSelect:** false

**Options:**
- **Paste URL** - I'll share the live homepage link
- **Describe page** - No URL, I'll paste copy/sections instead
- **Skip** - Use general SaaS homepage best practices

---

### Step 2: Ask Target Audience

**Question:** "Who is the primary audience for this homepage?"
**Header:** "Audience"
**MultiSelect:** false

**Options:**
- **SMB / Founders** - Small teams, fast decisions
- **Mid-Market** - Multiple stakeholders, ROI focus
- **Enterprise** - Security, compliance, scale concerns
- **Custom** - I'll describe the ICP

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Homepage Optimization Config

| Parameter | Value |
|-----------|-------|
| Page URL | [url / description] |
| Audience | [selected audience] |
| Skill | saas-homepage (`doddle.saas.homepage`) |
```

**Question:** "Proceed with homepage optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `page_url` + `audience` from steps above.
2. **Run skill blueprint** - Execute `doddle-saas-skills/.claude/skills/saas-homepage/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Hero, social proof, CTA, and friction fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, copy alternatives.
Save to: `./docs/saas/saas-homepage-[slug].md`
