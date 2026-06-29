---
name: content-extract
description: "Triggers: /extract, 'vytěž z videa', 'rozeber tohle video', 'extract from transcript', 'deep dive video', 'co se z toho dá naučit', 'rozbor přepisu'. When user wants DEEP multi-lens extraction of transferable value from a video/transcript/article (learning or system-mining) — not a quick summary."
---
# Content Extract — Deep Multi-Lens Extraction

**Verze:** 1.0.0 | **Pattern:** SKILL-TEMPLATE (dispatcher)

Hluboká extrakce přenositelné hodnoty z videa / transkriptu / textu pomocí
**8 analytických čoček**, z nichž skill **inteligentně vybere 1–3** podle typu
obsahu a záměru. Deep varianta k `/digest video` (rychlé shrnutí) a komplement
k `/book-analyze` (knihy) a `/explain-document` (výklad dokumentu).

---

## Behavioral Mode

**Mode:** Research (extraction)
- Věrnost zdroji — žádné dolepování mimo obsah; co tam není, nehalucinuj.
- Užitečnost před objemem — radši 2 ostré čočky než 8 tupých.
- Guardrail proti balastu: teaching-lenses (skill tree, mastery roadmap) jen na
  obsah, který reálně učí dovednost (viz `references/lenses.md` → FITS/NOISE).

## Language Rules

-> Viz CONSTITUTION.md -> "Output Language & Style"
- Čočky (analytický prompt) běží interně v **angličtině** (lepší kvalita).
- Finální výstup uživateli: **česky**, čtivě (prozaické sekce = plné věty).

---

## Input

**$ARGUMENTS** může být:
- YouTube ID nebo URL (`/extract 7HOcOd8iSCs`, `/extract https://youtu.be/...`)
- Cesta k souboru (`.md`/`.txt`/transkript/digest) — `/extract path/to/digest.md`
- `paste` → uživatel vloží transkript/text přímo
- prázdné → zeptej se na zdroj

Volitelně lze připojit záměr: `/extract <zdroj> learn` nebo `... mine`.

---

## Workflow

### 1. Získej obsah

**YouTube ID/URL** → stáhni transkript (POZOR: nová verze API, `get_transcript` už neexistuje):
```bash
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
ft = YouTubeTranscriptApi().fetch('<VIDEO_ID>', languages=['en','cs'])
print(' '.join(s.text for s in ft))
"
```
**Soubor** → Read (u velkých >50 KB jen vzorek + zpracuj programaticky, viz CLAUDE.md).
**Paste** → vezmi vložený text.

Pokud transkript není dostupný (žádné titulky) → řekni to a nabídni paste.

### 2. Klasifikuj typ obsahu

Urči dominantní typ: **instructional / commentary / conceptual / case-study**
(signály viz `references/lens-selection.md`). Hybridní → dominantní + 1 čočka druhého.

### 3. Zjisti záměr

- Z $ARGUMENTS (`learn` / `mine`) nebo z kontextu konverzace.
- Nejednoznačné → **AskUserQuestion** (learn = naučit se a použít / mine = vytěžit insight pro systém). Nehádej.

### 4. Vyber čočky (dispatcher)

Aplikuj mapu `references/lens-selection.md` (typ × záměr → čočky). Pravidla:
- **Strop 3 čočky** default.
- `#2` skill-tree a `#8` mastery-roadmap **nikdy default** — jen na explicitní „chci se to naučit do hloubky".
- Na commentary/news teaching-lenses nespouštěj vůbec.

**Než spustíš, oznam výběr:** „Obsah = {typ}, záměr = {záměr} → spustím čočky {seznam}. (Opt-in dostupné: {zbytek}.)"

### 5. Spusť vybrané čočky

Pro každou vybranou čočku aplikuj její prompt z `references/lenses.md` na získaný obsah.
- Víc čoček = spusť jako paralelní podúkoly (Agent) jen u dlouhých transkriptů (>5k slov);
  u kratších zvládneš inline.
- Drž věrnost zdroji — pokud čočka nemá v obsahu oporu (např. failure-map u čistého
  názoru), řekni to explicitně místo vymýšlení.

### 6. Nabídni zbytek jako opt-in

Po výstupu uveď, které čočky jsi nespustil a kdy by dávaly smysl
(„Chceš ještě #5 mentální modely / #4 playbook?").

### 7. Ulož

`<out>/extractions/YYYY-MM-DD-<slug>.md` s frontmatter:
```yaml
title, type: content-extraction, date, source (video_id/url/path),
content_type, intent, lenses_used
```

### 8. Nucleus kandidát (volitelně)

Pokud extrakce odhalí nový vzor/framework/techniku relevantní pro systém uživatele,
navrhni navazující krok (NE u každé extrakce)
nejdřív, ať neduplikuješ.

---

## Output Format

```markdown
# Extrakce — [název zdroje]

**Typ:** {instructional|commentary|conceptual|case-study} | **Záměr:** {learn|mine} | **Čočky:** {#X, #Y}

## [Název čočky #1]
[strukturovaný výstup čočky]

## [Název čočky #2]
...

---
*Zdroj: {video_id/url/path} | Nespuštěno (opt-in): {seznam}*
```

---

## Když to NEpoužít

| Situace | Místo toho |
|---------|-----------|
| Rychlé shrnutí videa „o čem to je" | `/digest video <id>` |
| Výklad dokumentu pro manažera (~1000 slov) | `/explain-document` |
| Hloubková analýza knihy s academic validací | `/book-analyze` |
| Multi-document synthesis | `/deep-research` |
| Jen jedna faktická otázka z textu | přímý dotaz, ne skill |

---

## Gates

- [ ] Obsah získán (transkript/soubor/paste), ne halucinace z názvu
- [ ] Typ obsahu klasifikován
- [ ] Záměr znám (zjištěn nebo dotázán)
- [ ] Vybráno ≤3 čočky default; teaching-lenses jen na explicit
- [ ] NOISE čočky nespuštěny na nevhodný typ (nebo s varováním)
- [ ] Výběr oznámen uživateli před spuštěním
- [ ] Výstup věrný zdroji (žádné dolepování)
- [ ] Uloženo do výstupní složky (`<out>/extractions/` nebo dle zadání)

---

## References

| File | Content |
|------|---------|
| `references/lenses.md` | 8 čoček (plné prompty) + FITS/NOISE guardrail |
| `references/lens-selection.md` | Typ × záměr → čočky mapa + anti-vzor |

---

## Empirický základ

Framework (content digestion — dispatcher nad 8 čočkami)
byl 8 paralelních promptů spouštěných na cokoliv. Test na Fable 5 transkriptu
(commentary) ukázal, že teaching-lenses (#2 skill-tree, #8 mastery-roadmap)
produkují prázdné lešení na ne-instruktážním obsahu. Reframed na **dispatcher**:
síla původních promptů zůstává, přidána selekce podle typu × záměru.

---

*Skill v1.0.0 | Plugin: research | Output: `<out>/extractions/` (nebo cwd)*

## Definition of Done

- [ ] Vstup přečten celý (ne jen začátek)
- [ ] Vybrané čočky odpovídají typu obsahu × záměru (1–3, ne všech 8)
- [ ] Každé tvrzení má oporu ve vstupu (žádné domýšlení)
- [ ] Výstup uložen do výstupní složky s frontmatter
