# Humanize

**Verze:** 1.1.0 | **Účel:** Odstranit typické AI vzory z textu, zachovat obsah

Humanizuj text — odstraň AI-ismy, zachovej obsah a odbornost: $ARGUMENTS

---

## Kdy aktivovat

- Uživatel volá `/humanize`
- Před odesláním nabídky, deliverables, blog postu
- Na jakémkoli textu kde je potřeba odstranit "AI tón"

---

## $ARGUMENTS

| Argument | Popis |
|----------|-------|
| `<file>` | Cesta k souboru ke zpracování |
| `<text>` | Inline text (v uvozovkách) |
| `--tone <mode>` | casual / professional / formal-consulting / academic (default: professional) |
| `--audit-only` | Jen identifikovat vzory, nepřepisovat |

---

## Workflow

### 1. Detekce jazyka

Automaticky rozpoznej jazyk vstupu:
- **Čeština** → použij české AI vzory
- **Angličtina** → použij anglické AI vzory
- **Mix** → zpracuj každou sekci podle jejího jazyka

### 2. Detekce tone mode

Pokud `--tone` není zadán, odvoď z kontextu:
- Nabídka / proposal / deliverable → `formal-consulting`
- Blog / sociální sítě → `casual`
- Email / report / prezentace → `professional`
- Research / analýza → `academic`

### 3. Průchod 1: Identifikace a přepis

Načti referenční skill podle jazyka:
- **CZ:** `references/humanizer-patterns-cz.md` (české vzory)
- **EN:** Originální 24 vzorů z blader/humanizer

Projdi text a identifikuj vzory. Pro každý nalezený:
- Zaznamenej kategorii a konkrétní výskyt
- Přepiš — zachovej faktický obsah, změň jen formu

### 4. Self-Audit

Po prvním přepisu se zeptej:

> "Co na tomto textu stále působí genericky / AI-generovaně?"

Zapiš zjištění.

### 5. Průchod 2: Finální přepis

Na základě auditu oprav zbývající AI-ismy.

### 6. Personality Check

Podle tone mode ověř:
- `casual` → má osobní hlas? variabilitu?
- `professional` → přirozený ale ne příliš osobní?
- `formal-consulting` → důvěryhodný, konkrétní, bez generik?
- `academic` → precizní, kvalifikovaný?

---

## Output

### Soubor → nový soubor (default)

Pokud vstup je soubor (`/humanize dokument.md`):
1. Vytvoř nový soubor: `dokument.humanized.md` (ve stejném adresáři)
2. Originál zůstane beze změny
3. Vypiš audit do konzole

Pojmenování: `{název}.humanized.{přípona}`
- `nabidka.md` → `nabidka.humanized.md`
- `report.docx` → zpracuj text, výstup `report.humanized.md`

### Inline text → konzole

Pokud vstup je text v uvozovkách, výstup jde přímo do konzole.

### --audit-only

Jen tabulka nalezených vzorů bez přepisu a bez nového souboru.

### Formát auditu (vždy do konzole)

```
✓ Humanizováno: dokument.humanized.md

| # | Kategorie | Originál | Změna |
|---|-----------|----------|-------|
| 1 | AI slovník | "implementovat" | → "zavést" |
| 2 | Filler | "Je třeba poznamenat" | → smazáno |

Nalezeno vzorů: X | Jazyk: CZ | Tone: professional
Originál: dokument.md (beze změny)
```

---

## Pravidla

1. **Nikdy neměň fakta** — jen formu a styl
2. **Neodstraňuj odbornost** — consulting text má být odborný
3. **Kontext rozhoduje** — technický termín v IT kontextu je OK
4. **Kratší > delší** — pokud lze říct stejně kratší větou
5. **Aktivní > pasivní** — "navrhuji" místo "je navrhováno"
6. **Konkrétní > abstraktní** — čísla a příklady místo generik
7. **Zachovej strukturu** — nadpisy, seznamy, tabulky nechat pokud dávají smysl

---

## Reference

- Český skill: `references/humanizer-patterns-cz.md`
- Analýza originálu: `references/humanizer-analysis.md`
- Originál: https://github.com/blader/humanizer
