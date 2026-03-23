---
name: research
description: "Evidence-driven research with mandatory citations, confidence gates, confidence scoring, and entity detection. When Claude needs to: (1) Research a topic or question with cited sources, (2) Gather evidence and validate claims, (3) Analyze trends with confidence scoring, (4) Deep-dive into any domain requiring citations and sources. Triggers: /research, 'research', 'find evidence', 'what do we know about', 'analyze topic', 'literature review', 'sources for', 'cite', 'evidence'"
---
# Research

**Version:** 4.1.0 | **Pattern:** SKILL-TEMPLATE

Evidence-driven research with mandatory citations, confidence gates, confidence scoring, and entity detection.

---

## Behavioral Mode

**Mode:** Research
- Every claim needs a source
- Prefer recent sources (<2 years)
- Note confidence levels
- Flag contradictions
- No opinions without evidence

## Language Rules

→ See README.md → "Language Configuration"

- Subagent output: **English** (prevents language mixing in synthesis)
- Final output: **Configured output language** with proper diacritics
- Technical terms: First mention = local language + English in parentheses, then abbreviation
- Tables OK for data comparisons, text sections = readable paragraphs

---

## Workflow

### 1. Confidence Gate (FIRST)

Assess request (100-200 tokens max):
- **Clarity:** Is request specific?
- **Scope:** Is it focused?
- **Context:** Do I have project/user info?

**Confidence = (Y count / 3) × 100**

| Confidence | Action |
|------------|--------|
| <50% | STOP → AskUserQuestion |
| 50-70% | Ask 1-2 questions, proceed |
| >70% | Proceed directly |

### 2. Load Context

```
mcp__memory__open_nodes ["Zdenek", "CommandHistory"]
```

Check previous research:
```bash
grep -l "$TOPIC" outputs/research/history/*.md
```

If found, offer: NAVÁZAT / AKTUALIZOVAT / NOVÝ

### 3. Subagent Decision

| Sources Expected | Time | Action |
|------------------|------|--------|
| 1-3 (Quick) | <2 min | Direct WebSearch |
| 4-7 (Moderate) | 2-5 min | Haiku subagent |
| 8+ (Deep) | >5 min | Sonnet subagent |

**Subagent:** `skills/subagents/research-agent.md`

### 4. Research Execution

- Recent sources (<2 years preferred)
- Multiple perspectives
- Note contradictions
- URLs for everything

**Trusted domains:** github.com, arxiv.org, nature.com, sciencedirect.com, wikipedia.org, institutional (.gov, .edu)

### 5. Confidence Scoring

**Freshness × Authority × Agreement scoring** for every source:

#### Freshness Score
| Timeframe | Score | Rationale |
|-----------|-------|-----------|
| Dnes/včera | HIGH (3) | Most current, relevant for fast-moving topics |
| Tento týden | GOOD (2) | Recent, likely still accurate |
| Tento měsíc | MODERATE (1) | Acceptable for stable domains |
| Starší | LOWER (0) | Use only if no recent alternatives |

#### Authority Score
| Source Type | Score | Examples |
|-------------|-------|----------|
| Official docs | HIGH (3) | Product docs, API specs, standards |
| Shared docs | GOOD (2) | Confluence, Notion, wikis |
| Meeting notes | MODERATE (1) | Decision records, session notes |
| Chat conclusions | LOW (0.5) | Slack threads, team chat |
| Drafts | LOWER (0) | WIP documents, unreviewed |

#### Agreement Score
| Scenario | Score | Action |
|----------|-------|--------|
| Consensus (3+ sources align) | HIGH (3) | Strong confidence |
| Partial agreement (2 sources) | MODERATE (1.5) | Note differences |
| Conflict (sources contradict) | FLAG | Surface explicitly, don't pick side |

**Total Confidence = (Freshness + Authority + Agreement) / 9 × 100**

#### Output Format

**CRITICAL:** Group by topic, NOT by source.

| Result Set Size | Format |
|----------------|--------|
| Small (1-3 findings) | Full detail with all sources per finding |
| Medium (4-7 findings) | Grouped by topic, sources footnoted |
| Large (8+ findings) | High-level summary + drill-down sections |

**Conflict Surfacing:**
```markdown
## Key Finding: [Topic]

**Consensus view** (confidence: 85%)
- Source A (official docs, today): [claim]
- Source B (shared docs, this week): [supporting claim]

⚠️ **CONFLICT DETECTED:**
- Source C (meeting notes, last month): [contradictory claim]
- **Assessment:** Older source, likely outdated. Recommend following official docs.
```

### 6. Entity Detection

Scan output for:
- GitHub URLs → repository
- Book mentions → book
- Tool/product names → tool
- Expert names → person

Check knowledge base, classify as EXISTS or NEW.

### 7. Save Output

**Template:** `templates/research-output.md`

**Location:**
1. Determine output directory
2. If active → `outputs/research/`
3. Fallback → `outputs/research/`

**History:** `outputs/research/history/YYYY-MM-DD-topic-slug.md`

---

## Gates

<gate severity="BLOCKER">
Confidence <50% → STOP and ask clarifying questions
</gate>

<gate severity="BLOCKER">
Every factual claim MUST have source with URL
</gate>

<gate severity="BLOCKER">
No hallucinated URLs - all sources must be real
</gate>

---

## Allowed Tools

| Tool | Purpose |
|------|---------|
| WebSearch | Find sources |
| WebFetch | Deep dive on source |
| Read | Load context files |
| Glob | Find existing research |
| Bash (knowledge/utils.py) | Query domain model, KG |
| mcp__memory__* | Check related knowledge |
| AskUserQuestion | Clarify requirements |
| Task | Delegate to subagent |
| Write | Save output (final only) |

---

## Output Structure

### Standard Format (default)

```markdown
# Research: [Topic]

## Executive Summary
## Key Findings (grouped by topic, with confidence scores)
## Detailed Analysis
## Confidence Assessment
- Overall confidence: XX%
- High confidence findings: [list]
- Flagged conflicts: [list]
## Contradictions & Debates
## Further Research
## Sources (with Freshness/Authority scores)
## Discovered Entities
```

### Market Report Format (`--format market-report`)

When `--format market-report` is specified, use template: `templates/market-report.md`

**Key differences:**
- 11-chapter structure (Exec Summary → Appendices)
- Includes frameworks: TAM/SAM/SOM, Porter's Five Forces, PESTLE, SWOT
- Competitive feature comparison matrix (Strong/Adequate/Weak/Absent)
- Strategic recommendations with prioritization (HIGH/MEDIUM/LOW)
- Single consolidated file (not modular)


---

## Forbidden Actions

- Skip confidence gate
- Research without checking history
- Claims without sources
- Hallucinated URLs
- Save to wrong location
- Ignore previous research
- Skip entity detection

---

## References

| File | Content |
|------|---------|
| `templates/research-output.md` | Full output template |
| `references/workflow.md` | Detailed step-by-step |
| `references/anti-patterns.md` | Common mistakes |

---

## Viz také

- `/deep-research` — 25+ sources, multi-pass


- `/knowledge save` — Save discovered entities

## Definition of Done

> Typ: `research` | Ref: `skills/research/references/definition-of-done.md`

Před finalizací ověř checklist pro typ `research`:
```
# Run Definition of Done checklist for research
```

