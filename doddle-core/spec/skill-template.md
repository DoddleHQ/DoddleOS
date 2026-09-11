# Skill Template (DoddleOS v2)

Use this template when creating or refactoring skills.
Each skill = human prompt (`SKILL.md`) + machine blueprint (`blueprint.yaml`).

File layout per skill (pack-relative; each `doddle-<domain>-skills/` pack is independent):
```
doddle-<domain>-skills/.claude/skills/<skill-name>/
├── SKILL.md        # human guidance, light frontmatter with blueprint pointer
└── blueprint.yaml  # DoddleOS graph blueprint: inputs, outputs, tools, nodes
doddle-<domain>-skills/.claude/agents/   # bundled agents this pack's nodes ref (local-first)
```

Tool namespace: `doddle.tool.v1.<server>.<tool>` (ex `doddle.tool.v1.gsc.getSearchAnalytics`).
Integration IDs must match `integrations/<service>/config.json` `name` field.

---

```markdown
---
name: skill-name
id: doddle.domain.skill-name
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to [action]... Also use when the user mentions [keywords]. For [related task], see [related-skill].
---

# Skill Title

One-paragraph description of what this skill does and when to use it.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- [Use case 1]
- [Use case 2]
- [Use case 3]

## Initial Assessment

Before providing recommendations, understand:

1. **[Assessment Dimension 1]**
   - [Question to ask]
   - [Question to ask]

2. **[Assessment Dimension 2]**
   - [Question to ask]
   - [Question to ask]

---

## Inputs Schema

Declare user inputs the blueprint expects. Keep table in SKILL.md, formal schema in `blueprint.yaml`.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| [input] | string/number/boolean/url | yes/no | [What to ask if missing] |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| [output] | markdown/json | [What engine returns] |

---

## Core Framework

### Step 1: [Framework Step]
[Description]

### Step 2: [Framework Step]
[Description]

### Step 3: [Framework Step]
[Description]

---

## Detailed Guidance

### [Subtopic 1]

**Key Principles:**
- [Principle 1]
- [Principle 2]

**Checklist:**
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

### [Subtopic 2]

[Same structure as above]

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| [Mistake] | [Reason] | [Alternative] |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| [Mistake] | [Reason] | [Alternative] |

### Analysis Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| [Mistake] | [Reason] | [Alternative] |

---

## Metrics to Track

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| [Metric] | [Definition] | [Target] | [Tool] |

---

## Decision Tree

[If user says X → do Y. If user says A → do B.]

---

## Quick Assessment Checklist

1. [ ] [Assessment question 1]
2. [ ] [Assessment question 2]
3. [ ] [Assessment question 3]
4. [ ] [Assessment question 4]
5. [ ] [Assessment question 5]

---

## Expected Output Format

Structure your response as:

### [Section 1]
[Description]

### [Section 2]
[Description]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| [Failure] | [Symptom] | [Fix] |

---

## MCP Tool Integration

Machine binding. Tool IDs MUST use `doddle.tool.v1` namespace. Full DAG lives in `blueprint.yaml`.

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.<server>.<tool> | [Use case] | [Data type] | yes/no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| [Agent] | [Use case] | [Contribution] |

---

## Related Skills

- **[skill-1]**: [When to use]
- **[skill-2]**: [When to use]

---

## Questions to Ask

1. [Question 1]
2. [Question 2]
3. [Question 3]
```

---

## Template Usage Guidelines

1. **Required Sections**: Name, Description, When to Use, Inputs Schema, Outputs Schema, Core Framework, Common Mistakes, Metrics, Expected Output, Failure Modes, MCP Tool Integration, Agent Collaboration, Questions to Ask
2. **Required Files**: `SKILL.md` + `blueprint.yaml` (see `blueprint-template.yaml` below)
3. **Frontmatter**: `name, id, version, blueprint, description`. `id` in frontmatter MUST equal `id` in blueprint.
4. **Adapt as Needed**: Not all skills need Decision Tree / Quick Assessment
5. **Keep Concise**: Prefer tables over paragraphs
6. **Cross-Reference**: Always link to related skills
7. **Validate**: Run `python3 doddle-core/scripts/validate.py` before commit

---

## blueprint.yaml Template

```yaml
id: doddle.domain.skill-name
version: 1.0.0
kind: skill
engine: doddle-os>=1.0
description: "[Same trigger description as SKILL.md frontmatter]"
inputs:
  - {name: primary_input, type: string, required: true, description: "[what to ask]"}
outputs:
  - {name: report, type: markdown, description: "[main deliverable]"}
tools:
  - {id: doddle.tool.v1.server.toolName, required: false, fallback: manual_review}
integrations:
  - server-name
nodes:
  - {id: assess, type: agent, ref: agent-name, needs: [inputs], produces: [assessment]}
  - {id: enrich, type: tool, ref: doddle.tool.v1.server.toolName, needs: [assess], produces: [data]}
  - {id: recommend, type: agent, ref: agent-name, needs: [enrich], produces: [report]}
on_fail: {retry: 1, fallback: manual_review}
```
