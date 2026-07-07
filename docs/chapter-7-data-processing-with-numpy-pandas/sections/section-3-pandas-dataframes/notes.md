# Section 7.3: Pandas DataFrames

## Overview

Pandas DataFrames bring spreadsheet-like and SQL-like operations into Python code. For data and operations work, this means cleaner handling of row/column data, easier inspection, and faster transformation from raw records into report-ready tables.

This section emphasizes practical entry points: creating DataFrames, reading CSV, inspecting schema, selecting rows/columns, and building derived columns.

## Core Concepts

- A `DataFrame` is a labeled table with rows and columns.
- A `Series` is a single labeled column.
- `read_csv()` imports structured files quickly.
- `head()`, `info()`, `describe()` support early data inspection.
- Column operations are vectorized.
- Boolean indexing supports row filtering.

## Code Walkthrough (incremental)

Import Pandas and create a DataFrame from Python records.

```python
import pandas as pd

records = [
    {"order_id": 1001, "region": "North", "units": 5, "price": 220.0},
    {"order_id": 1002, "region": "West", "units": 3, "price": 180.0},
    {"order_id": 1003, "region": "North", "units": 7, "price": 210.0},
]

df = pd.DataFrame(records)
print(df)
```

Inspect structure and quick statistics.

```python
print(df.head())
print(df.info())
print(df.describe(numeric_only=True))
```

Select columns and rows.

```python
print(df["region"])
print(df[["order_id", "units"]])
print(df.loc[df["region"] == "North"])
```

Create a derived metric column.

```python
df["revenue"] = df["units"] * df["price"]
print(df)
```

Sort by a metric.

```python
sorted_df = df.sort_values(by="revenue", ascending=False)
print(sorted_df)
```

Read data from CSV and inspect nulls.

```python
sales_csv = pd.read_csv("sales_sample.csv")
print(sales_csv.head())
print(sales_csv.isna().sum())
```

Clean missing values and type mismatches.

```python
sales_csv["units"] = sales_csv["units"].fillna(0).astype(int)
sales_csv["price"] = sales_csv["price"].fillna(0.0)
sales_csv["revenue"] = sales_csv["units"] * sales_csv["price"]
```

Combine multiple conditions for filtering.

```python
priority_rows = sales_csv[
    (sales_csv["region"] == "North") &
    (sales_csv["revenue"] > 1000)
]
print(priority_rows)
```

Compute grouped summaries by region.

```python
region_summary = sales_csv.groupby("region", as_index=False).agg(
    total_units=("units", "sum"),
    total_revenue=("revenue", "sum"),
    avg_order_value=("revenue", "mean"),
)
print(region_summary)
```

Realistic business slice: ticket operations table.

```python
tickets = pd.DataFrame([
    {"team": "Support", "resolved": 38, "opened": 42},
    {"team": "Billing", "resolved": 21, "opened": 25},
    {"team": "Onboarding", "resolved": 16, "opened": 18},
])

tickets["resolution_rate"] = (tickets["resolved"] / tickets["opened"]).round(2)
print(tickets)
```

## Try It (optional)

1. Create a DataFrame from 8-10 order rows with region, units, and price.
2. Add a revenue column.
3. Filter high-value rows (`revenue > 1000`).
4. Group by region and compute totals and average revenue.

## Summary

Pandas DataFrames provide a practical table model for analysis. With quick inspection APIs, vectorized column operations, and expressive filtering/grouping syntax, you can move from raw records to useful summaries with less code and fewer errors.
