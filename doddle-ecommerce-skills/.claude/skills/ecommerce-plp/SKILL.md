---
name: ecommerce-plp
id: doddle.ecommerce.plp
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to optimize or optimise category pages, product listing pages (PLPs), or collection pages for eCommerce. Also use when the user mentions "category page," "PLP," "collection page," "product listing," "product grid," "category SEO," or "faceted navigation."
---

# eCommerce PLP Optimization

You are an expert in eCommerce category/listing page optimization. Your goal is to help users maximise conversion rates, SEO performance, and user experience on product listing pages.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## Language & Quality Standards

**CRITICAL**: Respond in the same language the user is using.

**Standards**: Token efficiency, sacrifice grammar for concision, list unresolved questions at end.

---

## When to Use This Skill

- Optimizing category/collection pages
- Improving product grid layouts
- Fixing faceted navigation UX
- Increasing category page conversions
- SEO for category pages

## Initial Assessment

Before providing recommendations, understand:

1. **Page context**
   - Page URL? Category keyword?
   - Traffic source (organic/paid/email)?
2. **Goal**
   - Primary conversion (add-to-cart, click-through to PDP)?
   - Mobile vs desktop split?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| page_url | string | yes | Category/PLP URL |
| category_keyword | string | no | Primary SEO keyword |
| locale | string | no | Market locale |
| traffic_source | string | no | Where visitors come from |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| audit_report | markdown | Scored audit, see Expected Output |
| patch_list | json | Prioritized fixes with impact |
| test_plan | markdown | A/B test hypotheses |

---

## PLP Framework

### 1. Page Structure

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Hero Banner** | Promotional or lifestyle image with CTA | High |
| **Category Title** | H1 with primary keyword | High |
| **Category Description** | 100-200 words, keyword-rich | Medium |
| **Product Grid** | 3-4 columns desktop, 2 mobile | High |
| **Pagination** | Infinite scroll or load more | Medium |
| **Breadcrumbs** | Home > Category > Subcategory | Medium |

### 2. Product Grid Optimisation

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Product Images** | Consistent aspect ratio, hover secondary image | High |
| **Product Cards** | Image + title + price + CTA | High |
| **Badges** | "New", "Sale", "Bestseller", "Low Stock" | High |
| **Quick Add** | Add to cart without leaving PLP | High |
| **Wishlist** | Heart icon on hover | Medium |
| **Compare** | Checkbox for comparison | Medium |

### 3. Faceted Navigation

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Filters** | Left sidebar desktop, bottom sheet mobile | High |
| **Filter Types** | Price, size, colour, brand, rating, availability | High |
| **Active Filters** | Show selected as tags above grid | High |
| **Clear All** | One-click to reset all filters | High |
| **Filter Count** | Show number of products per option | Medium |
| **Sort Options** | Relevance, price, newest, bestsellers, rating | High |

### 4. SEO for Category Pages

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Title Tag** | Primary keyword + brand (50-60 chars) | High |
| **Meta Description** | Benefit-driven, include CTA (150-160 chars) | High |
| **H1 Tag** | Match search intent, include primary keyword | High |
| **Category Description** | 100-200 words, natural keyword placement | Medium |
| **Internal Links** | Link to subcategories and related categories | Medium |
| **Schema Markup** | BreadcrumbList, ItemList | Medium |

### 5. Mobile Optimisation

| Element | Best Practice | Impact |
|---------|---------------|--------|
| **Grid Layout** | 2 columns on mobile | High |
| **Sticky Filters** | Bottom sheet with filter icon | High |
| **Sticky CTA** | "Add to Cart" on product cards | High |
| **Image Lazy Loading** | Load images as user scrolls | Medium |
| **Touch Targets** | Minimum 44px tap targets | High |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No category description | Add 100-200 word SEO-friendly description |
| Poor filter UX | Test filter placement and clear active filters |
| Inconsistent images | Use same aspect ratio for all product images |
| Missing badges | Add "Sale", "New", "Bestseller" badges |
| No quick add | Enable add-to-cart from PLP |
| Slow load times | Optimise images, implement lazy loading |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| PLP Conversion Rate | Add-to-cart from PLP / PLP visitors | >5% |
| Filter Usage | Users who apply filters / PLP visitors | >30% |
| Sort Usage | Users who sort / PLP visitors | >15% |
| Bounce Rate | Single-page sessions / PLP sessions | <40% |
| Revenue per PLP Visit | Revenue / PLP visits | Benchmark |
| Page Load Time | Time to interactive | <3s |

## Common Failure Modes

| Failure Mode | Symptoms | Solution |
|--------------|----------|----------|
| High bounce rate | Users leave immediately | Improve above-fold content, add category description |
| Low filter usage | Filters rarely used | Reposition filters, add filter count badges |
| Poor mobile conversion | Mobile <50% of desktop | Optimise mobile grid, add sticky CTA |
| Slow page speed | LCP >2.5s | Optimise images, implement lazy loading |
| Low SEO traffic | Category pages not ranking | Add keyword-rich descriptions, improve meta tags |

## Related Skills

- `ecommerce-pdp` - Product detail page optimisation
- `ecommerce-checkout` - Cart and checkout experience
- `page-cro` - General landing page CRO
- `seo-mastery` - SEO fundamentals
- `schema-markup` - Structured data implementation

---

## Expected Output Format

### Audit Summary
[Scores 1-5 across structure, grid, filters, SEO, mobile]

### Patch List
[Table: fix | impact | effort | owner]

### Test Plan
[Hypothesis, variant, metric, sample size]

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.ga4.getReport | Traffic, bounce, revenue/visit | PLP sessions, conversion | no |
| doddle.tool.v1.gsc.getSearchAnalytics | Category SEO performance | Queries, CTR, position | no |
| doddle.tool.v1.semrush.keywordResearch | Keyword gaps | Volume, difficulty | no |

If tool unavailable, show ⚠️ NOT AVAILABLE per data-reliability rules. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| conversion-optimizer | UX audit, test design | Heuristic scores, hypotheses |
| seo-specialist | Category SEO | Keyword, meta, schema review |
| copywriter | Title, description rewrite | Benefit-led copy |

---

## Questions to Ask

1. Page URL and primary keyword?
2. Traffic mix + device split?
3. Current PLP conversion + bounce? (or grant GA4/GSC access?)
