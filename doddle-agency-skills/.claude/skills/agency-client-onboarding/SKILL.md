---
name: agency-client-onboarding
id: doddle.agency.client-onboarding
version: 1.0.0
blueprint: ./blueprint.yaml
description: When an agency signs a new client and needs to run kickoff: onboarding workflows, access and asset checklists, communication cadence, expectation setting, and the first-30-days plan. Also use when the user mentions "kickoff," "onboarding a new client," "client setup," "access checklist," "communication cadence," or "first 30 days." Produces an onboarding plan, machine-readable access checklist, and kickoff deck.
---

# Agency Client Onboarding

The first 30 days decide the whole relationship. This skill turns a signed deal into a structured kickoff: what the agency needs (access, assets, stakeholders), what the client gets (clarity, cadence, success criteria), and who owns each step — so delivery starts on day one, not day fifteen.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- A proposal was won and the engagement starts
- Onboarding is ad-hoc and new clients stall waiting on access/assets
- Communication cadence needs to be established with a new client
- First-30-days plan needs structure (quick wins + trust building)

## Initial Assessment

Before planning, evaluate:

1. **Deal state**
   - Signed SOW scope, start date, team assigned? What did the proposal promise?
2. **Client readiness**
   - Known stakeholders, decision-maker, and their availability?
   - What access (logins, docs, data) will delivery need?
3. **Risk surface**
   - What delayed past onboarding? (assets late, access delayed, stakeholders unavailable)

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | New client details, engagement type, scope, start date |
| contract | string | no | Signed SOW with scope and terms |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| onboarding_plan | markdown | Kickoff workflow: milestones, owners, first-30-days plan |
| access_checklist | json | Access and asset checklist with owners and status |
| kickoff_deck | markdown | Kickoff agenda and deck content |

---

## Core Framework

### Step 1: Extract the Delivery Prerequisites
From the SOW: what must exist before real work starts — logins, analytics access, brand assets, domain access, stakeholder approvals. Each becomes a checklist item with an owner (agency side / client side) and a due date. Missing prerequisites are the #1 onboarding delay; listing them with owners kills that delay.

### Step 2: Set the Communication Cadence
Decide and document: weekly status (day/time, format), async channel (which tool), escalation path (who to ping when blocked), and meeting types (kickoff, weekly sync, monthly review). Cadence is a promise — write it into the onboarding plan so both sides can hold each other to it.

### Step 3: Plan the First 30 Days
Structure for trust: week 1 = kickoff + access + quick audit (agency shows competence fast); week 2 = first deliverable or insight delivered; weeks 3-4 = first measurable progress against the SOW's success criteria. Every week has a client-visible output — silent weeks erode trust.

### Step 4: Define Success Criteria Explicitly
What does "going well" mean by day 30, 60, 90? Written, measurable, agreed at kickoff. These become the scoreboard for `agency-reporting` later.

### Step 5: Kickoff Deck
Agenda: intros, scope recap (in plain language), access checklist walkthrough, cadence commitments, success criteria, first-30-days preview, open questions. Send the deck before the call so the meeting is about alignment, not reading.

---

## Access Checklist Guidance

```json
{
  "client": "[name]",
  "engagement": "[type]",
  "items": [
    {"item": "Analytics access (GA4)", "owner": "client", "due": "day 2", "status": "pending"},
    {"item": "CMS / repo access", "owner": "client", "due": "day 2", "status": "pending"},
    {"item": "Brand assets + guidelines", "owner": "client", "due": "day 3", "status": "pending"},
    {"item": "Stakeholder approval matrix", "owner": "agency", "due": "kickoff", "status": "pending"}
  ],
  "cadence": {"weekly": "Thu 10:00", "async": "[channel]", "escalation": "[name]"}
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Kickoff as a courtesy call | Two weeks lost before work starts | Kickoff delivers the checklist + cadence decisions |
| No success criteria | Relationship judged on feelings | Measurable 30/60/90 criteria agreed at kickoff |
| Silent first weeks | Trust erodes before value arrives | Client-visible output every week |
| Assumed access | Delivery blocked at day 7 | Owner + due date per prerequisite |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Checklist without owners | Nobody fetches the access | Owner (agency/client) + due date per item |
| Cadence decided ad-hoc | Meetings drift, blockers pile up | Written cadence with escalation path |
| Kickoff deck sent after call | Reading session, no alignment | Pre-read; meeting is for decisions |

---

## Related Skills

- `doddle.agency.proposals` — the SOW this onboarding executes
- `doddle.agency.reporting` — consumes the success criteria set at kickoff
- `doddle.agency.pricing` — retainer utilization starts with clean onboarding
- `doddle.marketing.measurement-plan` — for engagements where tracking setup is a deliverable
