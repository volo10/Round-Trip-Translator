# Build and Test All Agent

You are the Master Build Agent. Your job is to run the complete build, test, and verification workflow.

## Complete Workflow

Execute these steps in sequence:

---

### PHASE 1: Setup
Run: `/setup-project`

Or manually:
```bash
python -m pip install -r requirements.txt
```

Verify all dependencies are installed.

---

### PHASE 2: Run Tests
Run: `/run-tests`

Or manually:
```bash
python -m pytest tests/ -v
```

All 75 tests must pass before proceeding.

---

### PHASE 3: Run Experiment
Run: `/run-full-experiment`

Or manually:
```bash
python scripts/run_experiment.py --local
```

This runs the full translation experiment with local models.

---

### PHASE 4: Verify Results
Run: `/verify-results`

Check that all assignment requirements are met.

---

## Output Format

```
====================================================
       BUILD AND TEST REPORT
====================================================

PHASE 1: SETUP
--------------
Status: [COMPLETE / FAILED]
Dependencies: [INSTALLED / MISSING]

PHASE 2: TESTS
--------------
Status: [COMPLETE / FAILED]
Tests Passed: [X]/75
Failed Tests: [list or "None"]

PHASE 3: EXPERIMENT
-------------------
Status: [COMPLETE / FAILED]
Mode: [Local/Mock/API]
Results File: [filename]
Graph File: [filename]

PHASE 4: VERIFICATION
---------------------
Status: [COMPLETE / FAILED]
Requirements Met: [X]/5

====================================================
       FINAL STATUS: [READY FOR SUBMISSION / NOT READY]
====================================================

Next Steps:
[List any remaining actions needed]
```

## Quick Commands Reference

| Step | Slash Command | Manual Command |
|------|---------------|----------------|
| Setup | `/setup-project` | `python -m pip install -r requirements.txt` |
| Test | `/run-tests` | `python -m pytest tests/ -v` |
| Experiment | `/run-full-experiment` | `python scripts/run_experiment.py --local` |
| Verify | `/verify-results` | (manual check) |
| All | `/build-and-test-all` | Run all above in sequence |
