# SPEC — Site engine (datově řízený) v1

**Status:** Fáze 1 · **Datum:** 2026-06-28 · Souvisí: `PRD-options-flow.md`

Cíl: generátor `concept-learning-site` přestane potřebovat ručně psaný JS pro mapy/galerie.
Vstup = `content.md` (čistý markdown + placeholdery) **+** `site.json` (data). Výstup = standalone HTML.
Zpětně kompatibilní: bez `--data` se chová jako dnes (jen markdown).

## Kontrakt

### V `content.md` jen placeholdery (žádný JS)
```html
<div class="cls-map" data-map="overview"></div>
<div class="cls-gallery" data-gallery="klicova-mista"></div>
```

### `site.json` — data
```json
{
  "categories": {
    "birds":   { "color": "#3fb6b6", "label": "Ptáci / mokřady" },
    "forest":  { "color": "#6fd99a", "label": "Les / potok" },
    "canyon":  { "color": "#d99a4a", "label": "Kaňon / vodopád" },
    "coast":   { "color": "#d9c04a", "label": "Pobřeží" },
    "geo":     { "color": "#b08968", "label": "Poušť / skály" },
    "airport": { "color": "#8b98a8", "label": "Letiště" }
  },
  "points": [
    { "id": "donana", "name": "Doňana / El Rocío", "lat": 37.13, "lng": -6.49,
      "cat": "birds", "desc": "Vrchol zimního ptactva…", "tags": ["v1","v3"] }
  ],
  "maps": {
    "overview": { "filterTag": null, "route": null },
    "v1": {
      "filterTag": "v1",
      "routeColor": "#e05a5a",
      "route": [
        { "name": "Málaga (AGP) — přílet", "lat": 36.675, "lng": -4.499 },
        { "name": "Báze A — Doňana", "lat": 37.13, "lng": -6.49 }
      ]
    }
  },
  "galleries": {
    "klicova-mista": {
      "images": [
        { "src": "https://…/donana.jpg", "alt": "Doňana",
          "caption": "Doňana — zimní ptactvo", "credit": "Wikimedia Commons" }
      ]
    }
  }
}
```

## Sémantika
- **categories** — barva + popisek do legendy. Sdílené napříč mapami.
- **points** — všechny body. `tags[]` říká, do kterých map/variant bod patří.
- **maps[id]** — co vykreslit do `data-map="id"`:
  - `filterTag: null` → všechny body (přehled). Jinak jen body, jejichž `tags` obsahují hodnotu.
  - `route` (volitelné) → číslované zastávky + přerušovaná linka; legenda dostane „trasa".
- **galleries[id]** — obrázky do `data-gallery="id"` (grid + lightbox; `credit` se zobrazí pod mřížkou).

## Chování generátoru
1. `gen.py --content content.md --data site.json --out …` (oba volitelné; bez `--data` = starý režim).
2. `site.json` se vloží do šablony jako `<script type="application/json" id="site-data">` (řídí ho generátor, ne marked → bezpečné).
3. Šablona přibalí `assets/site_engine.js` + Leaflet (CDN; dlaždice/fotky chtějí internet, text běží offline).
4. `site_engine.js` po renderu najde `[data-map]`/`[data-gallery]` a vykreslí z dat.

## Hranice v1
- Jedna stránka, víc map/galerií na ní. **Multi-page** (přehled ↔ detail variant jako oddělené stránky se sdílenou navigací) = `pages[]` v `site.json` → **Fáze 1b/2**.
- Žádná závislost na externí databázi ani paměti. Jen soubory dovnitř/ven.

## DoD Fáze 1
- [ ] `gen.py` přijímá `--data`, zpětně kompatibilní bez něj
- [ ] `site_engine.js` vendored, vykreslí mapy (body+trasa+legenda) i galerie+lightbox z `site.json`
- [ ] Existující web Andalusie převeden na data-driven (site.json + slim content) a vizuálně shodný
- [ ] Žádný ručně psaný JS v content/šabloně specifický pro konkrétní výlet
