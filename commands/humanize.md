# Humanize

**Version:** 1.1.0 | **Purpose:** Remove typical AI patterns from text while preserving content and expertise

Humanize text — remove AI-isms, preserve content and expertise: $ARGUMENTS

---

## When to Use

- Before sending proposals, deliverables, blog posts
- On any text that needs the "AI tone" removed
- After generating content with other commands

---

## $ARGUMENTS

| Argument | Description |
|----------|-------------|
| `<file>` | Path to file to process |
| `<text>` | Inline text (in quotes) |
| `--tone <mode>` | casual / professional / formal-consulting / academic (default: professional) |
| `--audit-only` | Only identify patterns, don't rewrite |

---

## Workflow

### 1. Language Detection

Automatically detect input language and apply appropriate AI pattern list.

### 2. Tone Mode Detection

If `--tone` is not specified, infer from context:
- Proposal / deliverable → `formal-consulting`
- Blog / social media → `casual`
- Email / report / presentation → `professional`
- Research / analysis → `academic`

### 3. Pass 1: Identify and Rewrite

Scan text for common AI patterns:

**Vocabulary patterns:**
- "implement/implementation" → deploy, set up, introduce
- "leverage" → use, build on
- "comprehensive/robust/sophisticated" → use specific adjective
- "seamless/seamlessly" → smooth, easy
- "paradigm shift/game-changer" → specific improvement

**Structure patterns:**
- "It's important to note" / "It should be mentioned" → delete
- "In the context of" → rephrase directly
- "Additionally" / "Furthermore" / "Moreover" at sentence start → vary or remove
- Excessive em-dash (—) usage
- Lists where a sentence would suffice
- Concluding paragraphs that repeat what was said

**Style patterns:**
- Passive voice → active voice
- Abstract → concrete (numbers and examples instead of generics)
- Long → short (if the same can be said in fewer words)

For each found pattern: record category and occurrence, rewrite preserving factual content.

### 4. Self-Audit

After first rewrite, ask: "What still sounds generic or AI-generated?" Record findings.

### 5. Pass 2: Final Rewrite

Fix remaining AI-isms based on audit.

### 6. Personality Check

Verify by tone mode:
- `casual` → personal voice? variation?
- `professional` → natural but not too personal?
- `formal-consulting` → credible, specific, no generics?
- `academic` → precise, qualified?

---

## Output

### File → new file (default)

If input is a file (`/humanize document.md`):
1. Create new file: `document.humanized.md` (same directory)
2. Original remains unchanged
3. Print audit to console

Naming: `{name}.humanized.{ext}`

### Inline text → console

If input is quoted text, output goes directly to console.

### --audit-only

Just a table of found patterns without rewriting.

### Audit format (always to console)

```
Humanized: document.humanized.md

| # | Category | Original | Change |
|---|----------|----------|--------|
| 1 | AI vocabulary | "implement" | → "set up" |
| 2 | Filler | "It should be noted" | → deleted |

Patterns found: X | Language: EN | Tone: professional
Original: document.md (unchanged)
```

---

## Rules

1. **Never change facts** — only form and style
2. **Don't remove expertise** — consulting text should remain expert
3. **Context decides** — technical term in IT context is OK
4. **Shorter > longer** — if the same can be said in fewer words
5. **Active > passive** — "I recommend" instead of "it is recommended"
6. **Specific > abstract** — numbers and examples instead of generics
7. **Preserve structure** — headings, lists, tables stay if they add value

---

## References

- English patterns: Built-in (24 patterns from blader/humanizer methodology)
- Czech patterns: `skills/humanize/references/czech-patterns.md`
- Original: https://github.com/blader/humanizer
