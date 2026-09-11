---
description: Activate alumni base for referrals and giving
argument-hint: [institution alumni-base]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `edu-alumni` (id `doddle.edu.alumni`), `email-marketing`, `referral-program` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Student privacy**: Never request or store student PII; use de-identified examples only.

---

## Interactive Parameter Collection

### Step 1: Ask Institution

**Question:** "What is the institution name?"
**Header:** "Institution"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the institution name
- **Skip** - Use generic institution placeholder

---

### Step 2: Ask Alumni Base

**Question:** "What is the alumni base focus?"
**Header:** "Alumni Base"
**MultiSelect:** false

**Options:**
- **Recent grads** - Last 5 years, engagement focus
- **Established** - Mid-career, referral focus
- **Donors** - Giving-capable, advancement focus

---

### Step 3: Confirmation

**Display summary:**
- Institution: [institution]
- Alumni base: [alumni_base]
- Skill: edu-alumni (`doddle.edu.alumni`)

**Question:** "Proceed with alumni activation?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, activate** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `institution` + `alumni_base` from steps above.
2. **Run skill blueprint** - Execute `doddle-education-skills/.claude/skills/edu-alumni/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Alumni activation and referral plays per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, alumni-engagement recommendations.
Save to: `./docs/edu/edu-alumni-[slug].md`
