---
description: Optimize SaaS trial and signup flow for activation
argument-hint: [signup-url trial-model]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `saas-trial` (id `doddle.saas.trial`), `signup-flow-cro`, `onboarding-cro`, `form-cro` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Signup URL

**Question:** "What is the signup / trial start URL?"
**Header:** "Signup URL"
**MultiSelect:** false

**Options:**
- **Paste URL** - I'll share the live signup link
- **Describe flow** - No URL, I'll outline the signup steps
- **Skip** - Use general trial best practices

---

### Step 2: Ask Trial Model

**Question:** "What trial model do you use?"
**Header:** "Trial Model"
**MultiSelect:** false

**Options:**
- **Free trial (no card)** - 7/14/30-day trial
- **Free trial (card upfront)** - Card required to start
- **Freemium** - Free plan with paid upgrade
- **Demo-gated / Sales-led** - No self-serve trial

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Trial Optimization Config

| Parameter | Value |
|-----------|-------|
| Signup URL | [url / flow description] |
| Trial Model | [selected model] |
| Skill | saas-trial (`doddle.saas.trial`) |
```

**Question:** "Proceed with trial optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `signup_url` + `trial_model` from steps above.
2. **Run skill blueprint** - Execute `doddle-saas-skills/.claude/skills/saas-trial/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Friction audit, activation, and upgrade-path fixes per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, activation recommendations.
Save to: `./docs/saas/saas-trial-[slug].md`
