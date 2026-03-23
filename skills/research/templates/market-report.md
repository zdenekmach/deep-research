# Market Research Report Template

Template for `--format market-report` output from `/research` and `/deep-research`.

---

## Frontmatter

```yaml
---
type: research
subtype: market-report
title: "Market Report: [Topic]"
date: YYYY-MM-DD
status: draft
confidence: 0.XX
sources_count: XX
tags: [market-research, topic-tag1, topic-tag2]
created_by: /research --format market-report
---
```

## Report Structure (11 Chapters)

### 1. Executive Summary (2-3 pages)

- **Market Snapshot Box:** Key metrics at a glance (market size, CAGR, key players)
- **Investment Thesis:** 3-5 point summary
- **Key Findings:** Main discoveries
- **Strategic Recommendations:** Top 3-5 recommendations

### 2. Market Overview & Size

- Market definition and boundaries
- **TAM** (Total Addressable Market) — total size
- **SAM** (Serviceable Addressable Market) — reachable segment
- **SOM** (Serviceable Obtainable Market) — realistic target
- Historical growth (3-5 years back)
- Projections (3-5 years forward)
- CAGR historical and projected

### 3. Industry Analysis (Porter's Five Forces)

| Force | Intensity | Key Factors |
|-------|-----------|-------------|
| Threat of New Entrants | High/Med/Low | [factors] |
| Bargaining Power of Suppliers | High/Med/Low | [factors] |
| Bargaining Power of Buyers | High/Med/Low | [factors] |
| Threat of Substitutes | High/Med/Low | [factors] |
| Competitive Rivalry | High/Med/Low | [factors] |

### 4. Macro Environment (PESTLE)

| Factor | Trend | Impact | Timeframe |
|--------|-------|--------|-----------|
| **P**olitical | | High/Med/Low | |
| **E**conomic | | High/Med/Low | |
| **S**ocial | | High/Med/Low | |
| **T**echnological | | High/Med/Low | |
| **L**egal | | High/Med/Low | |
| **E**nvironmental | | High/Med/Low | |

### 5. Customer Analysis

- Customer segments (size, growth, behavior)
- Needs & pain points per segment
- Decision-making process
- Value drivers

### 6. Competitive Landscape

- **Market share** of top players (table)
- **Competitive positioning matrix** (2×2: price × quality or other axes)
- **Feature comparison** of key solutions (table: Strong/Adequate/Weak/Absent)
- Barriers to entry

### 7. Technology Trends

- Current technology stack
- Emerging technologies
- Adoption timeline
- Innovation hotspots

### 8. Regulatory Environment

- Key regulations (current and upcoming)
- Compliance requirements
- Regulatory risk assessment

### 9. SWOT Analysis

| | Positive | Negative |
|---|----------|----------|
| **Internal** | Strengths | Weaknesses |
| **External** | Opportunities | Threats |

### 10. Strategic Recommendations

- Top 3-5 recommendations prioritized (HIGH/MEDIUM/LOW)
- For each: what, why, how, timeline, effort
- Risk/reward assessment
- Implementation roadmap (phases 1-3)

### 11. Appendices

- Data sources & methodology
- Detailed competitive profiles
- Glossary
- Full source list with confidence scores

---

## Recommended Visuals

| Section | Visual |
|---------|--------|
| Executive Summary | Executive infographic |
| Market Size | TAM/SAM/SOM funnel diagram |
| Porter's | Five Forces diagram |
| Competitive | Positioning matrix |
| SWOT | SWOT quadrant |
| Roadmap | Implementation timeline |

---

## Mapping to 4-Stream Pattern

When used with `/deep-research`:

| Stream | Chapters |
|--------|----------|
| MARKET | 2 (Market Size), 5 (Customer Analysis) |
| TECHNOLOGY | 7 (Technology Trends) |
| COMPETITION | 3 (Porter's), 6 (Competitive Landscape) |
| RISKS | 4 (PESTLE), 8 (Regulatory), 9 (SWOT) |

---

*Template v1.1.0*
