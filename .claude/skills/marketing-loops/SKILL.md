---
name: marketing-loops
id: doddle.marketing.marketing-loops
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to set up a recurring, self-running marketing workflow — a repeatable loop an AI agent runs on a schedule (daily, weekly, monthly). Also use when the user mentions "marketing loop," "automated workflow," "recurring task," "scheduled workflow," "marketing automation," or "self-running marketing."
---

# Marketing Loops

You are an expert in designing and implementing recurring marketing workflows. Your goal is to help users create self-running marketing loops that execute on a schedule, compound over time, and require minimal manual intervention.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply marketing loops expertise when:
- Setting up recurring marketing tasks
- Automating content distribution
- Creating evergreen campaigns
- Building growth loops
- Implementing scheduled workflows
- Reducing manual marketing work

## Initial Assessment

Before providing recommendations, understand:

1. **Current State**
   - What marketing tasks are manual?
   - What's being repeated regularly?
   - What's working that should be automated?
   - What's the current tech stack?

2. **Goals**
   - What outcomes should the loop produce?
   - What's the expected ROI?
   - What's the timeline to implement?

3. **Resources**
   - What tools are available?
   - What's the technical capability?
   - What's the budget for automation?

---

## Inputs Schema

Declare user inputs the blueprint expects. Formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Manual tasks to automate, current tech stack, resources |
| goal | string | no | Primary goal (automation, compounding output, manual work reduction) |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| strategy | markdown | Loop design with trigger, steps, output, metrics |
| action_plan | json | Loop tasks with owner, effort, impact |

---

## Core Framework

### What is a Marketing Loop?

```
Trigger → Action → Outcome → Trigger (repeat)
```

**Loop Components:**
| Component | Description | Example |
|-----------|-------------|---------|
| Trigger | What starts the loop | Schedule, event, condition |
| Action | What the loop does | Content creation, outreach |
| Outcome | What the loop produces | Leads, traffic, revenue |
| Trigger | What restarts the loop | New cycle begins |

### Types of Marketing Loops

| Loop Type | Trigger | Action | Outcome |
|-----------|---------|--------|---------|
| Content Distribution | New content published | Share across channels | Traffic, engagement |
| Lead Nurturing | New lead captured | Send nurture sequence | Conversions |
| Social Posting | Schedule (daily/weekly) | Create and post content | Engagement, followers |
| SEO Monitoring | Weekly schedule | Check rankings, fix issues | Organic traffic |
| Email Re-engagement | Inactivity trigger | Win-back sequence | Re-activated users |
| Referral Program | Customer success | Ask for referrals | New customers |
| Review Collection | Post-purchase | Request review | Social proof |
| Competitor Monitoring | Weekly schedule | Track competitor changes | Strategic insights |

### Loop Design Framework

```yaml
Loop Name: [Name]
Frequency: [Daily/Weekly/Monthly]
Trigger: [What starts it]
Steps:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
Output: [What it produces]
Metrics: [How to measure success]
Owner: [Who maintains it]
```

---

## Common Marketing Loops

### 1. Content Distribution Loop

```yaml
Loop: Content Distribution
Frequency: When new content published
Trigger: New blog post/content live

Steps:
  1. Share on Twitter/X (thread format)
  2. Share on LinkedIn (native post)
  3. Share in relevant communities
  4. Send to email list
  5. Schedule social reshares (1 week, 1 month, 3 months)
  6. Update internal content database

Output: Multi-channel traffic
Metrics: Views, clicks, shares
```

### 2. Social Media Posting Loop

```yaml
Loop: Social Content
Frequency: Daily
Trigger: Schedule (9am local time)

Steps:
  1. Pull content from content calendar
  2. Adapt for platform format
  3. Post to scheduled platform
  4. Monitor engagement (1 hour)
  5. Respond to comments
  6. Log performance metrics

Output: Consistent social presence
Metrics: Engagement rate, followers, reach
```

### 3. Lead Nurture Loop

```yaml
Loop: Lead Nurture
Frequency: Continuous (triggered)
Trigger: New lead captured

Steps:
  1. Send welcome email (immediate)
  2. Day 1: Quick win content
  3. Day 3: Brand story
  4. Day 5: Social proof
  5. Day 7: Engagement check
  6. Day 14: Product introduction
  7. Day 21: Offer

Output: Qualified leads
Metrics: Open rate, click rate, conversion
```

### 4. SEO Monitoring Loop

```yaml
Loop: SEO Monitor
Frequency: Weekly
Trigger: Monday 9am

Steps:
  1. Pull Google Search Console data
  2. Check ranking changes
  3. Identify new keyword opportunities
  4. Check for technical issues
  5. Review competitor rankings
  6. Generate weekly report
  7. Send to team

Output: SEO health report
Metrics: Rankings, traffic, issues fixed
```

### 5. Review Collection Loop

```yaml
Loop: Review Collection
Frequency: Continuous (triggered)
Trigger: 7 days post-purchase

Steps:
  1. Send review request email
  2. If positive → direct to review site
  3. If negative → direct to support
  4. Follow up if no response (3 days)
  5. Log all reviews
  6. Respond to reviews within 24 hours

Output: Social proof
Metrics: Review count, rating, response rate
```

### 6. Competitor Monitoring Loop

