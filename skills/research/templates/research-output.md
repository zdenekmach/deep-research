# Research Output Template

## File: `outputs/research/YYYY-MM-DD-topic-slug.md`

```markdown
---
type: research
subtype: standard
title: "Research: [Topic]"
date: YYYY-MM-DD
project: "[project-slug]"
status: completed
confidence: 0.XX
sources_count: X
tags: [topic-tag1, topic-tag2]
related:
  - knowledge-base/repositories/example.md
discovered_entities:
  - type: repository
    name: example-repo
    url: https://github.com/org/repo
    status: suggested_new
created_by: /research
---

# Research: [Topic]

## Executive Summary

[2-3 paragraphs of fluent prose summarizing key findings. See README.md → "Language Configuration".] 

---

## Key Findings

1. **[Finding 1]** - [Source](URL)
2. **[Finding 2]** - [Source](URL)
3. **[Finding 3]** - [Source](URL)

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
  - Assessment: [Which seems more supported]

---

## Further Research

- [Suggested topic 1] — Why: [reason]
- [Suggested topic 2] — Why: [reason]

---

## Sources

| # | Title | URL | Type | Date |
|---|-------|-----|------|------|
| 1 | [Title] | [Link](URL) | Article | YYYY-MM |
| 2 | [Title] | [Link](URL) | Paper | YYYY-MM |
| 3 | [Title] | [Link](URL) | Docs | YYYY-MM |

---

## Discovered Entities

### Linked (existing in knowledge base)

| Type | Name | Path |
|------|------|------|
| repository | langchain | knowledge-base/repositories/langchain.md |

### Suggested (new)

| Type | Name | URL/Reference | Quick Action |
|------|------|---------------|--------------|
| repository | llama-index | github.com/run-llama/llama_index | `/knowledge save` |
| book | "AI Engineering" | ISBN 978-... | `/knowledge save` |

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
| subtype | string | Yes | standard/deep/quick |
| confidence | float | Yes | 0.0-1.0 |
| sources_count | int | Yes | Number of sources used |
| related | array | No | Links to existing knowledge |
| discovered_entities | array | No | New entities found |

---

## History Summary Template

Save to: `outputs/research/history/YYYY-MM-DD-topic-slug.md`

```markdown
---
date: YYYY-MM-DD
topic: "[Topic]"
sources: X
output: "outputs/research/file.md"
---

# [Topic] - Summary

[2-3 sentence summary for future reference]

Key entities: [repo1], [book1]
Follow-up: [suggested topics]
```
