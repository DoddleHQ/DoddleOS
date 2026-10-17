"""Doddle SEO & GEO deterministic toolkit.

Every number a skill reports is computed here from recorded evidence. The toolkit is
stdlib-only so it runs anywhere Python 3.9+ runs, with no install step and no network
requirement for scoring a saved page.

Public entry points:
    - :func:`doddle_seo.score.score_page`  — score one page (citability + foundations)
    - :func:`doddle_seo.audit.audit_site`  — crawl and score a site
    - :mod:`doddle_seo.cli`                — the ``dseo`` command line
"""

from __future__ import annotations

TOOLKIT_VERSION = "0.1.0"
SCORING_VERSION = "geo-1"
DATA_VERSION = "ai-crawlers-2026-10"

__all__ = ["TOOLKIT_VERSION", "SCORING_VERSION", "DATA_VERSION"]
