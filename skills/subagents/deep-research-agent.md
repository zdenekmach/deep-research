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

## Phase 7: Final Output

### Modular Structure

- **Summary file**: Signal Map, executive summary, key findings, recommendations
- **Detail files**: One per STRONG stream (full analysis with sources)
- **WEAK streams**: Section in summary flagged as "low signal — directional only" (no separate file)

### Quality Checklist

- [ ] 25+ unique sources collected
- [ ] All sources SIFT-evaluated
- [ ] All conflicts resolved with reasoning
- [ ] Signal Map included in summary
- [ ] Recommendations match signal strength
- [ ] No precise claims on weak signals
- [ ] Output saved to file with frontmatter

---

*Version: 1.0.0 — Deep research methodology*
