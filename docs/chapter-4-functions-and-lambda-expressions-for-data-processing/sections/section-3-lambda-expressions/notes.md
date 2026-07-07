# Section 4.3: Lambda Expressions

## Overview

Lambdas are compact anonymous functions used for short transformations. They are especially useful in `sorted`, `filter`, and `map` when the logic is small and local.

## Core Concepts

- Lambda syntax: `lambda params: expression`
- Best for one clear expression.
- Common in key functions for sorting and filtering.
- Prefer named functions when logic grows beyond a small expression.

## Code Walkthrough (incremental)

Start with a list of small product records.

```python
products = [
    {"name": "Laptop", "cost": 650, "price": 900},
    {"name": "Mouse", "cost": 12, "price": 25},
    {"name": "Monitor", "cost": 140, "price": 240},
]
```

Use a lambda as a sort key.

```python
# sort by margin from highest to lowest
ranked = sorted(
    products,
    key=lambda product: product["price"] - product["cost"],
    reverse=True,
)
```

Use a lambda for filtering.

```python
# keep only products with enough margin
qualified = list(
    filter(lambda product: (product["price"] - product["cost"]) >= 80, products)
)
```

Use a lambda for projection.

```python
# keep only product names
names = list(map(lambda product: product["name"], qualified))
```

Compare lambda usage to a comprehension.

```python
# build name and margin rows with a comprehension
margins = [
    {"name": p["name"], "margin": p["price"] - p["cost"]}
    for p in products
]
```

Switch to a named function when the rule gets too long.

```python
def margin(product):
    return product["price"] - product["cost"]

ranked_again = sorted(products, key=margin, reverse=True)
```

## Try It (optional)

Given customer dictionaries with `score`, use a lambda to sort descending by score, filter to keep scores above a threshold, and return names.

## Summary

Lambdas are a precision tool for small transformations. Use them to keep focused operations concise, but switch to named functions when business rules become complex.
