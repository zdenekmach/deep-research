# Deep Research Subagent — Detailed Methodology

## Overview

Multi-pass parallel research using recursive methodology. Systematically explores topics from multiple angles, gathers 25+ quality sources, and synthesizes findings into actionable, opinionated insights.

## Phase 1: Topic Decomposition

1. Analyze the research topic
2. Decompose into 4-6 parallel research streams
3. For consulting/business topics: use 4-Stream pattern (MARKET, TECHNOLOGY, COMPETITION, RISKS)
4. For other domains: check `skills/research/domains/` for matching template
5. Define 3-5 search queries per stream

### Query Expansion Strategy

For each stream, generate queries from multiple angles:
- **Academic**: "[topic] research study peer-reviewed"
- **Institutional**: "[topic] report [institution] [year]"
- **Expert**: "[topic] best practices expert"
- **Community**: "[topic] experience lessons learned"
- **Media**: "[topic] trends forecast [year]"

## Phase 2: Parallel Broad Search

Launch 3-4 parallel agents (one per stream). Each agent:

1. Execute 3-5 WebSearch queries per stream
2. Collect 8-10 unique sources per stream
3. Record: URL, title, date, source type, initial credibility estimate
4. Identify gaps — what's missing?

**Target:** >= 20 total sources after Phase 2. WARNING if <20.

### Source Diversification

Aim for this mix per stream:
- 1-2 academic/peer-reviewed
- 1-2 institutional reports
- 2-3 expert practitioner sources
- 1-2 general/media sources
- 1-2 community/forum sources

## Phase 3: Signal Map

Assess signal strength per stream BEFORE deep dives:

| Metric | STRONG | MODERATE | WEAK |
|--------|--------|----------|------|
| Source count | 8+ | 4-7 | <4 |
| Credibility avg | >= +1 | mixed | low |
| Specificity | precise findings | general patterns | vague |
| Contradictions | few, resolvable | some | many or none |

Classify each stream and output a Signal Map table. This determines resource allocation in Phase 4.

## Phase 4: Adaptive Deep Dives

Allocate effort based on Signal Map:

- **STRONG streams**: More tokens, specific follow-up queries, nuanced comparison, edge cases, recursive exploration (max depth 3)
- **MODERATE streams**: Standard deep dive, focused queries
- **WEAK streams**: Fewer tokens, broader queries, aggregate directional signals. Do NOT force granularity on sparse data.

### Recursive Depth Pattern

For STRONG/MODERATE streams only:
```
Depth 0: Initial broad search
Depth 1: Follow-up on key findings (specific queries)
Depth 2: Verify contradictions, find primary sources
Depth 3: Edge cases, minority perspectives (only if warranted)
```

## Phase 5: Source Synthesis & Conflict Resolution

### SIFT Framework (mandatory for all sources)

- **S**top — Evaluate before using. Is this source appropriate?
- **I**nvestigate — Who is the author/organization? What's their expertise?
- **F**ind — Is there a better/more authoritative source for this claim?
- **T**race — Where does the original claim come from? Is it primary?

### Credibility Scoring

| Source Type | Score | Example |
|------------|-------|---------|
| Peer-reviewed journal | +3 | Nature, Science, domain journals |
| Institutional report | +2 | McKinsey, Gartner, RAND, government |
| Expert blog/practitioner | +1 | Named expert with credentials |
| General media | 0 | News articles, industry press |
| User-generated | -1 | Reddit, Medium without credentials |
| Anonymous/promotional | -2 | Vendor whitepapers, anonymous posts |

### Conflict Resolution

**CRITICAL:** Never write "sources disagree" and leave it at that. Always:
1. Document the conflict explicitly
2. Evaluate credibility of conflicting sources
3. Pick a position with reasoning, OR
4. State "insufficient data to decide" with specific gap identified

## Phase 6: Opinionated Recommendations

### 2D Confidence Model

