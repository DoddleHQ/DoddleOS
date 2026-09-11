---
description: Drive finance referrals from client network
argument-hint: [firm-name network]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `finance-referrals` (id `doddle.finance.referrals`), `email-sequence`, `social-media` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

**Compliance**: No guaranteed returns; all messaging must be compliant, no misleading claims.

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

**Question:** "What is the referral network?"
**Header:** "Network"
**MultiSelect:** false

**Options:**
- **Clients** - Existing customer base
- **Partners** - Brokers, accountants, lawyers
- **Community** - Local groups, associations

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Network: [network]
- Skill: finance-referrals (`doddle.finance.referrals`)

**Question:** "Proceed with referral program?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `network` from steps above.
2. **Run skill blueprint** - Execute `doddle-finance-skills/.claude/skills/finance-referrals/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Referral incentives and outreach playbook per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, referral recommendations.
Save to: `./docs/finance/finance-referrals-[slug].md`
