# Options Flow

Rozhodni se mezi variantami informovaně: $ARGUMENTS

---

## Quick Reference

```
/options "kam na vánoční dovolenou — Andalusie vs Kanáry vs Madeira"
/options "který CRM pro 12 lidí — Pipedrive vs HubSpot vs Attio"
/options <rozhodnutí> --out ./moje-slozka      # kam uložit (default: cwd / projekt)
/options <rozhodnutí> --deep                    # eskalace na deep-research-agent
/options <rozhodnutí> --profile trip            # cestovní rigor (GPS, počasí, golden hours, eBird)
/options <rozhodnutí> --profile trip:birding    # + eBird hotspoty / druhy
/options <rozhodnutí> --profile trip:photography # + golden/blue hours, shot list
```

---

## What It Does

Vezme **rozhodnutí s 2–4 variantami** a provede pět fází s lidskými checkpointy:

1. **Scope** — odvodí varianty + kritéria, nechá potvrdit (gate)
2. **Research** — paralelně prozkoumá každou variantu na stejných osách (`research-agent`, citace, pro/proti)
3. **Srovnávací web** — engine vygeneruje web: tabulka + mapa všech variant + per-varianta
4. **Rozhodnutí** — **člověk vybere** (gate; nástroj nerozhoduje)
5. **Detailní web** — engine vygeneruje proveditelný detail vybrané varianty

Těžší půlka je *vybrat*, ne *naplánovat*. Tohle řeší obě.

## Output Format

| Prvek | Popis |
|-------|-------|
| **research/<varianta>.md** | cited report na variantu, srovnatelné osy |
| **compare/index.html** | srovnávací web (tabulka, mapa, per-varianta) |
| **<varianta>/index.html** | detailní web vybrané varianty (mapa + trasa) |

## Když to nepoužít

- Jedno téma do hloubky (ne volba mezi variantami) → `/learning-site`
- Výklad jednoho dokumentu → `/explain-document`
- Rychlé shrnutí → `/digest`
- Rozhodnutí na odstavec → prostě odpověz

## Implementation

**Apply:** `skills/options-flow/SKILL.md`
**Pipeline (prompty pro sub-agenty):** `skills/options-flow/references/pipeline.md`
**Trip profil:** `skills/options-flow/references/profiles/trip.md` (+ data `assets/trip_apis.py`)
**Engine (Vrstva A):** `skills/concept-learning-site/assets/gen.py` (`--data site.json`)

## Output Location

`<OUT>/` = zadaná složka (`--out`) nebo cwd. In-system: `<OUT>/<slug>/`.

## Related Commands

- `/learning-site` — studijní web z jednoho tématu (sdílí engine)
- `/deep-research` — multi-pass research (eskalace fáze 2)

---

*Wrapper v1.0.0 | Full implementation in skill | Nahrazuje `trips` plugin (po paritě — Fáze 3)*
