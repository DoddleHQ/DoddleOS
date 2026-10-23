---
name: gtm-advocacy
id: doddle.gtm.gtm-advocacy
version: 0.2.0
blueprint: ./blueprint.yaml
description: "Design or review a customer advocacy program — references, reviews, referrals and community proof. Use when the user wants more proof assets, a reference program, review flywheel or referral motion."
---

# Advocacy Program

Turn existing customer wins into a repeatable proof engine — references, reviews, referrals —
without inventing proof you do not have.

## Deterministic Toolkit

- `dgtm report --export <file>` — aggregate recorded proof assets / closed-deal evidence into
  an envelope (`evidence.stamp` must be CURRENT to report as live).
- `dgtm frameworks --name case-study-brief|partnership-scorecard` — structure for each proof
  type; never paraphrase from memory.

Read the envelope's `scores`/`metrics` verbatim. Assets the user has not supplied are
`NOT AVAILABLE`, never assumed.

## Sub-flows

| Sub-flow | When to use | Toolkit focus |
|----------|-------------|---------------|
| `references` | Sales needs named customer references for live deals | `report` + case-study-brief |
| `reviews` | Building a review flywheel (G2, marketplaces, directories) | case-study-brief only |
| `referrals` | designing a customer referral motion with incentives | partnership-scorecard |
| `community` | Seeding proof from user community / events | case-study-brief only |

## Workflow

1. Confirm which advocacy motion the user wants (references / reviews / referrals / community)
   and for which segment (default SMB).
2. Run `dgtm report` on any supplied proof/deal export; record `evidence.stamp`.
3. Pull the framework structure (`dgtm frameworks --name <slug>`); fill it from user-supplied
   evidence only.
4. Design the program: who to ask, when (trigger moment), what they get, owner, cadence.
5. Flag consent and approval needs — every external proof artifact requires customer
   permission before it is published.

## Response Contract

Report in this order, every time:

1. **Headline result.** One sentence: the motion designed and the proof inventory size if
   measured (tag `live`/`advisory`), else `NOT AVAILABLE`.
2. **Key evidence.** Proof assets supplied, each tagged `advisory`; framework structure tagged
   `deterministic`.
3. **Artifact path.** Where the program doc was written, or "inline".
4. **One suggested next command.** Exactly one.

Hard rules: never invent a customer, quote, metric or permission; never do arithmetic; if proof
is missing, say `NOT AVAILABLE`. Full block: `common/response-contract.md`.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Inventing quotes or logos | Only user-supplied, consented proof enters the program |
| Asking at the wrong moment | Tie the ask to a trigger (first value moment, renewal, win) |
| Skipping consent | Every public proof artifact needs recorded permission |
| Treating advocacy as one motion | References, reviews, referrals and community need different designs |

## Related Skills

`gtm-case-study`, `gtm-partnerships`, `gtm-channel`, `gtm-onboarding`, `gtm-enablement`

## Inputs

| Input | Required | Type | Notes |
|-------|----------|------|-------|
| proof | yes | string/file | Proof assets or references available |
| goal | no | string | reviews / referrals / references / community |

## Outputs

| Output | Type | Notes |
|--------|------|-------|
| program | markdown | Advocacy program design |
| envelope | json | From `dgtm report` when an export is supplied |
