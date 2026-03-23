# Research Anti-Patterns

## Skip Confidence Gate

**BAD:**
```
User: "Tell me about AI"
Claude: *immediately starts researching*
→ Vague topic, no focus, wasted effort
```

**GOOD:**
```
User: "Tell me about AI"
Claude: "Confidence: 30% (LOW)
- Clarity: Too broad
- Scope: Unbounded
- Context: Unknown application
→ Need clarification: What aspect? For what purpose?"
```

---

## Research Without Context

**BAD:**
```
/research "LLM frameworks"
→ Start fresh, ignore previous work
→ Duplicate effort
```

**GOOD:**
```
/research "LLM frameworks"
→ Check outputs/research/history/
→ Found: 2026-01-15-llm-frameworks.md
→ "Found previous research from 3 weeks ago.
   CONTINUE (extend), UPDATE (refresh), or NEW (fresh)?"
```

---

## Claims Without Sources

**BAD:**
```
"LangChain is the most popular framework."
"90% of enterprises use RAG."
→ No source, could be hallucinated
```

**GOOD:**
```
"LangChain has 76k GitHub stars as of January 2026 ([GitHub](url))."
"According to [Survey](url), 67% of respondents reported RAG usage."
→ Every claim verifiable
```

---

## Hallucinated URLs

**BAD:**
```
"See [Documentation](https://docs.example.com/api/v2)"
→ URL doesn't exist or is wrong
```

**GOOD:**
```
- Fetch URL before citing
- If can't verify, mark: "[Source - unverified URL]"
- Use trusted domains from validate-research.sh
```

---

## Wrong Save Location

**BAD:**
```
Active project: beanz
Research saved to: outputs/research/
→ Research disconnected from project
```

**GOOD:**
```
Active project: beanz
Check: Determine output directory
Save to: outputs/research/
→ Research stays with project
```

---

## Skip Entity Detection

**BAD:**
```
Research mentions:
- github.com/langchain-ai/langchain
- "Designing Data-Intensive Applications" book
- Expert John Doe quoted
→ No entity linking, knowledge lost
```

**GOOD:**
```
Research mentions entities:
1. langchain → Check knowledge-base/repositories/ → EXISTS
2. "Designing Data..." → Check knowledge-base/books/ → NEW
3. John Doe → NEW expert

Output:
related: [knowledge-base/repositories/langchain.md]
discovered_entities:
  - type: book, name: "Designing Data-Intensive..."
  - type: person, name: "John Doe"
```

---

## Ignore Previous Research

**BAD:**
```
/research "vector databases"
→ Research from scratch
→ 3 days ago: similar research exists
→ Duplicated effort
```

**GOOD:**
```
/research "vector databases"
→ grep -l "vector" outputs/research/history/
→ Found: 2026-01-28-vector-db-comparison.md
→ "Found recent research. Want to:
   - EXTEND with new findings?
   - UPDATE with latest info?
   - START FRESH from different angle?"
```

---

## Single Source Reliance

**BAD:**
```
All findings from one vendor blog post
→ Biased perspective
→ No triangulation
```

**GOOD:**
```
Multiple source types:
- Vendor documentation
- Independent benchmarks
- Academic papers
- Community discussions
→ Triangulated, balanced view
```

---

## Outdated Sources

**BAD:**
```
"According to 2021 survey..."
"Based on documentation from 2022..."
→ LLM space moves fast, outdated info
```

**GOOD:**
```
Prefer sources <2 years old
Note age: "As of Q4 2025..."
Flag outdated: "[Note: Source from 2021, may be outdated]"
```
