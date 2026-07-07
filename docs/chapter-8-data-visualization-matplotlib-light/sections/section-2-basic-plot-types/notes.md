# Section 8.2: Basic Plot Types

## Overview

This section introduces three core plot types only: line, bar, and scatter. You will use a minimal set of commands so you can focus on meaning rather than mechanics.

## Core Concepts

- Line chart: trend through ordered values (often time).
- Bar chart: compare magnitudes across categories.
- Scatter plot: inspect whether two numeric variables move together.
- Labels and titles are mandatory for interpretation quality.

## Code Walkthrough (incremental)

### 1) Line chart

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
visitors = [120, 135, 128, 150, 160]

plt.plot(days, visitors)
plt.title("Daily Visitors")
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.show()
```

### 2) Bar chart

```python
products = ["A", "B", "C"]
sales = [42, 35, 51]

plt.bar(products, sales)
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units")
plt.show()
```

### 3) Scatter plot

```python
ad_spend = [200, 350, 500, 650, 800]
signups = [22, 30, 41, 44, 58]

plt.scatter(ad_spend, signups)
plt.title("Ad Spend vs Signups")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Signups")
plt.show()
```

## Try It (optional)

Pick one chart above and rewrite the title so a manager can understand it in 3 seconds.

## Summary

When learning visualization, accuracy of chart choice and clarity of labeling matter more than advanced styling.
