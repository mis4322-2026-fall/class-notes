# Section 8.3: Plotting from DataFrames

## Overview

You already use Pandas for tabular data. This section shows how to create simple plots directly from a DataFrame without writing a lot of plotting code.

## Core Concepts

- DataFrames connect naturally to visualization because columns already represent fields.
- Simple plotting from a DataFrame is enough for many first-pass business insights.
- Keep chart types limited to line, bar, and scatter.
- Validate labels and chart meaning before sharing.

## Code Walkthrough (incremental)

Create a DataFrame:

```python
import pandas as pd

df = pd.DataFrame(
    {
        "month": ["Jan", "Feb", "Mar", "Apr"],
        "revenue": [12, 15, 14, 18],
        "orders": [110, 125, 121, 140],
    }
)
```

Line and bar from columns:

```python
ax = df.plot(x="month", y="revenue", kind="line", title="Revenue by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (k$)")
```

```python
ax = df.plot(x="month", y="orders", kind="bar", title="Orders by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Orders")
```

Scatter from two numeric columns:

```python
ax = df.plot(x="orders", y="revenue", kind="scatter", title="Orders vs Revenue")
ax.set_xlabel("Orders")
ax.set_ylabel("Revenue (k$)")
```

## Try It (optional)

Change one axis label so it includes units (for example, dollars, percent, or count).

## Summary

DataFrame plotting is a fast bridge from cleaned data to an explainable visual. Keep plots simple and aligned to your question.
