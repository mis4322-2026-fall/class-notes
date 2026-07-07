# Exercise 1: Review Dependency Management Quality

## Task
Analyze the requirement lines below as if you were reviewing a small business analytics project before deployment.

```text
pandas==2.2.2
requests>=2.31
-e .
# internal tooling
```

For each line, decide whether it is:

1. Pinned
2. Unpinned
3. Editable
4. Ignored comment or blank content

Then answer these questions:

1. Which line creates the most reproducibility risk, and why?
2. What is the purpose of a pinned version?
3. When might an editable install be acceptable?

If `pip` is available in your environment, also run one of these commands and record the result:

```bash
python -m pip --version
python -m pip list
```

## Expected Deliverable
Submit:

1. A short classification table for the sample requirement lines
2. Brief answers to the three dependency-governance questions
3. Optional command output from a `pip` inspection command

## Success Criteria
- Each sample line is classified correctly.
- Your explanation clearly identifies why unpinned dependencies can cause drift.
- You distinguish development convenience from production stability.
- If you include command output, it is labeled and easy to interpret.