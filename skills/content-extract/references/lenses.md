# Lens Library — 8 analytických čoček

Každá čočka = samostatný prompt aplikovaný na získaný obsah (transkript / text).
**Použij jen vybrané čočky** (viz `lens-selection.md`), ne všechny najednou.

U každé čočky je `FITS` (typ obsahu, kde dává signál) a `NOISE` (kde vyrábí
prázdné lešení — tam ji nespouštěj, i kdyby ji uživatel chtěl, nejdřív varuj).

---

## #1 — Deep Content Deconstruction
**FITS:** vše (univerzální). **NOISE:** žádný — funguje i na krátký komentář (ve zkrácené formě).

> Analyze this content and produce a full structural deconstruction of its teaching.
> Output:
> 1. **CORE PROBLEM** — In one sentence, the exact problem or question this content is built to answer.
> 2. **NARRATIVE ARC** — Map how the explanation unfolds. Identify the 4–7 major sections, what each does, and why it appears in that order. Note shifts from problem → context → solution → application.
> 3. **KEY CONCEPTS** — For each: (a) what it is in plain language, (b) what misconception it corrects, (c) how it builds on what came before.
> 4. **TURNING POINTS** — The 2–3 moments where understanding should meaningfully shift. What does the reader now understand that they didn't before?
> 5. **KNOWLEDGE TRANSFER DESIGN** — How is the explanation structured to stick? Analogies, progressive disclosure, contrast, repetition.
> End with a one-paragraph synthesis: the complete insight a reader should leave with.

---

## #2 — Complete Skill Tree & Dependency Mapping
**FITS:** instruktážní / how-to / kurz (učí konkrétní dovednost). **NOISE:** komentář, news, launch, opinion — vyrábí generické „TIER 1: pochop základy" lešení. **Nespouštěj, pokud zdroj neučí dovednost.**

> From this content, extract a complete skill tree for mastering the topic taught.
> - **TIER 1 — FOUNDATIONS:** Non-negotiable prerequisite knowledge. For each: what it is, why required, how to verify you have it.
> - **TIER 2 — ENABLING SKILLS:** Core skills that unlock the rest. For each: (a) what it involves in practice, (b) most common way people get it wrong, (c) what it enables next.
> - **TIER 3 — EXECUTION SKILLS:** Skills that turn understanding into results. For each: (a) what proficient execution looks like, (b) novice vs competent, (c) fastest practice method.
> - **TIER 4 — ADVANCED OPTIMIZATION:** Refinements separating good from elite. For each: marginal gain + readiness signal.
> - **DEPENDENCY MAP:** Numbered list of which skills must precede others.
> - **LEARNING SEQUENCE:** Optimal order to learn, with reasoning.

---

## #3 — High-Leverage Insight Extraction (80/20)
**FITS:** vše (univerzální, nejvyšší ROI čočka). **NOISE:** žádný.

> Apply the 80/20 principle. Identify the small number of ideas that generate the majority of practical results.
> For each high-leverage insight:
> - **INSIGHT:** Crisp, actionable principle (one sentence max).
> - **WHY IT'S DISPROPORTIONATE:** The specific mechanism that makes this more valuable than the others.
> - **WHAT MOST PEOPLE DO INSTEAD:** The common default this insight corrects.
> - **IMMEDIATE APPLICATION:** The single most direct way to apply it in the next 48 hours.
> - **COMPOUNDING EFFECT:** How impact grows over time as skill increases.
> Rank by leverage (impact per unit effort) with reasoning.
> Final: a one-paragraph 'minimum effective dose' — if someone could take only one thing, what and why?

---

## #4 — Step-by-Step Execution Playbook
**FITS:** instruktážní, process/workflow, case-study s postupem. **NOISE:** opinion/komentář bez postupu — není co převést na kroky.

> Convert this content into a complete execution playbook someone could follow without the source.
> - **OVERVIEW:** What it achieves, who it's for, estimated time, required tools/resources.
> - **PHASES & STEPS:** 3–6 phases. Each phase: objective + numbered steps. Each step: action, input needed, expected output, decision points, quality gate to verify before moving on.
> - **COMMON DEVIATIONS:** 3–5 situations where the workflow breaks, the cause, and how to adapt.
> - **DONE CRITERIA:** How someone knows the process is complete and done well.
> Write so a competent professional with no prior context can execute without asking a question.

