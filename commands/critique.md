# Argument Critique

**Version:** 2.2.0 | **Purpose:** Logical analysis of arguments -- identify fallacies, assess evidence, generate counter-arguments

Find holes and weaknesses in this argument: $ARGUMENTS

---

## When to Use

- Analyzing articles, papers, presentations for logical flaws
- Preparing for debate or discussion
- Verifying own arguments before publication
- Evaluating claims and reasoning quality

---

## Workflow

1. **Extract argument** -- If URL: fetch and extract main arguments. If text: parse directly. Identify central claim and map argument structure (premises -> conclusion)
2. **Logical analysis** -- Identify argument type (deductive/inductive/abductive/analogical). Check for all logical fallacies (see checklist below)
3. **Assess evidence** -- Source quality (primary vs secondary, recency, conflicts of interest, methodology). Evidence gaps (missing evidence, alternative explanations, cherry-picked data)
4. **Counter-arguments** -- Steel-man the best counter-position. Identify most attackable premises. Suggest questions that would challenge the argument
5. **Write critique** -- Use output template. Save to project outputs directory

---

## Logical Fallacy Checklist

| Fallacy | Description |
|---------|-------------|
| Ad hominem | Attacking person not argument |
| Straw man | Misrepresenting opposing view |
| False dichotomy | Artificial either/or |
| Appeal to authority | Unqualified expert |
| Circular reasoning | Conclusion in premise |
| Slippery slope | Unsupported chain |
| Hasty generalization | Too few examples |
| Post hoc ergo propter hoc | False causation |
| No true Scotsman | Moving goalposts |
| Begging the question | Assuming conclusion |

---

## Pravidla

| Situace | Akce |
|---------|------|
| "I disagree" without specifics | Must specify: "Premise P2 contains hasty generalization -- 3 examples insufficient" |
| Weak counter-argument (straw man) | Must steel-man: present strongest possible version of opposition |
| Personal bias in assessment | Present findings objectively regardless of personal agreement |
| No distinction between disagreement and flaw | Distinguish "I disagree" from "this is logically flawed" |
| Missing severity assessment | Each issue must be rated High/Medium/Low severity |

---

## Token Budget

| Phase | Max Tokens |
|-------|------------|
| Context | 200 |
| Analysis | 1500 |
| Output | 800 |
| **Total** | 2500 |

---

## Gates (hard stop)

- [ ] All logical fallacies identified with type
- [ ] Evidence gaps clearly described
- [ ] Counter-arguments are steel-manned (strongest version)
- [ ] Objective assessment without personal bias
- [ ] Overall strength rating with reasoning

---

## Output

**Format:** markdown

**Template:**
```markdown
# Critique: [Claim/Topic]

**Source:** [URL or "Provided argument"]
**Type:** [Article/Paper/Doc/etc.]
**Date Analyzed:** [Today]

## TL;DR
[2-3 sentence summary]

## The Argument
[Main claim and structure]

### Argument Map
1. Premise: [P1]
2. Premise: [P2]
3. Therefore: [Conclusion]

## Strengths
- [What the argument does well]

## Weaknesses

| Issue | Type | Severity | Explanation |
|-------|------|----------|-------------|
| [Issue] | [Fallacy/Evidence/Logic] | [High/Med/Low] | [Why it matters] |

## Logical Fallacies Found
- **[Fallacy Name]**: [How it appears in this argument]

## Evidence Gaps
- [What's missing]

## Counter-Arguments
1. [Strong counter-argument 1]
2. [Strong counter-argument 2]

## Questions to Ask
- [Probing question that would test the argument]

## Overall Assessment
**Strength:** [Strong / Moderate / Weak]
**Confidence:** [High / Medium / Low]
[Summary judgment]
```

**Lokace:** `60-References/critiques/` or project outputs
**Type:** critique

---

## Co dal

- `/blog` for writing own response or counter-argument
- Fact-check agent in research workflows for verification

---

*References: context/profile.md*
