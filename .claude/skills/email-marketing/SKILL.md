---
name: email-marketing
id: doddle.marketing.email-marketing
version: 1.5.1
blueprint: ./blueprint.yaml
description: Email campaign strategy, automation, and optimization. Use when creating email sequences, improving deliverability, designing automation workflows, or optimizing email performance.
---

# Email Marketing

Email campaign strategy, automation, and optimization for engagement and conversion.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply email expertise when:
- Creating email sequences and automations
- Improving deliverability and inbox placement
- Optimizing open rates and click rates
- Designing lifecycle email workflows
- Segmenting audiences for personalization
- A/B testing email elements

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign goal, list or segment, offer, timeline |
| audience | string | no | Target audience or segment |
| channel | string | no | Delivery channel or page context |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| draft | markdown | Campaign plan, see Expected Output Format |
| variants | json | Alternative subjects and angles with rationale |

---

## Core Concepts

### Email Types & Timing

| Type | Purpose | Timing | Frequency |
|------|---------|--------|-----------|
| Welcome | Onboard new subscribers | Immediate (<5 min) | Once |
| Nurture | Build trust over time | Drip sequence | 1-2x/week |
| Promotional | Drive sales/signups | Campaign-based | 1-4x/month |
| Transactional | Confirm actions | Triggered | As needed |
| Re-engagement | Win back inactive | 30-90 days inactive | Once per cycle |

### Email Performance Benchmarks

| Metric | Acceptable | Good | Excellent |
|--------|------------|------|-----------|
| Open Rate | 15-20% | 20-25% | 25%+ |
| Click Rate | 1-2% | 2-5% | 5%+ |
| Click-to-Open | 10-15% | 15-20% | 20%+ |
| Unsubscribe | <1% | <0.5% | <0.2% |
| Bounce Rate | <5% | <2% | <0.5% |
| Spam Complaint | <0.1% | <0.05% | <0.01% |

### Email Anatomy

```
From: [Name] from [Brand] <email@domain.com>
Subject: [Hook + Benefit] (50 chars optimal)
Preview: [Extends subject curiosity] (90-100 chars)

[Personalized greeting]
[Hook - address pain/desire in first line]
[Value delivery - main content]
[Social proof - testimonial/stat - optional]
[Single CTA button - clear action]
[P.S. - additional hook or urgency]

[Signature with human touch]
```

### Subject Line Formulas

| Formula | Example | Best For |
|---------|---------|----------|
| Question | "Still struggling with [pain]?" | Engagement |
| How-to | "How to [achieve outcome] in [time]" | Education |
| Curiosity | "[X] thing [audience] forget about [topic]" | Opens |
| Social Proof | "How [customer] got [result]" | Conversion |
| Urgency | "[X] hours left: [offer]" | Promotions |
| Personal | "{{first_name}}, quick question" | Response |

### Sequence Framework

**Welcome Sequence (7 days, 5 emails)**:
1. Day 0: Welcome + deliver lead magnet
2. Day 1: Quick win / immediate value
3. Day 3: Brand story / why we exist
4. Day 5: Social proof / case study
5. Day 7: Engagement check / preferences

**Nurture Sequence (6 weeks)**:
1. Week 1-2: Problem awareness
2. Week 3-4: Solution education
3. Week 5-6: Product introduction + offer

### Segmentation Strategy

| Segment Type | Criteria | Use For |
|--------------|----------|---------|
| Engagement | Open/click behavior | Re-engagement targeting |
| Interest | Content consumed | Topic personalization |
| Lifecycle | Lead stage | Funnel-appropriate content |
| Demographic | Role, company size | Message customization |
| Behavioral | Website actions | Trigger-based emails |

## Best Practices

### Deliverability Excellence
1. **Warm Up New Domains**: Gradual volume increase
2. **Authentication**: SPF, DKIM, DMARC properly configured
3. **List Hygiene**: Remove bounces and inactive regularly
4. **Engagement Signals**: Encourage replies, adds to contacts

### Copy Excellence
1. **Mobile First**: 60%+ read on mobile
2. **Scannable**: Short paragraphs, bullets, bold
3. **One CTA**: Don't compete with yourself
4. **Personal Tone**: Write to one person, not a list

### Testing Excellence
1. **Subject Lines**: Always A/B test
2. **Send Times**: Find optimal windows per segment
3. **Content Length**: Test short vs. long
4. **CTA Buttons**: Text, color, placement

## Agent Integration

| Agent | How They Use This Skill |
|-------|------------------------|
| `email-wizard` | Sequence design, automation setup |
| `copywriter` | Email copy creation |
| `lead-qualifier` | Segmentation criteria, triggers |
| `continuity-specialist` | Re-engagement strategies |

## Deliverability Deep-Dive

### Deliverability Fundamentals

**What Determines Deliverability:**
| Factor | Weight | Description |
|--------|--------|-------------|
| Sender Reputation | 30% | IP/domain reputation score |
| Authentication | 25% | SPF, DKIM, DMARC setup |
| Content Quality | 20% | Spam triggers, relevance |
| Engagement Signals | 15% | Opens, clicks, replies |
| List Quality | 10% | Bounces, complaints, inactive |

