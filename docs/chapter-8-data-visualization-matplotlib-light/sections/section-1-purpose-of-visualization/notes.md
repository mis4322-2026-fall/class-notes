# Section 8.1: Purpose of Visualization

## Overview

Visualization helps convert raw numbers into quick pattern recognition. In data and operations work, this is useful for status updates, KPI monitoring, and communicating trends to decision-makers.

## Core Concepts

- A chart should answer one clear question.
- Visuals support decisions; they do not replace analysis.
- The same data can be shown well or poorly depending on chart choice.
- Good chart communication is often more valuable than advanced API usage.

### What chart to use when (quick guide)

- Use a line chart for changes over time.
- Use a bar chart for category comparison.
- Use a scatter plot for possible relationships between numeric fields.

## Code Walkthrough (incremental)

The section uses one tiny setup pattern for all later sections:

```python
import matplotlib.pyplot as plt

# Reused throughout the chapter
plt.style.use("default")
```

A minimal conceptual example:

```python
months = ["Jan", "Feb", "Mar"]
revenue = [12000, 14000, 13500]

plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.show()
```

This snippet is intentionally short. The point is not API depth. The point is matching a chart to a business question.

## Try It (optional)

Write one sentence for each:

1. A question that needs a line chart.
2. A question that needs a bar chart.
3. A question that needs a scatter plot.

## Summary

A useful chart is a communication choice. Start with the question, then choose the simplest chart that answers it clearly.
