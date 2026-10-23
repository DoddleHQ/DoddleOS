---
description: Run the full campaign pipeline end-to-end — intake to measurement, with a human approval gate before distribution
argument-hint: [campaign-name-or-goal]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `marketing-intake`, `campaign-plan`, `measurement-plan`, `budget-allocator`, `analytics-attribution` skills. Channel skills (per selected channels): `copywriting`, `email-marketing`, `social-media`, `paid-advertising`.

**Components**: Reference `./.claude/components/interactive-questions.md` and `./.claude/components/date-helpers.md`

**Workflows**: Follow `./.claude/workflows/data-reliability-rules.md` (MANDATORY) at every stage.

---

## Pipeline Overview

This command executes the full DoddleOS campaign pipeline:

```
Intake → Plan → Measurement → Budget → Create → APPROVE GATE → Distribute → Measure
```

Each stage saves a numbered artifact to `./plans/campaigns/<campaign-name>/` so a run can be resumed. Stage 6 is a **hard human approval gate** — the pipeline always stops there.

---

## Interactive Parameter Collection

### Step 0: Get Current Date (MANDATORY)

**Execute BEFORE asking any questions:**

```bash
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_MONTH=$(date +"%B %Y")
YYMMDD=$(bash -c 'date +%y%m%d')
echo "Pipeline run date: $CURRENT_DATE"
```

---

### Step 0.5: Resume Check

Check if `./plans/campaigns/<campaign-name>/01-brief-protocol.json` exists (or ask the user if a prior run exists).

```markdown
**Question:** "Resume an existing campaign run or start fresh?"
**Header:** "Resume"
**MultiSelect:** false

**Options:**
- **Resume at stage [N]** - Continue from the last saved artifact
- **Start fresh** - New run; existing artifacts will be overwritten
```

On resume: read the latest numbered artifact, show its summary, continue from the next incomplete stage.

---

### Step 1: Ask Campaign Goal (Stage 1 — Intake)

**Question:** "What is the goal of this campaign? Describe the problem or opportunity in your own words."
**Header:** "Goal"
**MultiSelect:** false

Collect via interactive questions (max 5): goal/problem, product/offer, audience, budget, timeline. Anything else becomes a **flagged assumption** in the brief protocol — never fabricated.

---

### Step 2: Ask Channels (Stage 2 — Plan)

**Question:** "Which channels are in scope?"
**Header:** "Channels"
**MultiSelect:** true

**Options:**
- **Email & Automation** - Sequences, drips, lifecycle
- **Paid Media** - PPC, social ads, retargeting
- **Organic & Content** - SEO, blog, social posts
- **Outbound & PR** - Cold outreach, launches, media

---

### Step 3: Confirmation

**Display summary:**

```markdown
## Pipeline Configuration

| Parameter | Value |
|-----------|-------|
| Campaign | [name] |
| Goal | [user's words] |
| Channels | [selected] |
| Budget | [from intake or TBD at Stage 4] |
| Timeline | [from intake] |
| Run directory | ./plans/campaigns/[name]/ |
| Approval gate | Stage 6 (hard stop) |
```

**Question:** "Proceed with the full pipeline (stop at approval before any distribution)?"
**Header:** "Confirm"
**MultiSelect:** false

**Options:**
- **Yes, run pipeline** - Start Stage 1
- **No, change settings** - Go back to modify

---

## Stage details

### Stage 1 — Intake (marketing-intake skill)

1. Restate the user's problem verbatim; classify intent (bottleneck / launch / decision / retention)
2. Fill every Brief Protocol field; unstated fields → `assumptions` with proposed defaults
3. Define primary KPI + guardrails + kill criteria precisely
4. **Save:** `01-brief.md` and `01-brief-protocol.json`

### Stage 2 — Plan (campaign-plan skill)

1. Generate the baseline call (analytics-attribution) — "⚠️ NOT AVAILABLE" allowed, never invented
2. Decompose into waves (0: measurement, 1: budget+pages, 2: parallel channel assets, 3: approval, 4: distribution, 5: measure)
3. Each job: owner agent + skill ref + needs (DAG-validated)
4. **Save:** `02-job-map.json` and `02-orchestration-notes.md`

### Stage 3 — Measurement (measurement-plan skill)