### Authentication Setup

**SPF (Sender Policy Framework):**
- Authorizes sending IPs for your domain
- DNS TXT record: `v=spf1 include:_spf.google.com ~all`
- Only one SPF record per domain

**DKIM (DomainKeys Identified Mail):**
- Cryptographic signature proving email authenticity
- Adds header with public key reference
- Required by major providers

**DMARC (Domain-based Message Authentication):**
- Policy for handling authentication failures
- DNS TXT record: `v=DMARC1; p=quarantine; rua=mailto:dmarc@domain.com`
- Start with `p=none`, graduate to `p=quarantine` or `p=reject`

### IP Warming Schedule

| Day | Volume | Purpose |
|-----|--------|---------|
| 1-3 | 50-100/day | Establish baseline |
| 4-7 | 100-500/day | Build reputation |
| 8-14 | 500-1000/day | Increase gradually |
| 15-21 | 1000-2000/day | Reach target volume |
| 22-30 | Full volume | Maintain reputation |

### Content Optimization

**Spam Trigger Words to Avoid:**
| Category | Words to Limit |
|----------|----------------|
| Urgency | "Act now," "Limited time," "Hurry" |
| Money | "Free," "Winner," "Cash," "Prize" |
| Medical | "Cure," "Remedy," "Weight loss" |
| Pressure | "Buy now," "Order today," "Don't miss" |

**Best Practices:**
- Text-to-image ratio > 60:40
- Single-link domains for tracking
- No URL shorteners
- Personalization tokens (reduces spam signals)
- Plain text version included

### List Hygiene

**Regular Cleaning Schedule:**
| Action | Frequency | Criteria |
|--------|-----------|----------|
| Hard bounce removal | Real-time | Immediate |
| Soft bounce monitoring | Per send | 3+ consecutive |
| Inactive subscriber review | Monthly | 90 days no opens |
| Spam complaint review | Per send | Any complaints |
| List validation | Quarterly | Full list scan |

**Re-engagement Campaign (for inactive subscribers):**
1. Email 1: "We miss you" + special offer
2. Email 2: "Is this still relevant?" + preference center
3. Email 3: "Last chance" + unsubscribe option
4. Remove non-responders after 3 emails

### Monitoring & Tools

**Deliverability Monitoring:**
| Metric | Tool | Target |
|--------|------|--------|
| Inbox Placement | GlockApps, Mail-Tester | >95% |
| Sender Score | SenderScore.org | >90 |
| Blacklist Check | MXToolbox | Not listed |
| Authentication | MXToolbox | All pass |

**Post-Send Analysis:**
- Monitor bounce rates by domain
- Track spam complaints per campaign
- Review block rates by ISP
- Analyze engagement by segment

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Wrong | Do This Instead |
|--------------|----------------|-----------------|
| Buying email lists | Destroys deliverability | Build organic list |
| No segmentation | Irrelevant content = unsubscribes | Segment by behavior |
| Too many CTAs | Confuses reader, dilutes clicks | One primary CTA |
| No unsubscribe | Illegal + spam complaints | Clear, easy unsubscribe |
| Batch and blast | No personalization | Behavior-triggered emails |

## Workflow Integration

- `crm-workflow.md` - Lead lifecycle stages, MQL/SQL definitions
- `sales-workflow.md` - Lead scoring thresholds for email triggers

## Related Commands

- `/sequence/welcome` - 7-day welcome sequence
- `/sequence/nurture` - 6-week lead nurture
- `/sequence/re-engage` - 21-day win-back
- `/content/email` - Email copy creation

## References

- `references/sequence-design.md` - Email sequence blueprints
- `references/deliverability.md` - Getting to inbox
- `references/segmentation.md` - Audience segmentation
- `references/automation.md` - Automation workflows
- `references/lead-nurturing-workflows.md` - Lead nurturing sequences

---

## Expected Output Format

Structure your response as:

### Campaign Plan
[Goal, segment, offer, schedule]

### Email Drafts
[Subject, preview, body, CTA per email]

### Deliverability Checklist
[Auth, list hygiene, warm-up status]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Batch and blast | Low opens, high unsubscribes | Segment by behavior |
| Poor deliverability | Spam placement | Authenticate, clean list, warm up |
| No attribution | Can't prove ROI | Track conversions to revenue |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.hubspot.contacts | Segments, automation, performance | Contact and engagement data | no |
| doddle.tool.v1.ga4.getReport | Post-click behavior, revenue | Sessions, conversions | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| email-wizard | Sequences, automation | Flow design, copy |
| lead-qualifier | Segmentation, scoring | Audience analysis |
| continuity-specialist | Retention campaigns | Lifecycle strategy |

---

## Related Skills

- **email-sequence**: For multi-email nurture and lifecycle flows
- **copywriting**: For landing pages emails link to
- **lead-magnets**: For list-growth assets
- **sms**: For cross-channel lifecycle messaging

---

## Questions to Ask

1. Campaign goal and timeline?
2. List or segment — size, source, engagement level?
3. Offer and primary CTA?
4. ESP, authentication status, and past performance?
