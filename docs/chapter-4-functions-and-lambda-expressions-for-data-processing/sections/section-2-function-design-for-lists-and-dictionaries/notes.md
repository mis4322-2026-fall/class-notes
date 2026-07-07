# Section 4.2: Function Design for Lists and Dictionaries

## Overview

Most business data pipelines use lists of dictionaries as the baseline shape. Function design for this shape should prioritize clear contracts, defensive handling, and predictable outputs.

## Core Concepts

- Define required fields at the function boundary.
- Keep one business objective per function.
- Return structured data designed for downstream use.
- Avoid hidden side effects unless mutation is explicitly required.

## Code Walkthrough (incremental)

Start with list-of-dictionary input.

```python
records = [
    {"department": "IT", "amount": 1200},
    {"department": "HR", "amount": 450},
    {"department": "IT", "amount": 800},
]
```

Define one function with one clear responsibility.

```python
# summarize totals and counts by department
def summarize_by_department(records):
    summary = {}
    for row in records:
        department = row["department"]
        amount = row["amount"]

        summary.setdefault(department, {"count": 0, "total": 0})
        summary[department]["count"] += 1
        summary[department]["total"] += amount
    return summary
```

Call the function with real input.

```python
summary = summarize_by_department(records)
```

Add average values after the first aggregation pass.

```python
# add averages to the existing summary structure
for department, metrics in summary.items():
    metrics["average"] = round(metrics["total"] / metrics["count"], 2)
```

Build a smaller reporting view.

```python
# keep only departments above a total threshold
high_spend_departments = {
    department: metrics
    for department, metrics in summary.items()
    if metrics["total"] >= 1000
}
```

Prefer returning new outputs instead of mutating inputs.

```python
# good pattern: leave `records` unchanged and build `summary` as a new structure
```

## Try It (optional)

Design a function for ticket records (`team`, `hours`) that returns count/total/average per team and a second dictionary of teams above an hours threshold.

## Summary

Strong function design for list/dict data improves correctness, readability, and testability in operational analytics code.
