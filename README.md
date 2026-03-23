# deep-research

**Version:** 1.0.0

Multi-pass parallel research plugin for [Claude Code](https://code.claude.com). Systematically explores topics from multiple angles using parallel agents, gathers 25+ quality sources, and synthesizes findings into actionable insights.

## What's Included

### Research Commands

| Command | Purpose | Sources | Time |
|---------|---------|---------|------|
| `deep-research` | Multi-pass parallel research with SIFT evaluation | 25-40 | 10-15 min |
| `research` | Quick to moderate evidence-driven research | 3-7 | 2-5 min |

### Quality & Review Commands

| Command | Purpose |
|---------|---------|
| `critique` | Logical analysis of arguments — fallacies, evidence gaps, counter-arguments |
| `verify` | Three-level content verification — facts, style, sources, implementation completeness |
| `humanize` | Remove AI-generated text patterns while preserving content and expertise |

### Specialized Agents

| Agent | Model | Purpose |
|-------|-------|---------|
| `deep-research-agent` | Opus | Multi-pass research with SIFT framework, credibility scoring, 25+ sources |
| `research-agent` | Sonnet | Topic decomposition, synthesis, entity detection |
| `fact-check-agent` | Haiku | Verify claims, citations, links, statistics |
| `critic-agent` | Sonnet | 4D content critique (accuracy, conciseness, readability, actionability) |

## Installation

```bash
# Load directly
claude --plugin-dir ./deep-research

# Or install from marketplace (when available)
# /plugin install deep-research
```

Commands are available as `/deep-research:<command>`.

## Key Features

### SIFT Framework
Every source is evaluated using the SIFT methodology:
- **Stop** — evaluate before using
- **Investigate** — who is the author/organization?
- **Find** — is there a better source?
- **Trace** — where does the original claim come from?

### Signal Map (Adaptive Research)
After initial broad search, each research stream is classified:
- **STRONG** (8+ sources, high credibility) → deep dive with nuanced comparison
- **MODERATE** (4-7 sources) → standard deep dive
- **WEAK** (<4 sources) → directional patterns only, no precise claims

### 2D Confidence Model
Recommendations use a two-dimensional model:
- Signal Strength (STRONG/MODERATE/WEAK) × Source Convergence (converging/contradictory)
- Prevents hallucinated precision on weak signals

### Opinionated Recommendations
No "you could do A or B" — always opinionated with reasoning, but precision matched to signal strength.

## Language Configuration

By default, subagent outputs are in **English** (prevents language mixing during synthesis). Final user-facing files follow your configured output language.

To configure output language, add to your project's `CLAUDE.md`:

```markdown
## Output Language
- Final output: English
- Technical terms: standard English terminology
```

Or for other languages:

```markdown
## Output Language
- Final output: Czech with full diacritics
- Technical terms: First mention = Czech + English in parentheses
```

## Directory Structure

```
deep-research/
├── .claude-plugin/plugin.json    # Plugin manifest
├── commands/                     # User-invokable commands
│   ├── deep-research.md          # Multi-pass parallel research
│   ├── research.md               # Quick research
│   ├── critique.md               # Argument analysis
│   ├── verify.md                 # Content verification
│   └── humanize.md               # AI pattern removal
├── agents/                       # Specialized agent definitions
│   ├── deep-research-agent.md    # Opus-powered deep research
│   ├── research-agent.md         # Sonnet research agent
│   ├── fact-check-agent.md       # Haiku fact-checker
│   └── critic-agent.md           # Sonnet content critic
└── skills/                       # Agent skills and references
    ├── research/                 # Core research skill
    │   ├── SKILL.md              # Full research methodology
    │   ├── templates/            # Output templates
    │   ├── references/           # Anti-patterns, methodology
    │   └── domains/              # Domain-specific research templates
    └── subagents/                # Detailed agent methodologies
        ├── research-agent.md
        ├── fact-check-agent.md
        └── critic-agent.md
```

## Output

Research outputs are saved to `outputs/research/` by default. Each output includes:
- YAML frontmatter (type, date, confidence, source count)
- Executive summary
- Detailed findings by stream/subtopic
- Source list with credibility scores
- Signal Map (for deep research)

## Requirements

- [Claude Code](https://code.claude.com) v1.0.33+
- Internet access (for WebSearch and WebFetch)
- Optional: [SearXNG](https://docs.searxng.org/) for enhanced search (218 engines)

## License

MIT — use freely, attribution appreciated.
