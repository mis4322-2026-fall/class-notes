# Exercise 1: Verify a Virtual Environment Setup

## Task
Create or inspect a virtual environment on your machine and document how you know it is active.

Work through these steps:

1. Create a practice environment in a scratch location such as `.venv-practice`.
2. Activate it in your shell.
3. Run checks that help confirm the environment is active.

Suggested checks:

```bash
python --version
python -c "import sys; print(sys.prefix); print(sys.base_prefix)"
python -c "import os; print(os.environ.get('PATH', ''))"
```

Then explain:

1. What changed after activation
2. How `sys.prefix` and `sys.base_prefix` help you detect an active environment
3. Why this matters for projects with multiple dependencies

## Expected Deliverable
Submit a short setup log that includes:

1. The commands you ran
2. The key output values you observed
3. A brief explanation of how you concluded the environment was active or not active

## Success Criteria
- Your submission shows evidence of checking environment activation, not just creating the folder.
- You correctly interpret either `sys.prefix` vs `sys.base_prefix`, `PATH`, or both.
- Your explanation connects environment isolation to dependency control or reproducibility.
- Your write-up is specific enough that another student could repeat your checks.