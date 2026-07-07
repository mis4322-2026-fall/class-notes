# Exercise 1: Classify Runtime Outcomes

## Task
Review the three execution scenarios below and classify each one using the runtime model from the notes.

| Scenario | Syntax Valid? | Runtime Error? |
| --- | --- | --- |
| A payroll script contains a missing colon after an `if` statement. | No | No |
| A reporting script starts correctly, then fails when dividing by zero. | Yes | Yes |
| A scheduled ETL script runs from start to finish with no exception. | Yes | No |

For each scenario, identify:

1. The correct `stage` value.
2. Whether `bytecode_ready` should be `True` or `False`.
3. One sentence explaining why the classification is useful in a support context.

## Expected Deliverable
Submit a short table or bullet list with one completed classification for each scenario.

## Success Criteria
- Each scenario uses one of these exact stage values: `parse_failed`, `runtime_failed`, or `executed`.
- Each scenario includes the correct `bytecode_ready` value.
- Each explanation distinguishes syntax problems from runtime problems.
- Your response is concise and uses business-facing language a support team could understand.