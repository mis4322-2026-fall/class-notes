# Section 5.2: CSV Structure

## Overview

CSV files look simple, but reliable processing depends on understanding structure: headers, columns, delimiters, and data consistency. This section focuses on reading CSV shape correctly before business logic.

## Core Concepts

- Headers define semantic meaning for each column.
- Delimiters separate fields, but quoted fields can contain commas.
- Rows must be validated for required fields and expected types.
- Structural validation should happen before aggregation.

## Code Walkthrough (incremental)

Read CSV rows as basic lists.

```python
import csv

with open("orders.csv", "r", encoding="utf-8", newline="") as handle:
    reader = csv.reader(handle)
    header = next(reader)
    first_row = next(reader)

# immediate result: positional values
print(header)
print(first_row)
```

Read the same file with a custom delimiter when needed.

```python
import csv

with open("orders_pipe.txt", "r", encoding="utf-8", newline="") as handle:
    # set delimiter explicitly for non-comma files
    reader = csv.reader(handle, delimiter="|")
    header = next(reader)

# immediate result: parsed header using pipe separator
print(header)
```

Read CSV rows as dictionaries by header name.

```python
import csv

with open("orders.csv", "r", encoding="utf-8", newline="") as handle:
    dict_reader = csv.DictReader(handle)
    row = next(dict_reader)

# immediate result: keyed access by column name
print(row["order_id"], row["department"])
```

Validate required fields.

```python
required = ["order_id", "customer", "quantity", "unit_price"]

# fail rows where any required field is blank
is_valid = all((row.get(field, "").strip() for field in required))
print(is_valid)
```

Convert field types explicitly.

```python
# convert text fields to numeric business types
quantity = int(row["quantity"])
unit_price = float(row["unit_price"])
line_total = round(quantity * unit_price, 2)

# immediate result: numeric value ready for reporting
print(line_total)
```

Normalize text fields before comparison.

```python
# normalize department for grouping consistency
department = row["department"].strip().lower()

# immediate result: stable grouping key like "it" or "operations"
print(department)
```

Write cleaned CSV output with controlled columns.

```python
import csv

fieldnames = ["order_id", "customer", "department", "quantity", "unit_price", "line_total"]

with open("clean_orders.csv", "w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()

    # explicit column names avoid accidental schema drift
    writer.writerow(
        {
            "order_id": "1001",
            "customer": "Acme",
            "department": "IT",
            "quantity": 3,
            "unit_price": "249.99",
            "line_total": "749.97",
        }
    )

# immediate result: output file has controlled column order and one cleaned row
```

## Try It (optional)

Take a CSV file with 10 rows and manually classify each row as valid or invalid based on required fields and numeric conversion rules.

## Summary

Strong CSV structure handling prevents subtle reporting errors. Header-aware parsing, required-field checks, and explicit conversions are core habits for dependable data work.