1. Build KPI tree from brief; set targets (assumption-flagged if no GA4/CRM MCP)
2. Freeze UTM + event taxonomy; document dataLayer structure
3. Pre-agree decision rules: `IF [metric] [op] [threshold] BY week N THEN [action]`
4. **Save:** `03-tracking-plan.md`, `03-kpi-targets.json`, `03-decision-rules.md`
5. **Instruction to user:** implement tracking (GTM/UI events) before any spend

### Stage 4 — Budget (budget-allocator skill)

1. Ask for exact total budget + price/ACV if not yet confirmed (propose assumptions, flagged)
2. Compute CAC ceiling, channel floors, allocations with rationale; contingency 5–10%
3. Emit lean/base/stretch scenarios
4. **Save:** `04-budget-split.json`, `04-unit-economics.md`

### Stage 5 — Create (parallel, per job map)

For each wave-2 job, dispatch to the matching agent/skill:
- Landing/email copy → `copywriter` (copywriting, email-sequence skills)
- Social → `copywriter` (social-media skill)
- Ads → `copywriter` (paid-advertising skill); support metrics from measurement-plan only
- Outbound/PR → `sales-enabler`, `attraction-specialist`

Each asset claims its tracking references (UTMs, event names) from Stage 3 — no asset ships without them.

**Save:** one asset file per job in `05-assets/`, named per the job map.

### Stage 6 — Approval Gate (HARD STOP)

```markdown
## 🛑 APPROVAL REQUIRED

Before anything is distributed:
1. Show asset index: file | job | channel | claims used
2. Route rejected-flag assets back to the owner agent with the user's notes (max 2 revise rounds)
3. Do NOT proceed to distribution without explicit user approval of every asset
```

**Question:** "Approve all listed assets for distribution?"
**Header:** "Approve"
**MultiSelect:** true (per-asset or all)

**Options:**
- **Approve all** - All assets pass the gate
- **Revise individually** - I'll give per-asset notes
- **Stop pipeline** - Save state; no distribution this run

On partial revise: loop Stage 5 for the revised jobs, then re-present only those assets.

### Stage 7 — Distribute (per approved asset only)

Distribution capability depends on MCP configuration:

| Capability | MCP Server | Fallback |
|------------|------------|----------|
| Publish social | `twitter`, `tiktok` | "⚠️ NOT AVAILABLE — post manually" |
| Send email | `hubspot` | "⚠️ NOT AVAILABLE — export files" |
| Launch ads | `meta-ads` | "⚠️ NOT AVAILABLE — set up manually" |
| Team notify | `slack`, `notion`, `asana` | "⚠️ NOT AVAILABLE" |

**Save:** `07-distribution-log.md` (channel, action, status, ⚠️ flags)

### Stage 8 — Measure (analytics-attribution + decision rules)

1. Run `/campaign:analyze` against the campaign after its first data window (≥7 days for most channels)
2. Compare actuals against `03-kpi-targets.json`; execute `03-decision-rules.md` as written
3. Reallocation/deeper analysis → `/campaign:reallocate` (when available) or next run iteration

**Save:** `08-measurement-notes.md`

---

## Data Reliability (MANDATORY — every stage)

1. **NEVER fabricate** metrics, benchmarks, baselines, or results
2. MCP data only for real numbers; show "⚠️ NOT AVAILABLE — [server] not configured" + setup pointer to `doddle-core/registry/integrations/_registry.md`
3. Assumptions must be labeled `assumed` everywhere they appear (brief, budget split, KPI targets)
4. Unresolvable blockers: save state, list unresolved questions, exit cleanly — never invent a way out

---

## Agent Delegation

| Stage | Agent | Trigger |
|------|-------|---------|
| Intake + gatekeeping | `project-manager` | Protocol, verification |
| Wave decomposition | `planner` | Job map |
| Baseline + measurement | `researcher` | Tracking + KPI data |
| Asset creation | `copywriter` (+ channel skills) | Per job map |
| Gate rework review | researcher + channel agents | Revise loops |
| Distribution | `mcp-manager` | Platform actions |

---

## Output Location

Save all stages to `./plans/campaigns/[campaign-name]/`:

```
./plans/campaigns/[name]/
├── 01-brief.md / 01-brief-protocol.json
├── 02-job-map.json / 02-orchestration-notes.md
├── 03-tracking-plan.md / 03-kpi-targets.json / 03-decision-rules.md
├── 04-budget-split.json / 04-unit-economics.md
├── 05-assets/
├── 06-approval-log.md
├── 07-distribution-log.md
└── 08-measurement-notes.md
```
