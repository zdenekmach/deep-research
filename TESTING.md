# Testing Guide

How to test the deep-research plugin.

## Setup

```bash
cd /path/to/deep-research
claude --plugin-dir .
```

Verify plugin loaded: type `/help` — you should see commands under the `deep-research` namespace.

---

## Test 1: Quick Research (basic functionality)

**Prompt:**
```
/deep-research:research "best practices for remote team onboarding 2025"
```

**Expected:**
- Confidence gate passes (topic is clear and focused)
- 3-7 sources found with URLs
- Output saved to `outputs/research/` directory
- Executive summary, key findings, sources table
- Each claim has a citation

**Pass criteria:** File created, 3+ sources with URLs, structured format.

---

## Test 2: Deep Research (parallel agents + Signal Map)

**Prompt:**
```
/deep-research:deep-research "AI adoption in European manufacturing sector"
```

**Expected:**
- Topic decomposed into 4+ streams (MARKET, TECHNOLOGY, COMPETITION, RISKS or similar)
- Parallel agents launched
- Signal Map created (STRONG/MODERATE/WEAK per stream)
- 20+ sources collected
- Modular output (summary + detail files for strong streams)
- Opinionated recommendations

**Pass criteria:** Signal Map present, 20+ sources, modular files, recommendations are opinionated (not "you could do A or B").

---

## Test 3: Market Report Format

**Prompt:**
```
/deep-research:research "European SaaS market 2026" --format market-report
```

**Expected:**
- 11-chapter structure (Exec Summary through Appendices)
- TAM/SAM/SOM section
- Porter's Five Forces table
- PESTLE table
- Competitive landscape
- SWOT analysis

**Pass criteria:** All 11 chapters present, tables filled with data, sources cited.

---

## Test 4: Critique

**Prompt:**
```
/deep-research:critique "The only way to solve climate change is through nuclear energy. Solar and wind are too unreliable and expensive. Every country that has reduced emissions has done so through nuclear power."
```

**Expected:**
- Argument structure mapped (premises → conclusion)
- Logical fallacies identified (false dichotomy, hasty generalization)
- Evidence gaps noted
- Counter-arguments steel-manned
- Severity ratings on each issue

**Pass criteria:** At least 2 fallacies identified, counter-arguments present, overall assessment with reasoning.

---

## Test 5: Verify (fact-check)

**Prompt:**
```
/deep-research:verify "According to a 2024 McKinsey study, 73% of companies have adopted AI in at least one business function. The global AI market is worth $500 billion as of 2025. OpenAI was founded in 2016 by Elon Musk and Sam Altman."
```

**Expected:**
- Claims extracted and categorized (statistics, facts)
- Each claim verified via WebSearch
- Fact-check report with VERIFIED/INCORRECT/UNVERIFIED status
- The OpenAI founding year should be flagged (2015, not 2016)
- McKinsey stat should be verified against original source

**Pass criteria:** At least one claim flagged as incorrect or needs attention. Structured report.

---

## Test 6: Humanize

**Prompt:**
```
/deep-research:humanize "It is important to note that implementing a comprehensive digital transformation strategy requires a robust framework that leverages synergistic capabilities across the organization. Furthermore, organizations must proactively optimize their operational paradigms to achieve seamless integration of innovative technologies."
```

**Expected:**
- AI patterns detected (implement, comprehensive, robust, leverage, synergistic, proactively, optimize, paradigm, seamless, innovative)
- Rewritten in natural language
- Audit table showing original → replacement
- Shorter output than input

**Pass criteria:** 5+ patterns detected, rewrite is natural and shorter, audit table present.

---

## Test 7: Domain Template (market-entry)

**Prompt:**
```
/deep-research:deep-research "entering the Polish fintech market for B2B payment solutions"
```

**Expected:**
- Should pick up `market-entry` domain template
- Decomposition includes: Market Size, Customer Landscape, Competitive Environment, Regulatory, Go-to-Market
- GO/NO-GO recommendation in output
- Market attractiveness score

**Pass criteria:** Domain template influence visible in decomposition structure.

---

## Test 8: Agents Available

**Prompt:**
```
/agents
```

**Expected:**
- `deep-research-agent` listed (Opus)
- `research-agent` listed (Sonnet)
- `fact-check-agent` listed (Haiku)
- `critic-agent` listed (Sonnet)

**Pass criteria:** All 4 agents visible.

---

## Quick Smoke Test (5 min)

If you only have 5 minutes, run tests 4, 6, and 8 — they're fast and cover critique, humanize, and agent registration without requiring WebSearch.

---

## Known Limitations

- Deep research (Test 2) takes 10-15 minutes and uses significant API tokens
- Market report (Test 3) is the most token-intensive test
- WebSearch availability affects Tests 1, 2, 3, 5, 7
- Domain template matching (Test 7) depends on the research skill detecting the template
