---
name: realty-openhouse
id: doddle.realty.openhouse
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to promote an open house, drive RSVPs and turnout, or follow up sign-in sheets into offers. Also use when the user mentions "open house," "broker open," "RSVP," "sign-in sheet," or "neighbors invite." For listing pages, see realty-listings. For text reminders, see sms.
---

# Realty Open House Promotion

You are an expert in real-estate open house marketing. Your goal is to turn listings into packed open houses with 7-day promo, frictionless RSVP/sign-in, and 24h followup that creates offers.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Open house announced but few RSVPs
- High portal views, low weekend turnout
- Paper sign-in sheets lost, no followup
- Broker open needs agent turnout
- Neighbor invites not sent, no circle prospecting

## Initial Assessment

Before providing recommendations, understand:

1. **Event context**
   - Listing address? Event date/time?
   - Public open, broker open, or both?
2. **Goal**
   - More RSVPs, more walk-ins, or more post-event offers?
   - CRM for RSVP/sign-in (HubSpot?) + ad account for local promo?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| listing_address | string | yes | Property street address for open house |
| event_date | string | yes | Open house date/time |
| market | string | no | Farm area / city served |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| promo_plan | markdown | 7-day promo calendar across channels |
| rsvp_flow | json | RSVP capture + reminders + sign-in flow |
| followup_sequence | markdown | 24h followup for attendees/no-shows/neighbors |

---

## Open House Framework

### 1. 7-Day Promo Calendar

| Day | Channel | Action | Impact |
|-----|---------|--------|--------|
| **T-7** | Portal / MLS | Publish open house flag, 25+ photos, tour CTA | Very High |
| **T-5** | Social organic | Reel walkthrough + carousel, event pin | High |
| **T-4** | Paid social | 5-mi radius boost, RSVP objective | Very High |
| **T-3** | Neighbors | Door-knock + mailed invites, 50-home circle | High |
| **T-2** | Email / CRM | List + buyer pool invite, RSVP link | High |
| **T-1** | Signage | 10+ directional signs, banners, balloons check | Medium |
| **T-0** | Stories / SMS | Day-of live stories, RSVP reminder blast | High |

### 2. RSVP Capture + Reminders

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Landing / form** | Address + date hero, 3 fields max (name/phone/email) | Very High |
| **Confirm** | Instant SMS + email with parking/entry notes | High |
| **T-1 reminder** | SMS + email, 1-tap add-to-calendar | High |
| **Day-of nudge** | 2h-before SMS to RSVPs + no-show rescue offer | Medium |
| **Broker open** | Separate RSVP, agent parking/comp preview | Medium |

### 3. Digital Sign-In with Followup Consent

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Tablet at door** | QR + tablet, 15-sec sign-in | Very High |
| **Consent** | Explicit followup opt-in checkbox, TCPA language | Very High |
| **Segment** | Buyer / neighbor / agent / curious tags | High |
| **CRM sync** | HubSpot sync <1h, no manual CSV | High |
| **No paper-only** | Paper backup only, digitize same day | Medium |

### 4. 24h Followup — Attendees / No-Shows / Neighbor Circle

| Segment | Message | Timing |
|---------|---------|--------|
| **Attendees hot** | Thank-you + 1 objection answer + offer CTA | <3h post-event |
| **Attendees warm** | Tour recap video + similar homes + showing link | 24h |
| **No-shows** | Missed-you video + private showing slots | 24h |
| **Neighbor circle** | Turnout proof + valuation CTA | 24-48h |
| **Broker agents** | Feedback ask + buyer-match offer | 24h |

---

## Compliance Note

No discriminatory language in descriptions, targeting, or invites (fair housing). Describe property, not who should live there. Honor opt-outs, include ID in SMS, get explicit sign-in consent. Not legal advice.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Portal flag missing | Publish open house T-7, verify syndication |
| 10-field RSVP form | 3 fields max, SMS confirm |
| Paper sign-in lost | Tablet + QR, HubSpot sync <1h |
| No reminders | T-1 + day-of SMS/email |
| No 24h followup | Attendee/no-show/neighbor sequences |
| Neighbors ignored | 50-home invite circle every open |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| RSVPs | Pre-registrations per event | >20 public / >10 broker |
| Turnout | Sign-ins / RSVPs + walk-ins | >50% RSVP show rate |
| Followup contact rate | Contacted <24h / total sign-ins | 100% <24h |
| Offers | Written offers / open house | Track per event |
| Neighbor leads | Valuation requests from circle | >3 per event |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| RSVPs no shows | Signups flat, turnout low | T-1 + day-of SMS, parking/entry clarity |
| Walk-ins no capture | Crowd, empty CRM | QR at door, greeter script, consent tag |
| No followup | Sign-ins stale >48h | HubSpot auto-sequence, <3h hot + 24h all |
| Neighbors annoyed | Complaints, no leads | Value invite, quiet hours signage, cleanup |

---

## Expected Output Format

### Promo Plan
[7-day calendar: portal/social/signage/neighbors with copy + slots]

### RSVP Flow
[Form fields + confirm/reminder JSON + sign-in QR script]

### Followup Sequence
[24h messages for attendees/no-shows/neighbor circle + broker]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | RSVP + sign-in sync | Contacts, lists, followup status | no |
| doddle.tool.v1.meta-ads.adsInsights | Local promo reach | Reach, RSVP clicks by ad | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate RSVPs or turnout.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| planner | Promo calendar + signage | 7-day schedule |
| copywriter | Invite + reminder copy | Portal/social/SMS copy |
| email-wizard | Followup sequences | 24h nurture flows |

---

## Related Skills

- `realty-listings` - Listing pages that feed open house traffic
- `events` - Event promo and logistics
- `sms` - RSVP reminders and day-of nudges

---

## Questions to Ask

1. Listing address + event date/time, public or broker open?
2. Market + CRM for RSVP/sign-in (HubSpot access?)?
3. Current RSVPs / turnout? (or grant HubSpot + Meta Ads access?)
