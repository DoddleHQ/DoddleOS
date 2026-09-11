# Doddle eCommerce Skills

> eCommerce-specific marketing skills for product listing pages, product detail pages, checkout, search, and revenue optimisation.

## Overview

This is an add-on skill pack for [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing). It provides 5 specialised eCommerce skills that cover the complete customer journey from product discovery to checkout completion.

## Skills Included

| Skill | Purpose | Command |
|-------|---------|---------|
| `ecommerce-plp` | Category/listing page optimisation | `/cro:page` (category context) |
| `ecommerce-pdp` | Product detail page optimisation | `/cro:page` (product context) |
| `ecommerce-checkout` | Cart & checkout flow optimisation | `/cro:form` (checkout context) |
| `ecommerce-search` | On-site search & product discovery | `/cro:page` (search context) |
| `ecommerce-revenue` | Revenue leakage & AOV optimisation | `/pricing:strategy` |

## Installation

### Option 1: Install as Plugin (Recommended)

```bash
# Add this repo as a marketplace
/plugin marketplace add doddleOS/doddle-ecommerce-skills

# Install the plugin
/plugin install doddle-ecommerce-skills@doddle-ecommerce-skills
```

### Option 2: Manual Installation

```bash
# Clone the repo
git clone https://github.com/doddleOS/doddle-ecommerce-skills.git

# Copy skills to your project
cp -r doddle-ecommerce-skills/.claude/skills/* your-project/.claude/skills/
```

## What Each Skill Covers

### ecommerce-plp (Category/Listings)

- Page structure (hero, title, description, product grid)
- Product grid optimisation (images, cards, badges, quick add)
- Faceted navigation (filters, sort, active filters)
- SEO for category pages (title, meta, H1, schema)
- Mobile optimisation (grid, sticky filters, lazy loading)

### ecommerce-pdp (Product Pages)

- Above the fold (images, price, variant selector, CTA)
- Product image optimisation (gallery, zoom, video, 360 view)
- Variant selector UX (colour swatches, size guide, stock display)
- Social proof ( reviews, Q&A, UGC, trust badges)
- Cross-sell & upsell (related products, bundles, recently viewed)
- SEO for product pages (title, meta, schema, alt text)

### ecommerce-checkout (Cart & Checkout)

- Cart page/drawer optimisation
- Checkout flow (guest checkout, progress indicator, auto-fill)
- Shipping (thresholds, options, calculator)
- Payment (multiple methods, express checkout, security)
- Cart abandonment recovery (email, SMS, retargeting)

### ecommerce-search (Search & Discovery)

- Search bar optimisation (placement, size, autocomplete)
- Search results page (layout, filters, sort, pagination)
- Zero results page (suggestions, spell check, synonyms)
- Search merchandising (promoted products, personalisation)
- Search analytics (usage, conversion, revenue)

### ecommerce-revenue (Revenue & AOV)

- Revenue leakage identification (cart, checkout, product, pricing)
- AOV strategies (free shipping threshold, bundles, volume discounts)
- Cross-sell & upsell (frequently bought together, post-purchase)
- Pricing tactics (anchoring, charm pricing, decoy effect)
- Scalability assessment (platform, performance, international)

## Audit Coverage

These 5 skills fill the gaps identified in a comprehensive eCommerce audit:

| Audit Requirement | Skill |
|-------------------|-------|
| Category/PLP effectiveness | `ecommerce-plp` |
| Product page/PDP effectiveness | `ecommerce-pdp` |
| Search & product discovery | `ecommerce-search` |
| Cart & checkout experience | `ecommerce-checkout` |
| Revenue leakage points | `ecommerce-revenue` |
| Opportunities to increase AOV | `ecommerce-revenue` |
| Scalability issues | `ecommerce-revenue` |

## Dependencies

This skill pack works best with the core [Doddle Marketing OS](https://github.com/doddleOS/doddleOS-marketing) skills:

- `page-cro` - General landing page CRO
- `form-cro` - Form optimisation fundamentals
- `seo-mastery` - SEO fundamentals
- `schema-markup` - Structured data implementation
- `analytics-attribution` - Performance measurement
- `copywriting` - Marketing copy optimisation

## License

MIT License - Same as Doddle Marketing OS core

## Support

- **Issues:** [GitHub Issues](https://github.com/doddleOS/doddle-ecommerce-skills/issues)
- **Community:** [GitHub Discussions](https://github.com/doddleOS/doddle-ecommerce-skills/discussions)
