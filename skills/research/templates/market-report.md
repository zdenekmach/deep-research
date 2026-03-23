# Market Research Report Template

Template pro `--format market-report` výstup z `/research` a `/deep-research`.

---

## Frontmatter

```yaml
---
type: research
subtype: market-report
title: "Market Report: [Topic]"
date: YYYY-MM-DD
project: "[slug]"
status: draft
confidence: 0.XX
sources_count: XX
tags: [market-research, topic-tag1, topic-tag2]
created_by: /research --format market-report
---
```

## Report Structure (11 kapitol)

### 1. Executive Summary (2-3 strany)

- **Market Snapshot Box:** Klíčové metriky na první pohled (velikost trhu, CAGR, klíčoví hráči)
- **Investment Thesis:** 3-5 bodů shrnutí
- **Key Findings:** Hlavní zjištění
- **Strategic Recommendations:** Top 3-5 doporučení

### 2. Market Overview & Size

- Definice a ohraničení trhu
- **TAM** (Total Addressable Market) — celková velikost
- **SAM** (Serviceable Addressable Market) — dosažitelný segment
- **SOM** (Serviceable Obtainable Market) — realistický cíl
- Historický růst (3-5 let zpět)
- Projekce (3-5 let dopředu)
- CAGR historický a projektovaný

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

- Segmenty zákazníků (velikost, růst, chování)
- Needs & pain points per segment
- Decision-making process
- Value drivers

### 6. Competitive Landscape

- **Market share** top hráčů (tabulka)
- **Competitive positioning matrix** (2x2: cena × kvalita nebo jiné osy)
- **Feature comparison** klíčových řešení (tabulka: Strong/Adequate/Weak/Absent)
- Barriers to entry

### 7. Technology Trends

- Současný technology stack
- Emerging technologies
- Adoption timeline
- Innovation hotspots

### 8. Regulatory Environment

- Klíčové regulace (stávající a připravované)
- Compliance requirements
- Regulatory risk assessment

### 9. SWOT Analysis

| | Positive | Negative |
|---|----------|----------|
| **Internal** | Strengths | Weaknesses |
| **External** | Opportunities | Threats |

### 10. Strategic Recommendations

- Top 3-5 doporučení s prioritizací (HIGH/MEDIUM/LOW)
- Pro každé: co, proč, jak, timeline, effort
- Risk/reward assessment
- Implementation roadmap (fáze 1-3)

### 11. Appendices

- Data sources & methodology
- Detailed competitive profiles
- Glossary
- Full source list s confidence scores

---

## Vizuální prvky (doporučené)

Ke generaci přes `/image --infographic`:

| Sekce | Vizuál |
|-------|--------|
| Executive Summary | Executive infographic |
| Market Size | TAM/SAM/SOM diagram (`--infographic stats`) |
| Porter's | Five Forces diagram (`--infographic hierarchy`) |
| Competitive | Positioning matrix (`--infographic comparison`) |
| SWOT | SWOT quadrant (`--infographic comparison`) |
| Roadmap | Implementation timeline (`--infographic timeline`) |

---

## Mapping na 4-Stream Pattern

Při použití s `/deep-research`:

| Stream | Kapitoly |
|--------|----------|
| MARKET | 2 (Market Size), 5 (Customer Analysis) |
| TECHNOLOGY | 7 (Technology Trends) |
| COMPETITION | 3 (Porter's), 6 (Competitive Landscape) |
| RISKS | 4 (PESTLE), 8 (Regulatory), 9 (SWOT) |

---

*Template v1.0.0 | Inspirováno K-Dense market-research-reports skill*
