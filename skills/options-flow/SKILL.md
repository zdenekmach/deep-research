---
name: options-flow
description: "Triggers: /options, 'kam vůbec jet', 'kterou variantu', 'pomoz mi vybrat mezi', 'srovnej varianty a pak rozpracuj', 'rozhodnout se mezi X a Y', 'compare options then plan'. When the user faces a DECISION with 2–4 meaningful alternatives and wants them researched, fairly compared on a shared interactive web, then — after THEY pick — the chosen one worked out into an actionable detail. The harder half is choosing, not planning. NOT a single-topic study site (→ /learning-site) and NOT a one-doc summary (→ /explain-document)."
---

# Options Flow Skill

**Verze:** 1.0.0 | **Pattern:** orchestrace (Vrstva B) nad datově řízeným site engine (Vrstva A = [[concept-learning-site]])
**Vzor:** scope → paralelní research variant → srovnávací web → rozhodnutí člověka → detailní web. Reálný vzor z Vánoc 2026/27: scope → paralelní research variant → srovnávací web → rozhodnutí člověka → detailní web vybrané varianty.

Generický **rozhodovací tok**. Vezme rozhodnutí s několika smysluplnými variantami, férově je prozkoumá a srovná na interaktivním webu, nechá **člověka vybrat** (gate), a teprve pak rozpracuje vybranou variantu do proveditelného detailu. Nástroj nerozhoduje za uživatele.

Job, který to dělá: *„Stojím před rozhodnutím s víc variantami a chci se rozhodnout informovaně, ne ze setrvačnosti."*

---

## Architektura — tři vrstvy (separation of concerns)

| Vrstva | Co | Kde |
|--------|----|----|
| **A — Site engine** | datově řízený renderer (mapy, galerie, srovnání) z `site.json` | `skills/concept-learning-site/assets/` (`gen.py --data`, `site_engine.js`) — **reuse, neměnit** |
| **B — Flow** | tenhle skill: scope → research → web → výběr → detail | `skills/options-flow/` |
| **C — Profily** | doménové prompty/struktura/gates (`--profile trip` …) | `skills/options-flow/references/profiles/trip.md` + `assets/trip_apis.py` |

Engine se **nepřepisuje per případ**. Flow jen produkuje `content.md` + `site.json` a volá `gen.py`. Veškerý JS pro mapy/galerie je generický (Fáze 1, hotová).

---

## Pět fází (s lidskými checkpointy)

Checkpointy jsou to, co dělá výsledek dobrým: nestaví se detail nad nerozhodnutou variantou a nesrovnává se nad neověřeným researchem. Detailní prompty pro sub-agenty: `references/pipeline.md`.

### Fáze 0 — Scope (gate)
Z dotazu odvoď **2–4 smysluplné varianty** a **kritéria rozhodnutí** (osy, na kterých budou varianty porovnatelné — např. cena, čas, jistota, riziko). Když varianty nejsou zřejmé, vyžádej si je.
- Volitelně: jedna **devil's advocate** varianta (ověř, že nejde o setrvačnost — „a co kdyby vůbec ne X?").
- Výstup: krátká scope-nóta — varianty + kritéria + co se researchuje.
- **Checkpoint:** uživatel potvrdí varianty a kritéria. Bez potvrzení se neresearchuje (research je drahý).

### Fáze 1 — Research (paralelně, úsporně)
Pro každou variantu spusť research **paralelně**. Default `research-agent` (sonnet, úsporný); eskalace na `deep-research-agent` (opus) jen na přání nebo u variant s vysokou nejistotou.
- **Sdílená kritéria** ze scope drž napříč variantami → výstupy jsou srovnatelné na stejných osách (jinak srovnání nedává smysl).
- Každá varianta: citace, SIFT, poctivé pro/proti (ne marketing).
- Výstup: `<OUT>/research/<variant-slug>.md` na variantu.
- **Checkpoint:** ověř, že každý report má závěr a srovnatelné osy. Doplň mezery před fází 2.

