# Migration checklist

Depth for `seo-migration`. The redirect map and cutover plan are `advisory`; the page-level
evidence comes from `dseo`. Work top to bottom, and do not start the next phase until the
previous one is complete.

## Phase 1 — Before (inventory)

- [ ] Crawl the source with `dseo audit <old-url> --json`; record every URL and status.
- [ ] Capture per URL: title, canonical, `technical.indexable`, `technical.https`.
- [ ] Identify high-value URLs: those with clicks/impressions (`seo-reporting`) and conversions.
- [ ] Note URLs with backlinks or external references, if a backlink tool is configured.
- [ ] Freeze the content plan; note pages being retired.

## Phase 2 — Redirect map

- [ ] Every old URL maps to exactly one new URL (`old → new → reason`).
- [ ] No chains, no loops, no mass redirect to the homepage.
- [ ] High-value URLs mapped first and checked by hand.
- [ ] Retired pages redirect to the most relevant surviving page.
- [ ] Old URLs that should 410 (intentionally gone) are listed and excluded from redirects.

## Phase 3 — Cutover configuration

- [ ] New URLs are `200`, indexable, and self-canonical.
- [ ] Staging `noindex` and any auth gate removed on launch.
- [ ] `robots.txt` updated for the new structure/domain.
- [ ] XML sitemaps regenerated with new URLs only.
- [ ] Internal links point at new URLs; no lingering old-domain links.
- [ ] hreflang (if any) updated — use `seo-hreflang`.
- [ ] Analytics and Search Console properties ready (new verified, old retained).

## Phase 4 — Launch day

- [ ] Spot-check redirects for status code and destination.
- [ ] Confirm the new site is indexable and self-canonical (`dseo technical`).
- [ ] Verify `robots.txt` and sitemaps are live and correct.
- [ ] Request indexing in Search Console if appropriate.

## Phase 5 — Post-launch monitoring (for weeks)

- [ ] Redirect coverage: sample old URLs weekly; every one 301s to the intended URL.
- [ ] 404 report reviewed; add any missing mapping.
- [ ] Index coverage trended; watch for a drop in indexed new URLs.
- [ ] Clicks/impressions trended against the pre-migration baseline (`seo-reporting`).
- [ ] Compare before/after `dseo audit` envelopes; state the deltas.
- [ ] hreflang/geo targeting verified if locales moved.

## Timing

- Keep the redirect map live indefinitely (at least until old URLs are no longer referenced).
- Expect ranking fluctuation during re-crawl; judge the migration on the trend, not one day.
- Re-audit the destination with `dseo audit` once crawling settles and compare to the baseline.
