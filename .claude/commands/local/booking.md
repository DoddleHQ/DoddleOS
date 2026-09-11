---
description: Optimize booking and call flow to convert local intent into appointments
argument-hint: [business-name + service]
---

## Language & Quality Standards

**CRITICAL**: Respond in same language user uses.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `local-booking` (id: doddle.local.booking), `page-cro`, `form-cro`.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Business Name

**Question:** "What is the business name?"
**Header:** "Business"
**MultiSelect:** false
**Accept:** Free text or `$ARGUMENTS` (e.g. "Acme Dental")

---

### Step 2: Ask Service

**Question:** "Which service should the booking flow optimize for?"
**Header:** "Service"
**MultiSelect:** false
**Accept:** Free text (e.g. "emergency cleaning, implants")

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Booking Flow Config

| Parameter | Value |
|-----------|-------|
| Business | [business_name] |
| Service | [service] |
```

**Question:** "Proceed with booking optimization?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, optimize booking** - Run skill blueprint
- **No, change settings** - Go back to modify

---

## Workflow

1. **Collect inputs**
   - Parse `$ARGUMENTS` for business_name + service, ask missing via Steps 1-2
2. **Run skill blueprint**
   - Load `doddle-local-skills/.claude/skills/local-booking/blueprint.yaml`
   - Execute nodes in order, follow node inputs/outputs
3. **Deliver outputs**
   - Return skill outputs (booking flow, CTA copy, follow-up scripts)
   - Save to Output Location, list unresolved questions

---

## Output Location

Save to: `./docs/local/local-booking-[business-slug].md`
