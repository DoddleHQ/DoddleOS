---
description: Build location and service pages for local SEO coverage
argument-hint: [business-name + locations + services]
---

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `local-pages` (id: doddle.local.pages), `seo-mastery`, `copywriting`.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business Name

**Question:** "What is the business name?"
**Header:** "Business"
**MultiSelect:** false
**Accept:** Free text or `$ARGUMENTS` (e.g. "Acme Plumbing")

---

### Step 2: Ask Locations + Services

**Question:** "Which locations and services need pages? (comma-separated)"
**Header:** "Pages"
**MultiSelect:** true
**Accept:** Free text (e.g. locations: "Austin, Round Rock"; services: "drain repair, water heater")

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Local Pages Config

| Parameter | Value |
|-----------|-------|
| Business | [business_name] |
| Locations | [locations] |
| Services | [services] |
```

**Question:** "Proceed with page build?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build pages** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow

1. **Collect inputs**
   - Parse `$ARGUMENTS` for business_name + locations + services, ask missing via Steps 1-2
2. **Run skill blueprint**
   - Load `doddle-local-skills/.claude/skills/local-pages/blueprint.yaml`
   - Execute nodes in order, follow node inputs/outputs
3. **Deliver outputs**
   - Return skill outputs (page outlines, copy blocks, internal-link map)
   - Save to Output Location, list unresolved questions

---

## Output Location

Save to: `./docs/local/local-pages-[business-slug].md`
