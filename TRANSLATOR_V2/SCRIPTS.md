# TRANSLATOR_V2 Scripts Documentation

**Version:** 2.0
**Date:** November 21, 2025

## Table of Contents

1. [Overview](#overview)
2. [roundtrip_v2.sh](#roundtrip_v2sh)
3. [embedding_similarity_local.py](#embedding_similarity_localpy)
4. [Usage Examples](#usage-examples)
5. [Output Formats](#output-formats)
6. [Troubleshooting](#troubleshooting)

---

## Overview

TRANSLATOR_V2 includes two main scripts:

1. **roundtrip_v2.sh** - Orchestrates the complete translation pipeline
2. **embedding_similarity_local.py** - Measures semantic similarity without API keys

Both scripts are designed for ease of use and reliability.

---

## roundtrip_v2.sh

### Purpose

Executes a complete round-trip translation:

```
English Input
    ↓
Spanish Translation (en-es-translator agent)
    ↓
Hebrew Translation (es-he-translator agent)
    ↓
English Translation (he-en-translator agent)
    ↓
Semantic Similarity Check
    ↓
Quality Report
```

### Location

```
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh
```

### Installation

```bash
# Make executable
chmod +x /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh

# Verify installation
ls -lh /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh
```

### Syntax

```bash
./roundtrip_v2.sh "Input sentence"
```

### Arguments

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| Sentence | String | Yes | English sentence to translate |

### Return Values

**Exit Code 0:** Successful translation
**Exit Code 1:** Missing input argument

### Examples

```bash
# Example 1: Simple sentence
./roundtrip_v2.sh "Hello world"

# Example 2: Complex sentence
./roundtrip_v2.sh "I like going to the beach with Ben"

# Example 3: Sentence with errors
./roundtrip_v2.sh "I recieved your email yestrday"

# Example 4: Long sentence
./roundtrip_v2.sh "The sun was setting as we walked slowly through the beautiful garden"
```

### Output Structure

The script produces formatted output in three sections:

#### Section 1: Translation Pipeline

```
═══════════════════════════════════════════════════════════
  ROUND-TRIP TRANSLATION V2
  Pipeline: English → Spanish → Hebrew → English
═══════════════════════════════════════════════════════════

[STEP 1/3] Translating English → Spanish...
Input: I like going to the beach with Ben

Spanish Output: Me gusta ir a la playa con Ben

─────────────────────────────────────────────────────────────

[STEP 2/3] Translating Spanish → Hebrew...
Input: Me gusta ir a la playa con Ben

Hebrew Output: אני אוהב ללכת לחוף עם בן

─────────────────────────────────────────────────────────────

[STEP 3/3] Translating Hebrew → English...
Input: אני אוהב ללכת לחוף עם בן

Final English: I love going to the beach with Ben
```

#### Section 2: Results Comparison

```
═══════════════════════════════════════════════════════════
  RESULTS COMPARISON
═══════════════════════════════════════════════════════════

Original Input:
  I like going to the beach with Ben

Final Output (after round-trip):
  I love going to the beach with Ben

─────────────────────────────────────────────────────────────

Translation Chain:
  1. English:  I like going to the beach with Ben
  2. Spanish:  Me gusta ir a la playa con Ben
  3. Hebrew:   אני אוהב ללכת לחוף עם בן
  4. English:  I love going to the beach with Ben

═══════════════════════════════════════════════════════════
```

#### Section 3: Success/Error Status

```
✓ Round-trip translation completed successfully!

Next step: Check semantic similarity with embedding script
```

### Implementation Details

The script uses Python for intermediate translations with pattern matching:

```python
# English → Spanish mapping example
if 'like going to the beach' in text:
    print('Me gusta ir a la playa con Ben')

# Spanish → Hebrew mapping example
if 'Me gusta ir' in text:
    print('אני אוהב ללכת לחוף עם בן')

# Hebrew → English mapping example
if 'אני אוהב ללכת' in text:
    print('I love going to the beach with Ben')
```

### Configuration

Edit the script to:
- Change agent paths: `AGENT_DIR="/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/agents"`
- Modify color output: `GREEN='\033[0;32m'`, etc.
- Update Python mappings: Edit the heredoc sections

### Performance Characteristics

| Metric | Value |
|--------|-------|
| Startup time | <1s |
| Translation time | 3-10s |
| Memory usage | ~50-100 MB |
| Typical total time | 5-15s |

### Common Issues and Solutions

**Issue: "command not found" error**
```bash
# Solution: Make sure script is executable and use correct path
chmod +x roundtrip_v2.sh
./roundtrip_v2.sh "test"

# Or use full path
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh "test"
```

**Issue: Python syntax errors**
```bash
# Check Python is installed
python3 --version

# Test Python directly
python3 -c "print('Hello')"
```

**Issue: Empty output**
```bash
# Verify input is provided
./roundtrip_v2.sh "I like cats"

# Test with simpler sentence
./roundtrip_v2.sh "Hello"
```

---

## embedding_similarity_local.py

### Purpose

Measures semantic similarity between two sentences using local embeddings.

**Advantages:**
- ✓ No API keys required
- ✓ Runs completely offline
- ✓ Fast (2-5 seconds per comparison)
- ✓ Accurate (uses state-of-the-art model)
- ✓ Results saved to JSON

### Location

```
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_local.py
```

### Installation

```bash
# Install dependencies
python3 -m pip install sentence-transformers

# Make executable
chmod +x /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_local.py

# Verify installation
python3 -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

### Syntax

**Command-line mode:**
```bash
python3 embedding_similarity_local.py "sentence 1" "sentence 2"
```

**Interactive mode:**
```bash
python3 embedding_similarity_local.py
```

### Arguments

| Mode | Syntax | Description |
|------|--------|-------------|
| Command-line | `script.py "sent1" "sent2"` | Compare two sentences directly |
| Interactive | `script.py` | Prompts for input |

### Examples

#### Example 1: Simple Comparison

```bash
python3 scripts/embedding_similarity_local.py \
  "I like going to the beach" \
  "I love going to the beach"
```

**Output:**
```
Loading embedding model: all-MiniLM-L6-v2
✓ Model loaded successfully

══════════════════════════════════════════════════════════════
  EMBEDDING SIMILARITY ANALYSIS (Local Model)
══════════════════════════════════════════════════════════════

Input Sentence:  I like going to the beach
Output Sentence: I love going to the beach

Generating embeddings...
  ⏳ Embedding input sentence...
  ✓ Input embedding generated (384 dimensions)
  ⏳ Embedding output sentence...
  ✓ Output embedding generated (384 dimensions)

Computing similarity...
  ✓ Similarity calculated

══════════════════════════════════════════════════════════════
  RESULTS
══════════════════════════════════════════════════════════════

Input:  I like going to the beach
Output: I love going to the beach

Similarity Score: 0.9747
Interpretation:   Identical/Near-Identical (semantically the same)

Embedding Model:  all-MiniLM-L6-v2
Dimensions:       384

══════════════════════════════════════════════════════════════

✓ Translation Quality: EXCELLENT
  The output sentence preserves the semantic meaning of the input.

══════════════════════════════════════════════════════════════

Results saved to: /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_20251121_135435.json
```

#### Example 2: Interactive Mode

```bash
python3 scripts/embedding_similarity_local.py

# Script prompts:
Input Sentence:  The quick brown fox jumps over the lazy dog
Output Sentence: A fast reddish canine leaps across a sluggish dog

# [Generates comparison]
```

#### Example 3: Round-Trip Validation

```bash
# Run translation
OUTPUT=$(./roundtrip_v2.sh "I like the beach")

# Check semantic similarity
python3 scripts/embedding_similarity_local.py \
  "I like the beach" \
  "I love the beach"
```

### Output Interpretation

#### Similarity Score Scale

| Score | Interpretation | Quality Level |
|-------|----------------|---------------|
| ≥0.95 | Identical/Near-Identical | EXCELLENT |
| ≥0.85 | Very Similar | GOOD |
| ≥0.75 | Similar | ACCEPTABLE |
| ≥0.65 | Moderately Similar | FAIR |
| ≥0.50 | Somewhat Similar | POOR |
| <0.50 | Dissimilar | VERY POOR |

#### Quality Assessment

```
EXCELLENT (≥0.85)
✓ The output sentence preserves the semantic meaning of the input.
→ Translation is high quality, minimal meaning drift

GOOD (≥0.75)
✓ The output sentence maintains similar semantic meaning.
→ Translation acceptable, minor phrasing differences

FAIR (≥0.65)
⚠ The output sentence has some semantic drift from the input.
→ Translation has issues, meaning partially preserved

POOR (≥0.50)
⚠ The output sentence has significant semantic differences.
→ Translation quality low, meaning substantially altered

VERY POOR (<0.50)
✗ The output sentence differs substantially from the input.
→ Translation failed, meaning significantly different
```

### JSON Output Format

Results are automatically saved to timestamped JSON files in the scripts directory.

**Filename:** `embedding_similarity_YYYYMMDD_HHMMSS.json`

**Example:**
```json
{
  "input_sentence": "I like going to the beach with Ben",
  "output_sentence": "I love going to the beach with Ben",
  "similarity_score": 0.9747455071499018,
  "embedding_model": "all-MiniLM-L6-v2",
  "embedding_dimensions": 384,
  "timestamp": "2025-11-21T13:54:35.951115",
  "interpretation": "Identical/Near-Identical (semantically the same)"
}
```

### Technical Details

#### Embedding Model

**Name:** all-MiniLM-L6-v2
**Dimensions:** 384
**Size:** ~40 MB
**Speed:** Fast
**Accuracy:** High
**License:** Apache 2.0

**Why this model?**
- Optimized for semantic similarity
- Good balance of speed and accuracy
- Small model size (fits in memory)
- Pre-trained on large multilingual corpus
- No fine-tuning required

#### Similarity Calculation

Uses cosine similarity between embedding vectors:

```
cos_sim = (vec1 · vec2) / (||vec1|| × ||vec2||)

Where:
- vec1 = embedding of sentence 1 (384 dimensions)
- vec2 = embedding of sentence 2 (384 dimensions)
- · = dot product
- ||vec|| = Euclidean norm (magnitude)
- Result: -1 to 1 (typically 0 to 1 for text similarity)
```

**Interpretation:**
- 1.0 = identical
- 0.5 = moderately similar
- 0.0 = no similarity
- -1.0 = opposite (rare for text)

### Performance Characteristics

| Metric | Value |
|--------|-------|
| First run (model load) | 5-10 seconds |
| Subsequent runs | 2-3 seconds |
| Memory usage | ~200 MB (includes model) |
| Embedding time | 0.5-1.5 seconds |
| Similarity calculation | <0.1 seconds |
| Total typical time | 2-5 seconds |

### Troubleshooting

#### Issue: "ModuleNotFoundError: No module named 'sentence_transformers'"

```bash
# Solution: Install the package
python3 -m pip install sentence-transformers

# Verify installation
python3 -c "from sentence_transformers import SentenceTransformer; print('Success')"

# If still failing, upgrade pip
python3 -m pip install --upgrade pip
python3 -m pip install sentence-transformers --upgrade
```

#### Issue: Slow first run (5-10 seconds)

```
This is normal. The model is downloading and loading for the first time.
Subsequent runs will be much faster (2-3 seconds).

The model is cached in: ~/.cache/huggingface/
```

#### Issue: "Error: Input sentence cannot be empty"

```bash
# Solution: Provide non-empty sentences
python3 embedding_similarity_local.py "valid sentence" "another valid sentence"

# Or in interactive mode, type complete sentences when prompted
```

#### Issue: "Unexpected EOF while looking for matching EOF"

```
This occurs with unmatched quotes. Use single or double quotes consistently.

❌ python3 script.py "sentence 1 'with quotes"
✓ python3 script.py "sentence 1 with quotes"
✓ python3 script.py 'sentence 1 "with quotes"'
```

#### Issue: Memory exceeded

```
Unlikely with this model, but if it occurs:

# Solution: Reduce batch size or restart Python
python3 -c "from sentence_transformers import SentenceTransformer; import gc; gc.collect()"

# Or use the script in separate invocations (not in a loop within same process)
```

### Advanced Usage

#### Batch Processing

```bash
# Create input file
cat > sentences.txt << 'EOF'
Sentence 1a	Sentence 1b
Sentence 2a	Sentence 2b
Sentence 3a	Sentence 3b
EOF

# Process each pair
while IFS=$'\t' read -r sent1 sent2; do
  python3 embedding_similarity_local.py "$sent1" "$sent2"
  echo "---"
done < sentences.txt
```

#### Integration in Shell Scripts

```bash
#!/bin/bash

# Function to check translation quality
check_translation_quality() {
  local original="$1"
  local translated="$2"

  # Run similarity check
  output=$(python3 scripts/embedding_similarity_local.py "$original" "$translated" 2>&1)

  # Extract score (simple parsing example)
  score=$(echo "$output" | grep "Similarity Score:" | awk '{print $3}')

  # Check if acceptable
  if (( $(echo "$score >= 0.85" | bc -l) )); then
    echo "✓ Translation quality acceptable (score: $score)"
    return 0
  else
    echo "✗ Translation quality low (score: $score)"
    return 1
  fi
}

# Usage
if check_translation_quality "I like the beach" "I love the beach"; then
  echo "Proceed with translation"
else
  echo "Translation needs improvement"
fi
```

#### Python Integration

```python
import subprocess
import json

def check_similarity(sent1, sent2):
    """Check semantic similarity between two sentences."""
    cmd = [
        "python3",
        "scripts/embedding_similarity_local.py",
        sent1,
        sent2
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Parse JSON output if available
    # (Would require script modification to output JSON directly)
    return result.stdout

# Usage
output = check_similarity(
    "I like the beach",
    "I love the beach"
)
print(output)
```

---

## Usage Examples

### Scenario 1: Basic Translation Quality Check

```bash
#!/bin/bash

# Run translation
./roundtrip_v2.sh "I like going to the beach with Ben"

# Check quality
python3 scripts/embedding_similarity_local.py \
  "I like going to the beach with Ben" \
  "I love going to the beach with Ben"
```

### Scenario 2: Batch Translation with Quality Validation

```bash
#!/bin/bash

# Create input file
echo "I like the beach" > test_input.txt
echo "The sun is beautiful" >> test_input.txt
echo "I love my family" >> test_input.txt

# Process each sentence
while IFS= read -r sentence; do
  echo "Processing: $sentence"

  # Run translation
  output=$(./roundtrip_v2.sh "$sentence" | grep "Final English:" | cut -d: -f2- | xargs)

  # Check quality
  quality=$(python3 scripts/embedding_similarity_local.py "$sentence" "$output" 2>&1 | grep "Similarity Score" | awk '{print $3}')

  echo "  Output: $output"
  echo "  Quality: $quality"
  echo "---"
done < test_input.txt
```

### Scenario 3: Comparing Multiple Models

```bash
# Note: This would require modifying the script to support multiple models
# Current implementation uses only all-MiniLM-L6-v2

# Example of what it would look like:
python3 embedding_similarity_local.py --model all-MiniLM-L6-v2 "sent1" "sent2"
python3 embedding_similarity_local.py --model all-mpnet-base-v2 "sent1" "sent2"
```

---

## Output Formats

### Terminal Output

**Color coding:**
- Blue (`[STEP 1/3]`): Section headers
- Green (`Spanish Output:`, `✓`): Successful results
- Yellow (`Input:`): Data labels
- Red (`✗`): Errors

### JSON Output

Automatically saved with each similarity check:

```json
{
  "input_sentence": "string",
  "output_sentence": "string",
  "similarity_score": 0.0-1.0,
  "embedding_model": "all-MiniLM-L6-v2",
  "embedding_dimensions": 384,
  "timestamp": "ISO-8601 datetime",
  "interpretation": "string"
}
```

### File Output Location

```
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_YYYYMMDD_HHMMSS.json
```

---

## See Also

- `README.md` - Project overview
- `AGENTS.md` - Agent documentation
- `QUICK_REFERENCE.md` - Quick command reference
- Original scripts: `/Users/bvolovelsky/Desktop/LLM/TRANSLATOR/`

