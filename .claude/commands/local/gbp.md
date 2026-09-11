---
description: Optimize Google Business Profile for local visibility and calls
argument-hint: [business-name + location]
---

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `local-gbp` (id: doddle.local.gbp), `seo-mastery`, `copywriting`.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business Name

**Question:** "What is the business name?"
**Header:** "Business"
**MultiSelect:** false
**Accept:** Free text or `$ARGUMENTS` (e.g. "Acme Dental")

---

### Step 2: Ask Location

**Question:** "What is the primary location (city / service area)?"
**Header:** "Location"
**MultiSelect:** false
**Accept:** Free text (e.g. "Austin, TX")

---

### Step 3: Confirmation

**Display summary:**

```markdown
## GBP Optimization Config

| Parameter | Value |
|-----------|-------|
| Business | [business_name] |
| Location | [location] |
```

**Question:** "Proceed with GBP optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize GBP** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow

1. **Collect inputs**
   - Parse `$ARGUMENTS` for business_name + location, ask missing via Steps 1-2
2. **Run skill blueprint**
   - Load `doddle-local-skills/.claude/skills/local-gbp/blueprint.yaml`
   - Execute nodes in order, follow node inputs/outputs
3. **Deliver outputs**
   - Return skill outputs (profile copy, categories, posts, Q&A)
   - Save to Output Location, list unresolved questions

---

## Output Location

Save to: `./docs/local/local-gbp-[business-slug].md`
