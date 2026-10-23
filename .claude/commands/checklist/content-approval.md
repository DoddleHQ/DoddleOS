---
description: Content approval workflow for team collaboration
argument-hint: [content-type] [approvers]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `content-strategy`, `marketing-fundamentals` skills.

**Components**: Reference `./.claude/components/interactive-questions.md`

---

## Interactive Parameter Collection

### Step 1: Ask Output Scope

**Question:** "What level of approval workflow do you need?"
**Header:** "Scope"
**MultiSelect:** false

**Options:**
- **Basic** - Simple workflow stages
- **Recommended** - Full workflow with checklists
- **Complete** - Enterprise with escalation
- **Custom** - I'll specify requirements

---

### Step 2: Ask Content Type

**Question:** "What type of content needs approval?"
**Header:** "Content"
**MultiSelect:** false

**Options:**
- **Blog/Article** - Written content
- **Social Post** - Social media content
- **Email** - Email campaigns
- **Landing Page** - Web pages

---

### Step 3: Ask Team Size

**Question:** "What's your team size and structure?"
**Header:** "Team"
**MultiSelect:** false

**Options:**
- **Solo** - Self-review only
- **Small** - 2-3 reviewers
- **Medium** - Multiple roles involved
- **Enterprise** - Full department

---

### Step 4: Ask Compliance Needs

**Question:** "What compliance requirements apply?"
**Header:** "Compliance"
**MultiSelect:** true

**Options:**
- **Brand** - Voice and style
- **SEO** - Search optimization
- **Legal** - Claims and disclaimers
- **Accessibility** - A11y standards

---

### Step 5: Confirmation

**Display summary:**

```markdown
## Content Approval Configuration

| Parameter | Value |
|-----------|-------|
| Content Type | [description] |
| Team Size | [selected team] |
| Compliance | [selected compliance] |
| Scope | [Basic/Recommended/Complete] |
```

**Question:** "Create this approval workflow?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, create workflow** - Start creation
- **No, change settings** - Go back to modify

---

## Workflow

1. **Draft Creation**
   - Creator completes content
   - Self-review checklist
   - Submit for review

2. **Review Process**
   - Content review
   - SEO review
   - Legal review (if needed)
   - Feedback provided

3. **Revisions**
   - Address feedback
   - Update version
   - Request re-review

4. **Approval & Publish**
   - Final sign-off
   - Schedule content
   - Publish and verify

---

## Agent Delegation

| Task | Agent | Trigger |
|------|-------|---------|
| Content creation | `copywriter` | Draft stage |
| SEO review | `attraction-specialist` | Optimization |
| Brand voice check | `brand-voice-guardian` | Gate review |
| CRO check | `conversion-optimizer` | Gate review (conversion content) |
| Quality check | `researcher` | Fact verification |
| Final polish | `copywriter` | Revisions |

---

## Output Format

### Basic Scope

```markdown
## Content Approval Workflow

### Stages
Draft → Review → Revisions → Approval → Publish

### Stage Checklist
**Draft:**
- [ ] Content complete
- [ ] Self-reviewed

**Review:**
- [ ] Feedback provided
- [ ] Revisions requested

**Approval:**
- [ ] Sign-off received
- [ ] Scheduled
```

### Recommended Scope

[Include Basic + Full stage checklists + Reviewer roles + SLA table + Feedback format]

### Complete Scope

[Include all + Escalation process + Quality standards + Content type matrix + Version control]

---

## Workflow Stages

### Stage 1: Draft Creation
- [ ] Brief reviewed and understood
- [ ] Target audience defined
- [ ] Key messages included
- [ ] SEO keywords incorporated
- [ ] CTA clear and compelling
- [ ] Self-review complete

### Stage 2: Review Process
**Content Reviewer:**
- [ ] Accuracy and factual correctness
- [ ] Brand voice consistency
- [ ] Grammar and spelling
- [ ] Logical flow

**SEO Reviewer:**
- [ ] Primary keyword placement
- [ ] Header structure
- [ ] Meta tags optimized

### Stage 3: Revisions
- [ ] Address all "Must Fix" items
- [ ] Consider "Should Fix" suggestions
- [ ] Update version number

### Stage 4: Final Approval
- [ ] All feedback addressed
- [ ] Quality standards met
- [ ] Tracking references claimed (UTMs, event names from the campaign measurement plan)
- [ ] Ready for publication

---

## Blueprint Gate Alignment

Creative skills in this pack end with an approval gate node (`type: gate`, `approvers: [owner]`, `on_approve: proceed`, `on_reject: revise`). When content comes from a Doddle blueprint run, this command fills the reviewer role of that gate:

| Skill | Gate id | Pre-gate reviewer agent |
|-------|---------|--------------------------|
| copywriting / conversion-copywriting | `approve_copy` | `brand-voice-guardian` or `conversion-optimizer` |
| email-sequence / email-marketing / sms | `approve_copy` | `brand-voice-guardian` |
| social-media / video-marketing / image | `approve_content` | `copywriter` + reviewer pair |

Gate rules: nothing distributes before approval; rejected assets loop back to the creating agent with user notes (max 2 rounds); approval decisions are logged per asset.

---

## Content Types & Requirements

| Type | Reviewers | Approval | SLA |
|------|-----------|----------|-----|
| Blog Post | Content + SEO | Marketing Lead | 3 days |
| Social Post | Content | Social Manager | Same day |
| Email | Content + Legal | Email Manager | 2 days |
| Landing Page | Content + SEO + Legal | Marketing Lead | 5 days |

---

## Output Location

Save workflow to: `./docs/workflows/approval-[content-type]-[YYYY-MM-DD].md`
