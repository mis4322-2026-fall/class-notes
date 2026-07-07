# Section 3.3: Dictionaries as Structured Data

## Overview

Dictionaries model named fields and are the default structure for record-like data. In business terms, each dictionary is similar to a row with explicit column names.

## Core Concepts

- Keys communicate semantic meaning directly.
- `get` supports safe reads with defaults.
- `setdefault` helps initialize grouped aggregates.
- `update` applies grouped field updates.
- Dictionary comprehensions create fast lookup tables.

## Code Walkthrough (incremental)

Start with one simple record, then move to multiple records.

```python
record = {"sku": "A100", "qty": 14, "reorder_level": 10}
```

Read values from a dictionary.

```python
# direct access when the key is expected
sku = record["sku"]

# safe access with a default when the key may be missing
category = record.get("category", "uncategorized")
```

Update values in place.

```python
# assign one key directly
record["qty"] = 16

# update several keys at once
record.update({"category": "accessory", "active": True})
```

Start with a list of records.

```python
records = [
    {"sku": "A100", "qty": 14, "reorder_level": 10, "category": "accessory"},
    {"sku": "B205", "qty": 8, "reorder_level": 12, "category": "hardware"},
    {"sku": "C010", "qty": 5, "reorder_level": 6},
]
```

Build a lookup table with a dictionary comprehension.

```python
# sku -> quantity lookup
qty_by_sku = {record["sku"]: record.get("qty", 0) for record in records}
```

Create a filtered list from dictionary fields.

```python
# keep only low-stock SKUs
low_stock_skus = sorted(
    [
        record["sku"]
        for record in records
        if record.get("qty", 0) < record.get("reorder_level", 0)
    ]
)
```

Count records by category with `setdefault`.

```python
category_counts = {}
for record in records:
    # use a fallback when category is missing
    category = record.get("category", "uncategorized")

    # initialize group count if needed
    category_counts.setdefault(category, 0)

    # increment group count
    category_counts[category] += 1
```

Add a derived field to each record.

```python
for record in records:
    # add a boolean field based on existing values
    record.update({
        "is_low_stock": record.get("qty", 0) < record.get("reorder_level", 0)
    })
```

Inspect keys and values.

```python
# field names in one record
fields = list(records[0].keys())

# category names from the grouped dictionary
all_categories = list(category_counts.keys())
```

## Try It (optional)

Create customer dictionaries with `id`, `segment`, and `balance`. Build a lookup by id, count customers by segment, and mark each customer as `high_balance` when balance exceeds a threshold.

## Summary

Dictionaries support clear, maintainable in-memory modeling. Using dictionary APIs consistently reduces missing-key errors and makes summarization logic easier to test.
