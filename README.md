# deep-research

**Version:** 1.6.0

Multi-pass parallel research plugin for [Claude Code](https://code.claude.com). Systematically explores topics from multiple angles using parallel agents, gathers 25+ quality sources, and synthesizes findings into actionable insights with practical context.

## What's Included

### Research Commands

| Command | Purpose | Sources | Time |
|---------|---------|---------|------|
| `deep-research` | Multi-pass parallel research with SIFT evaluation | 25-90 | 10-18 min |
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

# Or clone and load
git clone https://github.com/zdenekmach/deep-research.git
claude --plugin-dir ./deep-research
```

Commands are available as `/deep-research:<command>`.

## Key Features

### Topic Decomposition

Before searching, the plugin decomposes your topic into 4-6 independent research streams. For business topics it uses a four-stream pattern (MARKET / TECHNOLOGY / COMPETITION / RISKS); for other domains it applies domain-specific decomposition.

Why this matters: single-pass search follows keywords from your prompt. If you ask about "longevity biotech — senolytics, rapamycin, epigenetic clocks, blood plasma," you get answers about exactly those four topics. GLP-1 agonists, NAD+ precursors, or cellular reprogramming won't surface because you didn't ask. Deep-research decomposes based on problem structure, not just the prompt — and catches what you didn't know to ask about.

A validation checkpoint runs before any search begins: Are all key dimensions covered? Is there an obvious missing perspective? Are streams specific enough to search but broad enough for context?

### SIFT Framework & Credibility Scoring

Every source is evaluated using the SIFT methodology:
- **Stop** — evaluate before using
- **Investigate** — who is the author/organization?
- **Find** — is there a better source?
- **Trace** — where does the original claim come from?

Each source gets a credibility score:

| Score | Source Type | Example |
|-------|-----------|---------|
| +3 | Peer-reviewed | Nature, Lancet, NEJM |
| +2 | Institutional | WHO, FDA, McKinsey |
| +1 | Expert | Named expert with credentials |
| 0 | General media | News articles, industry press |
| -1 | User-generated | Reddit, Medium without credentials |
| -2 | Anonymous/promotional | Vendor whitepapers, anonymous posts |

Key claims require sources with score >= +1. Market projections from research firms get 0 and are explicitly flagged.

### Signal Map (Adaptive Research)

After initial broad search, each research stream is classified:
- **STRONG** (8+ sources, high credibility) — deep dive with nuanced comparison, full detail file
- **MODERATE** (4-7 sources) — standard deep dive
- **WEAK** (<4 sources) — directional patterns only, no precise claims, no separate file

Research effort adapts to signal strength: more tokens and recursive exploration for strong streams, broad aggregation for weak ones.

### 2D Confidence Model

Recommendations use a two-dimensional model:

| | Sources Converge | Sources Contradict |
|---|---|---|
| **Strong signal** | Precise claim: "Do X because Y" | Nuanced position: "X over Y, but consider Y when Z" |
| **Weak signal** | Directional trend: "Evidence suggests X" | Unknown: "Insufficient data. Verify Z" |

No "you could do A or B" — always opinionated with reasoning, but precision matched to signal strength.

### Practical Layer (v1.6.0)

Every research stream answers: What does this cost? Who offers it? How accessible is it today? What can someone actually do with this information? Includes concrete numbers (prices, timelines, providers) where available. If no practical data exists, it's explicitly flagged as a gap.

### Adjacent Topics (v1.6.0)

Every stream identifies 2-3 related topics that the research touches but doesn't cover in depth. Shows the reader what's beyond the edges of this research and where they could continue.

### Narrative Summary (v1.6.0)

The summary file reads as a cohesive narrative, not a structured data dump. Findings are woven across streams into a story — not siloed per section. Think "analyst report for a board member," not "database export."

### Numbered Bibliography (v1.6.0)

Inline references [1][2][3] throughout the text. Sources grouped by credibility tier (High/Medium/Low) at the end of each file. Format: `[N] Author/Org — "Title" — URL (Date) — Credibility: +X`.

## Comparison

| | Standard research | Gemini Deep Research | deep-research plugin |
|---|---|---|---|
| **Sources** | 3-7 | 30-45 | 25-90 |
| **Passes** | 1-2, serial | unknown (black-box) | 5+ phases, parallel (3-4 agents) |
| **Decomposition** | None | Implicit (thematic sections) | Explicit 4-6 streams with Signal Map |
| **Source evaluation** | None | None | SIFT framework + credibility -2 to +3 |
| **Confidence model** | 1D (high/medium/low) | None | 2D matrix: signal strength x source convergence |
| **Conflicts** | Flag | Avoids | Explicit resolution with reasoning |
| **Practical Layer** | No | Partial (prices) | Yes (prices, providers, budget stacks) |
| **Adjacent Topics** | No | Partial (AI/tech) | Yes (2-3 per stream) |
| **Narrative flow** | No | Strong | Yes (v1.6.0) |
| **Output** | Single file | Single file | Modular: summary + detail files |
| **Time** | 2-5 min | 5-10 min | 10-18 min |

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
    │   ├── templates/            # Output templates (research + deep-research + market-report)
    │   ├── references/           # Anti-patterns, methodology
    │   └── domains/              # Domain-specific research templates
    └── subagents/                # Detailed agent methodologies
        ├── deep-research-agent.md
        ├── research-agent.md
        ├── fact-check-agent.md
        └── critic-agent.md
```

## Domain Templates

The plugin includes domain-specific research templates that guide topic decomposition for common scenarios:

| Template | Use Case | Key Output |
|----------|----------|------------|
| `market-entry` | New market evaluation | GO/NO-GO with attractiveness score |
| `technology-evaluation` | Technology adoption decisions | Weighted decision matrix |
| `regulatory-landscape` | Compliance & regulation mapping | Gap analysis + remediation roadmap |
| `wildlife-photography` | Example non-business template | Species guide + photography settings |

Create your own templates in `skills/research/domains/` — the research agent automatically checks for matching domain templates during topic decomposition.

## Output Templates

| Template | Flag | Structure |
|----------|------|-----------|
| `research-output.md` | *(default for /research)* | Executive Summary → Findings → Contradictions → Sources |
| `deep-research-output.md` | *(default for /deep-research)* | Narrative Summary + Signal Map + Practical Layer → Detail files per stream |
| `market-report.md` | `--format market-report` | 11-chapter market report (TAM/SAM/SOM, Porter's, PESTLE, SWOT...) |

## Output

Research outputs are saved to `outputs/research/` by default. Each output includes:
- YAML frontmatter (type, date, confidence, source count)
- Narrative executive summary (v1.6.0 — woven across streams, not siloed)
- Signal Map with stream classification
- Detailed findings with inline references [N]
- Practical Layer per stream (costs, providers, accessibility)
- Adjacent Topics per stream (2-3 related areas)
- Numbered bibliography grouped by credibility tier
- Contradiction table with explicit resolutions

## Requirements

- [Claude Code](https://code.claude.com) v1.0.33+
- Internet access (for WebSearch and WebFetch)
- Optional: [SearXNG](https://docs.searxng.org/) for enhanced search (218 engines)

## Changelog

- **1.6.0** (2026-03-31): Narrative Summary, Practical Layer, Adjacent Topics, Numbered Bibliography. Inspired by comparative analysis with Gemini Deep Research.
- **1.5.0** (2026-02-09): Adaptive Resolution — Signal Map, 2D confidence model, adaptive token allocation.
- **1.1.0** (2026-01-23): Recursive Depth Pattern — dynamic sub-agent spawning for complex topics.
- **1.0.0** (2026-01-13): Initial release.

## License

MIT — use freely, attribution appreciated.
