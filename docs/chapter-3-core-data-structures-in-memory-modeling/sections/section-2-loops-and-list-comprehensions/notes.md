# Section 3.2: Loops and List Comprehensions

## Overview

Loops and comprehensions are the core execution patterns for list-based processing. business data is often messy, so you need repeatable logic for validation, transformation, and categorization.

## Core Concepts

- `for` loops are ideal for record-by-record traversal.
- `while` loops are useful when iteration depends on a changing condition or index.
- List comprehensions combine filter and transform in one readable expression.
- Pick the construct that maximizes clarity for future maintainers.

## Code Walkthrough (incremental)

Start with a short list that needs cleanup and classification:

```python
amounts = [45.0, None, 120.5, -5, 510.0, 85.25, 999.0]
```

Use a `for` loop when you want to process one value at a time.

```python
# build a cleaned list
valid_amounts = []
for amount in amounts:
    # skip missing and negative values
    if amount is None or amount < 0:
        continue

    # keep rounded valid values
    valid_amounts.append(round(amount, 2))
```

Use `enumerate` when you want both index and value.

```python
for index, amount in enumerate(valid_amounts):
    print(index, amount)
```

Use a `while` loop when position control matters.

```python
# walk the list by index
index = 0
high_value_count = 0
while index < len(valid_amounts):
    # check one value at the current position
    if valid_amounts[index] >= 500:
        high_value_count += 1
    index += 1
```

Use a comprehension when the transformation rule is short and clear.

```python
# map each amount to a category
categories = [
    "low" if amount < 100 else "medium" if amount < 500 else "high"
    for amount in valid_amounts
]
```

Filter with a comprehension when you want a smaller list.

```python
# keep only high values
high_amounts = [amount for amount in valid_amounts if amount >= 500]
```

Combine two lists into one reporting structure.

```python
# pair each amount with its category
classified_rows = [
    {"amount": amount, "category": category}
    for amount, category in zip(valid_amounts, categories)
]
```

## Try It (optional)

Use a list of support ticket resolution times. Remove invalid values, count SLA breaches with a loop, and classify each valid time as fast, normal, or slow.

## Summary

Loop design is about control and correctness. Comprehensions are about concise transformation. Use both deliberately to keep data-processing logic clear and testable.
