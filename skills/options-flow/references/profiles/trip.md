# Profil `trip` — doménová vrstva pro `/options --profile trip`

Tenká vrstva nad generickým flow (`pipeline.md`). Přidává **rigor cestovního plánu** (z původního `plan-trip`/`photo-trip`/`birding`) a napojuje **`trip_apis.py`** jako zdroj GPS/počasí/golden hours/eBird. Generický flow (5 fází) běží stejně; profil jen mění prompty, strukturu a gates jednotlivých fází.

**Data CLI** (volej přes Bash; výstup JSON): `assets/trip_apis.py`
```bash
TRIP=skills/options-flow/assets/trip_apis.py
python3 "$TRIP" geocode "El Rocío, Spain"          # → lat/lng + DMS + maps link
python3 "$TRIP" gps 37.13 -6.49                    # decimal + DMS + Google Maps
python3 "$TRIP" distance 36.675 -4.499 37.13 -6.49 # km (limity nájezdu)
python3 "$TRIP" weather 37.13 -6.49 --days 7       # počasí + precip_prob + cloudcover
python3 "$TRIP" sun 36.73 -2.11 --date 2026-12-31  # sunrise/sunset → golden/blue hours
python3 "$TRIP" hotspots 37.13 -6.49 --dist 30     # eBird (needs EBIRD_API_KEY; jinak WebSearch)
```
3 ze 4 zdrojů jsou **bez klíče** (geocode/počasí/slunce). eBird chce free `EBIRD_API_KEY` v env; bez něj vrať fallback a doplň hotspoty přes WebSearch. **Počasí**: forecast jen ~16 dní dopředu — pro vzdálenější termín použij klimatologii/normály (WebSearch „prosinec srážky Cádiz") a označ confidence `estimated`. Slunce/golden hours fungují pro libovolné datum.

---

## Fáze 0 — Scope (trip varianta)

Sběr požadavků navíc oproti generickému scope:
- **Destinace/směr** (může být otevřený: „kam na Vánoce k moři, přímý let z Prahy")
- **Termín** (přesná data — vstupuje do počasí, golden hours, sezónnosti)
- **Účel/zájmy** (ptáci, fotka, hory, klid, děti…) → určí sub-mód (birding/photography)
- **Limit denního nájezdu** (km/h za den), preferovaný počet bází
- **Rozpočet, doprava** (auto/veřejná), kdo jede (děti → tempo)

Kritéria srovnání variant typicky: **jistota počasí · dostupnost (přímý let) · sezónní vhodnost · zážitek/náplň · náročnost přejezdů · cena**. Předlož ke schválení (gate).

---

## Fáze 1 — Research varianty (trip)

K promptu z `pipeline.md` přidej osy specifické pro výlet — pokryj u KAŽDÉ varianty:
- **Sezónní vhodnost termínu** (co je v daný měsíc v provozu, počasí-normály, denní světlo)
- **Dostupnost** (přímý let / dojezd, brána, vouchery/cena)
- **Náplň dle zájmů** (klíčová místa; u birding/photo i konkrétní lokality + co tam v sezóně je)
- **Riziko počasí** + existence suchého/krytého backupu
Body, které půjdou na mapu, vracej **se souřadnicemi** (nebo názvy ke geokódování). Citace povinné.

---

## Fáze 2 — Srovnávací web (trip)

Srovnávací tabulka má řádky = trip kritéria výše. Mapa `overview` ukáže klíčová místa všech variant (body tagované variantou). „Jak se rozhodnout" zdůrazní trade-off **jistota počasí vs. zážitek vs. náročnost**. Jinak genericky.

---

## Fáze 4 — Detailní web (trip) — TADY je rigor

Detail vybrané varianty musí mít **≥** rigor starého `plan-trip`. Gates (DoD profilu):

| Gate | Co | Jak (data) |
|------|----|-----------|
| **GPS všech bodů** | každý bod plánu má decimal + DMS + Google Maps link; parkování u trailheadů | `trip_apis.py gps` / `geocode`. Geokódování = **BLOCKER**: bod bez souřadnic se nepustí do detailu |
| **Hodinový rozpis** | den po dni, časová osa; řazení **sunrise-first / sunset-last** (foto), backtracking minimalizovat, clustering bodů po dnech | `sun` na golden/blue hours; `distance` na přejezdy |
| **Limit denního nájezdu** | žádný den nepřekročí zadaný limit km/h; jinak rozděl bázi | `distance` mezi po sobě jdoucími body |
| **Počasí + déšťový backup** | u každého dne odhad počasí; **pro každý outdoor den existuje krytý/suchý plán B** | `weather` (≤16 dní) nebo klimatologie (WebSearch, confidence estimated) |
| **Golden/blue hours** (sub-mód photo) | u foto bodů čas zlatých/modrých hodin + co fotit | `sun --date <den>`; cloudcover z `weather` → kvalita světla |
| **eBird hotspoty** (sub-mód birding) | hotspoty poblíž bází, recent (14d) / notable druhy, target species | `hotspots` (+ `EBIRD_API_KEY`); bez klíče WebSearch |
| **Soběstačnost** | plán je proveditelný bez doptávání: adresy, otevírací doba, vstupné, rezervace, kontakty |  ověř v reportu/WebSearch |

`site.json` detailu: `points[]` se souřadnicemi (z geocode), `maps.detail.route[]` = číslované zastávky dle hodinového rozpisu + linka, `categories` dle typu (ptáci/les/kaňon/pobřeží/letiště), volitelně galerie.

### Sub-módy
- **`birding`** — přidej eBird vrstvu (hotspoty + druhy), pozorovatelny, příliv/odliv u mokřadů, brzké ráno.
- **`photography`** — golden/blue hours u každého foto bodu, weather-quality (oblačnost), shot list, gear checklist, fáze měsíce (noční).
Sub-mód se zapne ze zájmů ve scope nebo explicitně (`--profile trip:birding`). Lze kombinovat.

---

## Nezávislost

`trip_apis.py` je standalone (stdlib + `requests`). Žádná závislost na externí databázi. eBird klíč přes `EBIRD_API_KEY`; ostatní zdroje bez klíče.

## Parity test (DoD Fáze 3)

Přeplánovat reálný vícedenní výlet přes `/options --profile trip` a ověřit, že detail splní všechny gates výše (GPS, hodinový rozpis, počasí + déšťový backup, golden hours, eBird, limity nájezdu, soběstačnost).
