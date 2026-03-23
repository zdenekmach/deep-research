# Technology Evaluation Research Domain Template

Structure for deep research of technology adoption decisions.

---

## Subtopics for Decomposition

1. **Capabilities & Fit**
   - Core features vs. requirements
   - Integration with existing stack
   - Scalability (current and projected load)
   - Performance benchmarks

2. **Maturity & Ecosystem**
   - Release history and versioning
   - Community size and activity (GitHub stars, contributors, issues)
   - Documentation quality
   - Third-party plugins, extensions, integrations

3. **Total Cost of Ownership**
   - Licensing model (open-source, SaaS, enterprise)
   - Infrastructure costs
   - Training and onboarding effort
   - Migration costs from current solution

4. **Risk Assessment**
   - Vendor lock-in degree
   - Bus factor (single maintainer? VC-funded startup?)
   - Security track record (CVEs, audit history)
   - Compliance with relevant standards

5. **Alternatives Comparison**
   - Direct alternatives (feature parity)
   - Different-approach alternatives (solve same problem differently)
   - Build vs. buy analysis

---

## Search Query Templates

### Capabilities
```
"[technology] features overview [year]"
"[technology] vs [alternative] comparison"
"[technology] benchmark performance"
"[technology] integration [existing-stack]"
```

### Maturity
```
"[technology] github stars contributors"
"[technology] roadmap [year]"
"[technology] community size"
"[technology] production use cases"
```

### Cost
```
"[technology] pricing tiers"
"[technology] total cost ownership"
"[technology] migration from [current]"
```

### Risk
```
"[technology] security vulnerabilities CVE"
"[technology] vendor lock-in"
"[technology] company funding runway"
```

---

## Output Structure

### Decision Matrix

```markdown
| Criterion | Weight | [Tech A] | [Tech B] | [Tech C] |
|-----------|--------|----------|----------|----------|
| Feature fit | 30% | | | |
| Maturity | 20% | | | |
| TCO (3yr) | 25% | | | |
| Risk | 15% | | | |
| Ecosystem | 10% | | | |
| **Weighted** | 100% | | | |

## Recommendation
[Opinionated pick with reasoning and migration path]
```

---

*Domain template v1.0.0 — Technology evaluation research decomposition*
