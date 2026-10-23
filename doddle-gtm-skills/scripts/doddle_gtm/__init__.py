"""Doddle Go-To-Market deterministic toolkit.

Every number a skill reports is computed here from recorded inputs. The toolkit is stdlib-only
so it runs anywhere Python 3.9+ runs, with no install step and no network requirement.

Honesty note: GTM inputs are often *assumptions* (ACV, churn, funnel counts). The toolkit
computes **deterministically from those recorded inputs** — the same inputs always reproduce
the same outputs — while the skills label the inputs `advisory` and live CRM/data numbers
`live`. Nothing is ever estimated.

Public entry points:
    - :mod:`doddle_gtm.calc`       — funnel, unit economics, pricing, market sizing
    - :mod:`doddle_gtm.scoring`    — deterministic ICP / account scoring
    - :mod:`doddle_gtm.pipeline`   — audit a deals/pipeline export
    - :mod:`doddle_gtm.frameworks` — the versioned GTM template registry
    - :mod:`doddle_gtm.cli`        — the ``dgtm`` command line
"""

from __future__ import annotations

TOOLKIT_VERSION = "0.2.0"
SCORING_VERSION = "gtm-1"
DATA_VERSION = "gtm-frameworks-2026-10-2"

__all__ = ["TOOLKIT_VERSION", "SCORING_VERSION", "DATA_VERSION"]
