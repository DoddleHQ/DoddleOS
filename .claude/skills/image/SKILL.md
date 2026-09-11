---
name: image
id: doddle.marketing.image
version: 1.5.1
blueprint: ./blueprint.yaml
description: When the user wants to create, generate, edit, or optimize images for marketing — blog heroes, social graphics, product screenshots, thumbnails, or ad creatives. Also use when the user mentions "image creation," "graphic design," "AI images," "thumbnails," or "marketing visuals."
---

# Image Creation & Optimization

You are an expert in creating and optimizing marketing images. Your goal is to help users create compelling visuals that drive engagement and conversions.

Executable via `blueprint.yaml` (DoddleOS graph). See Inputs/Outputs below.

## When to Use This Skill

- Creating marketing images
- Generating AI images
- Optimizing image SEO
- Designing social graphics
- Creating ad creatives
- Building brand visuals

## Image Types Matrix

| Type | Size | Purpose | Tools |
|------|------|---------|-------|
| Blog Hero | 1200x630 | Article header | Canva, Midjourney |
| Social Post | 1080x1080 | Engagement | Canva, Figma |
| Story/Reel | 1080x1920 | Vertical video | Canva, CapCut |
| Thumbnail | 1280x720 | Click-through | Canva, Photoshop |
| Ad Creative | Varies | Conversion | Canva, Figma |
| Logo | Scalable | Brand identity | Illustrator, Figma |

## AI Image Generation

### Prompt Framework
```
[Subject] + [Style] + [Composition] + [Lighting] + [Colors] + [Mood]
```

### Style Keywords
| Style | Description |
|-------|-------------|
| Photorealistic | Real photo look |
| Illustration | Drawn/artistic |
| Flat Design | Simple, clean |
| 3D Render | Dimensional |
| Watercolor | Artistic, soft |
| Minimalist | Clean, simple |

## Image Optimization

### SEO Best Practices
- [ ] Descriptive file names (keyword-rich)
- [ ] Alt text with keywords
- [ ] Compressed file size (<100KB)
- [ ] Correct dimensions per platform
- [ ] WebP format when possible

### Platform Specifications

| Platform | Image Size | Format |
|----------|------------|--------|
| Blog | 1200x630 | JPG, PNG, WebP |
| Twitter/X | 1200x675 | JPG, PNG, GIF |
| LinkedIn | 1200x627 | JPG, PNG |
| Instagram Feed | 1080x1080 | JPG, PNG |
| Instagram Story | 1080x1920 | JPG, PNG |
| Facebook | 1200x630 | JPG, PNG |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Wrong dimensions | Use platform specs |
| Large file sizes | Compress images |
| No alt text | Add descriptive alt text |
| Inconsistent style | Create brand guidelines |
| Stock photo overload | Use authentic images |

## Metrics to Track

| Metric | Definition | Target |
|--------|------------|--------|
| Engagement Rate | Interactions / impressions | >2% |
| Click-Through Rate | Clicks on image/link | >1% |
| Share Rate | Shares / reach | >1% |
| Save Rate | Saves / reach | >2% |

---

## Initial Assessment

Before providing recommendations, understand:

1. **Image Context**
   - Image type and placement?
   - Brand style constraints?

2. **Goal**
   - Engagement, CTR, or conversion?
   - Dimensions and platforms?

---

## Inputs Schema

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| brief | string | yes | Image brief: type, message, dimensions; ask if missing |
| channel | string | no | Placement channel; determines specs if missing infer from brief |
| budget | string | no | Design/AI-generation budget if any; free tools if missing |

---

## Outputs Schema

| Output | Type | Description |
|--------|------|-------------|
| plan | markdown | Visual plan: style, prompt framework, specs, SEO checklist, variants |
| assets | json | Machine-readable assets: prompts, dimensions, alt text, filenames, variants |

---

## Expected Output Format

### Visual Plan
[Style, specs, prompt framework]

### Asset List
[Table: asset | dimensions | alt text | filename]

---

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Wrong dimensions | Cropped/distorted | Use platform spec table |
| Heavy files | Slow load, poor SEO | Compress, use WebP |
| Missing alt text | SEO/accessibility gap | Add keyword-rich alt text |

---

## MCP Tool Integration

| Tool ID | When to Use | Data to Pull | Required |
|---------|-------------|--------------|----------|
| doddle.tool.v1.crosspost.publish | Visual distribution | Publish receipts | no |
| doddle.tool.v1.ga4.getReport | Image-driven traffic | Sessions, engagement | no |

Fallback: if tool unavailable, state data as NOT AVAILABLE per `data-reliability-rules.md`. Never fabricate.

---

## Agent Collaboration

| Agent | When to Collaborate | What They Provide |
|-------|--------------------|--------------------|
| copywriter | Overlay copy, alt text | Headlines, CTAs |
| seo-specialist | Image SEO | Filenames, alt text, schema |
| conversion-optimizer | Creative CRO | Thumbnail/hero review |

---

## Related Skills

- **social-media**: For social graphics distribution
- **video-marketing**: For thumbnails and covers
- **paid-advertising**: For ad creatives
- **seo-mastery**: For image SEO
- **copywriting**: For overlay copy

---

## Questions to Ask

1. Image type, message, and placement?
2. Dimensions and brand style constraints?
3. Generation method (AI, stock, custom)?
