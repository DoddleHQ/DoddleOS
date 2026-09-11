---
name: saas-retention
id: doddle.saas.retention
version: 1.0.0
blueprint: ./blueprint.yaml
description: When the user wants to reduce SaaS churn, fix failed payments, or win back cancelled customers. Also use when the user mentions "churn," "dunning," "cancellation," "winback," "failed payment," "involuntary churn," "save rate," or "recovery rate."
---

# SaaS Retention & Dunning

You are an expert in SaaS retention. Your goal is to cut involuntary churn with dunning, deflect voluntary cancels with save flows, and win back lapsed customers with minimal revenue leakage.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Logo or MRR churn above target (>5% monthly SMB, >1% enterprise)
- Failed payments / involuntary churn with no dunning sequence
- Cancellation flow is one-click with no save attempt
- No pause / downgrade alternative to cancel
- Cancelled customers never get winback outreach

## Initial Assessment

Before providing recommendations, understand:

1. **Churn split**
   - Involuntary (failed payment) vs voluntary (active cancel) share?
   - Current logo churn + MRR churn? Stripe / HubSpot access?
2. **Goal**
   - Target recovery rate + save rate? Dunning exists today?
   - Who owns save (product, support, sales)?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| product | string | yes | Product or billing URL to audit |
| churn_rate | string | no | Current logo or MRR churn rate |
| dunning | string | no | Existing dunning setup |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| churn_audit | markdown | Churn taxonomy audit, involuntary vs voluntary |
| dunning_plan | markdown | Dunning calendar + in-app recovery spec |
| save_flow | json | Cancel-save reasons-to-offers + winback triggers |

---

## Retention Framework

### 1. Failed-Payment Dunning

| Day | Channel | Goal | CTA |
|-----|---------|------|-----|
| **0** | Email + in-app banner | Fix immediately, soft tone | Update payment method |
| **3** | Email retry notice | First retry failed, urgency up | Retry + update card |
| **7** | Email + in-app block | Second retry, value reminder | Keep access, fix billing |
| **14** | Final notice + support | Last chance before suspension | Contact support / pay now |
| **In-app** | Persistent banner + paywall | Unmissable for active users | One-click card update |

### 2. Cancellation Save Flow (Reasons to Offers)

| Cancel Reason | Save Offer | Impact |
|---------------|------------|--------|
| **Too expensive** | Downgrade / annual discount / pause | Very High |
| **Missing feature** | Roadmap + workaround + CSM call | High |
| **Not using** | Concierge onboarding / template reset | High |
| **Switched tool** | Comparison + migration-back offer | Medium |
| **Temporary** | Pause 1-3 months, keep data | Very High |

### 3. Pause / Downgrade Saves

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Pause** | 1-3 months, data kept, 1-click resume | Very High |
| **Downgrade** | Cheaper tier offered before cancel confirm | Very High |
| **Friction** | Reason survey required, save offer shown first | High |
| **Human** | High-MRR cancels route to CSM / call | High |

### 4. Winback Sequence

| Day | Goal | CTA |
|-----|------|-----|
| **30** | Fix original reason (feature / price) | What's new since you left |
| **60** | Social proof + incentive | Case stat + comeback discount |
| **90** | Final break-up or downsell | Stay on free / lite plan |

### 5. Churn Taxonomy

| Type | Examples | Owner |
|------|----------|-------|
| **Involuntary** | Card expired, insufficient funds, SCA fail | Billing / dunning |
| **Voluntary active** | Cancel click, downgrade to free | Product / save flow |
| **Voluntary passive** | Never activated, faded usage | Onboarding / nurture |

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Single dunning email then cancel | Day 0/3/7/14 + in-app banner |
| Cancel = instant loss, no save | Reason survey + matched offer first |
| No pause option | Offer 1-3 month pause, keep data |
| Winback never sent | Day 30/60/90 sequence in save_flow |
| Blaming all churn on price | Split involuntary vs voluntary, fix billing first |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Logo churn | Logos lost / start logos | <5% monthly SMB |
| MRR churn | MRR lost / start MRR | <2% monthly |
| Recovery rate | Failed payments recovered / total failed | >60% |
| Save rate | Cancels deflected / save offers shown | >20% |
| Winback rate | Returned / winback contacted | Benchmark |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| Silent dunning | Failed payments go straight to cancel | Day 0/3/7/14 + retries + in-app |
| Naked cancel | One-click cancel, zero deflection | Reason survey + offer matrix |
| No pause valve | Temporary leavers churn fully | Pause + downgrade before confirm |
| Dead winback | Ex-customers never contacted | 30/60/90 triggers in save_flow |

---

## Expected Output Format

### Churn Audit
[Involuntary vs voluntary split + taxonomy scores]

### Dunning Plan
[Day 0/3/7/14 calendar + in-app spec + retry logic]

### Save Flow
[JSON: cancel reasons, matched offers, pause rules, winback triggers]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.stripe.listInvoices | Failed-payment volume | Open / uncollectible invoices | no |
| doddle.tool.v1.stripe.getSubscriptions | Cancel / pause state | Status, MRR at risk | no |
| doddle.tool.v1.hubspot.contacts | Lifecycle + winback pool | Cancelled / at-risk contacts | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate rates.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| continuity-specialist | Churn audit, save design | Retention tactics |
| email-wizard | Dunning + winback copy | Day 0/3/7/14/30/60/90 emails |
| copywriter | Save-flow messaging | Reason-to-offer copy |
| lead-qualifier | At-risk scoring | Health thresholds |

---

## Related Skills

- `churn-prevention` - Churn reduction fundamentals
- `email-sequence` - Dunning + winback drip mechanics
- `saas-expansion` - Downgrade saves + expansion guardrails
- `onboarding-cro` - Fix passive churn at activation
- `revops` - Lifecycle + at-risk handoff ops

---

## Questions to Ask

1. Product / billing URL + current logo/MRR churn? (or grant Stripe/HubSpot access?)
2. Existing dunning + cancel flow? Pause offered?
3. Who owns saves + winback today?
