# Deep Research

**Version:** 1.5.0 | **Purpose:** Multi-pass parallel research with 25+ sources, SIFT evaluation, adaptive resolution, conflict resolution, and opinionated recommendations

Deep multi-pass research with parallel agents and multi-stream synthesis: $ARGUMENTS

---

## When to Use

- Research requiring high confidence (>80%)
- Multi-dimensional topics with complex trade-offs
- New knowledge domain exploration
- Foundation for domain model building
- Strategic decisions with long-term impact

---

## Quick Reference

```
/deep-research "wildlife photography Sri Lanka"
/deep-research "AI adoption in Czech banking"
/deep-research "Claude Code MCP server architecture"
/deep-research --sources 30 topic
/deep-research "AI consulting market" --format market-report  # 11-chapter market report
```

---

## Principle

```
ANTI-PATTERN: Single-pass research with 5-10 sources, no synthesis
PATTERN: Multi-stream parallel research 25+ sources, SIFT evaluation, conflict resolution, opinionated recommendations
```

---

## Search Infrastructure

**SearXNG** (optional, recommended): Pokud je dostupný Docker, spusť SearXNG pro lepší výsledky:
```bash
cd tools/searxng && docker compose up -d
# Test: curl -s "http://localhost:8888/search?q=test&format=json" | jq '.results | length'
```
SearXNG agreguje 218 engines (Google Scholar, arXiv, Semantic Scholar, HN, Reddit) do jednoho JSON API. Použij `tools/searxng/search.sh "query" [category]` pro paralelní dotazy.

---

## Workflow

1. **Topic Decomposition** -- Load context (MCP Memory, active project). Decompose topic into 4-6 parallel research streams. For consulting/business: use 4-Stream Consulting Pattern (MARKET, TECHNOLOGY, COMPETITION, RISKS). For other domains: use domain-specific decomposition. Check for domain template in `skills/research/domains/`. BLOCKER: decomposition must complete before parallel search.
2. **Phase 1: Parallel Broad Search** -- Launch 3 Task calls in SINGLE message for parallel execution. Each agent: 3-5 WebSearch queries, 8-10 unique sources, key facts with URLs, gap identification. Target: >=20 total sources. WARNING if <20 after phase 1.
3. **Phase 1.5: Signal Map** -- Assess signal strength per stream BEFORE deep dives. For each stream evaluate: source count (quantity), credibility distribution (quality), contradiction count (noise), specificity of findings (resolution). Classify each stream: STRONG (8+ sources, credibility avg ≥+1, specific findings) / MODERATE (4-7 sources, mixed quality) / WEAK (<4 sources, low quality, vague findings). Output a Signal Map table. This informs Phase 2 resource allocation. BLOCKER: signal map must exist before Phase 2.
4. **Phase 2: Adaptive Deep Dives** -- Allocate effort based on Signal Map. STRONG streams: more tokens, specific queries, nuanced comparison, edge cases. MODERATE streams: standard deep dive. WEAK streams: fewer tokens, broader queries, pattern detection across sparse sources, aggregate directional signals instead of precise claims. Recursive exploration for STRONG/MODERATE only. For WEAK: pool broadly, don't force granularity.
5. **Phase 3: Source Synthesis & Conflict Resolution** -- SIFT Framework: Stop (evaluate before use), Investigate (author/org?), Find (better source?), Trace (original claim?). Credibility scoring: peer-reviewed +3, institutional +2, expert blog +1, general 0, user-generated -1. Deduplicate, connect subtopics, build timeline. CRITICAL: explicit conflict resolution with reasoning -- never "sources disagree", always pick one with reasoning or state "insufficient data". BLOCKER: 25+ unique sources, all SIFT-evaluated, all conflicts resolved.
6. **Phase 4: Opinionated Recommendations** -- Transform facts into opinionated actionable insights. Use 2D confidence model: Signal Strength (STRONG/MODERATE/WEAK) × Source Convergence (converging/contradictory). STRONG+converging → PRECISE claim with specific action. STRONG+contradictory → NUANCED position with reasoning. MODERATE+converging → standard DO/AVOID/CONSIDER. WEAK+converging → DIRECTIONAL pattern (not precise claim). WEAK+contradictory → UNKNOWN — acknowledge gap, suggest further research. NEVER apply fine resolution to weak signal — that produces hallucinated precision. For consulting topics: include roadmap implications. BLOCKER: no "could do A or B" -- always opinionated, but match precision to signal strength.
7. **Phase 5: Final Output** -- **LANGUAGE:** Subagent outputs are in English; final user-facing files follow the configured output language (see README.md → "Language Configuration"). No language mixing. Full sentences, not telegraphic bullet dumps. Tables OK for data comparisons, but text sections must be readable prose. Modular structure: summary file + detail files. STRONG streams get full detail files. WEAK streams get a section in summary flagged as "low signal — directional only" (no separate detail file). Include Signal Map in summary. Save to active project `outputs/research/` (default: `outputs/research/`). Include frontmatter, all sources with credibility scores.

---

## Rules

| Situation | Action |
|---------|------|
| Consulting/business topic | Use 4-Stream Pattern: MARKET, TECHNOLOGY, COMPETITION, RISKS |
| Other domains | Use domain-specific decomposition (4-6 subtopics) |
| After Phase 1 | Build Signal Map — classify each stream as STRONG/MODERATE/WEAK |
| STRONG signal stream | Deep dive: specific queries, nuanced comparison, full detail file |
| WEAK signal stream | Broad aggregation: pattern detection, directional signals, no separate detail file |
| Conflicting sources | Never "sources disagree". Pick one with reasoning, or explicit "insufficient data to decide" |
| Recommendations | Always opinionated. Match precision to signal strength — PRECISE for strong, DIRECTIONAL for weak |
| Weak signal + precise claim | ANTI-PATTERN. Never force fine resolution on weak signal — hallucinated precision |
| Source evaluation | SIFT framework mandatory for all sources |
| Agent execution | Launch 3-4 agents in SINGLE message for parallelism |
| Output location | Active project outputs/research/ first, outputs/research/ only as fallback |

