---
name: budget-allocator
id: doddle.marketing.budget-allocator
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user allocates a campaign budget across channels, models unit economics, or stress-tests spend scenarios. Also use when the user mentions "budget split," "channel allocation," "CAC," "LTV," "payback period," "unit economics," "how much to spend," or "budget model." Produces channel-level allocations with expected CPA/ROAS, CAC-LTV unit economics, and graceful degradation scenarios.
---

# Budget Allocator

The money model for a campaign. Takes the brief and the total budget, and returns per-channel allocations with rationale, expected CPA/ROAS, and the CAC/LTV/payback math that tells you whether the plan survives contact with reality — before a dollar is spent.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using. If Vietnamese, respond in Vietnamese. If Spanish, respond in Spanish.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

Apply this skill when:
- Stepping a total budget into channel allocations
- Modeling CAC, LTV, payback, or margin for a campaign
- Comparing lean / base / stretch spend scenarios
- Deciding whether a channel earns budget at all
- Pre-launch sanity-checks from a finance perspective

## Initial Assessment

Before modeling, understand:

1. **Money bounds**
   - Total budget + timing (one-shot vs monthly)?
   - Price or ACV of the offer? (proposes an assumption if missing, flagged)
2. **Channel shortlist**
   - Any must-run or must-avoid channels (compliance, exec mandate)?
   - Any minimum viable test budgets?
3. **Goals**
   - From intake primary KPI: volume-target vs efficiency-target?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Campaign brief: goal, audience, channels |
| total_budget | number | yes | Total budget in account currency |
| price_or_acv | string | no | Deal size or price band; propose assumption if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| budget_split | json | Channel allocations with rationale and expected CPA/ROAS |
| unit_economics | markdown | CAC, LTV, payback, margin math + lean/base/stretch scenarios |

---

## Core Framework

### Step 1: Fix the Unit Economics
Compute with user numbers or explicitly-flagged assumptions:
- `LTV = ARPU × gross margin × avg lifetime` (state every input)
- `CAC ceiling = LTV ÷ target payback period (months)` (e.g. payback < 6 mo → max CAC ≈ 12 months ARPU × margin ÷ 6)
- Blended CAC ceiling for the campaign = the money constraint the plan must respect

### Step 2: Floor Every Channel
For each candidate channel: minimum viable budget (enough impressions/clicks to exit learning), expected CPA band, and ramp time. A channel below its floor gets 0, not a token amount that never exits learning.

### Step 3: Allocate with Rationale
Split by expected contribution to the primary KPI, not by habit:
- Proven channels (existing baseline data) get scale weight
- Test channels get capped test budgets (10–20% of total)
- Reserve 5–10% contingency; it is not extra channel budget
- Every line carries expected CPA/ROAS and its assumption

### Step 4: Stress-Test Scenarios
Emit three scenarios: lean (-30%), base, stretch (+30%). For each: expected signups volume, blended CAC, payback period, and the decision rule that moves money if actuals diverge.

### Step 5: Approval-Ready Summary
One-page allocation summary with Math, Assumptions, Limitations. Assumptions are the honest list — never fabricate benchmarks; label industry comparators as assumptions to validate.

---

## Budget Split Guidance

```json
{
  "total_budget": 20000,
  "currency": "USD",
  "cac_ceiling": 150,
  "contingency_pct": 8,
  "channels": [
    {
      "channel": "meta-ads",
      "amount": 8000,
      "expected_cpa": [60, 110],
      "rationale": "retargeting + lookalikes off existing pixel",
      "test_share": 0.15
    },
    {
      "channel": "seo/content",
      "amount": 6000,
      "expected_cpa": [35, 55],
      "ramp_weeks": 6,
      "note": "lower CPA, slow ramp; not cut in week 2"
    }
  ],
  "assumptions": [
    "assumed ACV $1,200 (unconfirmed — needs finance check)",
    "no top-of-funnel PR credited to conversion"
  ]
}
```

---

## Common Mistakes

### Strategy Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Equal splits | Spends according to taste, not math | CPA-based allocation with floor checks |
| No contingency | No budget to reallocate when a channel wins | 5–10% reserve, rule-governed |
| Channel budget without floor | $300 exits?? never exits learning | Minimum viable test budgets |
| Hidden CAC assumption | Model looks profitable via invented LTV | Every input labeled as fact or assumption |

### Execution Mistakes
| Mistake | Why It's Wrong | Do This Instead |
|---------|----------------|-----------------|
| Lifting benchmark numbers from memory | Fabricated data, wrong currency | ⚠️ NOT AVAILABLE + range assumptions, flagged |
| One-position allocation | Week-2 data has nowhere to go | Reallocation triggers pre-agreed (see measurement-plan) |
| Budget > channel saturation | Diminishing returns ignored | Cap per channel when CPA bends upward |

---

## MCP Tool Integration

| Tool ID | When to Use | Data | Fallback |
|---------|-------------|------|----------|
| doddle.tool.v1.ga4.getReport | Channel baselines, past CPA | Sessions, conversions | "⚠️ NOT AVAILABLE" |
| doddle.tool.v1.hubspot.deals | ACV, deal-size distribution | Deals | "⚠️ NOT AVAILABLE" |

Never fabricate benchmarks. If actuals are unavailable, use user-stated assumptions, label them, and list them in the summary.

---

## Related Skills

- `doddle.marketing.measurement-plan` — the KPI targets CAC/payback get checked against
- `doddle.marketing.paid-advertising` — lights implementation of the paid split
- `doddle.marketing.media-reallocator` (planned) — in-flight reallocation against these scenarios
