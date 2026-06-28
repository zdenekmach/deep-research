# Pipeline — prompty pro sub-agenty (`/options`)

Konkrétní zadání pro fáze 1, 2 a 4. Nahraď `<ROZHODNUTÍ>`, `<VARIANTA>`, `<VARIANT-SLUG>`, `<KRITÉRIA>`, `<OUT>`. Generický flow (bez profilu). Profil přidá doménové instrukce navrch (Vrstva C).

---

## Fáze 0 — Scope (řídí hlavní vlákno, ne sub-agent)

Z dotazu odvoď strukturu rozhodnutí. Drž to krátké a předlož ke schválení:

```
Rozhodnutí: <ROZHODNUTÍ>
Varianty (2–4):
  v1 — <název> — <jednovětý důvod, proč je ve hře>
  v2 — …
Kritéria (osy srovnání): <např. cena · čas · jistota · riziko · zážitek>
Devil's advocate (volitelné): <varianta, která zpochybní setrvačnost>
Co se researchuje na každé variantě: <stejné osy pro všechny>
```

**Gate:** bez potvrzení variant + kritérií se neresearchuje. Pokud uživatel varianty nedodal a nejsou zřejmé z dotazu, zeptej se — nevymýšlej je naslepo.

---

## Fáze 1 — Research varianty (`research-agent`, paralelně; eskalace `deep-research-agent`)

Spusť **jeden agent na variantu, paralelně** (víc tool-callů v jedné zprávě). Každému dej STEJNÁ kritéria, ať jsou výstupy srovnatelné.

> Proveď ověřený research **jedné varianty** rozhodnutí, jako podklad pro férové srovnání.
>
> **Rozhodnutí:** <ROZHODNUTÍ>
> **Tato varianta:** <VARIANTA>
> **Srovnávací kritéria (povinné osy — pokryj VŠECHNY, ať je varianta porovnatelná s ostatními):** <KRITÉRIA>
>
> **Metoda:** kvalitní zdroje (preferuj primární). Aplikuj SIFT, uveď credibility u klíčových tvrzení. Hledej i **proti** této variantě, ne jen pro — poctivé trade-offy, ne marketing. U každého claimu citace s URL.
>
> **Výstup** — markdown do `<OUT>/research/<VARIANT-SLUG>.md`:
> 1. Shrnutí varianty (čtivě, 1 odstavec: pro koho/kdy dává smysl)
> 2. **Hodnocení po kritériích** — sekce na každé kritérium z `<KRITÉRIA>` (fakta + číslo/odhad + citace + confidence)
> 3. Pro / proti (poctivé, vyvážené)
> 4. Klíčová fakta/místa/parametry (to, co půjde na mapu/do detailu — vč. souřadnic, pokud relevantní)
> 5. Otevřené otázky / co ověřit před rozhodnutím
> 6. Zdroje — **číslované, s URL**, s credibility
>
> Píš čtivě v češtině (odborné termíny anglicky s glossem). Na závěr vrať: jak varianta vychází na jednotlivých kritériích (1 řádek/kritérium) + největší slabina.

**Checkpoint:** každý report má všechny osy z `<KRITÉRIA>` a závěr. Když některý agent osu vynechal, doplň cíleně před fází 2 (srovnání by jinak mělo díry).

---

## Fáze 2 — Srovnávací obsah + data (content sub-agent nebo hlavní vlákno)

Syntéza VŠECH reportů do srovnání — proveď v hlavním vlákně, nebo spusť obecného sub-agenta. **Nerozhoduje** — připraví podklad pro rozhodnutí člověka.

