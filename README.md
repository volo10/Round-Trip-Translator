# Round-Trip-Translator - Multi-Agent Translation Pipeline

**Version:** 3.0
**Last Updated:** November 26, 2025
**Status:** Production Ready

## Assignment Overview

This project implements a **Multi-Agent Translation System** with **Vector Distance Analysis** as per the HW3 assignment requirements:

- **Translation Pipeline:** English → French → Hebrew → English
- **Spelling Error Testing:** 0% to 50% error rates
- **Vector Distance Measurement:** Cosine similarity using embeddings
- **Graph Visualization:** Spelling error % vs. vector distance

### Three Implementation Options

| Implementation | Description | Requires API Key? | Real Translations? |
|----------------|-------------|-------------------|-------------------|
| **Python + Local Models** | Uses MarianMT models locally | No | Yes |
| **Python + Claude API** | Uses Claude API for translations | Yes | Yes |
| **Claude Code Agents** | Interactive via slash commands | No | Yes |

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
   - [Windows](#windows-installation)
   - [macOS](#macos-installation)
3. [Project Structure](#project-structure)
4. [Implementation 1: Python Scripts](#implementation-1-python-scripts)
5. [Implementation 2: Claude Code Agents](#implementation-2-claude-code-agents)
6. [Test Sentences](#test-sentences)
7. [Agent Definitions](#agent-definitions)
8. [Running Tests](#running-tests)
9. [Assignment Deliverables](#assignment-deliverables)
10. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Step 1: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### Step 2: Choose a Mode and Run

| Mode | Command | Real Translations? | API Key? | Best For |
|------|---------|-------------------|----------|----------|
| **Local** | `python scripts/run_experiment.py --local` | Yes (MarianMT) | No | Assignment submission |
| **API** | `python scripts/run_experiment.py` | Yes (Claude) | Yes | Best quality |
| **Mock** | `python scripts/run_experiment.py --mock` | No (fake) | No | Fast testing |
| **Claude Code** | `/build-and-test-all` | Yes | No | Interactive |

### Step 3: Run Tests (Optional)
```bash
python -m pytest tests/ -v
```

---

## How to Run and Test - All Options Explained

### Option 1: Local Models (RECOMMENDED)

**Best for: Assignment submission, no API key needed**

```bash
python scripts/run_experiment.py --local
```

| Aspect | Details |
|--------|---------|
| Translation Engine | Helsinki-NLP MarianMT models |
| Quality | Good (real neural machine translation) |
| Speed | Medium (first run downloads ~900MB) |
| Cost | Free |
| Offline | Yes (after first download) |

**What happens:**
1. Downloads 3 models (~300MB each) on first run
2. Translates using local neural networks
3. No internet needed after download

---

### Option 2: Claude API

**Best for: Highest quality translations**

```bash
# Windows
set ANTHROPIC_API_KEY=your-key-here
python scripts/run_experiment.py

# macOS/Linux
export ANTHROPIC_API_KEY=your-key-here
python scripts/run_experiment.py
```

| Aspect | Details |
|--------|---------|
| Translation Engine | Claude AI (claude-sonnet) |
| Quality | Excellent (best available) |
| Speed | Fast |
| Cost | Requires API credits |
| Offline | No |

---

### Option 3: Mock Mode

**Best for: Testing the pipeline quickly**

```bash
python scripts/run_experiment.py --mock
```

| Aspect | Details |
|--------|---------|
| Translation Engine | Word-by-word dictionary lookup |
| Quality | Fake (not real translation) |
| Speed | Very fast |
| Cost | Free |
| Offline | Yes |

**Warning:** Mock translations are NOT real. Use only for testing the pipeline works.

---

### Option 4: Claude Code Agents (Interactive)

**Best for: Learning, exploration, step-by-step execution**

In Claude Code CLI, use these slash commands:

```bash
# Run entire workflow
/build-and-test-all

# Or step by step:
/setup-project          # Install dependencies
/run-tests              # Run all tests
/run-full-experiment    # Run experiment
/verify-results         # Check requirements met
```

| Aspect | Details |
|--------|---------|
| Translation Engine | Claude (via Claude Code) |
| Quality | Excellent |
| Speed | Interactive |
| Cost | Free (uses Claude Code) |
| Offline | No |

---

### Comparison Summary

| Mode | Command | Real Translations? | API Key? | Quality | Speed | Cost |
|------|---------|-------------------|----------|---------|-------|------|
| **Local** | `--local` | Yes (MarianMT) | No | Good | Medium | Free |
| **API** | (no flag) | Yes (Claude) | Yes | Excellent | Fast | Paid |
| **Mock** | `--mock` | No (fake) | No | N/A | Very Fast | Free |
| **Claude Code** | `/build-and-test-all` | Yes (Claude) | No | Excellent | Interactive | Free |

### Which Should I Use?

| Your Situation | Recommended Mode |
|----------------|------------------|
| Submitting assignment | `--local` |
| No API key, need real translations | `--local` |
| Have API key, want best quality | (no flag) |
| Just testing if code works | `--mock` |
| Want to learn how it works | Claude Code agents |

---

## Installation

### Windows Installation

```powershell
# 1. Ensure Python 3.8+ is installed
python --version

# 2. Navigate to project directory
cd Round-Trip-Translator

# 3. Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\activate

# 4. Install required packages
python -m pip install -r requirements.txt

# Or install individually:
python -m pip install sentence-transformers matplotlib pytest anthropic

# 5. Verify installation
python -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

> **Note:** On Windows, use `python -m pip` instead of just `pip` if you get "'pip' is not recognized" error.

#### Windows Requirements
- Python 3.8 or higher
- pip (Python package manager)
- ~500MB disk space for models (downloaded on first run)

### macOS Installation

```bash
# 1. Ensure Python 3.8+ is installed
python3 --version

# 2. Navigate to project directory
cd Round-Trip-Translator

# 3. Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# 4. Install required packages
pip install sentence-transformers matplotlib pytest anthropic

# 5. Verify installation
python3 -c "from sentence_transformers import SentenceTransformer; print('OK')"

# 6. Make shell script executable (optional)
chmod +x roundtrip_v2.sh
```

#### macOS Requirements
- Python 3.8 or higher (use Homebrew: `brew install python3`)
- pip (included with Python)
- ~500MB disk space for models

### Dependencies

| Package | Purpose | Install Command |
|---------|---------|-----------------|
| sentence-transformers | Embedding generation | `pip install sentence-transformers` |
| matplotlib | Graph generation | `pip install matplotlib` |
| pytest | Unit testing | `pip install pytest` |
| anthropic | Claude API (optional) | `pip install anthropic` |

---

## Project Structure

```
Round-Trip-Translator/
├── README.md                    # This documentation
├── HW3_eng.pdf                  # Assignment specification
├── requirements.txt             # Python dependencies
├── roundtrip_v2.sh              # Shell script for pipeline
│
├── agents/                      # Translation agent definitions
│   ├── en-fr-translator.md     # Agent 1: English → French
│   ├── fr-he-translator.md     # Agent 2: French → Hebrew
│   └── he-en-translator.md     # Agent 3: Hebrew → English
│
├── skills/                      # Agent skill modules
│   ├── en-fr-translator-skills/
│   │   ├── subjunctive_mastery.md
│   │   ├── partitive_article_usage.md
│   │   └── natural_phrasing_preservation.md
│   ├── fr-he-translator-skills/
│   │   ├── gender_transformation.md
│   │   ├── binyan_selection.md
│   │   └── article_system_conversion.md
│   └── he-en-translator-skills/
│       ├── word_order_conversion.md
│       └── gender_pronoun_mapping.md
│
├── .claude/                     # Claude Code integration
│   └── commands/               # Slash commands for Claude Code
│       │
│       │ # Build & Test Agents
│       ├── setup-project.md    # /setup-project - Install dependencies
│       ├── run-tests.md        # /run-tests - Run all unit tests
│       ├── run-full-experiment.md  # /run-full-experiment - Run experiment
│       ├── verify-results.md   # /verify-results - Check requirements
│       ├── build-and-test-all.md   # /build-and-test-all - Full workflow
│       │
│       │ # Translation Agents
│       ├── agent-en-fr.md      # /agent-en-fr - English to French
│       ├── agent-fr-he.md      # /agent-fr-he - French to Hebrew
│       ├── agent-he-en.md      # /agent-he-en - Hebrew to English
│       └── run-pipeline.md     # /run-pipeline - Full translation pipeline
│
├── scripts/                     # Python scripts
│   ├── run_experiment.py       # Main experiment runner
│   ├── agent_runner.py         # CLI agent runner (Claude API)
│   ├── spelling_error_injector.py  # Spelling error injection
│   └── embedding_similarity_local.py  # Vector similarity
│
└── tests/                       # Unit tests
    ├── conftest.py             # Pytest configuration
    ├── test_spelling_error_injector.py
    ├── test_embedding_similarity.py
    └── test_experiment_runner.py
```

---

## Implementation 1: Python Scripts

This implementation runs the experiment automatically using Python scripts.

### Full Experiment (with Claude API)

```bash
# Set your API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Run the experiment
python scripts/run_experiment.py
```

### Mock Mode (No API Key Required)

```bash
# Run with mock translations
python scripts/run_experiment.py --mock
```

### View Test Sentences Only

```bash
python scripts/run_experiment.py --sentences-only
```

### Custom Text Input

```bash
# Test with your own text
python scripts/run_experiment.py --mock --text "Your custom sentence here with many words to test"
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `--local` | Use local MarianMT models (real translations, no API) |
| `--mock` | Use mock translations (fake, for testing only) |
| `--text "TEXT"` | Use custom text instead of default sentences |
| `--sentences-only` | Display test sentences without running experiment |
| `--api-key KEY` | Provide API key directly |
| `--output-dir DIR` | Specify output directory |

### Using the Agent Runner (Individual Translations)

```bash
# Run full pipeline (EN → FR → HE → EN)
python scripts/agent_runner.py --pipeline --text "Your sentence here"

# Run individual translation agents
python scripts/agent_runner.py --agent en-fr --text "Hello world"
python scripts/agent_runner.py --agent fr-he --text "Bonjour le monde"
python scripts/agent_runner.py --agent he-en --text "שלום עולם"
```

### Claude Code Slash Commands

If using Claude Code CLI, you can invoke agents directly:

```
/translate-en-fr Your English text here
/translate-fr-he Votre texte français ici
/translate-he-en הטקסט העברי שלך כאן
/roundtrip-translate Full pipeline translation
/check-quality Compare original and translated text
```

### Output Files

After running, the script generates:
- `experiment_results_TIMESTAMP.json` - Full results data
- `spelling_error_graph_TIMESTAMP.png` - Visualization graph

---

## Implementation 2: Claude Code Agents

This implementation uses Claude Code slash commands for interactive translation. **No API key required** - it uses Claude Code directly.

### Available Slash Commands

#### Build & Test Agents
| Command | Description |
|---------|-------------|
| `/setup-project` | Install dependencies and verify setup |
| `/run-tests` | Run all 75 unit tests |
| `/run-full-experiment` | Run the complete experiment |
| `/verify-results` | Verify results meet assignment requirements |
| `/build-and-test-all` | Run entire workflow (setup → test → experiment → verify) |

#### Translation Agents
| Command | Description |
|---------|-------------|
| `/agent-en-fr [text]` | Translate English to French |
| `/agent-fr-he [text]` | Translate French to Hebrew |
| `/agent-he-en [text]` | Translate Hebrew to English |
| `/run-pipeline [text]` | Run full pipeline (EN → FR → HE → EN) |

### Single Translation Example

```bash
# In Claude Code CLI:
/agent-en-fr The beautiful sunset paints the sky with amazing golden colors
```

Output:
```
FRENCH: Le magnifique coucher de soleil peint le ciel avec d'incroyables couleurs dorées
```

### Full Pipeline Example

```bash
/run-pipeline The magnificent golden sunset painted the entire western sky with beautiful colors
```

Output:
```
=== ROUND-TRIP TRANSLATION RESULTS ===

ORIGINAL INPUT:
The magnificent golden sunset painted the entire western sky with beautiful colors

STEP 1 - English to French:
Le magnifique coucher de soleil doré a peint tout le ciel occidental avec de belles couleurs

STEP 2 - French to Hebrew:
השקיעה המוזהבת המרהיבה צבעה את כל השמיים המערביים בצבעים יפים

STEP 3 - Hebrew to English:
The magnificent golden sunset painted all the western skies in beautiful colors

=== END RESULTS ===
```

### Running the Full Experiment

```bash
/run-experiment
```

This will:
1. Take the test sentences
2. Inject spelling errors at 0%, 10%, 25%, 50%
3. Run each through the translation pipeline
4. Calculate vector distances
5. Display results table

### When to Use Each Implementation

| Use Case | Recommended |
|----------|-------------|
| **Assignment submission** | Python Scripts (`--local`) |
| No API key, real translations | Python Scripts (`--local`) |
| Fast pipeline testing | Python Scripts (`--mock`) |
| Best quality translations | Python Scripts (with API key) |
| Interactive exploration | Claude Code Agents |
| Learning how agents work | Claude Code Agents |

---

## Test Sentences

The experiment uses these test sentences (15+ words each, as required):

### Sentence 1 (20 words)
```
The magnificent golden sunset painted the entire western sky with
beautiful shades of orange, pink, and deep purple colors.
```

### Sentence 2 (18 words)
```
Every morning the dedicated young student walks through the peaceful
park to reach her university campus on time.
```

### Misspelled Versions

The spelling error injector creates variants at different error rates:

| Error Rate | Example (Sentence 1) |
|------------|---------------------|
| 0% | Original (no changes) |
| 10% | ~2 words modified |
| 25% | ~5 words modified |
| 50% | ~10 words modified |

---

## Agent Definitions

### Agent 1: English → French (`en-fr-translator.md`)

**Core Competencies:**
1. **Subjunctive Mastery** - French subjunctive mood usage
2. **Partitive Articles** - du/de la/de l'/des usage
3. **Natural Phrasing** - Avoiding literal translations

**Key Skills:**
- `subjunctive_mastery.md`
- `partitive_article_usage.md`
- `natural_phrasing_preservation.md`

### Agent 2: French → Hebrew (`fr-he-translator.md`)

**Core Competencies:**
1. **Gender Transformation** - Independent Hebrew gender lookup
2. **Binyan Selection** - 7 Hebrew verb patterns
3. **Article Conversion** - French articles to Hebrew system

**Key Skills:**
- `gender_transformation.md`
- `binyan_selection.md`
- `article_system_conversion.md`

### Agent 3: Hebrew → English (`he-en-translator.md`)

**Core Competencies:**
1. **Word Order Conversion** - VSO to SVO transformation
2. **Gender-Pronoun Mapping** - Hebrew gender to English pronouns
3. **Nikud Resolution** - Vowel ambiguity handling

**Key Skills:**
- `word_order_conversion.md`
- `gender_pronoun_mapping.md`

---

## Running Tests

### Run All Tests

```bash
python -m pytest tests/ -v
```

### Run Specific Test File

```bash
python -m pytest tests/test_spelling_error_injector.py -v
python -m pytest tests/test_embedding_similarity.py -v
python -m pytest tests/test_experiment_runner.py -v
```

### Run Tests with Coverage

```bash
python -m pip install pytest-cov
python -m pytest tests/ --cov=scripts --cov-report=html
```

### Test Categories

| Test File | Tests |
|-----------|-------|
| `test_spelling_error_injector.py` | Error injection, rates, reproducibility |
| `test_embedding_similarity.py` | Embeddings, similarity scores, thresholds |
| `test_experiment_runner.py` | Pipeline, experiment flow, results |

---

## Assignment Deliverables

### 1. Sentences Used (with misspellings)

See [Test Sentences](#test-sentences) section above.

### 2. Sentence Lengths

| Sentence | Word Count |
|----------|------------|
| Sentence 1 | 20 words |
| Sentence 2 | 18 words |

### 3. Agent Definitions/Skills

See [Agent Definitions](#agent-definitions) section above.

Full agent files in `agents/` directory:
- `en-fr-translator.md` (English → French)
- `fr-he-translator.md` (French → Hebrew)
- `he-en-translator.md` (Hebrew → English)

### 4. Graph

Generated by running:
```bash
python scripts/run_experiment.py --mock
```

Output: `spelling_error_graph_TIMESTAMP.png`

- **X-axis:** Spelling error percentage (0% - 50%)
- **Y-axis:** Vector distance between original and final sentences

### 5. Python Code

All Python code is in the `scripts/` directory:
- `run_experiment.py` - Main experiment runner
- `spelling_error_injector.py` - Spelling error injection (also runnable standalone)
- `embedding_similarity_local.py` - Embedding and similarity

#### Standalone Scripts

```bash
# Test spelling error injection with custom text
python scripts/spelling_error_injector.py "Your text here to test spelling errors"

# Run with default demo text
python scripts/spelling_error_injector.py
```

---

## Troubleshooting

### Common Issues

#### "'pip' is not recognized" (Windows)
```bash
# Use python -m pip instead of pip
python -m pip install -r requirements.txt
```

#### "sentence-transformers not installed"
```bash
python -m pip install sentence-transformers
```

#### "matplotlib not installed"
```bash
python -m pip install matplotlib
```

#### "ANTHROPIC_API_KEY not set"
```bash
# Option 1: Set environment variable
export ANTHROPIC_API_KEY="your-key"

# Option 2: Use mock mode (no API needed)
python scripts/run_experiment.py --mock
```

#### Model download slow
The first run downloads the embedding model (~90MB). This is normal and only happens once.

#### Windows: "python3 not found"
Use `python` instead of `python3` on Windows:
```powershell
python scripts/run_experiment.py --mock
```

#### macOS: Permission denied on shell script
```bash
chmod +x roundtrip_v2.sh
```

### Performance

| Operation | Time |
|-----------|------|
| Model loading | 5-10 seconds (first run) |
| Single embedding | 0.1-0.5 seconds |
| Full experiment (mock) | 30-60 seconds |
| Full experiment (API) | 2-5 minutes |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT PROCESSING                          │
│  Original English → Spelling Error Injection (0-50%)        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  TRANSLATION PIPELINE                        │
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Agent 1 │───▶│  Agent 2 │───▶│  Agent 3 │              │
│  │  EN→FR   │    │  FR→HE   │    │  HE→EN   │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  QUALITY MEASUREMENT                         │
│                                                              │
│  Original English ──┐                                        │
│                     ├──▶ Vector Embeddings ──▶ Cosine       │
│  Final English ─────┘                          Similarity   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    VISUALIZATION                             │
│  Graph: Spelling Error % vs Vector Distance                 │
└─────────────────────────────────────────────────────────────┘
```

---

## License

This project is for educational purposes as part of HW3 assignment.

---

## Support

For issues or questions, check the [Troubleshooting](#troubleshooting) section above.
