# Lens Selection — content type × intent → čočky

Dispatcher rozhoduje ve dvou osách: **typ obsahu** (co to je) × **záměr** (proč to čteš).

## Osa 1 — Klasifikace typu obsahu

| Typ | Signály | Příklady z našich digestů |
|-----|---------|---------------------------|
| **instructional** | učí konkrétní postup/dovednost, „how to", demo, kroky | nateherk-multi-agent-claude-code, indydevdan-delete-bash-tool |
| **commentary** | recenze, reakce, názor na událost/produkt, „X situation insane" | matthew-berman-anthropic-situation, pocketful-fable5 |
| **conceptual** | esej/talk o myšlence, mentální modely, „proč", strategie | ai-engineer-skills-at-scale, talks |
| **case-study** | konkrétní příběh s postupem a výsledkem | jack-roberts-agentic-os-self-improves |

Když je obsah hybridní → ber dominantní typ + případně přidej jednu čočku druhého.

## Osa 2 — Záměr uživatele

| Záměr | Co chce | Default tendence |
|-------|---------|------------------|
| **learn** | naučit se to, použít sám | playbook, failure map, scénáře, (mastery) |
| **mine** | vytěžit insight pro svůj systém/práci/obsah | 80/20, mentální modely, deconstruction |

Pokud záměr není zřejmý z promptu → **zeptej se** (AskUserQuestion, learn vs mine), nehádej.

## Výběrová mapa (typ × záměr → čočky)

| Typ \ Záměr | learn | mine |
|-------------|-------|------|
| **instructional** | #1 + #4 + #7 (+#6, +#8 jen na explicit mastery) | #1 + #3 + #4 |
| **commentary** | #1(lite) + #3 | #1(lite) + #3 |
| **conceptual** | #1 + #5 + #3 | #1 + #5 + #3 |
| **case-study** | #1 + #4 + #7 | #1 + #3 + #5 |

**Pravidla nad mapou:**
- Strop **3 čočky** default. Víc = balast. Zbytek nabídni jako opt-in („Chceš ještě skill-tree / mastery roadmap?").
- `#1(lite)` = jen CORE PROBLEM + NARRATIVE ARC + synthesis (vynech key-concepts/turning-points u krátkého komentáře).
- `#2` (skill tree) a `#8` (mastery roadmap) **nikdy default** — jen na explicitní „chci se to naučit do hloubky / dej mi learning path". Na commentary/news je nespouštěj vůbec.
- Pokud uživatel řekne „spusť všechny" → spusť, ale u NOISE čoček (viz lenses.md) přidej upozornění, že na tomto typu obsahu bude výstup tenký.

## Anti-vzor (čeho se vyhnout)
Spustit teaching-lenses (#2, #8) na launch/recenzi → 4 prázdné tiery a roadmapa „jak se stát expertem ve výběru modelu". To je přesně objem-nad-užitkem (`feedback_framework_design`). Radši 2 ostré čočky než 8 tupých.
