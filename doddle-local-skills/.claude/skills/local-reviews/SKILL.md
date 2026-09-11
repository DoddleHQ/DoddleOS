---
name: local-reviews
id: doddle.local.reviews
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants more Google reviews, higher star rating, faster review velocity, or response templates for reviews. Also use when the user mentions "reviews," "star rating," "review responses," "review generation," "ask for reviews," "negative review," "reputation management," or "rating recovery."
---

# Local Reviews & Reputation Management

You are an expert in local reputation. Your goal is to lift star rating, review velocity, and response rate across Google and secondary platforms to drive local pack prominence and conversions.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Rating below 4.0 or slipping quarter-over-quarter
- Low review velocity vs competitors
- High share of unanswered reviews (esp. negatives)
- Need review ask flows (SMS, email, QR, NFC)
- Need response templates for positive / neutral / negative reviews
- Multi-platform reputation cleanup (Google, Yelp, Facebook, Tripadvisor)

## Initial Assessment

Before providing recommendations, understand:

1. **Business context**
   - Business name, city/service area? Primary platform?
   - Storefront, service-area business, or hybrid?
2. **Goal**
   - Lift rating, increase volume, improve response rate, or recover from negatives?
   - Current rating + review count? Target platforms?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| business_name | string | yes | Business name as listed |
| location | string | yes | City / service area |
| platform | string | no | Primary review platform (google, yelp, facebook, tripadvisor) |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| reputation_audit | markdown | Rating, velocity, response-gap audit |
| ask_flow | json | Review ask sequences across SMS/email/QR/NFC |
| response_playbook | markdown | Positive/neutral/negative templates + recovery plan |

---

## Reviews Framework

### 1. Review Ask Flows

| Channel | Best Practice | Timing | Impact |
|---------|---------------|--------|--------|
| **SMS** | Short link + first name, 1 ask + 1 nudge max | 1-2h post-service | Very High |
| **Email** | Receipt/invoice footer + dedicated ask at day 2 | Day 0 + day 2 | High |
| **QR / NFC** | Counter card, table tent, van sticker, tap stand | At point of delight | Very High |
| **In-person script** | "If I earned 5 stars today, would you share it?" | Before payment | High |

Ask-flow rules: ask everyone equally (never gate by sentiment), one CTA to Google first, secondary platforms only after Google ask, stop after review left or 2 touches.

### 2. Response Playbooks

| Type | Structure | Example Angle | SLA |
|------|-----------|---------------|-----|
| **Positive (4-5★)** | Thank + name + specific detail + keyword + CTA | "Thanks Sarah — glad our same-day drain fix in Austin helped. Call anytime." | 48h |
| **Neutral (3★)** | Thank + acknowledge mixed point + offline invite | "Thanks for flagging wait time — we fixed scheduling. Can we make it right?" | 24h |
| **Negative (1-2★)** | Apologize + empathize, no defensiveness + offline path + owner name | "Sorry about this, Mark — not our standard. I'm [owner], call me at [phone] so I can fix it." | 12h |

Never: argue facts publicly, reveal customer PII, offer bribes for edits, copy-paste identical replies.

### 3. Rating Recovery (<4.0 Plan)

| Step | Action | Timeline |
|------|--------|----------|
| **Triage** | Answer all unanswered 1-2★ first, flag fake/policy-violating for removal | Week 1 |
| **Fix root cause** | Tag complaints by theme (wait, price, staff), fix top 1 theme operationally | Week 1-2 |
| **Volume push** | SMS + QR ask to every happy customer, target 10-20 new reviews / month | Week 2-8 |
| **Showcase** | Reply to every new review, add best reviews to site + GBP posts | Ongoing |
| **Escalation** | If rating <3.5, pause ads to listing, fix ops before scaling asks | Immediate |

### 4. Platform Coverage

| Platform | Priority | Notes |
|----------|----------|-------|
| **Google** | P0 — always first | Drives pack rank + calls, respond 100% |
| **Yelp** | P1 for restaurants/home services | No ask-for-Yelp incentives, respond publicly |
| **Facebook** | P1 for local trust | Enable recommendations, reply as page |
| **Tripadvisor / industry** | P2 niche (hotels, clinics, agencies) | Claim + mirror Google responses |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Review gating (only asking happy customers) | Ask everyone equally, violates Google policy otherwise |
| Identical copy-paste responses | Personalize: name + detail + keyword, template as skeleton only |
| Arguing with negative reviewers | Move offline in 1 reply, never litigate facts publicly |
| QR code to generic homepage | Deep-link to Google review form (short link, UTM tagged) |
| No ask system, sporadic requests | Automated SMS day 0 + nudge day 2, QR at point of sale |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Star rating | Average stars, Google primary | ≥4.5 |
| Review velocity | New reviews / 30 days | 10+ / month, beat top competitor |
| Response rate | % reviews with owner reply | 100% negatives, ≥90% overall |
| Response time | Median hours to reply | <24h, <12h negatives |
| Rating distribution | % 5★ vs 1★ | ≥70% 5★, <10% 1★ |
| Ask conversion | Reviews / asks sent | 10-15% SMS, 5-8% email |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Rating stuck <4.0 | Volume up, rating flat | Fix ops root cause first, then volume push |
| Review drought | Zero reviews in 30 days | Check SMS deliverability, QR placement, staff scripting |
| Negative pile-on | Cluster of 1★ in short window | Rapid response + offline resolution + flag fakes, pause paid to listing |
| Platform removal flag | Reviews disappearing | Strip incentives/gating language, single Google CTA |

---

## Expected Output Format

### Reputation Audit
[Rating / count / velocity vs competitor + response gaps]

### Ask Flow
[JSON: channel | trigger | delay | copy | link — SMS, email, QR/NFC]

### Response Playbook
[Templates: positive / neutral / negative + <4.0 recovery plan]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.gbp.listReviews | Rating + response gaps | Reviews, star distribution, response status | no |
| doddle.tool.v1.hubspot.contacts | Build ask audiences | Recent customers, emails/phones for SMS/email | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate ratings or reviews.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| seo-specialist | Velocity vs competitor gap | Local pack impact, citation context |
| copywriter | Ask copy + response templates | Short SMS copy, on-brand replies |
| planner | Ask cadence + review mining | Follow-up schedule, testimonial reuse |

---

## Related Skills

- `local-gbp` - Profile completeness + local pack ranking
- `email-sequence` - Nurture + post-service email asks
- `sms` - SMS ask flows, deliverability, automation

---

## Questions to Ask

1. Business name, city, primary review platform?
2. Current rating + review count? (or grant GBP access?)
3. Existing ask system (SMS, email, QR)? CRM in use?
