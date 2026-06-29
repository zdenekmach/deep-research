# Content Extract

Hluboká multi-čočková extrakce z videa/transkriptu/textu: $ARGUMENTS

---

## Quick Reference

```
/extract 7HOcOd8iSCs              # YouTube ID → stáhne transkript, vybere čočky
/extract https://youtu.be/...     # YouTube URL
/extract path/to/digest.md           # soubor (md/txt/transkript)
/extract <zdroj> learn            # vynutí záměr: naučit se
/extract <zdroj> mine             # vynutí záměr: vytěžit pro systém
/extract paste                    # vložíš transkript přímo
```

---

## What It Does

1. Získá obsah (transkript / soubor / paste)
2. Klasifikuje typ: instructional / commentary / conceptual / case-study
3. Zjistí záměr (learn vs mine) — zeptá se, když není zřejmý
4. **Vybere 1–3 relevantní čočky z 8** (dispatcher, ne „spusť všechno")
5. Spustí je, zbytek nabídne jako opt-in
6. Uloží do `<out>/extractions/`

8 čoček: deconstruction, skill-tree, 80/20 insight, playbook, mental models,
scénáře, failure map, mastery roadmap. Skill nespouští teaching-lenses na
komentář/news (vyrobily by prázdné lešení).

## Když to nepoužít

- Rychlé shrnutí „o čem to je" → `/digest video <id>`
- Výklad dokumentu pro manažera → `/explain-document`
- Hloubková analýza knihy → `/book-analyze`
- Jedna faktická otázka → přímý dotaz

## Implementation

**Apply:** `skills/content-extract/SKILL.md`

**References:** `references/lenses.md` (8 promptů), `references/lens-selection.md` (výběrová mapa)

## Related Commands

- `/digest video` — rychlé shrnutí videa
- `/explain-document` — strukturovaný výklad dokumentu
- `/book-analyze` — deep rozbor knihy
- `/deep-research` — multi-source synthesis

---

*Wrapper v1.0.0 | Full implementation in skill*
