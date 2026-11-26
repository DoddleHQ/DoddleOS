# Survey & Community Attribution Modeling

Community advocacy (getting the proof) and community **attribution** (measuring it) are
different jobs. This file covers the measurement.

## Two bases, never merged

| Basis | Source field | Meaning |
|-------|--------------|---------|
| `self_reported` | `heard_from` | The person named the source themselves |
| `modeled` | `other_source` | The primary answer was empty and a secondary source was recorded |

Report them separately. A modelled attribution is a hypothesis; a self-reported one is a
statement. Merging them inflates the result.

## Influenced revenue

Won deals whose `person_id` appears in community activity. Only `won` deals carry revenue, and
the person must appear in the community file — otherwise the deal is not counted at all (not
counted as zero, not counted).

## Confidence

| Level | Condition (default `min_sample` 30) |
|-------|---------------------------------------|
| `low` | responses < `min_sample` |
| `medium` | responses < 3 × `min_sample` |
| `high` | responses ≥ 3 × `min_sample` |

Always print the sample size with the number. A 90% figure from six responses is not a result.

## Consent

- Every survey row should carry a consent value. Rows without one are counted in
  `consent_missing` and are **blocked** from any external artifact.
- Use hashed `person_id` values. Never carry raw identities into a prompt or a report.
- Apply minimum cohort sizes before publishing any breakdown.

## Rules

- Community activity is a signal; attribution needs a survey or a tracked link.
- Never name individual community members.
- Never present community activity as revenue without the survey basis.
- Report the confidence level with the number, every time.
