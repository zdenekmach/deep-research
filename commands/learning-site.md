# Concept Learning Site

Interaktivní offline studijní web ze složitého tématu: $ARGUMENTS

---

## Quick Reference

```
/learning-site systémové myšlení          # téma → research → obsah → web
/learning-site "FRAM a resilience engineering"
/learning-site <téma> --project living-organization   # kam uložit
```

---

## What It Does

Ze zadaného tématu postaví studijní web ve třech fázích s kontrolními body:

1. **Research** — hloubkový multi-source cited report (`deep-research-agent`)
2. **Obsah** — strukturovaný studijní markdown v exposition mode + analytické čočky, schválení uživatelem
3. **Web** — `gen.py` vygeneruje standalone `index.html` (levý nav, search, mermaid, klikací citace, active recall) — plně offline, vendorované knihovny

## Output Format

| Prvek | Popis |
|-------|-------|
| **research/** | cited report s číslovanými zdroji |
| **site/content.md** | studijní obsah (editovatelný, na canvas) |
| **site/index.html** | standalone offline web + `assets/` |

## Když to nepoužít

- Výklad jednoho dokumentu → `/explain-document`
- Rychlé shrnutí → `/digest`
- Hloubka jedné knihy → `/book-analyze`
- Vytěžení videa → `/extract`

## Implementation

**Apply:** `skills/concept-learning-site/SKILL.md`

**Pipeline (prompty pro sub-agenty):** `skills/concept-learning-site/references/pipeline.md`

## Output Location

`<OUT>/<slug>/research/` + `<OUT>/<slug>/site/`

## Related Commands

- `/deep-research` — multi-pass research (fáze 1)
- `/explain-document` — exposition mode výklad jednoho dokumentu
- `/extract` — multi-lens extrakce

## Empirický základ

Pilot „systems thinking" (2026-06-17): research (26 zdrojů) → obsah (~5500 slov, exposition mode + 6 čoček) → offline web. Pattern ověřen jako reprodukovatelný; `gen.py` + `web_template.html` jsou téma-agnostická kostra.

---

*Wrapper v1.0.0 | Full implementation in skill*
