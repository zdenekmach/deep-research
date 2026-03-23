---
name: humanizer-cs
version: 1.0.0
description: |
  Identifikuj a přepiš typické vzory AI-generovaného textu v češtině.
  Adaptace blader/humanizer pro český jazyk a profesionální/consulting kontext.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Humanizer CS

Identifikuj a odstraň typické znaky AI-generovaného textu v češtině. Zachovej odbornost a profesionalitu, ale odstraň robotický a generický tón.

---

## Tone Modes

Před zpracováním identifikuj požadovaný tón:

| Mode | Popis | Příklad kontextu |
|------|-------|-----------------|
| `casual` | Neformální, osobní, blog | Blog, sociální sítě, interní poznámky |
| `professional` | Profesionální, ale přirozený | Emaily, prezentace, reporty |
| `formal-consulting` | Formální, důvěryhodný, bez generik | Nabídky, deliverables, executive summaries |
| `academic` | Akademický, precizní | Research, analýzy, studie |

**Default:** `professional`

---

## České AI vzory (detekuj a přepiš)

### Kategorie 1: Nafouklý význam
- "klíčový milník", "zásadní moment", "přelomový krok"
- "představuje významný posun", "je důkazem toho, že"
- "historicky bezprecedentní"
→ **Fix:** Konkrétní čísla, fakta. "Zvýšili jsme konverzi o 15%" místo "dosáhli jsme zásadního milníku"

### Kategorie 2: Vágní atribuce
- "Odborníci se shodují...", "Podle analytiků..."
- "Trendy ukazují...", "Praxe potvrzuje..."
- "Jak ukazují zkušenosti..."
→ **Fix:** Konkrétní zdroj nebo smazat. Pokud nevíš kdo, nepiš "odborníci".

### Kategorie 3: AI slovník (české AI-ismy)

**Vždy nahradit:**
| AI slovo | Alternativy |
|----------|-------------|
| synergický | společný, propojený, kombinovaný |
| holistický | celkový, komplexní přístup k... |
| implementovat | zavést, spustit, realizovat |
| optimalizovat | zlepšit, upravit, zefektivnit |
| akcelerovat | zrychlit, urychlit |
| transformační | měnící, zásadní změna |
| proaktivní | aktivní, předvídat |
| komplexní (jako buzzword) | rozsáhlý, mnohostranný |
| strategicky klíčový | důležitý pro... |
| robustní | spolehlivý, odolný |
| inovativní | nový, originální |
| disruptivní | narušující, měnící pravidla |
| leveragovat | využít, vytěžit |
| skalovat | rozšířit, zvětšit |
| stakeholder | zainteresovaná strana, účastník |
| mindset | přístup, nastavení |
| best practice | osvědčený postup |
| framework | rámec, struktura |

**Pozor:** V consulting kontextu jsou některé anglicismy akceptovatelné (stakeholder, framework). Nahrazuj jen ty, které zní přehnaně.

### Kategorie 4: Formulaické struktury
- "Navzdory výzvám se daří..." / "I přes překážky..."
- "V dnešní dynamické době..."
- "V neposlední řadě..."
- "Je nutné podotknout, že..."
- "Nelze opomenout fakt, že..."
→ **Fix:** Smazat nebo přeformulovat přímo k pointě.

### Kategorie 5: Kopulové obcházení
- "představuje klíčový nástroj" → "je klíčový nástroj" nebo lépe konkrétní tvrzení
- "slouží jako základ pro" → "je základem"
- "zaujímá pozici" → "je"
→ **Fix:** Používej "je" a "jsou". Jednoduché sloveso je silnější.

### Kategorie 6: Filler a hedging
| Filler | Alternativa |
|--------|-------------|
| Z důvodu | Protože, kvůli |
| S ohledem na skutečnost, že | Protože |
| V kontextu (aktuální situace) | Smazat, přejít k pointě |
| Je třeba poznamenat, že | Smazat |
| Není bez zajímavosti | Smazat nebo přeformulovat |
| Dá se říci, že | Říci přímo |
| V zásadě | Smazat |
| Obecně lze konstatovat | Smazat |

### Kategorie 7: Generické závěry
- "Budoucnost vypadá slibně"
- "Pouze čas ukáže..."
- "Jedno je jisté — [generické tvrzení]"
- "Celkově lze konstatovat, že..."
→ **Fix:** Konkrétní závěr nebo doporučení. Žádné generic happy ending.

### Kategorie 8: Stylové vzory
- **Přehnané tučné písmo** — ne každé druhé slovo tučně
- **Emoji jako struktura** — profesionální text bez emoji
- **Pravidlo tří overuse** — ne vždy 3 příklady
- **Seznam místo textu** — ne vše musí být odrážkový seznam
- **Nadpisy na všechno** — ne každý odstavec potřebuje nadpis

---

## Workflow

### Průchod 1: Detekce a přepis

1. Přečti vstupní text
2. Identifikuj všechny české AI vzory (kategorie 1-8)
3. Přepiš problematické sekce
4. Zachovej factual content — měníš jen formu, ne obsah

### Self-Audit

Po prvním přepisu se zeptej sám sebe:

> "Co na tomto textu stále působí genericky / AI-generovaně?"

Zapiš zjištění jako bullet points.

### Průchod 2: Finální přepis

Na základě auditu proveď finální úpravy.

### Personality Check (podle tone mode)

**casual:** Přidej osobní hlas, názory, humor kde to sedí.
**professional:** Přidej variabilitu rytmu vět, občasnou kratší větu, přiznání limitů.
**formal-consulting:** Zachovej formálnost, ale odstraň robota. Konkrétní tvrzení místo generik. Čísla místo buzzwordů.
**academic:** Precizní formulace, citace, kvalifikované závěry.

---

## Output

```
## Přepis

[Finální text]

## Audit

- [Nalezené vzory a co bylo změněno]

## Shrnutí změn

- Počet nalezených AI vzorů: X
- Hlavní kategorie: [seznam]
- Tone mode: [mode]
```

---

## Pravidla

1. **Nikdy neměň fakta** — jen formu a styl
2. **Neodstraňuj odbornost** — consulting text má být odborný, ne dumbed-down
3. **Kontext rozhoduje** — "implementovat" v IT kontextu je OK, v generickém ne
4. **Kratší > delší** — pokud lze říct stejně kratší větou, udělej to
5. **Aktivní > pasivní** — "navrhuji" místo "je navrhováno"
6. **Konkrétní > abstraktní** — čísla, příklady, jména místo generik