> Z research reportů variant vytvoř **srovnávací podklad** k rozhodnutí <ROZHODNUTÍ>.
>
> **Přečti PŘED psaním:**
> 1. Všechny reporty: `<OUT>/research/*.md` (zdroj pravdy, nevymýšlej fakta)
> 2. Kontrakt dat: `skills/options-flow/references/site-data-contract.md`
> 3. Styl: čtivá próza, jedna myšlenka na větu, čísla a notace patří do tabulek (ne do vět).
>
> **Režim:** exposition mode, čtivá próza, jedna myšlenka na větu. Confidence (verified/estimated/inferred) u netriviálních tvrzení.
>
> **Vytvoř DVA soubory:**
>
> **A) `<OUT>/compare/content.md`** — sekce:
> 1. O jaké rozhodnutí jde + jak ho číst (hook, 1 odstavec)
> 2. **Srovnávací tabulka** — markdown tabulka `| Kritérium | v1 | v2 | … |`, řádek na každé kritérium z `<KRITÉRIA>`. Buňky stručné, čísla/odhady.
> 3. Mapa všech variant: placeholder `<div class="cls-map" data-map="overview"></div>`
> 4. Per-varianta blok (`## <název varianty>`): shrnutí, pro/proti, klíčová fakta, citace `[n]`
> 5. **Jak se rozhodnout** — ne *co vybrat*: které kritérium komu váží víc, jaké otázky si položit, kde jsou rozhodující trade-offy. Výběr nech na člověku.
> 6. Zdroje — sloučená číslovaná tabulka `| # | Zdroj — URL | Credibility |` (přečísluj napříč variantami konzistentně)
>
> Konvence webu: citace `[n]`, cross-ref „sekce N.N", active recall `<details>` volitelně. (Stejné jako concept-learning-site.)
>
> **B) `<OUT>/compare/site.json`** — dle `site-data-contract.md`:
> - `categories`: typy bodů (barva + label)
> - `points[]`: klíčová místa/objekty ze VŠECH variant, každý `tags:["<varianta>"]` (bod může patřit víc variantám)
> - `maps.overview`: `{ "filterTag": null, "route": null }` (přehled všech bodů)
> - volitelně `maps.<varianta>`: `{ "filterTag":"<varianta>", … }` pro samostatnou mapu varianty
> - volitelně `galleries`
>
> Na závěr vrať shrnutí + mezery k doplnění.

**Checkpoint:** vygeneruj web a otevři (viz Fáze gen). Uživatel projde a **vybere variantu** (Fáze 3). Ladí se `content.md`/`site.json`, ne HTML.

---

## Fáze 3 — Rozhodnutí (gate)

Člověk vybere. Hlavní vlákno zaznamená: `vybraná varianta = <…>`, `důvod = <…>`. Nepokračuj do detailu bez výběru.

---

## Fáze 4 — Detail vybrané varianty (content sub-agent / hlavní vlákno, + cílený research dle potřeby)

Jen pro vybranou variantu. Nejdřív dohleď chybějící fakta (jeden cílený `research-agent` na konkrétní mezery), pak detail.

> Z research reportu vybrané varianty vytvoř **proveditelný detailní podklad**.
>
> **Vybraná varianta:** <VARIANTA> (důvod výběru: <…>)
> **Přečti:** `<OUT>/research/<VARIANT-SLUG>.md` + případné doplňující reporty + `site-data-contract.md`. Styl: čtivá próza, jedna myšlenka na větu.
>
> **Vytvoř DVA soubory:**
> - **`<OUT>/<VARIANT-SLUG>/content.md`** — detailní, akční plán/postup vybrané varianty. Tak, aby podle něj člověk jednal bez doptávání. (Doménový profil — pokud zadán — přidá strukturu: u `trip` hodinový rozpis, počasí + déšťový backup, golden hours, limity nájezdu. Bez profilu: logická akční struktura dle domény rozhodnutí.) Mapa: `<div class="cls-map" data-map="detail"></div>`, galerie volitelně.
> - **`<OUT>/<VARIANT-SLUG>/site.json`** — detailní mapa: `points[]` (body + souřadnice), `maps.detail` s `route[]` (číslované zastávky + linka) je-li relevantní, legenda přes `categories`, galerie.
>
> Konvence webu jako výše. Na závěr vrať shrnutí + co ještě ověřit před realizací.

**Checkpoint:** otevři, ověř proveditelnost (vše potřebné je uvnitř).

---

## Fáze gen — Web (deterministicky, bez agenta)

```bash
ENGINE=skills/concept-learning-site/assets/gen.py

# srovnávací web
python3 "$ENGINE" --content "<OUT>/compare/content.md" --data "<OUT>/compare/site.json" \
  --out "<OUT>/compare/" --title "<ROZHODNUTÍ> — srovnání variant" --subtitle "rozhodovací podklad"
open "<OUT>/compare/index.html"

# detailní web vybrané varianty (po výběru)
python3 "$ENGINE" --content "<OUT>/<VARIANT-SLUG>/content.md" --data "<OUT>/<VARIANT-SLUG>/site.json" \
  --out "<OUT>/<VARIANT-SLUG>/" --title "<VARIANTA> — detailní plán" --subtitle "proveditelný plán"
open "<OUT>/<VARIANT-SLUG>/index.html"
```

Generátor s `--data` použije `site_template.html` + `site_engine.js` (mapy/galerie z dat). Zkopíruje `marked.min.js`, `mermaid.min.js`, `site_engine.js` vedle `index.html`.

**Ověř** (zejm. bez prohlížeče): `index.html` neobsahuje `__TITLE__`/`__SITEDATA__`, obsahuje `src="assets/site_engine.js"`, `assets/` se zkopírovaly, a `site.json` je validní JSON (gen.py spadne na nevalidním). Mapy/trasy potvrď vizuálně.
