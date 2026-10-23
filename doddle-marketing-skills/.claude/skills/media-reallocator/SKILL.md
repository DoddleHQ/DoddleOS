---
name: media-reallocator
id: doddle.marketing.media-reallocator
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to move budget between channels mid-campaign, reallocate spend based on results, or execute pre-agreed decision rules on live data. Also use when the user mentions "reallocate," "shift budget," "move spend," "rebalance," "channel is underperforming," or "execute the decision rules." Produces approved-candidate reallocation moves with triggers and projected impact — nothing moves without user approval.
---

# Media Reallocation

The in-flight counterpart of `budget-allocator`: takes the current budget split and measured actuals, executes the pre-agreed decision rules from `measurement-plan`, and proposes concrete money moves. This skill proposes; the user approves; the rules decide when a review is even needed — that discipline is what separates reallocation from panic moving.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- A weekly (or cadence-defined) review is due and rules from the measurement plan apply
- One channel is materially off-target and another has headroom
- New evidence (creative fatigue test, CPA bend) suggests moving money
- The user asks where the next dollar should go given actuals

## Initial Assessment

Before proposing moves, evaluate:

1. **Plan state**
   - Current budget split (Stage 4 output) + decision rules (Stage 3) available?
   - Is any minimum-ramp-period protection in the plan (don't cut a 2-week-old SEO channel)?
2. **Data state**
   - Actuals per channel available from MCP, or "⚠️ NOT AVAILABLE" per data-reliability-rules?
   - Enough data (volume) per channel to compare fairly, or still learning-phase?
3. **Rule state**
   - Which decision rules have triggered so far, per the pre-agreed list?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| budget_split | string | yes | Current allocations (budget-allocator output path or inline JSON) |
| actuals | string | no | Measured performance per channel; pull via MCP or ask |
| decision_rules | string | no | Measurement-plan decision rules to execute as written |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| reallocation_plan | json | Moves: from-channel, to-channel, amount, trigger, projected impact |
| reallocation_notes | markdown | Rationale, rules executed, assumptions, execution steps |

---

## Core Framework

### Step 1: Build the Channel Scorecard
Per channel: spend to date, KPI actuals vs targets (`03-kpi-targets.json`), CPA/ROAS trend, volume (fair-comparison check), and phase (learning / scaling / bending). No number appears without a source; unavailable ⇒ "⚠️ NOT AVAILABLE", not an estimate.

### Step 2: Execute the Decision Rules First
For each rule from the measurement plan: did it trigger, at what threshold, what is the prescribed action? Rules execute as written; a rule that shouldn't apply anymore must be formally amended (audit note), not quietly skipped.

### Step 3: Propose Moves Constrained by Floors
Moves respect budget-allocator constraints: no channel below its floor, contingency reserve preserved, ramp-period channels protected. Each move states: from, to, amount, triggering rule, projected impact range, and what data window it's based on.

### Step 4: Watch What You Can't Move Yet
Channels too small or too new to judge get a "next checkpoint" date instead of a move. Reallocation discipline includes explicitly not moving.

### Step 5: Handoff for Approval
Emit the plan + notes; the `/campaign:reallocate` command stops for user approval before any execution step. Log approval outcome against the plan.

---

## Reallocation Plan Guidance

```json
{
  "review_window": "2026-10-14_2026-10-21",
  "moves": [
    {
      "from": "meta-ads-display",
      "to": "meta-ads-lookalike",
      "amount": 1500,
      "trigger": "RULE-2: CPA > $150 for 7 consecutive days",
      "cpa_actual": 182,
      "projected": {"cpa_after": [95, 140], "signups_per_week": [12, 18]},
      "data_basis": "ga4.getReport 14d + meta ads estimator"
    }
  ],
  "watchlist": ["seo-content: check again on 2026-11-04 (ramp week 4)"],
  "rules_not_triggered": ["RULE-1", "RULE-3"]
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Reallocation without rules | Money follows the loudest channel, not data | Execute the pre-agreed rules first |
| Cutting below channel floor | Killed channel can't recover post-realloc | Floors carried over from budget-allocator |
| Moving too early (learning phase) | CPA noise in week 1 misdirects everything | Volume/phase check before judging |
| Improvised thresholds | Rules "interpreted" to mean what feels right | Written rules executed as written; amendments logged |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Fabricated actuals | Reallocation on invented numbers | MCP or ⚠️ NOT AVAILABLE; no estimates |
| Missing projected impact | Move someone must accept without the math | Impact range + data basis per move |
| All moves at once | Can't attribute outcome to a causal change | One move family per review where possible |

---

## MCP Tool Integration

| Tool ID | When to Use | Data | Fallback |
|---------|-------------|------|----------|
| doddle.tool.v1.ga4.getReport | Channel traffic/conversions | Sessions, conversions | "⚠️ NOT AVAILABLE" |
| doddle.tool.v1.hubspot.contacts | Lead/deal performance per source | Contacts, deals | "⚠️ NOT AVAILABLE" |

---

## Related Skills

- `doddle.marketing.budget-allocator` — the plan this reallocates (budget_split input)
- `doddle.marketing.measurement-plan` — decision rules and KPI targets this executes
- `doddle.marketing.analytics-attribution` — measurement engine feeding the scorecard
- `/campaign:reallocate` command — the interactive runner that stops at approval
