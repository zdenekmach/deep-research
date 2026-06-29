---
name: document-explainer
description: "Triggers: /explain-document, 'vysvětli dokument', 'explain this document', 'výukové shrnutí', 'výklad dokumentu', 'document exposition', 'study brief', 'rychlé pochopení článku'. When user wants a structured exposition (~800–1500 words) of a complex document — not summary, not abstract, but tutor-style exposition that delivers comprehension to manager-level reader in 5–10 minutes. Goal: rychle pochopit, co text TVRDÍ, jaký staví argument a co z toho plyne."
---

# Document Explainer Skill

**Verze:** 1.0.0 | **Pattern:** SKILL-TEMPLATE
**Zdroj design:** Comprehension falsify experiment (2026-05-07/08), styleguide ověřený proti Claude.ai / NotebookLM baseline.

Strukturovaný výukový výklad libovolného složitého dokumentu (PDF, MD, TXT, DOCX) v exposition mode — vysvětluje téma, ne reportuje o textu.

---

## Behavioral Mode

**Mode:** Tutor / Expert Exposition
- **Vysvětluj téma, jako bys ho učil** — ne reportuj o textu
- Source refs jako fact-check anchors, ne attribution
- Lidská řeč, žádné akademické distance, žádný marketingový tón
- Konkrétní data inline (jména, čísla, roky) — ne „studie ukazují"
- Slabiny / counter-arg explicit — pokud autor sám hedguje, nezamlčet

## Klíčový rozdíl: exposition mode vs. reportáž mode

| ❌ Reportáž (NE) | ✅ Exposition (ANO) |
|------|------|
| „Dokument tvrdí, že..." | (přímo argument) |
| „Autor cituje Pencavela..." | „Pencavel 2014 ukázal..." |
| „Hlavním sdělením textu je..." | (přímo sdělení v lidské řeči) |
| „V sekci 3 autor argumentuje, že X" | „X — důvod: ..." |
| „Studie přiznává limitace" | „Vzorek je ale jen 293 amatérů, ne profesionálů — efekt na experty se neměřil" |

## Language Rules

- **Jazyk:** stejný jako zdroj (česky → česky, anglicky → anglicky)
- **Technical/academic terms:** první použití = překlad + anglický termín v závorce
- **Tón:** věcný, přímý, tutorial-style; bez korporátních frází

## Input

**$ARGUMENTS:** cesta k dokumentu (relative or absolute)

Příklady:
```
/explain-document 11-Client-Projects/dq-konzultace/outputs/.../debate-prep.md
/explain-document /Users/.../paper.pdf
/explain-document path/to/study.pdf
```

Pokud cesta nezadána → request ji od uživatele.

## Workflow

### Krok 1: Načtení a inspekce dokumentu

1. **Determine type** by extension:
   - `.md`, `.txt`, `.markdown` → načíst přímo
   - `.pdf` → konvertovat: `pdftotext -layout <path> /tmp/doc-<hash>.md`
   - `.docx` → konvertovat: `pandoc <path> -o /tmp/doc-<hash>.md`
   - jiné → zeptat se uživatele

2. **Size check:**
   - <50K znaků: načti celé
   - 50K–200K: načti, ale strukturovaně (headings, klíčové sekce)
   - >200K: zeptat se uživatele zda zaměřit na konkrétní část, nebo split

3. **Inspekce:**
   - Frontmatter (YAML) → metadata o žánru, audience, cíli
   - Heading hierarchy → struktura argumentu
   - Length, sekce, tabulky, references count

### Krok 2: Identifikace argumentní struktury

Před psaním výkladu interně namapuj:

