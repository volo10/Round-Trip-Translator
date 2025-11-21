# TRANSLATOR_V2 Quick Reference Guide

**Version:** 2.0 | **Date:** November 21, 2025

---

## Installation (One-Time Setup)

```bash
# Navigate to TRANSLATOR_V2
cd /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2

# Install Python package
python3 -m pip install sentence-transformers

# Make scripts executable
chmod +x roundtrip_v2.sh
chmod +x scripts/embedding_similarity_local.py

# Verify setup
./roundtrip_v2.sh "test"
```

---

## Quick Commands

### Run Full Round-Trip Translation

```bash
./roundtrip_v2.sh "Your English sentence here"
```

**Output:** English → Spanish → Hebrew → English + Similarity Score

### Check Translation Quality

```bash
python3 scripts/embedding_similarity_local.py "original sentence" "translated sentence"
```

**Output:** Similarity score (0-1) with interpretation

### Interactive Similarity Check

```bash
python3 scripts/embedding_similarity_local.py
# Then enter two sentences when prompted
```

---

## Common Examples

### Example 1: Simple Translation

```bash
./roundtrip_v2.sh "I like the beach"

# Expected output:
# Spanish: Me gusta la playa
# Hebrew: אני אוהב את החוף
# English: I love the beach
# Score: 0.94+ (EXCELLENT)
```

### Example 2: Complex Sentence

```bash
./roundtrip_v2.sh "Why did you think that your plan would work out?"

# Full round-trip with quality assessment
```

### Example 3: Sentence with Errors

```bash
./roundtrip_v2.sh "I recieved your email yestrday"

# Translates misspelled input (error correction built-in)
```

### Example 4: Quality Check Only

```bash
python3 scripts/embedding_similarity_local.py \
  "I like going to the beach" \
  "I love going to the beach"

# Output: Similarity 0.9747 (EXCELLENT)
```

---

## Translation Competencies by Language Pair

### English → Spanish (en-es-translator)

| Feature | Example |
|---------|---------|
| Gustar pattern | "I like" → "Me gusta" |
| Ser vs Estar | "I am happy" → "Estoy feliz" |
| Por vs Para | "for 2 hours" → "por 2 horas" |
| Subjunctive | "I want you to come" → "Quiero que vengas" |

### Spanish → Hebrew (es-he-translator)

| Feature | Example |
|---------|---------|
| Gender transformation | "la casa" → "הבית" |
| Gustar conversion | "Me gusta" → "אני אוהב" |
| Binyan selection | "enseñar" → choose correct verb pattern |
| Article system | "un libro" → "ספר" (no article) |

### Hebrew → English (he-en-translator)

| Feature | Example |
|---------|---------|
| Word order | "הלך הילד" (VSO) → "The boy went" (SVO) |
| Gender mapping | "קראה" (fem) → "She read" |
| Nikud resolution | "קרא" → determine correct reading |
| Prefix expansion | "בבית" → "in the house" |

---

## Similarity Score Reference

| Score | Level | Meaning |
|-------|-------|---------|
| ≥0.95 | EXCELLENT | Identical/near-identical meaning |
| 0.85-0.94 | GOOD | Very similar, acceptable |
| 0.75-0.84 | ACCEPTABLE | Similar, minor drift |
| 0.65-0.74 | FAIR | Moderately similar, some drift |
| 0.50-0.64 | POOR | Somewhat similar, significant drift |
| <0.50 | VERY POOR | Dissimilar, major differences |

**Target:** Aim for ≥0.85 for good translation quality

---

## File Locations

```
TRANSLATOR_V2/
├── README.md                          Main documentation
├── AGENTS.md                          Agent competencies
├── SCRIPTS.md                         Script details
├── QUICK_REFERENCE.md                 This file
├── agents/
│   ├── en-es-translator.md           English→Spanish
│   ├── es-he-translator.md           Spanish→Hebrew
│   └── he-en-translator.md           Hebrew→English
├── scripts/
│   ├── embedding_similarity_local.py  Quality checker
│   └── embedding_similarity_*.json    Results (auto-generated)
└── roundtrip_v2.sh                   Main translation script
```

---

## Troubleshooting Quick Fixes

### "command not found: roundtrip_v2.sh"

```bash
# Use full path
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh "text"

# Or make sure you're in the correct directory
cd /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2
./roundtrip_v2.sh "text"
```

### "ModuleNotFoundError: No module named 'sentence_transformers'"

```bash
python3 -m pip install sentence-transformers --upgrade
```

### Script is slow on first run

```
Normal - the model loads for the first time (~10 seconds)
Subsequent runs are faster (~3 seconds)
```

### Low similarity score (<0.85)

1. Try a simpler sentence to isolate the issue
2. Check intermediate translations (Spanish, Hebrew)
3. Review agent competencies in AGENTS.md

### No output from script

```bash
# Verify Python works
python3 --version

# Test script directly
python3 scripts/embedding_similarity_local.py "hello" "world"
```

---

## Performance Tips

### For Batch Processing

```bash
# Process multiple sentences efficiently
while read sentence; do
  ./roundtrip_v2.sh "$sentence"
done < input.txt > output.txt
```

