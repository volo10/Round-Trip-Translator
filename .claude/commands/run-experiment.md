# Translation Experiment Runner

Run the full spelling error vs vector distance experiment using Claude Code agents.

## Instructions

You will run a complete experiment following these steps:

### Step 1: Read the test sentences from the experiment runner
Read the file `scripts/run_experiment.py` to get the TEST_SENTENCES.

### Step 2: For each test sentence, run translations at different error levels

Use the spelling error injector to create variants:
```bash
python scripts/spelling_error_injector.py "SENTENCE"
```

### Step 3: For each variant, run the translation pipeline

For each error level (0%, 10%, 25%, 50%), translate through the pipeline:
1. English (with errors) → French
2. French → Hebrew
3. Hebrew → English

### Step 4: Calculate similarity scores

Use the embedding similarity checker:
```bash
python scripts/embedding_similarity_local.py "original sentence" "final translation"
```

### Step 5: Report results

Present results in this format:

```
=== EXPERIMENT RESULTS ===

SENTENCE 1: [original sentence]
Word Count: [number]

| Error Rate | Final Translation | Similarity | Distance |
|------------|-------------------|------------|----------|
| 0%         | [translation]     | [score]    | [1-score]|
| 10%        | [translation]     | [score]    | [1-score]|
| 25%        | [translation]     | [score]    | [1-score]|
| 50%        | [translation]     | [score]    | [1-score]|

SENTENCE 2: [original sentence]
...

=== SUMMARY ===
Average distance at 0%: [value]
Average distance at 50%: [value]
```

## Execute Now

Begin the experiment with the default test sentences.
