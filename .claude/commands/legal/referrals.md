---
description: Grow legal referral network and partner pipeline
argument-hint: [firm-name network]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `legal-referrals` (id `doddle.legal.referrals`) skill.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Bar Rules**: Follow attorney advertising rules; no guaranteed outcomes; include disclaimers where required.

---

## Interactive Parameter Collection

### Step 1: Ask Firm Name

**Question:** "What is the firm name?"
**Header:** "Firm Name"
**MultiSelect:** false

**Options:**
- **Enter name** - I'll share the firm name
- **Skip** - Use generic firm placeholder

---

### Step 2: Ask Network

**Question:** "What is the referral network focus?"
**Header:** "Network"
**MultiSelect:** false

**Options:**
- **Attorney partners** - Cross-practice firm referrals
- **Local professionals** - Medical / real estate / financial contacts
- **Past clients / Community** - Client and community sources

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Network: [network]
- Skill: legal-referrals (`doddle.legal.referrals`)

**Question:** "Proceed with referral growth?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, grow** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `network` from steps above.
2. **Run skill blueprint** - Execute `doddle-legal-skills/.claude/skills/legal-referrals/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Referral partner plan and outreach assets per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized partners, referral recommendations.
Save to: `./docs/legal/legal-referrals-[slug].md`
