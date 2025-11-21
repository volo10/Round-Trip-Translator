# TRANSLATOR_V2 Documentation Index

**Version:** 2.0 | **Last Updated:** November 21, 2025

## Welcome to TRANSLATOR_V2!

This is your complete documentation hub for the professional translation pipeline. Choose the document that matches your need below.

---

## Quick Navigation

### 👤 First Time User?

**Start here:** [`README.md`](README.md)

Covers:
- Project overview and innovations
- Quick start guide
- Installation instructions
- Feature highlights
- Basic usage examples
- Quality assurance approach

**Time to read:** 15-20 minutes

### ⚡ Need Quick Commands?

**Go here:** [`QUICK_REFERENCE.md`](QUICK_REFERENCE.md)

Contains:
- One-time setup commands
- Common usage patterns
- Example sentences
- Troubleshooting quick fixes
- Similarity score interpretation
- Keyboard shortcuts & aliases

**Time to read:** 5 minutes

### 🎯 Developing Translations?

**Read this:** [`AGENTS.md`](AGENTS.md)

Details:
- Complete agent competencies
- Translation rules and patterns
- Natural phrasing guidelines
- Linguistic explanations
- Common pitfalls and solutions
- Advanced translation topics

**Time to read:** 30-40 minutes

### 🔧 Integrating or Scripting?

**Check this:** [`SCRIPTS.md`](SCRIPTS.md)

Explains:
- roundtrip_v2.sh usage and options
- embedding_similarity_local.py documentation
- Output formats and interpretation
- Performance characteristics
- Advanced usage patterns
- Integration examples

**Time to read:** 20-30 minutes

---

## Document Overview

| Document | Size | Focus | Best For |
|----------|------|-------|----------|
| **README.md** | 741 lines | Overview & setup | Getting started |
| **AGENTS.md** | 806 lines | Linguistic details | Understanding translation |
| **SCRIPTS.md** | 696 lines | Implementation | Integration & scripting |
| **QUICK_REFERENCE.md** | 434 lines | Command reference | Daily usage |
| **INDEX.md** | This file | Navigation | Finding what you need |

**Total Documentation:** 2,677 lines of comprehensive guidance

---

## By Use Case

### Use Case: "I want to translate something"