---

## Comparison: /research vs /deep-research

| Aspect | /research | /deep-research |
|--------|-----------|----------------|
| Sources | 3-7 | 25-40 |
| Iterations | 1-2 | 3-5 multi-pass |
| Agents | 0-1 | 3-4 parallel |
| Time | 2-5 min | 10-15 min |
| Token budget | 6,000 | 16,500 |
| Recommendations | Summary | Opinionated (HIGH/MEDIUM/LOW) |
| Conflict resolution | Flag contradictions | Explicit reasoning + pick one |
| Output | Single file | Modular (summary + details) |

---

## Token Budget

| Phase | Tokens | Purpose |
|-------|--------|---------|
| Phase 0: Decomposition | 500 | Topic analysis |
| Phase 1: Broad Search | 4,500 | 3 parallel agents x 1,500 |
| Phase 1.5: Signal Map | 300 | Assess signal strength per stream |
| Phase 2: Adaptive Deep Dives | 6,000 | Allocated by signal: STRONG ~2,500, MODERATE ~2,000, WEAK ~1,500 |
| Phase 3: Synthesis | 2,000 | Source evaluation, connections |
| Phase 4: Recommendations | 1,500 | 2D confidence model (signal × convergence) |
| Phase 5: Output | 2,000 | Final documents |
| **Total** | **16,800** | ~10-15 minutes |

---

## Anti-Patterns

| Bad | Good |
|-----|------|
| Single-pass research 10 sources | Multi-pass 25+ sources with 4-stream pattern |
| Sequential agent execution | Parallel execution (3-4 in single message) |
| Generic subtopics | MARKET/TECH/COMPETITION/RISKS for consulting |
| Equal effort on all streams | Signal Map → adaptive allocation (more on strong, less on weak) |
| Precise claims on weak signal | Directional patterns on weak signal, precise claims on strong |
| "Sources disagree" | Explicit conflict resolution with reasoning |
| "You could do A or B" | "DO THIS because X" (opinionated + confidence) |
| Fixed HIGH/MEDIUM/LOW confidence | 2D model: signal strength × source convergence |
| Raw facts without context | Opinionated recommendations with roadmap implications |
| No source evaluation | SIFT + credibility scoring |
| Monolithic output | Modular (summary + detail files, weak streams in summary only) |
| Saved to wrong location when project exists | Saved to outputs/research/ (use configured output dir) |
| Output without proper diacritics | Full diacritics in configured output language |
| Mixed-language sentences | Subagents write English, final output in configured language |
| Telegraphic bullet dumps | Full sentences and paragraphs (tables OK for structured data) |

---

## Error Handling

| Situation | Action |
|---------|------|
| Agent timeout | Retry with smaller scope |
| < 20 sources after Phase 1 | Additional search round required |
| Conflicting sources | Document conflict, resolve with reasoning |
| No practical applications | Explicitly extract from raw facts |

---

## Gates (hard stop)

- [ ] Topic decomposed into 4+ streams/subtopics
- [ ] 3-4 parallel agents launched (Phase 1)
- [ ] Signal Map created — each stream classified STRONG/MODERATE/WEAK
- [ ] Phase 2 effort allocated based on Signal Map
- [ ] 25+ unique sources collected
- [ ] SIFT evaluation completed for all sources
- [ ] All conflicts have explicit resolution with reasoning
- [ ] 2D confidence model applied (signal strength × convergence)
- [ ] No precise claims on WEAK signal streams (directional only)
- [ ] Opinionated recommendations matching precision to signal strength
- [ ] Roadmap implications included (for consulting topics)
- [ ] Modular output (STRONG → detail files, WEAK → summary section only)
- [ ] Signal Map included in summary output
- [ ] Saved to project outputs/research/ with frontmatter
- [ ] No hallucinated sources
- [ ] No "could do A or B" -- always opinionated with reasoning
- [ ] Final output in configured language with full diacritics (no language mixing, no bullet dumps)
- [ ] Output saved to configured directory
- [ ] Subagent prompts explicitly request English output

---

## Output Formats

| Format | Flag | Structure |
|--------|------|-----------|
| Standard | *(default)* | Modular: summary + detail files per stream |
| Market Report | `--format market-report` | 11 chapters per template `skills/research/templates/market-report.md` |

When `--format market-report`:
- 4-Stream pattern maps to chapters: MARKET→kap2+5, TECHNOLOGY→kap7, COMPETITION→kap3+6, RISKS→kap4+8+9
- Output is single consolidated file (not modular)


---

## Output

**Format:** markdown (modular: summary + detail files)
**Location:** `outputs/research/YYYY-MM-DD-{topic}-summary.md` (project) or `outputs/research/` (fallback)
**Type:** deep-research

**Frontmatter:**
```yaml
---
type: research
subtype: deep-research
title: "Deep Research: [Topic]"
date: YYYY-MM-DD
project: "[project-slug]"
status: completed
confidence: 0.XX
sources_count: XX
research_time: "XX min"
tags: [topic-tag1, topic-tag2]
related:
  - YYYY-MM-DD-{topic}-{subtema1}.md
  - YYYY-MM-DD-{topic}-{subtema2}.md
discovered_entities: []
created_by: /deep-research
---
```

---

*References: skills/research/domains/ | Subagents: skills/subagents/research-agent.md, skills/subagents/deep-research-agent.md*
