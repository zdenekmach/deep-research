# Document Explainer

Strukturovaný výklad dokumentu: $ARGUMENTS

---

## Quick Reference

```
/explain-document path/to/study.pdf
/explain-document 11-Client-Projects/dq-konzultace/outputs/.../debate-prep.md
/explain-document /path/to/document.docx
```

---

## What It Does

1. Načte dokument (PDF/MD/DOCX/TXT) a zinspectuje strukturu
2. Identifikuje hlavní tezi, vrstvy důkazu, klíčová data, slabiny, implikace
3. Vygeneruje výklad 800–1500 slov v **exposition mode** (vysvětluje téma, ne reportuje o textu)
4. Self-validuje (length / exposition mode / faithfulness / limitations / navigability)
5. Uloží do `<out>/explanations/<slug>-explained.md`

## Output Format

| Sekce | Obsah |
|-------|-------|
| **Hlavní teze** | 1–2 věty, přímo (bez „dokument říká") |
| **Vrstvy důkazu** | Kolik vrstev má text, tolik dostaneš (faithful structure) |
| **Slabiny** | Explicit oddíl o counter-arg / hedges autora |
| **Reader guide** | Volitelně — kdo má číst co |
| **Co z toho plyne** | 1–3 actionable rules pro čtenáře |

## Když to nepoužít

- Vyhledávání faktů z dokumentu → použij `/research` nebo přímý dotaz na Claude.ai
- Hluboká analýza s validací proti academic consensus → `/book-analyze`
- Multi-document synthesis → `/deep-research`
- Ad-hoc otázka „o čem ten paper je" → stačí přímo zeptat (skill je pro structured output, ne quick Q&A)

## Implementation

**Apply:** `skills/document-explainer/SKILL.md`

**Template:** `skills/document-explainer/templates/explanation-output.md`

## Output Location

`<out>/explanations/<slug>-explained.md`

## Related Commands

- `/research` — General research (multi-source)
- `/book-analyze` — Deep book analysis with academic validation
- `/deep-research` — Multi-pass research
- `/knowledge` — Knowledge graph operations

## Empirický základ

Styleguide ověřený proti baseline (plain Claude vs NotebookLM) v comprehension testu.

Synthesis: hypotéza „strukturní lešení > plain LLM pro výklad" byla vyvrácena, ale **exposition-mode prompt sám o sobě je validní artefakt** — funguje napříč Claude.ai, NotebookLM i scaffolded systému. Tento skill destiluje styleguide do reusable command.

---

*Wrapper v1.0.0 | Full implementation in skill*
