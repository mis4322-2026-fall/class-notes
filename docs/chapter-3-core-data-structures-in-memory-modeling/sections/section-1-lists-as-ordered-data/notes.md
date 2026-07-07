# Section 3.1: Lists as Ordered Data

## Overview

Lists are the most direct way to model ordered business data in Python. In business workflows, order often carries meaning: transaction sequence, weekly performance, queue priority, or time-series movement.

## Core Concepts

- A list preserves insertion order.
- Indexing reads one position: `values[0]`, `values[-1]`.
- Slicing reads a range without mutating the source list.
- Core mutation APIs support operational updates:
  - `append` for one new value.
  - `extend` for multiple values.
  - `insert` for position-aware insertion.
  - `remove` and `pop` for deletions.
- Sorting and copying choices affect downstream reporting integrity.

## Code Walkthrough (incremental)

Start with one simple list and inspect it in small steps:

```python
weekly_orders = [42, 38, 57, 49, 61]
```

Read individual values without changing the list.

```python
# get first item
first_week = weekly_orders[0]

# get last item, does not mutate
latest_week = weekly_orders[-1]

# get a slice, does not mutate
mid_window = weekly_orders[1:4]
```

Add new values to the end.

```python
# add one new value
weekly_orders.append(65)

# add multiple values
weekly_orders.extend([59, 71])
```

Insert a value at a specific position.

```python
# insert a corrected value at index 2
weekly_orders.insert(2, 40)
```

Remove values in two different ways.

```python
# remove by value, mutates
weekly_orders.remove(38)

# remove last item, mutates
last_week = weekly_orders.pop()

# remove first item, mutates
first_archived_week = weekly_orders.pop(0)
```

Create safe reporting views.

```python
# copy list, does not mutate original
chronological = list(weekly_orders)

# sorted view, does not mutate original
ranked_high_to_low = sorted(weekly_orders, reverse=True)

# most recent values, does not mutate original
recent_three = weekly_orders[-3:]

# summary helpers
total_orders = sum(weekly_orders)
avg_orders = round(total_orders / len(weekly_orders), 2)
peak_week = max(weekly_orders)
```

## Try It (optional)

Create a list of daily support tickets for one week. Add two late-arriving days, remove one invalid value, and produce both chronological and sorted views. Then compute total, average, and peak tickets.

## Summary

Lists are not only containers. They are an ordered modeling tool for operational timelines. Mastering list APIs helps you keep sequence, corrections, and analytical views consistent.
