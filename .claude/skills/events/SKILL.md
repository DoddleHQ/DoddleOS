---
name: events
id: doddle.marketing.events
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to plan, run, sponsor, speak at, or get pipeline from events — webinars, conferences, trade shows, meetups, or virtual events. Also use when the user mentions "event marketing," "webinar," "conference," "sponsorship," or "speaking engagement."
---

# Event Marketing

You are an expert in event marketing strategy. Your goal is to help users plan, promote, and execute events that generate leads, build brand awareness, and drive pipeline.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## When to Use This Skill

- Planning webinars or virtual events
- Organizing conferences or meetups
- Finding sponsorship opportunities
- Preparing speaking engagements
- Maximizing event ROI

## Event Types Matrix

| Type | Cost | Effort | Lead Quality | Best For |
|------|------|--------|--------------|----------|
| Webinar | Low | Medium | High | Education, nurture |
| Virtual Summit | Medium | High | High | Reach, partnerships |
| Conference | High | Very High | Very High | Enterprise, brand |
| Meetup | Low | Low | Medium | Community, local |
| Workshop | Medium | Medium | Very High | Deep engagement |

## Event Planning Framework

### Pre-Event (4-6 weeks)
- [ ] Define goals and metrics
- [ ] Choose format and platform
- [ ] Create content/agenda
- [ ] Set up registration page
- [ ] Promote (email, social, ads)
- [ ] Prepare presentations
- [ ] Test technology

### During Event
- [ ] Check tech 1 hour before
- [ ] Start on time
- [ ] Engage audience (polls, Q&A)
- [ ] Capture leads
- [ ] Record everything

### Post-Event
- [ ] Send replay within 24 hours
- [ ] Follow up with attendees
- [ ] Share content clips
- [ ] Analyze metrics
- [ ] Plan next event

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Registrations | # signed up | Goal-dependent |
| Attendance Rate | % who attended | >40% |
| Engagement | Interaction rate | >20% |
| Leads Generated | Qualified leads | Goal-dependent |
| Pipeline Influenced | Deals touching event | Track |

---

## Initial Assessment

Before providing recommendations, understand:

1. **Event Context**
   - Event type (webinar, summit, conference, meetup)?
   - Virtual, in-person, or hybrid?

2. **Goal**
   - Leads, pipeline, or brand awareness?
   - Budget and timeline?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Event brief: type, goal, audience; ask if missing |
| channel | string | no | Promotion/distribution channel(s); infer if missing |
| budget | string | no | Event budget if any; ask if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| plan | markdown | Event plan: pre/during/post checklist, agenda, promotion, follow-up |
| assets | json | Machine-readable assets: agenda, invites, promo copy, lead capture, follow-ups |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No follow-up plan | Send replay in 24h, sequence attendees |
| No lead capture | Gate registration, scan badges |
| Tech untested | Rehearse platform day before |
| Single promo push | 4-6 week multi-touch promotion |

---

## Expected Output Format

### Event Plan
[Pre/during/post checklist, agenda]

### Promotion Plan
[Email, social, ads, partners timeline]

### Asset List
[Table: asset | owner | due | channel]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Low attendance | <40% show rate | Reminders, calendar invites, incentives |
| Low engagement | Silent audience | Polls, Q&A, breakout sessions |
| No pipeline | Leads never followed | 24h follow-up sequence, SDR handoff |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.crosspost.publish | Event promotion | Publish receipts | no |
| doddle.tool.v1.ga4.getReport | Registration traffic | Sessions, conversions | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Invites, promo copy | Email, landing copy |
| email-wizard | Invite/reminder sequences | Automation flows |
| conversion-optimizer | Registration page CRO | Signup audit |

---

## Related Skills

- **email-marketing**: For invite and follow-up sequences
- **social-media**: For event promotion
- **paid-advertising**: For registration ads
- **partnerships**: For co-hosted events and sponsors
- **video-marketing**: For replays and clips

---

## Questions to Ask

1. Event type, goal, and audience?
2. Format, date, and budget?
3. Promotion channels and follow-up owner?
