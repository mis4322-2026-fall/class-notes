# Section 4.4: Applying Functions and Lambdas in Data Pipelines

## Overview

Real data scripts are pipelines: filter records, transform values, aggregate outputs, and format results. This section combines named functions and lambdas into an end-to-end pipeline pattern.

## Core Concepts

- Pipelines should have clear stages and contracts.
- Named functions fit major transformation stages.
- Lambdas fit small local rules (keys, filters, projections).
- Pipeline outputs should be deterministic and report-ready.

## Code Walkthrough (incremental)

Start with a short list of order records.

```python
orders = [
    {"region": "North", "qty": 10, "unit_price": 25.0, "status": "complete"},
    {"region": "South", "qty": 5, "unit_price": 100.0, "status": "pending"},
    {"region": "North", "qty": 8, "unit_price": 20.0, "status": "complete"},
]
```

Filter the raw input first.

```python
# keep only completed orders
complete_orders = list(filter(lambda row: row["status"] == "complete", orders))
```

Use a named function for one transformation step.

```python
# convert one order row into a smaller reporting row
def with_revenue(row):
    return {
        "region": row["region"],
        "revenue": row["qty"] * row["unit_price"],
    }

revenue_rows = [with_revenue(row) for row in complete_orders]
```

Use a second named function for aggregation.

```python
# group revenue by region
def aggregate_by_region(rows):
    totals = {}
    for row in rows:
        region = row["region"]
        totals[region] = totals.get(region, 0.0) + row["revenue"]
    return totals

region_totals = aggregate_by_region(revenue_rows)
```

Use lambdas for small final-stage rules.

```python
# keep only regions above the minimum threshold
qualified = list(filter(lambda item: item[1] >= 300, region_totals.items()))

# sort from highest revenue to lowest
report = sorted(qualified, key=lambda item: item[1], reverse=True)
```

Wrap the pipeline in one reusable function.

```python
def build_region_report(orders, min_total):
    complete_orders = list(filter(lambda row: row["status"] == "complete", orders))
    revenue_rows = [with_revenue(row) for row in complete_orders]
    region_totals = aggregate_by_region(revenue_rows)
    qualified = list(filter(lambda item: item[1] >= min_total, region_totals.items()))
    return sorted(qualified, key=lambda item: item[1], reverse=True)
```

## Try It (optional)

Build a pipeline for support tickets: keep resolved tickets, calculate handling cost per ticket, aggregate by team, and return teams sorted by total cost.

## Summary

Pipelines become robust when each stage is explicit and testable. Named functions provide structure while lambdas keep small rules concise.
