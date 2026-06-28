---
name: concept-learning-site
description: "Triggers: /learning-site, 'studijní web', 'learning site', 'web na pochopení tématu', 'interaktivní studijní materiál', 'udělej mi web ke studiu X', 'concept learning site'. When user wants to deeply LEARN a complex topic and prefers an interactive offline study website over a flat document — research + structured content + standalone HTML SPA (left nav, search, mermaid diagrams, clickable citations, active recall). NOT a one-doc summary (→ /explain-document) and NOT a quick gist (→ /digest)."
---

# Concept Learning Site Skill

**Verze:** 1.0.0 | **Pattern:** SKILL-TEMPLATE + generátor (markdown → standalone HTML)
**Pattern:** hybrid — exposition mode (vysvětluj téma, ne „dokument říká") + analytické čočky (80/20 jádro, mental models, deconstruction, mastery roadmap, playbook, failure map) + prezentační vrstva (standalone HTML).

Ze složitého tématu vyrobí **interaktivní offline studijní web**. Vstupem je jen název tématu, výstupem standalone `index.html`, který se otevře bez serveru a funguje bez internetu.

---

## Co skill dělá (3 fáze s checkpointy)

Pipeline je záměrně rozdělená do tří fází s lidskými kontrolními body. Checkpointy jsou to, co dělá výsledek dobrým — nestaví se web nad neověřeným obsahem. Detailní prompty pro sub-agenty: `references/pipeline.md`.

### Fáze 1 — Research
Spusť hloubkový research na téma (sub-agent `deep-research-agent` nebo `/deep-research`). Cíl: cited markdown report s číslovanými zdroji (s URL), foundational koncepty, klíčoví aktéři/školy, vztahy, kritiky.
- Výstup: `<OUT>/<slug>/research/deep-research-<slug>.md`
- **Checkpoint:** ověř kompletnost (sekce + počet zdrojů + závěr). Až pak dál.

### Fáze 2 — Obsah
Sub-agent (nebo hlavní vlákno) přetaví report do studijního markdownu v **exposition mode** (vysvětluj téma, ne „report říká"). Aplikuj analytické čočky: 80/20 jádro, mental models, deconstruction, mastery roadmap, playbook, failure map.
- Výstup: `<OUT>/<slug>/site/content.md`
- Doporučené sekce: proč na tom záleží → 80/20 jádro → foundational koncepty (každý + active recall `<details>`) → mentální modely → aktéři a školy → deconstruction vztahů → aplikace → časté chyby → mastery roadmap → glossary → zdroje.
- **Checkpoint:** uživatel schválí obsah. Obsah se ladí v markdownu, ne v HTML.

### Fáze 3 — Web
Vygeneruj standalone web a otevři ho.
- Zkopíruj `assets/` (web_template.html, gen.py, marked.min.js, mermaid.min.js) do `<OUT>/<slug>/site/`, NEBO spusť `gen.py` přímo ze skillu s `--content` a `--out`.
- `python3 assets/gen.py --content <…>/site/content.md --out <…>/site/ --title "<Téma>"`
- Generátor vloží markdown do template, nahradí `__TITLE__`/`__SUBTITLE__`/`__VERSION__`, a **zkopíruje knihovny vedle `index.html`** → výsledek je plně offline a přenositelný.
- Otevři `index.html` (`open` / na canvas).

---

## Konvence obsahu (kvůli kompatibilitě s template post-processorem)

Template po renderu sám propojí odkazy — ale jen když fáze 2 dodrží tyto konvence:

| Prvek | Jak psát v `content.md` | Co template udělá |
|-------|--------------------------|--------------------|
| Citace | `[1]`, `[25]` v textu | klikací odkaz → skok na řádek zdroje + zvýraznění |
| Zdroje | sekce „Zdroje" jako tabulka `\| # \| Zdroj — https://… \| Cred \|` | řádky dostanou kotvu `src-N`, URL se autolinkují |
| Cross-ref | „sekce 3.1", „sekci 7.4" (nadpisy číslované `## 5.` / `### 3.1`) | „N.N" → odkaz na příslušný nadpis |
| Diagramy | ```` ```mermaid ```` bloky, popisky se závorkami v `["…"]` | render + lightbox na zoom |
| Active recall | `<details><summary>otázka</summary>odpověď</details>` | karta s otázkou (klik rozbalí) |

Nadpisy `## ` se automaticky stanou levou navigací se scrollspy. Live search a reading progress jsou součástí template.

---

## Kdy to NEpoužít

- Výklad jednoho konkrétního dokumentu → `/explain-document`
- Rychlé shrnutí „o čem to je" → `/digest`
- Hloubková analýza jedné knihy s academic validací → `/book-analyze`
- Vytěžení videa/transkriptu přes čočky → `/extract`
- Téma, které zvládneš vysvětlit v odstavci → prostě odpověz

---

## Artefakty skillu

```
concept-learning-site/
  SKILL.md                  # tento soubor
  assets/
    web_template.html       # standalone HTML shell (__TITLE__/__CONTENT__ placeholdery)
    gen.py                  # generátor markdown → offline index.html (kopíruje assets)
    marked.min.js           # vendored (offline render markdownu)
    mermaid.min.js          # vendored (offline diagramy)
  references/
    pipeline.md             # prompty pro sub-agenty fází 1 a 2
```

## Output umístění

`<OUT>/<slug>/research/` (report) + `<OUT>/<slug>/site/` (content.md + index.html + assets/).

---

*Wrapper command: `/learning-site`.*
