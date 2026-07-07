# Section 6.4: Transforming API Data

## Overview

Raw API data is rarely ready for reporting. This section teaches practical transformation patterns: filtering, reshaping, aggregating, and enriching data for downstream analysis. These skills connect API consumption to reporting workflows.

## Core Concepts

- Dictionary comprehensions efficiently filter and reshape records.
- `filter()` and `map()` functions support functional transformation patterns.
- Aggregation functions (`sum()`, `max()`, `min()`) compute summaries from lists.
- Enrichment adds computed fields to existing records.
- Filtering removes invalid or irrelevant records.
- Grouping collects records by a common field for category-based reporting.
- Transformation pipelines separate concerns (fetch, validate, transform, aggregate).

## Code Walkthrough (incremental)

Filter records using a list comprehension.

```python
customers = [
    {"id": 1, "name": "Alice", "status": "active"},
    {"id": 2, "name": "Bob", "status": "inactive"},
    {"id": 3, "name": "Carol", "status": "active"},
]
active = [c for c in customers if c['status'] == 'active']
# result: active = [Alice, Carol]
```

Extract and reshape a list of records with comprehension.

```python
names_and_ids = [{"id": c['id'], "name": c['name']} for c in customers]
# result: [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, ...]
```

Enrich records by adding computed fields.

```python
for customer in customers:
    customer['name_upper'] = customer['name'].upper()
# result: Each customer now has name_upper field
```

Aggregate multiple records into summary metrics.

```python
orders = [
    {"id": 1, "amount": 100, "customer_id": 1},
    {"id": 2, "amount": 250, "customer_id": 1},
    {"id": 3, "amount": 150, "customer_id": 2},
]
total_revenue = sum(order['amount'] for order in orders)
# result: 500
```

Group records by a category field.

```python
from collections import defaultdict
by_customer = defaultdict(list)
for order in orders:
    by_customer[order['customer_id']].append(order)
# result: Orders grouped by customer_id
```

Compute per-group summaries.

```python
customer_totals = {}
for customer_id, customer_orders in by_customer.items():
    customer_totals[customer_id] = sum(o['amount'] for o in customer_orders)
# result: customer_totals = {1: 350, 2: 150}
```

Use map() to apply a transformation function to every record.

```python
def extract_name_only(customer):
    return customer['name']

names = list(map(extract_name_only, customers))
# result: ['Alice', 'Bob', 'Carol']
```

Chain multiple transformations in a pipeline.

```python
# Fetch → Filter → Enrich → Aggregate
active_customers = [c for c in customers if c['status'] == 'active']
for c in active_customers:
    c['category'] = 'Premium' if c['id'] < 3 else 'Standard'
summary = {"count": len(active_customers), "premium": sum(1 for c in active_customers if c['category'] == 'Premium')}
# result: Organized workflow from raw data to insights
```

Use filter() with a lambda for selective processing.

```python
high_value = list(filter(lambda o: o['amount'] > 150, orders))
# result: Orders with amount > 150
```

## Try It (optional)

Take a list of user records from an API response. Filter to active users, add a 'tier' field based on purchase history, group by company, and compute company-level summaries (count of users, total purchase amount, average purchase per user).

## Summary

Data transformation bridges raw API output and decision-ready reporting. Master comprehensions, aggregations, and grouping patterns. Build testable pipeline functions that each do one thing well. Clean, organized transformation code is easier to debug and evolve.
