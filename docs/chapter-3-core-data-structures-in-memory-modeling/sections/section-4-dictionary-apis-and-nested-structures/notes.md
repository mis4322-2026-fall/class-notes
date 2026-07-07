# Section 3.4: Dictionary APIs and Nested Structures

## Overview

Most business datasets are nested: a top-level entity contains a child list of related records. This section shows how to traverse and aggregate nested dictionaries safely.

## Core Concepts

- Parent dictionaries hold entity-level fields.
- Nested lists capture one-to-many relationships.
- Nested loops are required for complete aggregation.
- `get` and `setdefault` make optional fields safe.
- Dictionary comprehensions help produce final report slices.

## Code Walkthrough (incremental)

Start with nested records where each department has a list of purchases.

```python
records = [
    {
        "department": "IT",
        "purchases": [
            {"item": "Laptop", "quantity": 2, "unit_cost": 900.0},
            {"item": "Monitor", "quantity": 3, "unit_cost": 210.0},
        ],
    },
    {
        "department": "HR",
        "purchases": [
            {"item": "Chair", "quantity": 4, "unit_cost": 120.0},
        ],
    },
]
```

Read the top-level dictionary first.

```python
# get the first department name
first_department = records[0]["department"]

# get nested purchases list
first_purchases = records[0].get("purchases", [])
```

Read fields from one nested purchase.

```python
# get the first purchase inside the first department
first_purchase = records[0]["purchases"][0]

# read nested values
item_name = first_purchase["item"]
quantity = first_purchase["quantity"]
unit_cost = first_purchase["unit_cost"]
```

Initialize grouped totals.

```python
totals = {}
```

Traverse parent records and nested purchases.

```python
for record in records:
    # read top-level field safely
    department = record.get("department", "UNKNOWN")

    # initialize department total if needed
    totals.setdefault(department, 0.0)

    # loop through child purchases
    for purchase in record.get("purchases", []):
        qty = purchase.get("quantity", 0)
        unit_cost = purchase.get("unit_cost", 0.0)
        totals[department] += qty * unit_cost
```

Normalize totals for reporting.

```python
# round totals into a new dictionary
rounded_totals = {
    department: round(total, 2)
    for department, total in totals.items()
}
```

Build a filtered threshold view.

```python
# keep only large totals
above_threshold = {
    department: total
    for department, total in rounded_totals.items()
    if total >= 1000
}
```

Create another derived view from the same nested records.

```python
# count number of purchases per department
item_counts = {
    record.get("department", "UNKNOWN"): len(record.get("purchases", []))
    for record in records
}
```

## Try It (optional)

Model customers with nested orders. Calculate customer revenue totals and then build a second dictionary containing only customers above a selected revenue threshold.

## Summary

Nested structures are common in JSON and API work. Safe traversal, grouped aggregation, and post-processing comprehensions are the key workflow pattern.
