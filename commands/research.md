# Research

Conduct research on: $ARGUMENTS

---

## Quick Reference

```
/research Claude Code hooks                            # Quick research (3-7 sources)
/research "EU taxonomy banking"                        # Moderate research
/research "AI in Czech banking" --format market-report # Market report (11 chapters)
/deep-research topic                                   # Deep research (25+ sources)
```

---

## When to Use

| Need | Command | Time | Sources |
|------|---------|------|---------|
| Quick lookup | `/research` | 2-5 min | 3-7 |
| Deep analysis | `/deep-research` | 10-15 min | 25-40 |

---

## Constraints Summary

| Aspect | Value |
|--------|-------|
| Mode | Research (evidence-driven) |
| Token Budget | 6000 max |
| Confidence Gate | Required (>50%) |
| Sources | Every claim needs URL |

---

## Implementation

**Apply:** `skills/research/SKILL.md`

---

## Output Location

- **With project:** `outputs/research/` (use configured output dir)
- **Without project:** `outputs/research/`
## Language

- Follow configured output language with proper diacritics
- See README.md → "Language Configuration"

---

## Output Formats

| Format | Flag | Structure |
|--------|------|-----------|
| Standard | *(default)* | Executive Summary → Findings → Sources. Template: `skills/research/templates/research-output.md` |
| Market Report | `--format market-report` | 11 chapters (Exec Summary, TAM/SAM/SOM, Porter's, PESTLE, Customer, Competitive, Tech, Regulatory, SWOT, Recommendations, Appendices). Template: `skills/research/templates/market-report.md` |

Default template is always applied. Use `--format market-report` for comprehensive market analysis.

---

## Related Commands

- `/deep-research` — Multi-pass research (25+ sources)
- `/critique` — Logical analysis of findings
- `/verify` — Fact-check before publication

---

*Wrapper v2.0.0 | Full implementation in skill*