| | Source Convergence: Converging | Source Convergence: Contradictory |
|---|---|---|
| **Signal: STRONG** | PRECISE claim with specific action | NUANCED position with reasoning |
| **Signal: MODERATE** | Standard DO/AVOID/CONSIDER | Acknowledge debate, lean one way |
| **Signal: WEAK** | DIRECTIONAL pattern only | UNKNOWN — acknowledge gap |

**Rules:**
- NEVER apply fine resolution to weak signal — that produces hallucinated precision
- NEVER write "you could do A or B" — always pick one with reasoning
- Match precision to signal strength

## Phase 6.5: Practical Layer & Adjacent Topics (v1.6.0)

### Practical Layer Collection

For each stream, actively search for practical information:

```
Practical layer queries:
- "[topic] cost pricing 2025 2026"
- "[topic] providers clinics companies available"
- "[topic] how to access get started"
- "[topic] commercial availability consumer"
```

Record per stream:
- **Costs:** prices, cost ranges, insurance coverage
- **Availability:** who offers it, where, how to access
- **Timeline:** when realistically available for end-user
- **Action steps:** what can the reader do TODAY

If practical data doesn't exist → explicitly flag: "Practical data gap: no pricing/availability information found."

### Adjacent Topic Detection

During research, note topics that repeatedly surface but fall outside scope:

```
Example for "Senolytics" stream:
- Adjacent: GLP-1 agonists — anti-inflammatory effects overlap with senolytic mechanisms, but different drug class
- Adjacent: Senescence biomarkers — needed for patient selection but no validated clinical biomarker exists
- Adjacent: CAR-T senolytic cells — next-gen approach, only preclinical
```

Every stream MUST identify at least 2 adjacent topics. This helps the reader see what's beyond the research boundaries and where they could continue.

## Phase 7: Final Output

### Modular Structure

- **Summary file (NARRATIVE)**: Must read as a cohesive narrative, not a structured data dump. Flow: macro context → key findings woven across streams (not siloed) → implications and synthesis → what's missing. Think "analyst report for a board member", not "database export". Includes Signal Map, practical layer summary, and numbered bibliography.
- **Detail files**: One per STRONG stream (full analysis with sources). Each MUST include:
  - Deep analysis in prose
  - **Practical Layer** (costs, providers, accessibility, action steps)
  - **Adjacent Topics** (2-3 related topics at section end)
  - Numbered bibliography specific to this stream
- **WEAK streams**: Section in summary flagged as "low signal — directional only" (no separate file)

### Bibliography Format (v1.6.0)

Use numbered inline references [1][2][3] throughout text. At end of each file:

```markdown
## Sources

### High Credibility (+2/+3)
[1] Fuentealba et al. — "Impact of TPE on Biological Age" — https://... (May 2025) — Credibility: +3
[2] Nature Communications — "14 Epigenetic Clocks Compared" — https://... (2025) — Credibility: +3

### Medium Credibility (+1/0)
[5] Longevity.Technology — "NewLimit $130M" — https://... (2025) — Credibility: +1

### Low Credibility (-1/-2)
[9] Market Research Firm — "Senolytic Market Size" — https://... (2025) — Credibility: 0
```

### Quality Checklist

- [ ] 25+ unique sources collected
- [ ] All sources SIFT-evaluated
- [ ] All conflicts resolved with reasoning
- [ ] Signal Map included in summary
- [ ] Recommendations match signal strength
- [ ] No precise claims on weak signals
- [ ] **Summary reads as cohesive narrative** (not siloed stream sections)
- [ ] **Practical Layer** present in every stream (costs, providers, accessibility)
- [ ] **Adjacent Topics** (2-3) identified per stream
- [ ] **Numbered inline refs** [1][2] + bibliography grouped by credibility tier
- [ ] Output saved to file with frontmatter

---

*Version: 1.6.0 — Deep research methodology. v1.6.0: Added Narrative Summary, Practical Layer, Adjacent Topics, Numbered Bibliography.*
