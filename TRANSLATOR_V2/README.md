# TRANSLATOR_V2 - Multi-Agent Translation Pipeline

**Version:** 2.1
**Last Updated:** November 22, 2025
**Status:** Production Ready

## Assignment Overview

This project implements a **Multi-Agent Translation System** with **Vector Distance Analysis** as per the HW3 assignment requirements:

- **Translation Pipeline:** English → French → Hebrew → English
- **Spelling Error Testing:** 0% to 50% error rates
- **Vector Distance Measurement:** Cosine similarity using embeddings
- **Graph Visualization:** Spelling error % vs. vector distance

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
   - [Windows](#windows-installation)
   - [macOS](#macos-installation)
3. [Project Structure](#project-structure)
4. [Running the Experiment](#running-the-experiment)
5. [Test Sentences](#test-sentences)
6. [Agent Definitions](#agent-definitions)
7. [Running Tests](#running-tests)
8. [Assignment Deliverables](#assignment-deliverables)
9. [Troubleshooting](#troubleshooting)

---

## Quick Start

```bash
# 1. Install dependencies
pip install sentence-transformers matplotlib pytest

# 2. Run the experiment (mock mode - no API key needed)
python scripts/run_experiment.py --mock

# 3. Run tests
pytest tests/ -v
```

---

## Installation

### Windows Installation

```powershell
# 1. Ensure Python 3.8+ is installed
python --version

# 2. Navigate to project directory
cd C:\path\to\TRANSLATOR_V2

# 3. Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\activate

# 4. Install required packages
pip install sentence-transformers matplotlib pytest anthropic

# 5. Verify installation
python -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

#### Windows Requirements
- Python 3.8 or higher
- pip (Python package manager)
- ~500MB disk space for models (downloaded on first run)

### macOS Installation

```bash
# 1. Ensure Python 3.8+ is installed
python3 --version

# 2. Navigate to project directory
cd /path/to/TRANSLATOR_V2

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
TRANSLATOR_V2/
├── README.md                    # This documentation
├── HW3_eng.pdf                  # Assignment specification
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
├── scripts/                     # Python scripts
│   ├── run_experiment.py       # Main experiment runner
│   ├── spelling_error_injector.py  # Spelling error injection
│   └── embedding_similarity_local.py  # Vector similarity
│
├── tests/                       # Unit tests
│   ├── conftest.py             # Pytest configuration
│   ├── test_spelling_error_injector.py
│   ├── test_embedding_similarity.py
│   └── test_experiment_runner.py
│
└── roundtrip_v2.sh             # Shell script for pipeline
```

---

## Running the Experiment

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

### Command Line Options

| Option | Description |
|--------|-------------|
| `--mock` | Use mock translations (no API calls) |
| `--sentences-only` | Display test sentences without running experiment |
| `--api-key KEY` | Provide API key directly |
| `--output-dir DIR` | Specify output directory |

### Output Files

After running, the script generates:
- `experiment_results_TIMESTAMP.json` - Full results data
- `spelling_error_graph_TIMESTAMP.png` - Visualization graph

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
# Windows
python -m pytest tests/ -v

# macOS/Linux
pytest tests/ -v
```

### Run Specific Test File

```bash
pytest tests/test_spelling_error_injector.py -v
pytest tests/test_embedding_similarity.py -v
pytest tests/test_experiment_runner.py -v
```

### Run Tests with Coverage

```bash
pip install pytest-cov
pytest tests/ --cov=scripts --cov-report=html
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
- `spelling_error_injector.py` - Spelling error injection
- `embedding_similarity_local.py` - Embedding and similarity

---

## Troubleshooting

### Common Issues

#### "sentence-transformers not installed"
```bash
pip install sentence-transformers
```

#### "matplotlib not installed"
```bash
pip install matplotlib
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
