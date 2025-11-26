# Experiment Runner Agent

You are the Experiment Agent. Your job is to run the full translation experiment and generate results.

## Tasks

### Step 1: Choose Mode

Select the appropriate mode:

**Option A: Local Models (Recommended)**
```bash
python scripts/run_experiment.py --local
```
- Real translations
- No API key needed
- First run downloads models (~300MB each)

**Option B: Mock Mode (Fast testing)**
```bash
python scripts/run_experiment.py --mock
```
- Fake translations
- Very fast
- For testing pipeline only

**Option C: Claude API (Best quality)**
```bash
python scripts/run_experiment.py
```
- Requires ANTHROPIC_API_KEY
- Best translation quality

### Step 2: Run the Experiment

Execute the chosen command and wait for completion.

The experiment will:
1. Take 2 test sentences (15+ words each)
2. Inject spelling errors at 0%, 10%, 20%, 25%, 30%, 40%, 50%
3. Translate each: English → French → Hebrew → English
4. Calculate vector distance between original and final
5. Generate graph

### Step 3: Verify Output Files

Check that these files were created in `scripts/`:
- `experiment_results_TIMESTAMP.json` - Raw data
- `spelling_error_graph_TIMESTAMP.png` - Visualization

### Step 4: Display Results Summary

Read the JSON file and summarize:
- Error rates tested
- Average distances at each rate
- Overall trend

## Output Format

```
=== EXPERIMENT COMPLETE ===

Mode: [Local/Mock/API]
Sentences Tested: [number]
Error Rates: 0%, 10%, 20%, 25%, 30%, 40%, 50%

Results Summary:
| Error Rate | Avg Distance | Avg Similarity |
|------------|--------------|----------------|
| 0%         | [value]      | [value]        |
| 10%        | [value]      | [value]        |
| ...        | ...          | ...            |

Output Files:
- Results: [filename]
- Graph: [filename]

Status: [SUCCESS / FAILED]
```
