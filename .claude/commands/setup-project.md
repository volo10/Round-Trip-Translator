# Setup Project Agent

You are the Setup Agent. Your job is to install all dependencies and verify the project is ready to run.

## Tasks

Execute these steps in order:

### Step 1: Check Python Version
```bash
python --version
```
Verify Python 3.8+ is installed.

### Step 2: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

This installs:
- `sentence-transformers` - For embeddings
- `transformers` - For local translation models
- `sentencepiece` - For tokenization
- `matplotlib` - For graphs
- `pytest` - For testing

### Step 3: Verify Installations
```bash
python -c "from sentence_transformers import SentenceTransformer; print('sentence-transformers: OK')"
python -c "from transformers import MarianMTModel; print('transformers: OK')"
python -c "import matplotlib; print('matplotlib: OK')"
python -c "import pytest; print('pytest: OK')"
```

### Step 4: Check Project Structure
Verify these files exist:
- `scripts/run_experiment.py`
- `scripts/local_translation_agents.py`
- `scripts/spelling_error_injector.py`
- `scripts/embedding_similarity_local.py`
- `agents/en-fr-translator.md`
- `agents/fr-he-translator.md`
- `agents/he-en-translator.md`

## Output Format

Report status:
```
=== PROJECT SETUP STATUS ===

Python Version: [version]
Dependencies: [INSTALLED / FAILED]
Project Files: [OK / MISSING: list]

Status: [READY / NOT READY]

Next step: [command to run]
```
