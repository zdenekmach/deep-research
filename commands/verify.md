# Quality Verification

**Version:** 1.3.0 | **Purpose:** Content quality verification (facts, style, sources) and implementation completeness (three-level verification)

Verify content quality: $ARGUMENTS

---

## When to Use

- Before publishing blog posts or articles
- After research with many claims — fact-check
- Quality check consulting deliverables
- Before merge/deploy of implementations
- After refactoring to detect orphaned files
- `/verify [file]`, `/verify facts`, `/verify style`, `/verify sources`, `/verify implementation [path]`, `/verify gaps [path]`

---

## Workflow

### Content Quality (original)
1. **Fact checking** -- Extract claims, find evidence, cross-reference, assign confidence
2. **Style checking** -- Analyze style compliance, report issues
3. **Source validation** -- Extract URLs/citations, check accessibility, credibility, recency
4. **Comprehensive** -- All checks + unified quality score

### Implementation Completeness
5. **Level 1: Exists** -- File exists, non-empty, correct structure (frontmatter, exports, imports)
6. **Level 2: Substantive** -- Real implementation (not stub): detect TODO, FIXME, placeholder, empty function bodies, lorem ipsum
7. **Level 3: Wired** -- Connected to system: registered in plugin.json, imported, tested
8. **Gap report** -- Structured findings report with severity (blocking/minor/warning) and suggested fixes
9. **Re-verification** -- After fix: re-check only previously failed items, delta report

---

## Rules

| Situation | Action |
|-----------|--------|
| Trust all sources | Always credibility assessment |
| Skip fact-check | Fast mode: top 10 claims only |
| Assume file works | Three-level verification |
| Accept stubs | Detect stub patterns proactively |
| Manual orphan hunt | Automated grep/usage checks |

---

## Quality Thresholds

```yaml
# Content Quality
content_thresholds:
  publish_ready: 8.0
  needs_review: 6.0
  reject: 4.0
  by_category:
    factual_accuracy: 8.0
    style_compliance: 7.0
    source_quality: 7.5

# Implementation Completeness
implementation_thresholds:
  production_ready:
    level_1_exists: 100%
    level_2_substantive: 90%
    level_3_wired: 80%
    blocking_gaps: 0
  usable_with_warnings:
    level_1_exists: 100%
    level_2_substantive: 70%
    level_3_wired: 50%
    blocking_gaps: 0
```

---

## Stub Patterns to Detect

- `TODO`, `FIXME`, `XXX`, `HACK` comments
- `not implemented`, `placeholder`, `coming soon`
- Empty function bodies: `function foo() {}`
- Single `return null` or `pass` statements
- Lorem ipsum text or `[TBD]` markers
- MD: headings without content (>50% empty sections)
- Code: functions without logic (only constants or throws)

---

## Wired Verification Methods

```bash
# Grep usage across codebase
rg "import.*ComponentName" --type ts
rg "from.*file-name" --type py

# Check plugin registration
cat plugin.json | jq '.commands[]'

# Check routes
rg "path.*component-name" router/
```

---

## Gates (hard stop)

- [ ] Content: Overall score >= 6.0 for review, >= 8.0 for publication
- [ ] Content: Unverified claims <= 20%
- [ ] Implementation: Blocking gaps = 0 for production
- [ ] Gap report has actionable fixes
- [ ] Re-verification shows improvement delta

---

## Output

**Format:** markdown (verification report)
**Location:** inline response
**Type:** verification

---

*Version 1.3.0 | Verify plugin*
