---
description: Review a live campaign and reallocate budget based on measured performance and pre-agreed decision rules
argument-hint: [campaign-name]
---

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

**Skills**: Activate `media-reallocator`, `measurement-plan`, `budget-allocator`, `analytics-attribution` skills.

**Components**: Reference `./.claude/components/interactive-questions.md` and `./.claude/components/date-helpers.md`

---

## Pipeline Context

Runs after a campaign has live data (typically ≥7 days, or the cadence defined in the campaign's measurement plan). Requires artifacts saved by `/campaign:run`:

```
./plans/campaigns/[name]/03-kpi-targets.json     — targets to measure against
./plans/campaigns/[name]/03-decision-rules.md    — rules to execute as written
./plans/campaigns/[name]/04-budget-split.json    — current allocations
./plans/campaigns/[name]/04-unit-economics.md    — CAC ceiling + scenarios in force
```

---

## Step 0: Get Current Date (MANDATORY)

**Execute BEFORE asking any questions:**

```bash
CURRENT_DATE=$(date +%Y-%m-%d)
DATA_START=$(date -v-14d +%Y-%m-%d 2>/dev/null || date -d "-14 days" +%Y-%m-%d)
echo "Reallocation review: $CURRENT_DATE (window from $DATA_START)"
```

---

## Step 1: Load Campaign State

Ask which campaign to review. Read the four artifacts above; if any is missing, show exactly what is absent:

```markdown
## Missing Artifacts

| Artifact | Status |
|----------|--------|
| 03-decision-rules.md | Requested |
| 04-budget-split.json | Show a "create via /campaign:run Stage 4 first" |
```

Reallocation without decision rules or a budget split is misdirected money — stop and route the user to the missing stage, don't improvise.

---

## Step 2: Pull Actuals (Data Reliability MANDATORY)

Follow `./.claude/workflows/data-reliability-rules.md`:

| Data | MCP Server | Fallback |
|------|------------|----------|
| Channel traffic/conversions | `google-analytics` | "⚠️ NOT AVAILABLE — configure GA4" |
| Lead/deal performance | `hubspot` | "⚠️ NOT AVAILABLE — configure HubSpot" |
| Paid platform spend | `meta-ads` | "⚠️ NOT AVAILABLE" |

**NEVER fabricate actuals.** If all sources are unavailable, end with setup instructions and no plan — do not estimate channel performance.

---

## Step 3: Scorecard + Rule Execution

Per the `media-reallocator` skill:

1. Channel scorecard: spend, KPI actuals vs `03-kpi-targets.json`, CPA/ROAS trend, volume, phase (learning/scaling/bending)
2. Execute `03-decision-rules.md` **as written** — triggered / not-triggered lists, with thresholds and windows
3. Rule amendments (e.g. plan conditions changed) are proposals logged as audit notes, not silent skips

---

## Step 4: Propose Moves

Constrained by `04-budget-split.json` floors and `04-unit-economics.md` ceilings:

- Each move: from → to, amount, triggering rule (or rationale), projected impact range, data basis
- Watchlist: channels too new/small to judge → next checkpoint date, not a move
- Reserve (contingency) untouched unless a written rule allows it

---

## Step 5: Approval (HARD STOP)

Display the moves table, then:

**Question:** "Apply these reallocation moves?"
**Header:** "Approve"
**MultiSelect:** true

**Options:**
- **Approve all moves** - Proceed to execution
- **Approve selectively** - I'll pick which moves
- **No moves this cycle** - Save scorecard + watchlist only

**Nothing executes before user approval. Rejected items are logged, not silenced.**

---

## Step 6: Execute + Log

| Execution | Method | Fallback |
|-----------|--------|----------|
| Platform budget changes | `meta-ads` (mcp-manager) | "⚠️ NOT AVAILABLE — change budgets in Platform UI per reallocation_plan" |
| Organic content shifts | Agent work per plan | Document as next-week jobs in `02-job-map.json` |
| Team notification | `slack`, `notion`, `asana` | "⚠️ NOT AVAILABLE" |

**Save:**

```
./plans/campaigns/[campaign-name]/
├── 09-reallocation-plan-[YYMMDD].json    — approved moves, watchlist, rules status
└── 09-reallocation-notes-[YYMMDD].md     — scorecard, rules executed, audit notes
```

---

## Step 7: Schedule Next Review

Ask for review cadence (default from measurement plan; weekly if unset). Offer `/ops:weekly` integration point: next review runs with fresh actuals against the updated split.

---

## Data Reliability (MANDATORY)

1. **NEVER fabricate** performance numbers or platform estimates
2. MCP data only; otherwise "⚠️ NOT AVAILABLE — [server] not configured" + pointer to `doddle-core/registry/integrations/_registry.md`
3. Projections are ranges with stated basis — they are analysis artifacts, not measurements
4. List unresolved questions at the end
