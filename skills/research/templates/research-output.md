# Research Output Template

Default template for standard research output.

## File: `outputs/research/YYYY-MM-DD-topic-slug.md`

```markdown
---
type: research
subtype: standard
title: "Research: [Topic]"
date: YYYY-MM-DD
status: completed
confidence: 0.XX
sources_count: X
tags: [topic-tag1, topic-tag2]
created_by: /research
---

# Research: [Topic]

## Executive Summary

[2-3 paragraphs of fluent prose summarizing key findings.]

---

## Key Findings

1. **[Finding 1]** — [Source](URL)
2. **[Finding 2]** — [Source](URL)
3. **[Finding 3]** — [Source](URL)

---

## Detailed Analysis

### [Section 1]

[Analysis with inline citations]

According to [Source](URL), the main approach involves...

### [Section 2]

[Further analysis]

---

## Contradictions & Debates

- **[Point of contention]**
  - View A: [Perspective](URL)
  - View B: [Counter-perspective](URL)
  - Assessment: [Which seems more supported and why]

---

## Further Research

- [Suggested topic 1] — Why: [reason]
- [Suggested topic 2] — Why: [reason]

---

## Sources

| # | Title | URL | Type | Date | Credibility |
|---|-------|-----|------|------|-------------|
| 1 | [Title] | [Link](URL) | Article | YYYY-MM | +1 |
| 2 | [Title] | [Link](URL) | Paper | YYYY-MM | +3 |
| 3 | [Title] | [Link](URL) | Docs | YYYY-MM | +2 |

---

*Research conducted: YYYY-MM-DD*
*Methodology: [Direct/Subagent]*
*Confidence: [X]%*
```

---

## Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| type | string | Yes | Always "research" |
| subtype | string | Yes | standard / deep / quick |
| confidence | float | Yes | 0.0-1.0 |
| sources_count | int | Yes | Number of sources used |
| tags | array | No | Topic tags for categorization |

---

*Template v1.1.0*
