---
name: campaign-plan
id: doddle.marketing.campaign-plan
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to orchestrate or split a campaign into coordinated parallel jobs. Also use when the user mentions "orchestration," "job map," "who does what," "wave planning," "execution plan," "campaign decomposition," or "project plan" for marketing work. Consumes the intake protocol and baseline data, decomposes the campaign into parallel jobs with owners, waves, and dependencies. For the interactive document version, see the /campaign:plan command.
---

# Campaign Orchestration

Take a locked intake protocol and baseline performance data, and decompose the campaign into parallel jobs a project manager can dispatch — each job naming its owner agent and skill, its wave, and its dependencies. This is the machine counterpart of the project-manager's "assign each job to a specialist, track it, collect the output."

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- An intake brief exists and execution planning must start
- Work needs decomposition into parallel, non-conflicting jobs
- Multiple channels must be created in waves with dependencies
- The user asks "who does what, in what order?"
- Sequencing must reflect data dependencies (tracking before ads, pages before traffic)

## Initial Assessment

Before decomposing, understand:

1. **Protocol state**
   - Is there a locked intake brief? (maps to `brief` input; if missing, the intake sub-graph runs first)
   - Are KPI targets and constraints already fixed?
2. **Scope**
   - Channels in scope, budget ballpark, timeline?
3. **Resource reality**
   - Which agents/MCP integrations are actually configured vs. NOT AVAILABLE?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| context | string | yes | Raw problem or goal, in the user's words |
| brief | string | no | Existing intake protocol; skips the intake sub-graph when provided |
| channels | string | no | Channels in scope; propose from brief if missing |
| budget | string | no | Total budget ballpark; ask if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| job_map | json | Jobs by wave with owner, skill ref, inputs, dependencies |
| orchestration_notes | markdown | Sequencing rationale, risks, handoffs |

---

## Core Framework

### Step 1: Lock the Protocol
Run the intake sub-graph if no brief exists. Confirm primary KPI, guardrails, budget, timeline. Do not plan against an unlocked brief.

### Step 2: Baseline Before Traffic
Pull the analytics sub-graph (existing baseline data or explicit "⚠️ NOT AVAILABLE"). Wave 0 always includes the tracking foundation — nothing spends money before it.

### Step 3: Decompose into Waves
Split jobs by dependency, not by channel enthusiasm:

| Wave | Job pattern | Depends on |
|------|-------------|------------|
| 0 | Measurement plan + tracking events | Intake brief |
| 1 | Budget allocation + landing/offers | Wave 0 |
| 2 | Asset creation per channel (parallel) | Wave 1 |
| 3 | Approval gate on all assets | Wave 2 |
| 4 | Distribution per approved asset | Wave 3 |
| 5 | Measurement loop + reallocation | Wave 4 + 7d data |

### Step 4: Assign Owners
Each job names its owner agent (`researcher`, `planner`, `copywriter`, `email-wizard`, `conversion-optimizer`, `project-manager`) and optional skill ref (`doddle.marketing.*`) so the DAG is executable, not aspirational.

### Step 5: Write the Handoff Notes
Record what was sequenced, why, the top risks, and the handoff points (e.g. "copy needs claims review before paid promotion").

---

## Job Map Schema (guidance)

```json
{
  "campaign": "name",
  "small_h": "parallel job map",
  "waves": [
    {
      "wave": 0,
      "jobs": [
        {
          "id": "tracking_setup",
          "owner": "researcher",
          "skill": "doddle.marketing.measurement-plan",
          "inputs": {"brief": "<brief_schema ref>"},
          "needs": [],
          "outputs": ["tracking_plan"]
        }
      ]
    }
  ]
}
```

Rules:
- Job `needs` reference job ids within the map (DAG check before emitting)
- Wave 0 must include measurement — if it doesn't, re-split
- Parallel creation jobs never share a single file as their output target

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Planning before data | Creatives built on fabricated baselines | Baseline sub-graph in wave 0 |
| One giant wave | Everything blocks on everything | Split creation by channel (parallel) |
| Unassigned jobs | "The team will handle it" | Named owner per job or NOT AVAILABLE |
| No approval wave | Unreviewed assets ship | Formal gate between create and distribute |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Circular deps | DAG won't schedule | Validate the map emits ref-free waves |
| Skills referencing missing agents | Node fails at runtime | Use agents from `.claude/agents/` only |
| Budget math inside the job map | Duplicates budget skill | Call `budget-allocator` as its own wave |

---

## Related Skills

- `doddle.marketing.marketing-intake` — the protocol this consumes
- `doddle.marketing.measurement-plan` — wave 0 in every map
- `doddle.marketing.budget-allocator` — wave 1 money split
- `/campaign:run` command — executes all waves end-to-end interactively