1. **Hlavní teze** — co text tvrdí (1–2 věty, bez „dokument říká")
2. **Vrstvy důkazu** — kolik logických vrstev (3–5 obvykle), jaké jsou jejich vztahy
3. **Klíčová data** — čísla, jména autorů, roky, citace (pro exact reproduction)
4. **Counter-argumenty / slabiny** — kde se autor sám hedguje (`Limitations`, `Caveats`, „We acknowledge...", „Tady je ale...")
5. **Implikace / decision triggers** — co z toho plyne pro čtenáře

### Krok 3: Generování výkladu

**Cílová délka:** 800–1500 slov (1–2 strany hutného textu, podle délky zdroje)

**Struktura (top-down):**

```markdown
# {Téma — 1 řádek, výstižný}

## Hlavní teze

{Jednou až dvěma větami, bez meta-vrstvy. Přímo to, co text tvrdí.}

## {Vrstva 1: heading reflektující obsah, ne pozici}

{Exposition — vysvětli vrstvu jako učitel. Inline data: "X 2024 ukázal, že Y" ne "X v sekci 3 cituje Y".}

## {Vrstva 2: ...}

...

## {Co text sám přiznává jako slabinu / Limitations}

{Explicitní oddíl — autor hedguje, counter-formulace, schematické tvrzení.}

## Reader guide (volitelně, pokud má pro reader hodnotu)

{3-tier: kdo má číst co — TL;DR / specifické sekce / celý text}

## Co z toho plyne pro tebe

{1-3 actionable rules pro čtenáře — ne "doporučuji se zamyslet", ale "pokud rozhoduješ o X, pak Y".}
```

### Krok 4: Self-validation před uložením

1. **Length check:** 800–1500 slov
2. **Exposition mode check:** `grep -ciE "studie|dokument|autor (uvádí|cituje|říká|tvrdí)|text (říká|tvrdí|obsahuje)"` → max 5 výskytů
3. **Source faithfulness check:** vyber 3 random claims z výkladu, ověř proti zdroji
4. **Limitations included check:** explicit oddíl o slabinách / counter-formulacích?
5. **Navigability check:** alespoň 3 inline odkazy na zdroj (sekce / krátký citát)
6. **Top-down check:** výklad nezačíná seznamem entit nebo lineárním shrnutím

### Krok 5: Output

**Default save location:**

```
<out>/explanations/{slug}-explained.md
```

Kde `{slug}` je odvozeno z filename zdroje (lowercased, dashed).

**Frontmatter:**

```yaml
---
type: explanation
source: {original-path}
generated: {ISO timestamp}
words: {count}
---
```

Ulož + report user:
- Path k uloženému výkladu
- Word count
- Self-validation summary (které checks prošly)

## Anti-patterns (NE)

- **Žádné meta-narrativy** o textu („dokument je", „autor argumentuje", „text obsahuje", „v sekci X je")
- **Žádný flat seznam bullet points** jako primary structure (próza s headings ano)
- **Žádné přepisy** dokumentu (vysvětli, ne kopíruj)
- **Žádné AI-přidané rady** mimo zdroj („doporučuji konzultovat odborníka")
- **Žádné fabrications** (čísla, jména, citace) — pokud nevíš, řekni to
- **Žádné zamlčování slabin** — pokud autor sám hedguje, do výkladu patří

## References (detailní podklad pro skill)

- Empirický základ: styleguide ověřený proti baseline (plain Claude vs NotebookLM) v exposition/comprehension testu.

## Test cases (eval reference)

Existující dokumenty s ground-truth výkladem (output-C-scaffolded.md):

1. `experiments/2026-05-07-comprehension-falsify/docs/v4-utilization-95pct-debate-prep/`
   - Source: debate-prep, krátký, silný TL;DR
   - Eval: ~25-27/30
2. `experiments/2026-05-07-comprehension-falsify/docs/doshi-hauser-genai-creativity-2024/`
   - Source: akademický paper, dlouhý, supplementary tables
   - Eval: ~25/30

Pokud se skill spustí na jeden z těchto testovacích dokumentů, výstup by měl skórovat ≥ 25 / 30 podle `eval-template.md`.

## Invariants (co skill NESMÍ)

- Generovat výklad delší než 1500 slov nebo kratší než 800 (mimo extreme krátký dokument <500 slov)
- Halucinovat čísla / jména / citace, které ve zdroji nejsou
- Vynechat autorovy explicit limitations / counter-formulace
- Použít reportáž mode na primary content (max 5 výskytů „dokument/autor/text říká" napříč)
- Uložit výstup bez self-validation
