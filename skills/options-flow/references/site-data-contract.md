# site.json — kontrakt pro `/options`

Engine je **Vrstva A** (`concept-learning-site`). Plný kontrakt: `docs/SPEC-site-engine.md`. Tady jen **jak namapovat varianty rozhodnutí** na ten kontrakt — engine se nemění.

## Klíče (z engine SPEC)

| Klíč | Význam |
|------|--------|
| `categories` | `{ id: {color, label} }` — typy bodů; barva + popisek do legendy, sdílené napříč mapami |
| `points[]` | všechny body: `{id, name, lat, lng, cat, desc, tags[]}` |
| `maps[id]` | co vykreslit do `data-map="id"`: `{filterTag, route?, routeColor?}` |
| `galleries[id]` | obrázky do `data-gallery="id"`: `{images:[{src, alt, caption, credit}]}` |

## Vzor: varianty ↔ `tags` ↔ `maps`

Varianta = **tag**. Bod patří variantě (i víc variantám) přes `tags[]`. Mapa varianty filtruje přes `filterTag`.

```json
{
  "categories": {
    "key":  { "color": "#3fb6b6", "label": "Klíčové místo" },
    "hub":  { "color": "#8b98a8", "label": "Uzel / brána" }
  },
  "points": [
    { "id": "a1", "name": "Místo A", "lat": 37.1, "lng": -6.5, "cat": "key",
      "desc": "Proč je relevantní…", "tags": ["v1"] },
    { "id": "shared", "name": "Společný uzel", "lat": 36.7, "lng": -4.5, "cat": "hub",
      "desc": "Patří víc variantám", "tags": ["v1","v2"] }
  ],
  "maps": {
    "overview": { "filterTag": null, "route": null },
    "v1": { "filterTag": "v1", "routeColor": "#e05a5a",
            "route": [ { "name": "Start", "lat": 36.7, "lng": -4.5 },
                       { "name": "Místo A", "lat": 37.1, "lng": -6.5 } ] }
  }
}
```

## Pravidla použití ve flow

- **Srovnávací web (Fáze 2):** `maps.overview` s `filterTag:null` ukáže body všech variant najednou. Volitelně přidej `maps.<varianta>` pro samostatný pohled na variantu. `route` u přehledu obvykle `null` (přehled není trasa).
- **Detailní web (Fáze 4):** jedna varianta → `maps.detail` s `route[]` (číslované zastávky + linka), pokud detail je itinerář/posloupnost. `filterTag` = ta varianta, nebo `null` (web má jen body té varianty).
- **Konzistence barev:** `categories` definuj jednou, používej `cat` na bodech. Trasa dostane legendu automaticky z `routeColor`.
- **Placeholder v `content.md`:** `<div class="cls-map" data-map="overview"></div>`, `<div class="cls-gallery" data-gallery="…"></div>`. Žádný ručně psaný JS.

Vzor dat: detailní web jedné varianty = `points[]` se souřadnicemi + jedna `maps.detail` s `route[]` (číslované zastávky + linka).
