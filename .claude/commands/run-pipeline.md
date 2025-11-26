# Round-Trip Translation Pipeline

Execute the full translation pipeline: English → French → Hebrew → English

## Input Text
$ARGUMENTS

## Instructions

You must perform THREE sequential translation steps. Execute each step and show all intermediate results.

---

## STEP 1: English → French

Translate the input to French following these rules:
- Use subjunctive for doubt, emotion, desire, necessity
- Apply partitive articles (du/de la/de l'/des)
- Natural phrasing: "I miss you" → "Tu me manques", "I am cold" → "J'ai froid"
- Handle any spelling errors by understanding intended meaning

---

## STEP 2: French → Hebrew

Translate the French result to Hebrew following these rules:
- French gender does NOT transfer - determine Hebrew gender independently
- Select correct binyan based on meaning
- Convert articles: le/la/les → ה prefix
- Tense mapping: passé composé → past, futur → future

---

## STEP 3: Hebrew → English

Translate the Hebrew result to English following these rules:
- Resolve nikud ambiguities using context
- Convert VSO word order to SVO
- Map gender to correct pronouns
- Expand prefixes: ב → "in", ל → "to", מ → "from", ה → "the"
- Produce natural, native-sounding English

---

## Required Output Format

You MUST respond with exactly this format:

```
=== ROUND-TRIP TRANSLATION RESULTS ===

ORIGINAL INPUT:
[the original English text]

STEP 1 - English to French:
[French translation]

STEP 2 - French to Hebrew:
[Hebrew translation]

STEP 3 - Hebrew to English:
[Final English translation]

=== END RESULTS ===
```

Do not include any other text or explanations.