1. Read: [README.md - Quick Start](README.md#quick-start) (5 min)
2. Run: [QUICK_REFERENCE.md - Quick Commands](QUICK_REFERENCE.md#quick-commands) (1 min)
3. Check quality: [QUICK_REFERENCE.md - Similarity Score Reference](QUICK_REFERENCE.md#similarity-score-reference) (2 min)

**Total time:** 8 minutes

### Use Case: "Something isn't working"

1. Check: [QUICK_REFERENCE.md - Troubleshooting](QUICK_REFERENCE.md#troubleshooting-quick-fixes) (3 min)
2. If not resolved, read: [SCRIPTS.md - Troubleshooting](SCRIPTS.md#troubleshooting) (10 min)
3. If still stuck, review: [README.md - Troubleshooting](README.md#troubleshooting) (10 min)

**Total time:** 10-20 minutes

### Use Case: "I need to understand how translations work"

1. Read: [README.md - Architecture](README.md#architecture) (10 min)
2. Study: [AGENTS.md - Complete Document](AGENTS.md) (40 min)
3. Reference: [QUICK_REFERENCE.md - Key Concepts](QUICK_REFERENCE.md#key-concepts-at-a-glance) (5 min)

**Total time:** 55 minutes

### Use Case: "I want to integrate this into my application"

1. Learn: [SCRIPTS.md - Overview](SCRIPTS.md#overview) (10 min)
2. Study: [SCRIPTS.md - embedding_similarity_local.py](SCRIPTS.md#embedding_similarity_localpy) (15 min)
3. Review: [SCRIPTS.md - Advanced Usage](SCRIPTS.md#advanced-usage) (15 min)
4. Check: [QUICK_REFERENCE.md - Aliases](QUICK_REFERENCE.md#keyboard-shortcuts--aliases) (5 min)

**Total time:** 45 minutes

### Use Case: "I want to improve translation quality"

1. Understand: [AGENTS.md - Core Competencies](AGENTS.md#core-competencies) (30 min)
2. Learn: [AGENTS.md - Natural Phrasing Rules](AGENTS.md#natural-phrasing-rules) (20 min)
3. Reference: [README.md - Quality Assurance](README.md#quality-assurance) (10 min)
4. Interpret: [QUICK_REFERENCE.md - Similarity Scores](QUICK_REFERENCE.md#similarity-score-reference) (3 min)

**Total time:** 63 minutes

---

## Search Guide

### Looking for specific topics?

**Agents and Translation:**
- Agent overview → [README.md - Agents](README.md#agents)
- English to Spanish rules → [AGENTS.md - English to Spanish Agent](AGENTS.md#english-to-spanish-agent)
- Spanish to Hebrew rules → [AGENTS.md - Spanish to Hebrew Agent](AGENTS.md#spanish-to-hebrew-agent)
- Hebrew to English rules → [AGENTS.md - Hebrew to English Agent](AGENTS.md#hebrew-to-english-agent)

**Scripts and Tools:**
- roundtrip_v2.sh → [SCRIPTS.md - roundtrip_v2.sh](SCRIPTS.md#roundtrip_v2sh)
- embedding_similarity_local.py → [SCRIPTS.md - embedding_similarity_local.py](SCRIPTS.md#embedding_similarity_localpy)
- Batch processing → [SCRIPTS.md - Advanced Usage](SCRIPTS.md#advanced-usage)

**Installation and Setup:**
- One-time setup → [README.md - Quick Start](README.md#quick-start)
- Installation details → [SCRIPTS.md - Installation](SCRIPTS.md#installation)
- Quick setup → [QUICK_REFERENCE.md - Installation](QUICK_REFERENCE.md#installation-one-time-setup)

**Quality and Testing:**
- Validation criteria → [README.md - Quality Assurance](README.md#quality-assurance)
- Similarity interpretation → [SCRIPTS.md - Output Interpretation](SCRIPTS.md#output-interpretation)
- Quality scoring → [QUICK_REFERENCE.md - Similarity Score Reference](QUICK_REFERENCE.md#similarity-score-reference)

**Troubleshooting:**
- General issues → [README.md - Troubleshooting](README.md#troubleshooting)
- Script issues → [SCRIPTS.md - Troubleshooting](SCRIPTS.md#troubleshooting)
- Quick fixes → [QUICK_REFERENCE.md - Troubleshooting](QUICK_REFERENCE.md#troubleshooting-quick-fixes)

---

## Project Structure Reference

```
TRANSLATOR_V2/
├── INDEX.md ...................... You are here
├── README.md ...................... Main documentation
├── AGENTS.md ...................... Agent competencies
├── SCRIPTS.md ..................... Script reference
├── QUICK_REFERENCE.md ............. Quick lookups
│
├── agents/ ........................ Translation agents
│   ├── en-es-translator.md ....... English→Spanish
│   ├── es-he-translator.md ....... Spanish→Hebrew
│   └── he-en-translator.md ....... Hebrew→English
│
├── scripts/ ....................... Tools and utilities
│   ├── embedding_similarity_local.py ... Quality checker
│   └── embedding_similarity_*.json ..... Results (auto)
│
└── roundtrip_v2.sh ................ Main translation script
```

---

## Common Questions

### Q: Where should I start?

**A:** Read [README.md](README.md) first (20 minutes). It provides the foundation.

### Q: How do I run a translation?

**A:** Use the command in [QUICK_REFERENCE.md - Quick Commands](QUICK_REFERENCE.md#quick-commands).

### Q: Why is my translation quality low?

**A:** Check:
1. [QUICK_REFERENCE.md - Similarity Scores](QUICK_REFERENCE.md#similarity-score-reference)
2. [AGENTS.md - Natural Phrasing Rules](AGENTS.md#natural-phrasing-rules)
3. [README.md - Quality Assurance](README.md#quality-assurance)

### Q: How do I integrate this into my app?

**A:** Read [SCRIPTS.md - Advanced Usage](SCRIPTS.md#advanced-usage).

### Q: What if something breaks?

**A:** Follow [QUICK_REFERENCE.md - Troubleshooting](QUICK_REFERENCE.md#troubleshooting-quick-fixes).

### Q: How can I improve translations?

**A:** Study [AGENTS.md - Core Competencies](AGENTS.md#core-competencies).

### Q: What does the similarity score mean?

**A:** See [QUICK_REFERENCE.md - Similarity Score Reference](QUICK_REFERENCE.md#similarity-score-reference).

---

## Reading Paths by Experience Level

### Path 1: Beginner (First-time users)

1. INDEX.md (this file) - 5 min
2. README.md - 20 min
3. QUICK_REFERENCE.md - 10 min
4. Try first translation - 5 min
5. SCRIPTS.md - 20 min (if needed)

**Total:** 60 minutes to full competency

### Path 2: Intermediate (Some experience)

1. QUICK_REFERENCE.md - 10 min
2. AGENTS.md (relevant sections) - 20 min
3. SCRIPTS.md (relevant sections) - 15 min
4. Experimental usage - 15 min

**Total:** 60 minutes for specific needs

### Path 3: Advanced (Integration/customization)

1. QUICK_REFERENCE.md - 5 min (review)
2. SCRIPTS.md (all sections) - 30 min
3. AGENTS.md (advanced topics) - 20 min
4. README.md - Architecture - 10 min

**Total:** 65 minutes for deep understanding

---

## Key Definitions

### Round-Trip Translation
Translation through multiple languages and back to the original (English → Spanish → Hebrew → English). Tests semantic preservation.

### Semantic Similarity
Numerical measure (0-1) of how similar two sentences are in meaning. Used to validate translation quality.

### Natural Phrasing Preservation
Technique to prevent awkward literal translations by applying language-specific rules at each translation stage.

### Binyan System
Hebrew verb conjugation patterns (7 different patterns). Critical for Spanish→Hebrew translation.

### YAML Frontmatter
Structured metadata format at top of agent files (---\ndescription: ...\n---). Makes agents compliant with Claude Code.

---

## Quick Reference Tables

### Similarity Score Scale

| Score | Level | Status |
|-------|-------|--------|
| ≥0.95 | EXCELLENT | Perfect |
| 0.85-0.94 | GOOD | Acceptable |
| 0.75-0.84 | ACCEPTABLE | Minor drift |
| <0.75 | POOR | Needs review |

### Documentation by Format

| Format | Size | Content Type |
|--------|------|--------------|
| README.md | 741 lines | Prose + examples |
| AGENTS.md | 806 lines | Technical + tables |
| SCRIPTS.md | 696 lines | Reference + code |
| QUICK_REFERENCE.md | 434 lines | Condensed reference |

### File Locations

```
Main scripts:
  /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/roundtrip_v2.sh
  /Users/bvolovelsky/Desktop/LLM/TRANSLATOR_V2/scripts/embedding_similarity_local.py

Original (v1):
  /Users/bvolovelsky/Desktop/LLM/TRANSLATOR/roundtrip_with_agents.sh
  /Users/bvolovelsky/Desktop/LLM/TRANSLATOR/embedding_similarity_local.py
```

---

## Related Resources

### Original TRANSLATOR Project
Location: `/Users/bvolovelsky/Desktop/LLM/TRANSLATOR/`
Purpose: Original agent-based system (v1)
Status: Maintained for reference

### External Documentation
- [Claude Code Agents](https://docs.claude.com/en/docs/claude-code/)
- [sentence-transformers](https://www.sbert.net/)
- [Semantic Similarity](https://en.wikipedia.org/wiki/Semantic_similarity)

---

## Version History

### v2.0 (Current)
- YAML frontmatter agents
- Concise agent design
- Embedded competencies
- Local embedding checker
- Comprehensive documentation
- Better error handling

**Release Date:** November 21, 2025

### v1.0 (Original)
- Verbose agent documentation
- External skill files
- Non-standard format
- OpenAI API dependency

**Status:** Superseded by v2.0

---

## Documentation Status

| Document | Status | Completeness | Last Review |
|----------|--------|--------------|-------------|
| README.md | ✓ Complete | 100% | Nov 21, 2025 |
| AGENTS.md | ✓ Complete | 100% | Nov 21, 2025 |
| SCRIPTS.md | ✓ Complete | 100% | Nov 21, 2025 |
| QUICK_REFERENCE.md | ✓ Complete | 100% | Nov 21, 2025 |
| INDEX.md | ✓ Complete | 100% | Nov 21, 2025 |

**Total Documentation:** 2,777 lines | **Coverage:** 100%

---

## Getting Help

### If you're stuck:

1. **Quick fix needed?**
   → [QUICK_REFERENCE.md - Troubleshooting](QUICK_REFERENCE.md#troubleshooting-quick-fixes)

2. **Don't understand something?**
   → [INDEX.md - Search Guide](#search-guide) (find the topic)

3. **Need implementation help?**
   → [SCRIPTS.md - Advanced Usage](SCRIPTS.md#advanced-usage)

4. **Translation rules question?**
   → [AGENTS.md - Natural Phrasing Rules](AGENTS.md#natural-phrasing-rules)

---

## Feedback and Updates

**Documentation Version:** 2.0
**Created:** November 21, 2025
**Last Updated:** November 21, 2025
**Next Review:** December 21, 2025

For improvements to this documentation, consider:
- Adding examples you find helpful
- Clarifying confusing sections
- Reporting broken references
- Suggesting additional topics

---

## Let's Get Started! 🚀

### First-time user?

→ Start with [README.md](README.md)

### Need to translate something?

→ Go to [QUICK_REFERENCE.md - Quick Commands](QUICK_REFERENCE.md#quick-commands)

### Something not working?

→ Check [QUICK_REFERENCE.md - Troubleshooting](QUICK_REFERENCE.md#troubleshooting-quick-fixes)

### Want to understand everything?

→ Read all documents in this order:
1. README.md
2. AGENTS.md
3. SCRIPTS.md
4. QUICK_REFERENCE.md

---

**Welcome to TRANSLATOR_V2!**

Your complete multilingual translation pipeline with semantic quality validation.

