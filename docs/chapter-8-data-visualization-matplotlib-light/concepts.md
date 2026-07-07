# Concepts

Chapter 8 introduces visualization as a communication tool, not a deep plotting library tutorial. In business workflows, charts help teams notice trends, compare categories, and explore relationships before making decisions.

## Why Visualize

A good chart answers a focused question quickly:

- Is performance rising or falling over time?
- Which categories are highest or lowest?
- Do two variables appear related?

Visualization is valuable when your audience needs a fast pattern-level view.

## Minimal Chart Set for This Course

This chapter only uses three chart types:

- Line chart: trend over time or ordered sequence.
- Bar chart: compare values across categories.
- Scatter plot: inspect possible relationship between two numeric variables.

Keeping the API surface small helps you focus on reasoning and communication quality.

## What Makes a Chart Useful

A useful chart is:

- Purposeful: one clear question.
- Readable: simple title, labeled axes, legible category names.
- Honest: scale and formatting do not exaggerate differences.
- Actionable: the viewer can state one likely insight.

Minimal Matplotlib pattern used in this chapter:

```python
import matplotlib.pyplot as plt

plt.plot(x_values, y_values)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.show()
```

## Common Mistakes to Avoid

- Choosing the wrong chart for the question.
- Missing title or axis labels.
- Starting a bar chart at a non-zero baseline without explanation.
- Overloaded visuals with too many series or colors.
- Treating correlation in a scatter plot as proof of causation.

## Interpretation Mindset

Always separate three statements:

1. Observation: what the chart shows.
2. Interpretation: what it might mean.
3. Decision: what action to take next.

Strong analysts communicate uncertainty and limits, not just the most dramatic story.
