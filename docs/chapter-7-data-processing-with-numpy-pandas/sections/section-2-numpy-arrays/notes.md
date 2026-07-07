# Section 7.2: NumPy Arrays

## Overview

NumPy gives you a fast, consistent array type for numeric data. Instead of writing long loops for every metric, you can express operations at the array level. This section moves from array creation to practical calculations using indexing, slicing, boolean masks, broadcasting, and aggregation.

## Core Concepts

- `ndarray` is NumPy's core structure for n-dimensional numeric data.
- `dtype` controls type consistency (int, float, etc.).
- Vectorized expressions operate on full arrays.
- Boolean masks filter values without manual loops.
- Broadcasting applies operations across compatible shapes.
- Aggregation functions compute metrics quickly (`sum`, `mean`, `min`, `max`).

## Code Walkthrough (incremental)

Import NumPy and create a basic 1D array.

```python
import numpy as np

daily_sales = np.array([1200, 1350, 980, 1500, 1640], dtype=float)
print(daily_sales)
print(daily_sales.dtype)
print(daily_sales.shape)
```

Perform vectorized arithmetic.

```python
# 8% projected growth
next_week_projection = daily_sales * 1.08
print(next_week_projection)

# Discount scenario
discounted = daily_sales - 100
print(discounted)
```

Compute summary metrics.

```python
print("Total:", daily_sales.sum())
print("Average:", daily_sales.mean())
print("Minimum:", daily_sales.min())
print("Maximum:", daily_sales.max())
```

Use indexing and slicing.

```python
print("First day:", daily_sales[0])
print("Last two days:", daily_sales[-2:])
print("Mid window:", daily_sales[1:4])
```

Apply boolean masks for business-style filtering.

```python
high_days = daily_sales[daily_sales > 1300]
print(high_days)

# Count how many days exceed threshold
count_high = (daily_sales > 1300).sum()
print(count_high)
```

Create a 2D array for branch-level weekly sales.

```python
branch_sales = np.array([
    [1200, 1320, 1280, 1400],
    [980, 1025, 1100, 1150],
    [1500, 1490, 1530, 1600],
], dtype=float)

print(branch_sales.shape)   # (3 branches, 4 weeks)
```

Aggregate by axis.

```python
# Weekly totals across branches
weekly_totals = branch_sales.sum(axis=0)
print(weekly_totals)

# Per-branch average
branch_averages = branch_sales.mean(axis=1)
print(branch_averages)
```

Broadcasting example: apply branch-specific adjustment factors.

```python
factors = np.array([1.00, 0.97, 1.05])  # one per branch
adjusted = branch_sales * factors.reshape(-1, 1)
print(adjusted)
```

Compute KPI flags using `where`.

```python
target = 1300
performance_flags = np.where(branch_sales >= target, "met", "below")
print(performance_flags)
```

Realistic mini-workflow: margin analysis from units and cost arrays.

```python
units = np.array([40, 28, 32, 50])
price = np.array([240, 180, 210, 150], dtype=float)
cost = np.array([160, 120, 140, 95], dtype=float)

revenue = units * price
gross_profit = units * (price - cost)
margin_pct = np.round((gross_profit / revenue) * 100, 2)

print("Revenue:", revenue)
print("Gross profit:", gross_profit)
print("Margin %:", margin_pct)
```

## Try It (optional)

1. Build a 2D NumPy array with monthly sales for 4 products over 6 months.
2. Compute totals by product and by month.
3. Filter products where average monthly sales exceed a threshold.
4. Apply a 5% growth factor and compare before/after totals.

## Summary

NumPy arrays replace repetitive loops with concise, high-performance expressions. With shape awareness, boolean masks, and axis-based aggregations, you can compute practical business metrics clearly and efficiently.
