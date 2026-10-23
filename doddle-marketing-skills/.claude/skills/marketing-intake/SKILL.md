---
name: marketing-intake
id: doddle.marketing.marketing-intake
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user brings a business problem, growth bottleneck, campaign request, or new client work and wants it turned into an executable brief. Also use when the user mentions "intake," "marketing brief," "project brief," "kickoff," "objectives," "constraints," "success criteria," or "turn this into a plan." Produces the machine-readable protocol (brief_schema) that downstream Doddle blueprint nodes consume.
---

# Marketing Intake

Turn a raw problem — growth bottleneck, campaign request, new client work — into a protocol the engine can run. This is the entry node of the DoddleOS campaign pipeline: it captures what the business wants (the goal, the offer, the constraints) and writes it so downstream skills can consume it without re-asking.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Starting any new campaign, client engagement, or marketing initiative
- A user describes a problem in prose and expects a plan to follow
- Prior work exists but lacks a written success definition (goal, KPIs, constraints)
- Fragmented requests need consolidation into one source of truth before planning
- An existing brief exists but is missing budget, timeline, or KPI targets

## Initial Assessment

Before structuring the brief, extract (ask only for what is missing — max 5 questions):

1. **The problem type**
   - Growth bottleneck (traffic, conversion, retention)?
   - A product launch or feature campaign?
   - An owner decision (pricing, channel mix, budget)?
2. **The business**
   - What is being sold, at what price, to whom?
   - What constraints apply (budget, time, headcount, compliance)?
3. **What success means**
   - One primary KPI, at most two guardrail KPIs
   - Over what time window?

---

## Inputs Schema

Declare user inputs the blueprint expects. Formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Raw problem or request in the user's words |
| product | string | no | Product or service; infer from context if missing |
| audience | string | no | Target audience or segment; infer if missing |
| offer | string | no | Offer, price, or ask; propose from context if missing |
| budget | string | no | Budget range; ask if missing |
| timeline | string | no | Key dates; ask if missing |
| kpi_targets | string | no | Success metrics; propose from context if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| brief | markdown | Written intake protocol: goal, offer, constraints, success definition |
| brief_schema | json | Machine-readable protocol for downstream DAG nodes |

---

## Core Framework

### Step 1: Capture the Problem Verbatim
Restate the user's situation in one paragraph without inventing detail. Quote their words for the goal and constraints.

### Step 2: Classify the Intent
| Intent | Signature | Downstream focus |
|--------|-----------|------------------|
| Bottleneck | Metric is stuck, fix needed | Diagnose → measure-plan |
| Launch | New offer, date-driven | Create → approve → distribute |
| Decision | Options on the table | Budget-allocator + analyze |
| Retention | Churn/expansion focus | Lifecycle + revops |

### Step 3: Extract the Protocol Fields
Fill every field of the Brief Protocol template. Anything not stated is an `assumption` — mark it, propose a default, and list it in unresolved questions. Never leave a field silently empty.

### Step 4: Define Success Precisely
- **Primary KPI**: the single number this campaign must move (e.g. trial signups/mo)
- **Guardrail KPIs**: what must not degrade (e.g. CAC ceiling, unsubscribe rate)
- **Kill criteria**: when to stop or pivot (e.g. CAC > $150 after 200 spend)

### Step 5: Emit the Protocol
Produce `brief` (human document) and `brief_schema` (machine JSON). The JSON is the artifact downstream nodes consume — keep field names stable.

---

## Brief Protocol Template

```markdown
# Intake Brief: [Campaign name]
**Date:** [YYYY-MM-DD] | **Owner:** [name/team] | **Status:** draft

## 1. Problem & Goal
- **Problem type:** [bottleneck / launch / decision / retention]
- **Primary KPI:** [metric] → [target] by [date]

## 2. Offer & Audience
- **Offer:** [what is being sold, price, ask]
- **Audience:** [segment, size estimate, where they are]

## 3. Constraints
- **Budget:** [amount / range / unconfirmed]
- **Timeline:** [start → end, key milestones]
- **Resources:** [people, tools]
- **Compliance/brand:** [disclaimers, restricted topics, tone rules]

## 4. Success Definition
- **Primary KPI:** [metric = definition, target, measurement source]
- **Guardrails:** [metric + ceiling]
- **Kill criteria:** [when to stop]

## 5. Open Assumptions
- [Assumption → proposed default → needs confirmation? Y/N]
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Goal-less briefs | "More growth" can't be measured | One primary KPI with number + date |
| Silent assumptions | Downstream stages plan on guesses | Mark every assumed field explicitly |
| Scope in prose only | Agents can't consume prose reliably | Emit brief_schema JSON alongside |
| Multiple primary KPIs | Split resourcing and reporting | Rank metrics; one primary, rest guardrails |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Interrogation fatigue | 12 questions lose the user | Max 5 questions; infer + flag the rest |
| Skipping kill criteria | Failing campaigns run forever | Define stop conditions at intake |
| Vague constraints | "soon-ish" breaks scheduling | Convert to dates or ranges or mark unconfirmed |

---

## Related Skills

- `doddle.marketing.campaign-plan` — decomposes this protocol into parallel jobs
- `doddle.marketing.measurement-plan` — turns KPI targets into tracking + decision rules
- `doddle.marketing.budget-allocator` — turns the constraint block into channel allocations

## Missing Data Rule

If required context is missing after 5 questions, emit a **partial** brief with `assumptions` flagged and route to `manual_review` per `on_fail`. Never fabricate budget, dates, or targets — show "⚠️ NOT AVAILABLE — [field] unconfirmed" per `data-reliability-rules.md`.