---

## #5 — Mental Models & Expert Thinking Patterns
**FITS:** koncepční, talk, esej, strategický obsah. **NOISE:** čistě procedurální how-to bez reasoningu.

> Identify the mental models and expert reasoning patterns — both explicit and implied by how the creator thinks through the problem.
> For each mental model:
> - **NAME & DEFINITION:** Clear, memorable name + two-sentence definition.
> - **HOW AN EXPERT USES IT:** The decision scenario where it applies. What question does the expert ask themselves?
> - **CONTRAST WITH NOVICE THINKING:** How a beginner approaches the same situation, and the mistake that follows.
> - **ADOPTION EXERCISE:** Simplest real-world practice that builds the habit.
> - **TRANSFER CASES:** 2–3 other domains where the same model applies.
> After all models, identify the single model that would create the largest shift in how someone approaches this topic, and why.

---

## #6 — Real-World Implementation Scenarios
**FITS:** instruktážní, applied skill. **NOISE:** abstraktní/news — scénáře vyjdou vykonstruované.

> Create 4 distinct, realistic scenarios where someone would apply this knowledge. Each a different context, skill level, or constraint.
> For each:
> - **SITUATION:** Starting conditions in concrete terms — who, goal, constraints.
> - **TRIGGER:** What requires them to apply what they learned.
> - **EXECUTION WALKTHROUGH:** Step by step how they apply the concepts.
> - **DECISION PRESSURE POINT:** The moment understanding is truly tested. Wrong choice vs right.
> - **OUTCOME:** What success looks like; the measurable result.
> - **FAILURE BRANCH:** What goes wrong without this knowledge.
> Range from straightforward application to a complex, time-pressured one.

---

## #7 — Failure Points & Beginner Pitfalls
**FITS:** instruktážní, applied skill, process. **NOISE:** opinion/news bez praxe k pokažení.

> Produce a complete failure map for anyone implementing what this teaches.
> For each failure point:
> - **MISTAKE:** Concise and precise.
> - **ROOT CAUSE:** The underlying reason beginners fall into it.
> - **HOW IT MANIFESTS:** Observable symptoms in practice.
> - **EARLY DETECTION:** Earliest signal, before significant damage.
> - **DOWNSTREAM IMPACT:** How it compounds if uncorrected.
> - **CORRECT APPROACH:** The exact right behaviour that prevents/fixes it.
> - **RECOVERY PATH:** Fastest way to correct course if already made.
> End with a ranked list: most costly mistake and why; most common.

---

## #8 — Structured Mastery Roadmap
**FITS:** instruktážní obsah o dovednosti, kterou se uživatel reálně chce naučit do hloubky. **NOISE:** cokoliv, co není learnable skill — vyrábí absurdní „týden 1–2 / měsíc 2–4" plány. **Nejpřísnější guardrail — spouštěj jen na explicitní záměr „chci se to naučit do mistrovství".**

> Design a complete mastery roadmap from zero to expert-level competence.
> - **STAGE 1 — BEGINNER (weeks 1–2):** Foundational knowledge first, 2–3 core skills, daily practice format, what good progress looks like, the most common mistake, readiness signal to advance.
> - **STAGE 2 — DEVELOPING (weeks 3–6):** New skills to layer in, practice projects, challenges to seek, the mental shift from Stage 1, readiness signal.
> - **STAGE 3 — ADVANCED (months 2–4):** Refinements with disproportionate payoff, working with real stakes/feedback, metrics to track, the anti-pattern advanced practitioners fall into, readiness signal.
> - **STAGE 4 — EXPERT:** What separates expert from advanced, how experts improve with no structured lessons, the habits/systems that sustain performance.
> Final: one-paragraph summary of the full transformation start to finish.

---

*Dispatcher nad 8 analytickými čočkami; výběr dle typu obsahu × záměru.*
