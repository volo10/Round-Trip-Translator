# Round-Trip Translation Pipeline

You are the master orchestrator for the round-trip translation experiment.

## Your Task

Take the following English text and translate it through the full pipeline:
1. English → French (Agent 1)
2. French → Hebrew (Agent 2)
3. Hebrew → English (Agent 3)

Input text:
$ARGUMENTS

## Execution Steps

### Step 1: English to French
Translate the input to French following en-fr-translator guidelines:
- Use proper subjunctive mood
- Apply partitive articles correctly
- Maintain natural French phrasing

### Step 2: French to Hebrew
Translate the French output to Hebrew following fr-he-translator guidelines:
- Independently determine Hebrew gender
- Select appropriate binyan
- Convert article systems

### Step 3: Hebrew to English
Translate the Hebrew output to English following he-en-translator guidelines:
- Resolve nikud ambiguities
- Convert VSO to SVO word order
- Map gender to pronouns

## Output Format

Provide the output in this format:

```
ORIGINAL: [the original English input]

STEP 1 (EN → FR): [French translation]

STEP 2 (FR → HE): [Hebrew translation]

STEP 3 (HE → EN): [Final English translation]
```