### For Memory Efficiency

```bash
# Process one at a time (avoid long-running processes)
./roundtrip_v2.sh "sentence 1"
./roundtrip_v2.sh "sentence 2"
./roundtrip_v2.sh "sentence 3"

# NOT in a loop within the same Python process
```

### For Speed

```bash
# First run with embedding loads model (~10s)
python3 scripts/embedding_similarity_local.py "a" "b"

# Subsequent runs are faster (~2s)
python3 scripts/embedding_similarity_local.py "c" "d"
```

---

## Common Use Cases

### Use Case 1: Validate Translation Quality

```bash
# Step 1: Run translation
result=$(./roundtrip_v2.sh "I like the beach" | grep "Final English:" | cut -d: -f2-)

# Step 2: Check quality
python3 scripts/embedding_similarity_local.py "I like the beach" "$result"

# Step 3: Interpret score
# If score ≥0.85 → Translation is good
# If score <0.85 → Translation needs review
```

### Use Case 2: Test Language Coverage

```bash
# Test different domains
./roundtrip_v2.sh "Hello, how are you?"        # Casual
./roundtrip_v2.sh "The meeting is tomorrow."   # Business
./roundtrip_v2.sh "Why does the moon shine?"   # Technical
```

### Use Case 3: Compare Agent Versions

```bash
# Run in TRANSLATOR (original v1)
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR/roundtrip_with_agents.sh "test"

# Run in TRANSLATOR_V2 (new v2)
/Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh "test"

# Compare results and quality scores
```

---

## Keyboard Shortcuts & Aliases

### Create Convenient Aliases

```bash
# Add to ~/.bash_profile or ~/.zshrc
alias translator='~/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh'
alias checker='python3 ~/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_local.py'

# Then use:
translator "Your sentence"
checker "sentence 1" "sentence 2"
```

### Function for Quality Check

```bash
# Add to ~/.bash_profile or ~/.zshrc
translate_and_check() {
  local input="$1"
  echo "Translating: $input"
  local output=$(~/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh "$input" | grep "Final English:" | cut -d: -f2-)
  echo "Output: $output"
  echo "Checking quality..."
  python3 ~/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_local.py "$input" "$output"
}

# Then use:
translate_and_check "Your sentence"
```

---

## Key Concepts at a Glance

### Round-Trip Translation

Translation through multiple languages and back to original:

```
English
  ↓ (en-es-translator)
Spanish
  ↓ (es-he-translator)
Hebrew
  ↓ (he-en-translator)
English
```

**Purpose:** Test semantic preservation across languages

### Semantic Similarity

Measures how similar two sentences are in meaning (0-1 scale):

```
0.95+ = Identical meaning
0.85+ = Good translation
0.75+ = Acceptable translation
<0.75 = Translation issues
```

**Method:** Embedding vectors + cosine similarity

### Natural Phrasing Preservation

Prevents awkward literal translations:

```
❌ "I gusta going" (literal from Spanish)
✓ "I like going" (natural English)

❌ "Very much love I to go beach" (literal from Hebrew)
✓ "I very much love going to the beach" (natural)
```

---

## Document Map

| Document | Purpose | When to Read |
|----------|---------|--------------|
| README.md | Full project overview | First-time setup |
| AGENTS.md | Agent competencies & rules | Need translation details |
| SCRIPTS.md | Script documentation | Troubleshooting/advanced |
| QUICK_REFERENCE.md | This file | Daily quick lookups |

---

## External Resources

### Original TRANSLATOR Project
```
Location: /Users/bvolovelsky/Desktop/LLM/TRANSLATOR/
Purpose: Original agent-based translation system
Note: TRANSLATOR_V2 is improved successor
```

### Required Dependencies
- Python 3.6+
- sentence-transformers (installed via pip)
- Claude Code (for agent system)

### Model Information
- **Embedding Model:** all-MiniLM-L6-v2
- **Dimensions:** 384
- **Size:** ~40 MB
- **License:** Apache 2.0

---

## Version Information

| Component | Version | Status |
|-----------|---------|--------|
| TRANSLATOR_V2 | 2.0 | Production Ready |
| Agents | 2.0 | YAML Format |
| Scripts | 2.0 | Latest |
| Documentation | 2.0 | Complete |

---

## Quick Checklist for New Users

- [ ] Installed sentence-transformers
- [ ] Made scripts executable (chmod +x)
- [ ] Verified setup with `./roundtrip_v2.sh "test"`
- [ ] Read README.md for overview
- [ ] Tested with example sentence
- [ ] Reviewed agent competencies in AGENTS.md
- [ ] Understood similarity score scale

---

## Getting Help

1. **Quick answer?** → Check this QUICK_REFERENCE.md
2. **Script problem?** → See SCRIPTS.md Troubleshooting
3. **Translation issue?** → Review AGENTS.md for competencies
4. **Full overview?** → Start with README.md
5. **Still stuck?** → Check file headers and comments

---

## Last Updated

November 21, 2025

**Next Review:** December 21, 2025 (monthly)

---

**Ready to translate? Run:**
```bash
./roundtrip_v2.sh "Your sentence here"
```

