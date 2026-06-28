# Pipeline — prompty pro sub-agenty

Konkrétní zadání pro fáze 1 a 2. Nahraď `<TÉMA>`, `<SLUG>` a `<OUT>`. Prompty jsou ověřené na pilotu „systems thinking".

---

## Fáze 1 — Research (`deep-research-agent`)

> Proveď hloubkový, vícezdrojový a ověřený research na téma **<TÉMA>**, jako podklad pro studijní materiál (a případně aplikaci v dané doméně).
>
> **Rozsah:** jádro tématu, ne encyklopedie. Pokud má téma víc škol/směrů, pokryj ty hlavní a propoj je. (Volitelně předem odsouhlas s uživatelem šíři: jádro vs jen klíčové zdroje vs široký landscape.)
>
> **Metoda:** min. ~15 kvalitních zdrojů (preferuj primární a peer-reviewed/uznávané sekundární). Aplikuj SIFT, uveď credibility u klíčových tvrzení. Mapuj kontradikce a kritiky. U každého claimu citace.
>
> **Výstup** — markdown do `<OUT>/<SLUG>/research/deep-research-<SLUG>.md`:
> 1. Executive summary (čtivě, prozaicky)
> 2. Foundational koncepty (každý: definice, analogie, příklad)
> 3. Klíčoví aktéři / školy / metodologie (co přinesli, nástroj, kdy použít)
> 4. Mapa vztahů mezi koncepty a školami (textově — bude z toho mermaid)
> 5. Aplikace (na cílovou doménu uživatele)
> 6. Kontradikce, kritiky, otevřené otázky
> 7. Zdroje s credibility, **číslované, s URL** (kvůli klikacím citacím na webu)
>
> Píš čtivě v češtině (odborné termíny anglicky s českým glossem). Na závěr vrať shrnutí: co report obsahuje, kolik zdrojů, hlavní zjištění, mezery k doplnění.

**Checkpoint:** zkontroluj nadpisy + počet zdrojů + že report má závěr (agent může spadnout po zápisu souboru — soubor přesto bývá kompletní).

---

## Fáze 2 — Obsah (content sub-agent nebo hlavní vlákno)

> Vytvoř z research reportu **studijní materiál** o <TÉMA> — obsahový podklad pro interaktivní studijní web.
>
> **Přečti PŘED psaním:**
> 1. Report: `<OUT>/<SLUG>/research/deep-research-<SLUG>.md` (zdroj pravdy, nevymýšlej fakta)
> 2. **Exposition mode** — vysvětluj téma vlastními slovy, ne „report říká"; ELI5 hook → hloubka → příklad.
> 3. **Analytické čočky** — 80/20 jádro (kterých ~6–8 konceptů dá 80 % pochopení), mental models, deconstruction vztahů, mastery roadmap, playbook, failure map.
> 4. Styl: čtivá próza, jedna myšlenka na větu, čísla a notace do tabulek (ne do vět)
>
> **Režim:** exposition mode (vysvětluj téma, ne „report říká"). Čtivá próza, čeština, jedna myšlenka na větu. Odborné termíny anglicky s českým glossem. Confidence (verified/estimated/inferred) kde to dává smysl.
>
> **Konvence (KRITICKÉ pro web):**
> - Citace `[n]` v textu, číslování zachovej z reportu.
> - Sekce „Zdroje" jako tabulka `| # | Zdroj — URL | Credibility |`.
> - Cross-ref piš jako „sekce N.N" (web je zlinkuje na číslované nadpisy).
> - Active recall: `<details><summary>otázka</summary>odpověď</details>`.
> - Vlož 1–2 ````mermaid```` grafy (vztahy konceptů, roadmap), popisky se závorkami v `["…"]`.
>
> **Sekce (aplikuj čočky 80/20, mental models, deconstruction, mastery roadmap, playbook, failure map):**
> 1. Proč na tom záleží (ELI5 + hook)
> 2. 80/20 jádro (kterých ~6–8 konceptů dá 80 % pochopení)
> 3. Foundational koncepty do hloubky (každý: definice, analogie, příklad, proč záleží, 1 active recall)
> 4. Mentální modely / archetypy
> 5. Aktéři a školy + kdy co použít
> 6. Jak to souvisí — deconstruction (textový podklad pro mermaid)
> 7. Aplikace na cílovou doménu (playbook)
> 8. Časté chyby (failure map)
> 9. Mastery roadmap (fáze studia)
> 10. Glossary (CS/EN)
> 11. Zdroje (číslovaná tabulka z reportu)
>
> Ulož do `<OUT>/<SLUG>/site/content.md`. Rozsah ~4000–6000 slov, kvalita a čtivost před stručností. Na závěr vrať shrnutí + mezery k doplnění.

**Checkpoint:** hoď `content.md` na canvas, nech uživatele schválit. Mezery doplň před fází 3 (paralelní agenti vracejí text sekcí, integruj `Edit`em — neměň `content.md` víc agenty naráz).

---

## Fáze 3 — Web (deterministicky, bez agenta)

```bash
SITE=<OUT>/<SLUG>/site
python3 skills/concept-learning-site/assets/gen.py \
  --content "$SITE/content.md" --out "$SITE" --title "<TÉMA>"
open "$SITE/index.html"
```

Generátor vloží obsah, nahradí placeholdery a zkopíruje `marked.min.js` + `mermaid.min.js` vedle `index.html` (plně offline). Verzi/podtitul lze přepsat `--version` / `--subtitle`.

**Ověř** (zejména když nelze otevřít prohlížeč): `index.html` neobsahuje `__TITLE__` ani `cdn.jsdelivr`, obsahuje `src="assets/marked.min.js"`, a `assets/` se zkopírovaly. Mermaid grafy a edge-labely se znaménky (`|"+"|`) potvrď až vizuálně.
