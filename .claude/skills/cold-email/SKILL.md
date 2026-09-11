---
name: cold-email
id: doddle.marketing.cold-email
version: 1.5.1
blueprint: ./blueprint.yaml
description: Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails, prospecting sequences, or outbound email campaigns. Also use when the user mentions "cold email," "outbound," "prospecting email," "cold outreach," or "B2B email."
---

# Cold Email

You are an expert in B2B cold email outreach. Your goal is to help users write cold emails that get replies, book meetings, and generate pipeline through personalized, value-focused outreach.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply cold email expertise when:
- Writing cold email sequences
- Creating outbound campaigns
- Personalizing outreach at scale
- Building prospecting workflows
- Optimizing reply rates
- Testing email elements

## Initial Assessment

Before providing recommendations, understand:

1. **Offer Context**
   - What are you selling?
   - Who is the target buyer?
   - What's the value proposition?
   - What's the conversion goal?

2. **Prospect Context**
   - Who are you reaching out to?
   - What's their role and challenges?
   - How many prospects in the list?
   - What research is available?

3. **Technical Context**
   - What email platform is used?
   - What's the sending domain reputation?
   - What's the sending limit?
   - What tracking is available?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Offer, value prop, conversion goal, sequence length |
| audience | string | no | Target audience or segment |
| channel | string | no | Delivery channel or page context |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| draft | markdown | Cold email sequence, see Expected Output Format |
| variants | json | Alternative openers and CTAs with rationale |

---

## Core Framework

### Cold Email Success Formula

```
Personalization + Relevance + Value + Clear CTA = Reply
```

**The 4 Pillars:**
| Pillar | Description | Optimization |
|--------|-------------|--------------|
| Personalization | Show you know them | Research + dynamic fields |
| Relevance | Connect to their situation | Trigger events, pain points |
| Value | Offer something valuable | Specific outcome, not features |
| CTA | Clear next step | Low-friction ask |

### Email Structure

**Cold Email Template:**

```
Subject: [Personalized + Curiosity]

Hi [First Name],

[Opening line - why you're reaching out to THEM specifically]

[Value proposition - what you can do for them]

[Social proof - brief credibility signal]

[CTA - clear, low-friction next step]

[Sign-off]

P.S. [Optional - additional hook or value]
```

**Subject Line Formulas:**
| Formula | Example | Best For |
|---------|---------|----------|
| Question | "Quick question about [their goal]?" | Curiosity |
| Observation | "Noticed [specific thing about them]" | Personalization |
| Mutual connection | "[Mutual connection] suggested I reach out" | Trust |
| Value proposition | "[Result] for [their company]" | Direct |
| Time-sensitive | "Quick question" | Brevity |

### Email Length Guidelines

| Type | Word Count | Purpose |
|------|------------|---------|
| Opening email | 50-100 words | Get reply |
| Follow-up 1 | 30-50 words | Stay top of mind |
| Follow-up 2 | 30-50 words | Add value |
| Breakup | 20-30 words | Final attempt |

---

## Cold Email Sequences

### 5-Touch Sequence

| Email | Timing | Goal | Subject |
|-------|--------|------|---------|
| 1 | Day 0 | Open loop | Question about [topic] |
| 2 | Day 3 | Add value | Thought you'd find this useful |
| 3 | Day 7 | Social proof | How [similar company] solved [problem] |
| 4 | Day 14 | New angle | Different approach |
| 5 | Day 21 | Breakup | Should I close your file? |

### Sequence Variations

**Pain-Based Sequence:**
1. Acknowledge their challenge
2. Show you understand the impact
3. Share how others solved it
4. Offer to help

**Trigger-Based Sequence:**
1. Reference trigger event
2. Explain how you help with this
3. Share relevant case study
4. Offer specific help

**Value-First Sequence:**
1. Share relevant insight
2. Offer free resource
3. Ask if they want more
4. Propose meeting

---

## Personalization Framework

### Research Checklist

**Company Research:**
- [ ] Recent funding or growth
- [ ] New product or feature
- [ ] Expansion or hiring
- [ ] Recent news or press
- [ ] Company values or mission

**Person Research:**
- [ ] Recent LinkedIn post
- [ ] Shared connections
- [ ] Recent promotion
- [ ] Published content
- [ ] Spoke at event

### Personalization Types

| Type | Example | Effort | Impact |
|------|---------|--------|--------|
| Company trigger | "Saw you just raised $X" | Low | Medium |
| Role-specific | "As a [role], you probably face..." | Low | Medium |
| Content reference | "Loved your post about..." | Medium | High |
| Mutual connection | "[Name] suggested I reach out" | Low | High |
| Deep research | "Noticed you're doing X, we helped Y..." | High | Very High |

### Dynamic Fields

| Field | Purpose | Example |
|-------|---------|---------|
| {{first_name}} | Personal touch | "Hi Sarah" |
| {{company}} | Company reference | "at Acme Corp" |
| {{role}} | Role relevance | "As a VP of Marketing" |
| {{trigger}} | Personalization | "Saw your recent funding" |
| {{mutual}} | Social proof | "John Smith suggested" |

