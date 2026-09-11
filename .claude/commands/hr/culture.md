---
description: Diagnose culture issue and recommend fixes by company size
argument-hint: [company-size issue]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `hr-culture` (id `doddle.hr.culture`), `brand-building`, `problem-solving` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Company Size

**Question:** "What is the company size?"
**Header:** "Company Size"
**MultiSelect:** false

**Options:**
- **Startup (1-50)** - Early-stage team
- **Mid-size (51-500)** - Growing org
- **Enterprise (500+)** - Large org

---

### Step 2: Ask Issue

**Question:** "What culture issue needs attention?"
**Header:** "Issue"
**MultiSelect:** false

**Options:**
- **Enter issue** - I'll describe the problem (e.g. retention, morale)
- **General audit** - Full culture health check

---

### Step 3: Confirmation

**Display summary:**
- Company size: [company_size]
- Issue: [issue]
- Skill: hr-culture (`doddle.hr.culture`)

**Question:** "Proceed with culture diagnosis?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, diagnose** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `company_size` + `issue` from steps above.
2. **Run skill blueprint** - Execute `doddle-hr-skills/.claude/skills/hr-culture/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Culture diagnosis and action plan per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, culture recommendations.
Save to: `./docs/hr/hr-culture-[slug].md`