```yaml
Loop: Competitor Watch
Frequency: Weekly
Trigger: Friday 10am

Steps:
  1. Check competitor websites for changes
  2. Monitor competitor social accounts
  3. Track competitor pricing changes
  4. Review competitor content updates
  5. Check for new competitor features
  6. Generate competitive intelligence report

Output: Competitive intelligence
Metrics: Changes detected, strategic insights
```

---

## Loop Implementation

### Tool Stack for Loops

| Loop Type | Tools | Integration |
|-----------|-------|-------------|
| Content | Buffer/Hootsuite + Email | Zapier/Make |
| Social | Scheduling tool + Analytics | Native integrations |
| Lead Nurture | Email platform + CRM | Native integrations |
| SEO | GSC + Ahrefs/SEMrush | API + Zapier |
| Reviews | Email + Review platforms | Zapier |
| Competitors | Web scraper + Alerting | Custom scripts |

### Implementation Checklist

- [ ] Define loop trigger
- [ ] Map all steps
- [ ] Set up automation tool
- [ ] Create templates/content
- [ ] Configure notifications
- [ ] Set up tracking
- [ ] Test the loop
- [ ] Document the process
- [ ] Schedule the loop
- [ ] Monitor first few cycles

### Loop Documentation Template

```markdown
# [Loop Name]

## Overview
- **Purpose:** [What this loop does]
- **Frequency:** [How often it runs]
- **Owner:** [Who maintains it]
- **Tools:** [What's used]

## Trigger
[What starts this loop]

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Output
[What this loop produces]

## Metrics
| Metric | Target | Current |
|--------|--------|---------|
| [Metric] | [Target] | [Current] |

## Troubleshooting
| Issue | Solution |
|-------|----------|
| [Common issue] | [Fix] |

## Updates
| Date | Change | Why |
|------|--------|-----|
| [Date] | [Change] | [Reason] |
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Too many loops | Overwhelmed, quality drops | Start with 2-3 key loops |
| No clear outcome | Loops without purpose | Define success metrics |
| Manual loops | Defeats the purpose | Automate execution |
| No ownership | Loops get neglected | Assign clear owners |

### Implementation Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Over-automation | Robots talking to robots | Keep human touch points |
| No monitoring | Loops break silently | Monitor first cycles |
| No documentation | Can't maintain | Document everything |
| No testing | Broken loops | Test before launching |

### Optimization Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Set and forget | Loops degrade | Regular optimization |
| No A/B testing | Missing improvements | Test loop elements |
| No feedback loop | Can't improve | Collect feedback |
| No reporting | Can't measure | Track and report |

---

## Metrics to Track

### Loop Performance Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Loop Completion | % cycles completed | >95% | Automation tool |
| Output Volume | # of outputs per cycle | Growing | Manual tracking |
| Quality Score | Quality of outputs | >8/10 | Manual review |
| Time Saved | Hours saved vs. manual | >80% | Estimate |

### Business Impact Metrics
| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| Traffic Generated | Visitors from loops | Growing | Analytics |
| Leads Generated | Leads from loops | Growing | CRM |
| Revenue Influenced | Revenue from loops | Growing | CRM |
| Efficiency Gain | Cost reduction | Growing | Finance |

---

## Decision Tree

**If user wants to...**

| Goal | Approach | Primary Actions |
|------|----------|-----------------|
| Automate repetitive tasks | Identify → Map → Automate | Task analysis, tool selection |
| Build growth loops | Design → Implement → Optimize | Loop design, testing |
| Reduce manual work | Audit → Prioritize → Automate | Task audit, automation |
| Scale marketing | Systematize → Automate → Measure | Loop creation, metrics |

---

## Quick Assessment Checklist

1. [ ] Is there a clear trigger?
2. [ ] Are all steps defined?
3. [ ] Is the loop automated?
4. [ ] Is there a success metric?
5. [ ] Is someone monitoring it?
6. [ ] Is it documented?
7. [ ] Is it optimized regularly?
8. [ ] Is it generating value?

---

## Expected Output Format

Structure your response as:

### Loop Design
[Complete loop specification]

### Implementation Plan
[Tools, setup, timeline]

### Documentation
[Process documentation]

### Metrics Dashboard
[How to measure success]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Loop breaks | Output stops | Monitor and alerting |
| Quality degrades | Poor outputs | Quality checks |
| No engagement | Low performance | Optimize content |
| Over-automation | Robotic feel | Add human touch |
| No ROI | Not worth it | Re-evaluate loop value |

---

## MCP Tool Integration

| Tool | When to Use | Data to Pull |
|------|-------------|--------------|
| zapier | Automation | Workflow data |
| hubspot | CRM automation | Contact data |
| google-analytics | Performance | Traffic data |
| slack | Notifications | Alert messages |

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| project-manager | Loop management | Task tracking |
| email-wizard | Email loops | Email automation |
| content-strategy | Content loops | Content planning |
| analytics-attribution | Measurement | Performance data |

---

## Questions to Ask

1. Which manual tasks should the loop replace, and on what schedule?
2. Current tech stack and automation budget?
3. What output should each loop run produce, and how is success measured?
4. Who owns the loop when it breaks?

---

## Related Skills

- **email-sequence**: For email automation loops
- **content-strategy**: For content distribution loops
- **social-media**: For social posting loops
- **analytics-attribution**: For measuring loop performance
- **project-manager**: For loop management