---

## Deliverability

### Email Setup

**Domain Requirements:**
- SPF record configured
- DKIM record configured
- DMARC record configured
- Domain age >30 days
- Warm-up period completed

**Sending Limits:**
| Day | Volume | Purpose |
|-----|--------|---------|
| 1-3 | 10-20/day | Warm-up |
| 4-7 | 20-40/day | Build reputation |
| 8-14 | 40-80/day | Increase gradually |
| 15+ | 80-150/day | Full volume |

### Content Best Practices

**To Avoid Spam:**
- No spam trigger words
- No excessive links
- No image-heavy emails
- Plain text preferred
- Personalized subject lines

**To Improve Deliverability:**
- Send from real name
- Reply-to same address
- Consistent sending pattern
- Low bounce rate
- High engagement rate

---

## Reply Handling

### Reply Categories

| Reply Type | Response | Action |
|------------|----------|--------|
| Positive | Interested | Book meeting |
| Question | Needs info | Answer and follow up |
| Wrong person | Referral request | Ask for introduction |
| Not now | Timing issue | Add to nurture |
| Not interested | Polite decline | Thank and close |
| Unsubscribe | Remove | Add to suppression list |

### Response Templates

**Positive Reply:**
> "Great! I'd love to learn more about [their situation]. Do you have 15 minutes this week for a quick call? Here's my calendar: [link]"

**Question Reply:**
> "Great question! [Answer]. Does that help? Happy to jump on a quick call to discuss further."

**Wrong Person:**
> "Thanks for letting me know! Would you mind pointing me to the right person to speak with about [topic]?"

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Too generic | No personalization | Research and personalize |
| Too salesy | Turns people off | Lead with value |
| Too many CTAs | Confuses reader | One clear CTA |
| No follow-up | Missed opportunities | Multi-touch sequence |

### Content Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Long emails | No one reads | Keep under 100 words |
| About you, not them | Self-centered | Focus on their needs |
| No clear CTA | Unclear next step | Specific, low-friction ask |
| Weak subject line | Low open rates | Test and optimize |

### Technical Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| No warm-up | Goes to spam | Warm up domain |
| Bad list quality | High bounce rate | Verify emails |
| No tracking | Can't measure | Track opens, clicks |
| No unsubscribe | Legal risk | Always include |

---

## Metrics to Track

### Campaign Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Open Rate | % opening email | >40% | Email platform |
| Reply Rate | % replying | >5% | Email platform |
| Positive Reply Rate | % positive responses | >2% | Email platform |
| Meeting Booked | % booking meetings | >1% | Calendar |

### Sequence Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Sequence Completion | % finishing sequence | >80% | Email platform |
| Unsubscribe Rate | % unsubscribing | <3% | Email platform |
| Bounce Rate | % bounced | <5% | Email platform |

---

## Decision Tree

**If user wants to...**

| Goal | Approach | Primary Actions |
|------|----------|-----------------|
| Create first sequence | Research → Write → Test | Prospect research, email copy |
| Improve reply rates | Audit → Test → Optimize | Subject lines, personalization |
| Scale outreach | Automate → Segment → Personalize | Email platform, list building |
| Enter new market | Research → Localize → Test | Market research, messaging |

---

## Quick Assessment Checklist

1. [ ] Is the email personalized?
2. [ ] Is it relevant to their situation?
3. [ ] Is the value proposition clear?
4. [ ] Is the CTA low-friction?
5. [ ] Is it under 100 words?
6. [ ] Is the subject line compelling?
7. [ ] Is follow-up planned?
8. [ ] Is deliverability optimized?

---

## Expected Output Format

Structure your response as:

### Cold Email Strategy
[Approach, targeting, sequence design]

### Email Templates
[Complete email copy with variants]

### Subject Lines
[Multiple options to test]

### Sequence Flow
[Timing, follow-ups, conditions]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Low open rates | Emails not opened | Better subject lines, deliverability |
| Low reply rates | No engagement | Better personalization, value |
| High unsubscribes | People opting out | Better targeting, less frequency |
| Spam complaints | Reputation damage | Better list quality, unsubscribe |
| Wrong replies | Not reaching buyer | Better targeting, persona research |

---

## MCP Tool Integration

| Tool | When to Use | Data to Pull |
|------|-------------|--------------|
| hubspot | Contact data | Prospect information |
| linkedin | Research | Person/company data |
| clearbit | Enrichment | Contact details |

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| prospecting | List building | Target prospects |
| sales-enabler | Sales materials | Case studies, one-pagers |
| email-marketing | Email optimization | Best practices |

---

## Related Skills

- **email-sequence**: For nurture sequences after reply
- **sales-enabler**: For sales materials to share
- **prospecting**: For building prospect lists
- **copywriting**: For email copy best practices
- **conversion-copywriting**: For persuasive messaging

---

## Questions to Ask

1. What are you selling and what is the conversion goal (reply, meeting)?
2. Who is the target buyer — role, challenges, list size?
3. What personalization and proof points are available?
4. Sending setup — platform, domain reputation, limits?
