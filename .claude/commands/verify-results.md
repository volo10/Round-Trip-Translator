# Results Verification Agent

You are the Verification Agent. Your job is to verify the experiment results meet assignment requirements.

## Tasks

### Step 1: Find Latest Results

Look for the most recent files in `scripts/`:
```bash
dir scripts\experiment_results_*.json
dir scripts\spelling_error_graph_*.png
```

### Step 2: Read and Verify Results

Read the latest JSON file and check:

#### Requirement 1: Test Sentences
- [ ] At least 2 sentences used
- [ ] Each sentence has 15+ words
- [ ] Sentences are in English

#### Requirement 2: Spelling Errors
- [ ] Error rates from 0% to 50% tested
- [ ] At least 25% error rate included
- [ ] Misspelled versions recorded

#### Requirement 3: Translation Pipeline
- [ ] English → French translations recorded
- [ ] French → Hebrew translations recorded
- [ ] Hebrew → English translations recorded

#### Requirement 4: Vector Distance
- [ ] Similarity scores calculated
- [ ] Distance = 1 - similarity
- [ ] Values between 0 and 1

#### Requirement 5: Graph
- [ ] Graph file exists
- [ ] X-axis: Spelling error % (0-50%)
- [ ] Y-axis: Vector distance

### Step 3: Verify Graph

Read the graph image and confirm:
- Shows increasing distance with more errors
- Has proper labels
- Shows data points for all error rates

### Step 4: Generate Deliverables Checklist

## Output Format

```
=== ASSIGNMENT VERIFICATION ===

REQUIREMENT 1: Test Sentences
- Sentences used: [number] [PASS/FAIL]
- Word counts: [list] [PASS/FAIL]

REQUIREMENT 2: Spelling Errors
- Error rates tested: [list] [PASS/FAIL]
- 25%+ errors included: [YES/NO] [PASS/FAIL]

REQUIREMENT 3: Translation Pipeline
- EN→FR recorded: [YES/NO] [PASS/FAIL]
- FR→HE recorded: [YES/NO] [PASS/FAIL]
- HE→EN recorded: [YES/NO] [PASS/FAIL]

REQUIREMENT 4: Vector Distance
- Distances calculated: [YES/NO] [PASS/FAIL]
- Expected trend (more errors = more distance): [YES/NO]

REQUIREMENT 5: Graph
- Graph exists: [YES/NO] [PASS/FAIL]
- Proper axes: [YES/NO] [PASS/FAIL]

=== OVERALL STATUS ===
[ALL REQUIREMENTS MET / MISSING: list]

=== DELIVERABLES ===
1. Sentences: [filename or location]
2. Sentence lengths: [list]
3. Agent definitions: agents/*.md
4. Graph: [filename]
5. Python code: scripts/*.py
```
