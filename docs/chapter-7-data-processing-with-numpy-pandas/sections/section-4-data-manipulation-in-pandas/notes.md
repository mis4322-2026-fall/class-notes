# Section 7.4: Data Manipulation in Pandas

## Overview

This section focuses on end-to-end transformation patterns in Pandas: cleaning, reshaping, aggregating, and preparing outputs for reporting. The examples build from simple operations to a realistic reporting pipeline using sales and operations data.

## Core Concepts

- Data cleaning includes null handling, type normalization, and text normalization.
- Feature engineering creates analysis-ready derived columns.
- Grouping and pivoting convert row-level data into summary views.
- Merging joins related tables for richer analysis.
- Method chaining can make transformations readable and reproducible.

## Code Walkthrough (incremental)

Start from a raw sales DataFrame with common quality issues.

```python
import pandas as pd

raw = pd.DataFrame([
    {"order_id": 1, "region": "North", "units": 4, "price": 220.0, "status": "Closed"},
    {"order_id": 2, "region": "north", "units": None, "price": 180.0, "status": "Closed"},
    {"order_id": 3, "region": "West", "units": 6, "price": None, "status": "Pending"},
    {"order_id": 4, "region": "South", "units": 3, "price": 200.0, "status": "Closed"},
])

print(raw)
```

Standardize text columns and fill missing numeric values.

```python
clean = raw.copy()
clean["region"] = clean["region"].str.title()
clean["units"] = clean["units"].fillna(0).astype(int)
clean["price"] = clean["price"].fillna(clean["price"].median())
print(clean)
```

Build derived columns for reporting.

```python
clean["revenue"] = clean["units"] * clean["price"]
clean["is_closed"] = clean["status"].eq("Closed")
print(clean)
```

Filter to finalized orders and sort by revenue.

```python
closed_orders = clean[clean["is_closed"]].sort_values(by="revenue", ascending=False)
print(closed_orders)
```

Aggregate KPIs by region.

```python
region_kpis = closed_orders.groupby("region", as_index=False).agg(
    orders=("order_id", "count"),
    total_units=("units", "sum"),
    total_revenue=("revenue", "sum"),
    avg_revenue=("revenue", "mean"),
)
print(region_kpis)
```

Create a pivot table for manager-facing summaries.

```python
pivot = pd.pivot_table(
    clean,
    index="region",
    columns="status",
    values="order_id",
    aggfunc="count",
    fill_value=0,
)
print(pivot)
```

Merge with a lookup table (e.g., regional manager assignment).

```python
region_lookup = pd.DataFrame([
    {"region": "North", "manager": "A. Lee"},
    {"region": "South", "manager": "R. Diaz"},
    {"region": "West", "manager": "S. Patel"},
])

merged = region_kpis.merge(region_lookup, on="region", how="left")
print(merged)
```

Method-chaining workflow example.

```python
pipeline_output = (
    raw
    .assign(
        region=lambda d: d["region"].str.title(),
        units=lambda d: d["units"].fillna(0).astype(int),
        price=lambda d: d["price"].fillna(d["price"].median()),
    )
    .assign(revenue=lambda d: d["units"] * d["price"])
    .query("status == 'Closed'")
    .groupby("region", as_index=False)
    .agg(total_revenue=("revenue", "sum"), total_units=("units", "sum"))
    .sort_values(by="total_revenue", ascending=False)
)

print(pipeline_output)
```

Export final summary for dashboard ingestion.

```python
pipeline_output.to_csv("region_kpi_summary.csv", index=False)
```

## Try It (optional)

1. Build a DataFrame with at least 12 orders and intentionally include nulls or inconsistent text values.
2. Clean the data and create a revenue column.
3. Keep only finalized orders.
4. Produce a region-level summary table and export it to CSV.

## Summary

Pandas manipulation skills make raw operational records usable for decision-making. Cleaning, deriving columns, grouping, pivoting, and merging form a practical sequence you can reuse in analytics tasks and project deliverables.
