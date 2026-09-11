---
description: Grow revenue with finance cross-sell to existing book
argument-hint: [firm-name book-size]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `finance-crosssell` (id `doddle.finance.crosssell`), `email-sequence`, `page-cro` skills.

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

### Step 2: Ask Book Size

**Question:** "What is the client book size?"
**Header:** "Book Size"
**MultiSelect:** false

**Options:**
- **Small (<1k)** - Early book, manual outreach
- **Mid (1k-10k)** - Segmented campaigns
- **Large (10k+)** - Automated cross-sell

---

### Step 3: Confirmation

**Display summary:**
- Firm: [firm_name]
- Book size: [book_size]
- Skill: finance-crosssell (`doddle.finance.crosssell`)

**Question:** "Proceed with cross-sell plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs** - Confirm `firm_name` + `book_size` from steps above.
2. **Run skill blueprint** - Execute `doddle-finance-skills/.claude/skills/finance-crosssell/blueprint.yaml` nodes in order, using skill guidance for analysis.
3. **Deliver skill outputs** - Cross-sell offers and sequencing per skill output contract.

---

## Output Format + Location
Short report per skill outputs: scored findings, prioritized fixes, cross-sell recommendations.
Save to: `./docs/finance/finance-crosssell-[slug].md`
