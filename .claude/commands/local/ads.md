---
description: Plan local ads campaign with budget, geo-targeting, and ad copy
argument-hint: [business-name + service-area + monthly-budget]
---

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `local-ads` (id: doddle.local.ads), `paid-advertising`, `copywriting`.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business + Service Area

**Question:** "What business and service area is this for?"
**Header:** "Business"
**MultiSelect:** false
**Accept:** Free text or `$ARGUMENTS` (e.g. "Acme HVAC, Greater Austin")

---

### Step 2: Ask Monthly Budget

**Question:** "What is the monthly ad budget?"
**Header:** "Budget"
**MultiSelect:** false

**Options:**
- **Under $1k** - Test budget, single service + geo
- **$1k-$3k** - Local scale, 2-3 campaigns
- **$3k+** - Multi-service + multi-geo coverage
- **Custom** - I'll specify exact budget

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Local Ads Config

| Parameter | Value |
|-----------|-------|
| Business | [business_name] |
| Service Area | [service_area] |
| Monthly Budget | [monthly_budget] |
```

**Question:** "Proceed with ads plan?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, plan ads** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs**
   - Parse `$ARGUMENTS` for business_name + service_area + monthly_budget, ask missing via Steps 1-2
2. **Run skill blueprint**
   - Load `doddle-local-skills/.claude/skills/local-ads/blueprint.yaml`
   - Execute nodes in order, follow node inputs/outputs
3. **Deliver outputs**
   - Return skill outputs (campaign structure, geo-targets, ad copy, budget split)
   - Save to Output Location, list unresolved questions

---

## Output Location
Save to: `./docs/local/local-ads-[business-slug].md`