### Fáze 2 — Srovnávací web
Z reportů vytvoř **jeden** srovnávací web (multi-page je Fáze 1b; zatím dvěma weby).
- `content.md`: hook → **srovnávací tabulka** (varianty × kritéria) → mapa všech variant → per-varianta shrnutí s pro/proti a citacemi → doporučení *jak se rozhodnout* (ne *co vybrat*).
- `site.json`: `points[]` tagované variantou (`tags:["v1"]…`), `maps.overview` (`filterTag:null` = všechny body) + volitelně per-varianta mapa, volitelně galerie. Kontrakt: `references/site-data-contract.md` → odkazuje na engine SPEC.
- Vygeneruj: `gen.py --content … --data … --out <OUT>/compare/` → `index.html`.
- **Checkpoint:** otevři web, nech uživatele projít. Obsah se ladí v `content.md`/`site.json`, ne v HTML.

### Fáze 3 — Rozhodnutí (gate — člověk)
Uživatel vybere variantu. **Nástroj nerozhoduje.** Smí shrnout trade-offy, ale výběr je na člověku. Zaznamenej vybranou variantu + důvod (vstupuje do detailu).

### Fáze 4 — Detailní web vybrané varianty
Pro vybranou variantu: dohleď chybějící fakta (cílený research jen na tu jednu), pak proveditelný detail.
- `content.md`: detailní plán/postup vybrané varianty (u domén s profilem dle profilu — viz Vrstva C).
- `site.json`: detailní mapa (body + trasa + legenda), galerie.
- Vygeneruj: `gen.py … --out <OUT>/<variant-slug>/` → `index.html`.
- **Checkpoint:** otevři, ověř proveditelnost (vše, co člověk potřebuje, aniž by se doptával).

---

## Profily (Vrstva C) — tenká doménová vrstva

Profil = doménové prompty + struktura + gates, **přepínač** `--profile <jméno>`. Generický flow běží bez profilu. Při `--profile trip` načti `references/profiles/trip.md` PŘED fází 0 a aplikuj jeho instrukce na každou fázi.

| Profil | Stav | Co přidá |
|--------|------|----------|
| (žádný) | **hotovo** | generický scope/research/srovnání/detail |
| `trip` | **hotovo** | rigor z `plan-trip`: GPS všech bodů, hodinový rozpis, počasí + déšťový backup, golden hours, eBird, limity denního nájezdu, soběstačnost. Data přes `assets/trip_apis.py` (standalone port `personal_apis.py`). Sub-módy `trip:birding` / `trip:photography`. → `references/profiles/trip.md` |

---

## Nezávislost

Plugin je standalone. **Nezávisí** na žádné externí databázi ani paměti. Závisí jen na agentech v témže pluginu (`research-agent` / `deep-research-agent`) a na engine z `skills/concept-learning-site`.

- **Výstup (`<OUT>`):** uživatelem zadaná složka nebo cwd. Text/argumenty drž generické.
- Mapové dlaždice + vzdálené fotky chtějí internet při prohlížení (zdokumentuj); text/struktura/srovnání fungují offline.

---

## Kdy to NEpoužít

- Jedno téma do hloubky (ne rozhodnutí mezi variantami) → `/learning-site`
- Jednorázový research bez rozhodování → `/research` nebo `/deep-research`
- Rozhodnutí, které zvládneš zodpovědět odstavcem → prostě odpověz

---

## Artefakty skillu

```
options-flow/
  SKILL.md                       # tento soubor
  assets/
    trip_apis.py                 # standalone domain data (geocode/počasí/slunce/eBird) pro trip profil
  references/
    pipeline.md                  # prompty pro sub-agenty (scope, research, srovnání, detail)
    site-data-contract.md        # jak namapovat varianty na site.json (odkaz na engine SPEC)
    profiles/
      trip.md                    # trip profil: rigor plan-trip + napojení na trip_apis.py
```

Engine (gen.py, site_engine.js, site_template.html, knihovny) se **nekopíruje sem** — žije v `skills/concept-learning-site/assets/` a volá se odtud.

## Output umístění

`<OUT>/research/<variant>.md` (reporty) · `<OUT>/compare/` (srovnávací web) · `<OUT>/<variant-slug>/` (detail vybrané varianty).

---

*Wrapper command: `/options`. Vrstva B (orchestrace) nad Vrstvou A (engine z concept-learning-site).*
