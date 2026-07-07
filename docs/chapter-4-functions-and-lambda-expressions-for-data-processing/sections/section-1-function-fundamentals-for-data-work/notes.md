# Section 4.1: Function Fundamentals for Data Work

## Overview

Functions package repeated logic into reusable units. In reporting work, function boundaries make business rules explicit, testable, and easier to maintain.

## Core Concepts

- Function names should reflect business intent.
- Parameters define required inputs and expected data shapes.
- Return values make results reusable by downstream steps.
- Guard clauses protect against empty or invalid inputs.

## Code Walkthrough (incremental)

Start with a very small function.

```python
# return one simple result
def total_sales(amounts):
    return sum(amounts)
```

Call the function with concrete input.

```python
sales = [1200, 980, 1420, 1100]
total = total_sales(sales)
```

Return more than one metric in a dictionary.

```python
# return a structured result
def sales_metrics(amounts):
    if not amounts:
        return {"count": 0, "total": 0, "average": 0}

    total = sum(amounts)
    return {
        "count": len(amounts),
        "total": total,
        "average": round(total / len(amounts), 2),
    }
```

Add more fields when the business question grows.

```python
# extend the result with min and max
def sales_metrics_with_range(amounts):
    if not amounts:
        return {"count": 0, "total": 0, "average": 0, "min": None, "max": None}

    total = sum(amounts)
    return {
        "count": len(amounts),
        "total": total,
        "average": round(total / len(amounts), 2),
        "min": min(amounts),
        "max": max(amounts),
    }
```

Reuse the returned dictionary.

```python
# call the function once
metrics = sales_metrics_with_range([1200, 980, 1420, 1100])

# read fields from the returned dictionary
summary = f"{metrics['count']} days, total={metrics['total']}, avg={metrics['average']}"
```

Add a guard clause for empty input.

```python
# return a safe default for empty input
empty_metrics = sales_metrics_with_range([])
```

## Try It (optional)

Write a function that accepts a list of daily ticket counts and returns count, total, average, minimum, and maximum.

## Summary

Function fundamentals are about reliable contracts. Strong input/output design makes business logic easier to verify and reuse across reports.
