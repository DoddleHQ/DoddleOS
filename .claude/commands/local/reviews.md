---
description: Generate review request system and response templates for local business
argument-hint: [business-name + location + platform]
---

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `local-reviews` (id: doddle.local.reviews), `copywriting`, `marketing-psychology`.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business + Location

**Question:** "What business and location is this for?"
**Header:** "Business"
**MultiSelect:** false
**Accept:** Free text or `$ARGUMENTS` (e.g. "Acme Dental, Austin TX")

---

### Step 2: Ask Platform

**Question:** "Which review platform to prioritize?"
**Header:** "Platform"
**MultiSelect:** false

**Options:**
- **Google** - Google Business Profile reviews
- **Yelp / Facebook** - Secondary local platforms
- **Industry** - Avvo, Healthgrades, TripAdvisor, etc.
- **Custom** - I'll specify the platform

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Review System Config

| Parameter | Value |
|-----------|-------|
| Business | [business_name] |
| Location | [location] |
| Platform | [platform] |
```

**Question:** "Proceed with review system?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, build system** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow
1. **Collect inputs**
   - Parse `$ARGUMENTS` for business_name + location + platform, ask missing via Steps 1-2
2. **Run skill blueprint**
   - Load `doddle-local-skills/.claude/skills/local-reviews/blueprint.yaml`
   - Execute nodes in order, follow node inputs/outputs
3. **Deliver outputs**
   - Return skill outputs (request scripts, response templates, escalation flow)
   - Save to Output Location, list unresolved questions

---

## Output Location
Save to: `./docs/local/local-reviews-[business-slug].md`
