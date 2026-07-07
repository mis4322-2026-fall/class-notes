# Section 5.3: Working with CSV in Python

## Overview

This section turns CSV structure knowledge into practical Python workflows. You will read row dictionaries, perform type conversion, compute grouped metrics, and write output files for reporting.

## Core Concepts

- `csv.DictReader` improves readability by using column names.
- Aggregation is easier with dictionary accumulators.
- `csv.DictWriter` gives explicit control over output schema and order.
- Conversion, filtering, and grouping should be visible and testable.

## Code Walkthrough (incremental)

Load CSV rows as dictionaries.

```python
import csv

with open("monthly_expenses.csv", "r", encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    rows = list(reader)

# immediate result: first row is a dict keyed by headers
print(rows[0])
```

Inspect available columns before processing.

```python
# inspect header names from DictReader
columns = list(rows[0].keys())

# immediate result: explicit schema list for validation/debugging
print(columns)
```

Convert numeric fields before calculations.

```python
first = rows[0]

# convert string amount to float once, then reuse
amount = float(first["amount"])
print(amount)
```

Filter rows by business rule.

```python
# keep approved rows only
approved_rows = [row for row in rows if row["approved"].strip().lower() == "yes"]

# immediate result: filtered dataset for downstream aggregation
print(len(approved_rows))
```

Project only fields needed for reporting.

```python
# reduce each row to report-relevant fields
compact_rows = [
    {"category": row["category"].strip(), "amount": float(row["amount"])}
    for row in approved_rows
]

# immediate result: cleaner shape for aggregation
print(compact_rows[0])
```

Aggregate totals by category.

```python
category_totals = {}
for row in approved_rows:
    category = row["category"].strip()
    amount = float(row["amount"])
    category_totals[category] = category_totals.get(category, 0.0) + amount

print(category_totals)
```

Compute grand total for ratio metrics.

```python
# sum category totals once for downstream percentages
grand_total = sum(category_totals.values())

# immediate result: one number for share calculations
print(round(grand_total, 2))
```

Write summary rows with `csv.DictWriter`.

```python
import csv

fieldnames = ["category", "total_amount"]
with open("expense_summary.csv", "w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)

    # write a stable header for downstream users
    writer.writeheader()

    for category, total in sorted(category_totals.items()):
        writer.writerow({"category": category, "total_amount": f"{total:.2f}"})

# immediate result: deterministic summary CSV sorted by category
```

## Try It (optional)

Add a new output column `share_of_total` that shows each category total divided by grand total.

## Summary

Python's CSV APIs support readable, maintainable data workflows when you combine them with explicit filtering, conversion, and grouped metric logic.
