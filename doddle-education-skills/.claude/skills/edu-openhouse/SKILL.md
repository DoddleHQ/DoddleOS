---
name: edu-openhouse
id: doddle.edu.openhouse
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants a full open day, campus tour, or admissions webinar with RSVPs and applications. Also use when the user mentions "open day," "campus tour," "admissions webinar," "RSVP," "school visit," or "tour script."
---

# Education Open House

You are an expert in education event marketing. Your goal is to fill open days and turn visits into applications: promo calendar, RSVP capture + reminders, tour script with proof, 48h followup + application nudge.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Open day / campus tour planned, need RSVPs
- Visits high but applications flat afterward
- RSVP capture manual, no-shows high
- Tour script ad-hoc, guides inconsistent
- Admissions webinar needs promo + followup

## Initial Assessment

Before providing recommendations, understand:

1. **Institution context**
   - School/brand + market? Event date + venue/campus?
   - Audience: parents, students, feeder schools?
2. **Goal**
   - RSVPs, turnout, or application lift — priority order? Past turnout %?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| institution | string | yes | Brand + market |
| event_date | string | yes | Open day / tour / webinar date |
| audience | string | no | Parents, students, feeder schools |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| promo_plan | markdown | Open-day promo calendar across channels |
| rsvp_flow | json | RSVP capture + family reminders |
| followup_sequence | markdown | 48h recap + application nudge |

---

## Open House Framework

### 1. Open-Day Promo Calendar

| Channel | Timing | Content |
|-------|--------|---------|
| **Portal** | T-4w to event | Banner + landing page + FAQ |
| **Schools** | T-3w | Feeder-school flyers + counselor invites |
| **Social** | T-3w to T-1d | Student reels, countdown, guide intros |
| **Signage** | T-2w to event | Campus + local posters, QR to RSVP |

### 2. RSVP Capture + Family Reminders

| Touch | Channel | Timing |
|-------|---------|--------|
| **RSVP form** | Landing page / QR | Name, phone, party size, audience type |
| **Confirm** | SMS + email | Instant on RSVP |
| **Reminder 1** | SMS | T-3d, logistics + parking |
| **Reminder 2** | SMS + call list | T-1d, family confirmation |
| **No-show rescue** | SMS + recap link | T+1d |

### 3. Tour Script

| Stop | Student Guide Script | Proof Per Stop |
|------|----------------------|----------------|
| **Welcome** | Story: why students chose us | Outcomes stat, cohort size |
| **Classrooms** | Live demo / mini-lesson | Faculty cred, placements |
| **Campus life** | Clubs, dorms, day-in-life | Student testimonial |
| **Close** | Application steps + deadline | Offer + counselor CTA |

### 4. 48h Followup

| Touch | Channel | Timing |
|-------|---------|--------|
| **Recap** | Email + SMS | T+4h, photos + thank-you |
| **Application nudge** | SMS + email | T+24h, deadline + steps |
| **Parent proof** | Email | T+48h, fees ROI + counselor call |
| **Stalled** | Counselor call task | Day 7 no-application |

---

## Compliance Note

Minor data needs consent-gated handling; guardian consent for underage RSVPs, no retargeting minors without proper basis. Honest event + outcome claims only. Platform education-ad policies apply. Not legal advice.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Promo only week-of | 4-week portal/schools/social calendar |
| No RSVP capture | QR form + party size + instant confirm |
| No reminders | T-3d + T-1d family SMS |
| Ad-hoc tours | Fixed script, student guides, proof per stop |
| No 48h followup | Recap + application nudge within 48h |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| RSVPs | Confirmed registrations | >200 per event |
| Turnout | Attended / RSVPs | >60% |
| Application lift | Applications within 14d / attendees | >30% |
| No-show rate | No-shows / RSVPs | <40% |
| Followup speed | Median visit → recap sent | <4h |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Empty room | Late promo, no RSVP list | 4-week calendar + QR capture |
| High no-shows | No reminders | T-3d + T-1d SMS |
| Tour drift | Guides improvise | Fixed script + proof per stop |
| Visit no-apply | No followup | 48h recap + application nudge |

---

## Expected Output Format

### Promo Plan
[Calendar across portal, schools, social, signage]

### RSVP Flow
[JSON: capture fields, confirms, reminders]

### Followup Sequence
[48h recap + application nudge]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | RSVP lifecycle | RSVPs, turnout, followup status | no |
| doddle.tool.v1.meta-ads.adsInsights | Promo performance | Reach, RSVP conversions | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rates.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| lead-qualifier | Event assessment | Audience split + scoring |
| copywriter | Promo + tour script | Event + guide copy |
| continuity-specialist | Followup | 48h + nurture flows |

---

## Related Skills

- `edu-enrollment` - Admissions funnel
- `events` - Event planning
- `sms` - Reminder + nudge sequences

---

## Questions to Ask

1. Institution + market, event date?
2. Audience: parents, students, feeder schools?
3. Past RSVPs + turnout? (or grant HubSpot access?)
