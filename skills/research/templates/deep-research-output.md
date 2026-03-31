# Deep Research Output Template (v1.6.0)

Template for deep-research modular output: summary file + detail files per stream.

---

## Summary File: `outputs/research/YYYY-MM-DD-topic-summary.md`

```markdown
---
type: research
subtype: deep-research
title: "Deep Research: [Topic]"
date: YYYY-MM-DD
status: completed
confidence: 0.XX
sources_count: XX
research_time: "XX min"
tags: [topic-tag1, topic-tag2]
related:
  - YYYY-MM-DD-topic-stream1.md
  - YYYY-MM-DD-topic-stream2.md
discovered_entities: []
created_by: /deep-research
---

# [Topic]: [Subtitle that captures the narrative angle]

## Executive Summary

[NARRATIVE PROSE — 5-8 paragraphs weaving findings across ALL streams into a
coherent story. Flow: macro context → key discoveries → cross-stream synthesis →
implications → what's missing. The reader should understand the full picture
WITHOUT opening detail files.

Do NOT write siloed summaries per stream. Instead, tell a story that connects
the streams. Example: "While clinical evidence for X is strengthening [stream 1],
the investment landscape tells a different story [stream 2], and regulatory
frameworks are only beginning to catch up [stream 3]..."]

---

## Signal Map

| Stream | Sources | Avg Credibility | Specificity | Signal | Detail File |
|--------|---------|-----------------|-------------|--------|-------------|
| [Stream 1] | 12 | +2.1 | High | STRONG | [link] |
| [Stream 2] | 7 | +1.2 | Medium | MODERATE | [link] |
| [Stream 3] | 3 | +0.4 | Low | WEAK | — (below) |

---

## Key Findings

### [Stream 1 — Title]

[Prose synthesis of key findings with inline references [1][2][3].]

**Practical Layer:** [Cost: $X-Y per unit. Providers: A, B, C. Accessibility:
available in N countries. Action: readers can do X today.]

**Adjacent Topics:**
- Adjacent: [Topic A] — [why relevant, what we didn't cover]
- Adjacent: [Topic B] — [why relevant, what we didn't cover]

→ Full analysis: [link to detail file]

### [Stream 2 — Title]

[Same structure as above.]

### [Stream 3 — WEAK SIGNAL] (directional only)

[Brief directional findings. No precise claims. Flagged as low-confidence.]

---

## Contradictions & Resolutions

| Claim | Source A (credibility) | Source B (credibility) | Resolution |
|-------|----------------------|----------------------|------------|
| [Claim] | [Position] (+3) | [Counter] (+1) | [Pick with reasoning] |

---

## What's Missing

[Explicit gaps: what this research did NOT cover and why. What would strengthen
the findings. Suggested follow-up research directions.]

---

## Sources

### High Credibility (+2/+3)
[1] Author/Org — "Title" — URL (Date) — Credibility: +3
[2] Author/Org — "Title" — URL (Date) — Credibility: +2

### Medium Credibility (+1/0)
[5] Author/Org — "Title" — URL (Date) — Credibility: +1

### Low Credibility (-1/-2)
[8] Author/Org — "Title" — URL (Date) — Credibility: -1

---

*Deep research conducted: YYYY-MM-DD | Sources: XX | Time: XX min | Confidence: XX%*
```

---

## Detail File: `outputs/research/YYYY-MM-DD-topic-stream-name.md`

```markdown
---
type: research
subtype: deep-research
title: "[Stream Name]: [Topic Detail]"
date: YYYY-MM-DD
parent: YYYY-MM-DD-topic-summary.md
signal: STRONG
sources_count: XX
tags: [topic-tag1, stream-tag]
created_by: /deep-research
---

# [Stream Name]: [Detailed Title]

## Overview

[2-3 paragraphs of prose contextualizing this stream within the broader topic.]

---

## Findings

### [Section 1]

[Deep analysis in prose with numbered inline references [1][2][3].
Tables OK for structured comparisons, but text sections are readable prose.]

### [Section 2]

[Further analysis...]

---

## Contradictions

| Claim | Evidence For | Evidence Against | Resolution |
|-------|-------------|-----------------|------------|
| [Claim] | [Sources, credibility] | [Sources, credibility] | [Decision + reasoning] |

---

## Practical Layer

| Aspect | Details |
|--------|---------|
| **Cost** | $X-Y per unit/session/year |
| **Providers** | Company A, Clinic B, Platform C |
| **Availability** | Available in X countries; regulatory status Y |
| **Timeline** | Available today / Expected 2027 / Preclinical only |
| **Action Steps** | What the reader can do now |

[If no practical data available: "Practical data gap: no pricing/availability
information found for this area. This is typical for [reason]."]

---

## Adjacent Topics

- **Adjacent: [Topic A]** — [Why relevant to this stream. What we encountered
  but didn't cover. Where the reader could continue research.]
- **Adjacent: [Topic B]** — [Same format.]
- **Adjacent: [Topic C]** — [Optional third.]

---

## Sources

### High Credibility (+2/+3)
[1] Author/Org — "Title" — URL (Date) — Credibility: +3

### Medium Credibility (+1/0)
[4] Author/Org — "Title" — URL (Date) — Credibility: +1

### Low Credibility (-1/-2)
[7] Author/Org — "Title" — URL (Date) — Credibility: 0
```

---

## Template Rules

1. **Summary = narrative, not data dump.** If it reads like siloed sections, rewrite.
2. **Practical Layer is mandatory.** No stream gets a pass — if data is missing, say so explicitly.
3. **Adjacent Topics are mandatory.** Minimum 2 per stream.
4. **Bibliography is numbered and tiered.** Inline [N] refs throughout, grouped by credibility at end.
5. **WEAK streams stay in summary only.** No detail file for streams with <4 sources.
6. **Tables for data, prose for analysis.** Never a bullet list where a paragraph would be clearer.

---

*Template v1.6.0*
