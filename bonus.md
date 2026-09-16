# MIS 4322 — Code Walkthroughs

**September 16**

The purpose of these examples is to perform the same task in multiple ways and compare:

- **Result:** Do the approaches produce the same output?
- **Mutation:** Does the operation change the original object?
- **Return value:** Does it return a list, an iterator, a string, or `None`?
- **Readability:** Which version makes the intention easiest to see?

All examples below are complete and can be run from top to bottom.

## 0. Sample data

```python
orders = [
    {
        "order_id": 1001,
        "customer": "  Acme Coffee  ",
        "region": "North",
        "status": "complete",
        "qty": 3,
        "unit_price": 12.50,
    },
    {
        "order_id": 1002,
        "customer": "Baylor Books",
        "region": "South",
        "status": "pending",
        "qty": 2,
        "unit_price": 25.00,
    },
    {
        "order_id": 1003,
        "customer": "Cameron Catering",
        "region": "North",
        "status": "complete",
        "qty": 5,
        "unit_price": 8.00,
    },
    {
        "order_id": 1004,
        "customer": "Dr Pepper Museum",
        "region": "Central",
        "status": "cancelled",
        "qty": 1,
        "unit_price": 100.00,
    },
]

products = [
    {"name": "Keyboard", "price": 80.00, "cost": 50.00},
    {"name": "Monitor", "price": 240.00, "cost": 170.00},
    {"name": "Mouse", "price": 35.00, "cost": 12.00},
]
```

## 1. String methods

Strings are **immutable**. A string method returns a new string instead of changing the original string.

```python
raw_customer = "  Acme Coffee  "

clean_customer = raw_customer.strip()  # remove whitespace from both ends
lower_customer = clean_customer.lower()  # return lowercase copy
upper_customer = clean_customer.upper()  # return uppercase copy
renamed_customer = clean_customer.replace("Coffee", "Roasters")  # replace text
words = clean_customer.split()  # split on whitespace; return list[str]

print(raw_customer)      # "  Acme Coffee  " — unchanged
print(clean_customer)    # "Acme Coffee"
print(lower_customer)    # "acme coffee"
print(upper_customer)    # "ACME COFFEE"
print(renamed_customer)  # "Acme Roasters"
print(words)             # ["Acme", "Coffee"]
```

### Chained methods vs. separate steps

```python
raw_region = "  NORTH REGION  "

region_a = raw_region.strip().lower()  # concise: pass each result to next method

without_spaces = raw_region.strip()  # explicit intermediate result
region_b = without_spaces.lower()

print(region_a)              # "north region"
print(region_b)              # "north region"
print(raw_region)            # "  NORTH REGION  " — unchanged
print(region_a == region_b)  # True
```

> Python uses `strip()`, not `trim()`.

## 2. Keep matching records: comprehension vs. `filter`

### Conditional list comprehension

```python
complete_a = [
    order
    for order in orders
    if order["status"] == "complete"  # keep only matching orders
]

print([order["order_id"] for order in complete_a])  # [1001, 1003]
```

### `filter` with a lambda

```python
complete_iterator = filter(
    lambda order: order["status"] == "complete",  # predicate: True means keep
    orders,
)

print(complete_iterator)  # <filter object ...> — lazy iterator, not a list

complete_b = list(complete_iterator)  # consume iterator; build a list

print([order["order_id"] for order in complete_b])  # [1001, 1003]
print(complete_a == complete_b)                      # True
print(len(orders))                                   # 4 — source unchanged
```

### `filter` with a named predicate

```python
def is_complete(order):
    """Return True when an order should be kept."""
    return order["status"] == "complete"


complete_c = list(filter(is_complete, orders))

print([order["order_id"] for order in complete_c])  # [1001, 1003]
print(complete_a == complete_c)                     # True
```

### Compare

- The comprehension places the **selection rule** inside the list construction.
- `filter` emphasizes applying a **predicate** to every item.
- A comprehension returns a list immediately.
- `filter` returns an iterator; `list(...)` converts it into a list.
- None of these approaches changes `orders`.

## 3. Transform every record: comprehension vs. `map`

### Transforming list comprehension

```python
revenue_a = [
    order["qty"] * order["unit_price"]  # transform one order into one number
    for order in complete_a
]

print(revenue_a)  # [37.5, 40.0]
```

### `map` with a lambda

```python
revenue_iterator = map(
    lambda order: order["qty"] * order["unit_price"],  # transformation
    complete_a,
)

print(revenue_iterator)  # <map object ...> — lazy iterator, not a list

revenue_b = list(revenue_iterator)  # consume iterator; build a list

print(revenue_b)               # [37.5, 40.0]
print(revenue_a == revenue_b)  # True
```

### `map` with a named function

```python
def calculate_revenue(order):
    """Calculate revenue for one order."""
    return order["qty"] * order["unit_price"]


revenue_c = list(map(calculate_revenue, complete_a))

print(revenue_c)               # [37.5, 40.0]
print(revenue_a == revenue_c)  # True
```

### Compare

- The comprehension displays the **expression** and **iteration** together.
- `map` emphasizes applying one transformation function to every item.
- A comprehension returns a list immediately.
- `map` returns an iterator.
- A named function is useful when the business rule deserves a name or tests.

## 4. Sort a list of integers

### 4.1 `list.sort()` changes the existing list

```python
scores = [82, 95, 71, 88]

sort_result = scores.sort()  # mutate scores; return None

print(scores)       # [71, 82, 88, 95]
print(sort_result)  # None
```

Do not assign the result of `list.sort()` back to the variable:

```python
scores = [82, 95, 71, 88]

scores = scores.sort()  # common mistake: sort() returns None

print(scores)  # None
```

### 4.2 `sorted()` returns a new list

```python
scores = [82, 95, 71, 88]

ascending = sorted(scores)                 # new list; source unchanged
descending = sorted(scores, reverse=True)  # new list; largest first

print(scores)      # [82, 95, 71, 88]
print(ascending)   # [71, 82, 88, 95]
print(descending)  # [95, 88, 82, 71]
```

### 4.3 Same ordering, different effects

```python
scores = [82, 95, 71, 88]

working = scores.copy()  # protect original by sorting a copy
working.sort(reverse=True)

ranked = sorted(scores, reverse=True)

print(working)            # [95, 88, 82, 71]
print(ranked)             # [95, 88, 82, 71]
print(working == ranked)  # True — same result
print(scores)             # [82, 95, 71, 88] — original unchanged
```

### Compare

- `list.sort()` mutates one particular list and returns `None`.
- `sorted()` accepts any iterable and returns a new list.
- Both support `key=` and `reverse=`.

## 5. Sort strings

### Default ordering

```python
regions = ["South", "north", "Central", "east"]

default_order = sorted(regions)  # uppercase sorts before lowercase

print(default_order)  # ["Central", "South", "east", "north"]
print(regions)        # ["South", "north", "Central", "east"] — unchanged
```

### Case-insensitive ordering with `key`

```python
case_insensitive = sorted(
    regions,
    key=str.lower,  # compare lowercase copies; return original strings
)

print(case_insensitive)  # ["Central", "east", "north", "South"]
print(regions)           # source remains unchanged
```

The `key` function produces a temporary comparison value. It does not replace the original item in the result.

## 6. Sort a list of dictionaries

Python cannot infer which dictionary field should control the ordering. Supply a `key` function.

### 6.1 Sort by one dictionary value

```python
orders_by_price = sorted(
    orders,
    key=lambda order: order["unit_price"],  # compare one numeric value
)

print([order["order_id"] for order in orders_by_price])
# [1003, 1001, 1002, 1004]

print([order["unit_price"] for order in orders_by_price])
# [8.0, 12.5, 25.0, 100.0]

print([order["order_id"] for order in orders])
# [1001, 1002, 1003, 1004] — source order unchanged
```

### 6.2 Sort by a calculated value

```python
orders_by_revenue = sorted(
    orders,
    key=lambda order: order["qty"] * order["unit_price"],  # calculated key
    reverse=True,  # highest revenue first
)

for order in orders_by_revenue:
    revenue = order["qty"] * order["unit_price"]
    print(order["order_id"], revenue)

# Expected output:
# 1004 100.0
# 1002 50.0
# 1003 40.0
# 1001 37.5
```

### 6.3 Sort by multiple values with a tuple key

```python
orders_by_region_and_price = sorted(
    orders,
    key=lambda order: (
        order["region"],      # primary key
        order["unit_price"],  # tie-breaker within each region
    ),
)

print([
    (order["region"], order["unit_price"], order["order_id"])
    for order in orders_by_region_and_price
])

# Expected output:
# [
#     ("Central", 100.0, 1004),
#     ("North", 8.0, 1003),
#     ("North", 12.5, 1001),
#     ("South", 25.0, 1002),
# ]
```

### 6.4 Lambda vs. named sorting function

```python
# Lambda: useful for a short rule used only here.
ranked_a = sorted(
    products,
    key=lambda product: product["price"] - product["cost"],
    reverse=True,
)


def margin(product):
    """Return the gross margin for one product."""
    return product["price"] - product["cost"]


# Named function: business meaning is explicit and reusable.
ranked_b = sorted(products, key=margin, reverse=True)

print([product["name"] for product in ranked_a])  # ["Monitor", "Keyboard", "Mouse"]
print([product["name"] for product in ranked_b])  # ["Monitor", "Keyboard", "Mouse"]
print(ranked_a == ranked_b)                       # True
```

## 7. Combine filtering, transformation, and sorting

### Step-by-step pipeline

```python
# Stage 1: filter — keep complete orders.
complete_orders = [
    order
    for order in orders
    if order["status"] == "complete"
]

# Stage 2: transform — create smaller report rows.
revenue_rows = [
    {
        "order_id": order["order_id"],
        "region": order["region"],
        "revenue": order["qty"] * order["unit_price"],
    }
    for order in complete_orders
]

# Stage 3: sort — return a new report list.
report = sorted(
    revenue_rows,
    key=lambda row: row["revenue"],
    reverse=True,
)

print(report)
# [
#     {"order_id": 1003, "region": "North", "revenue": 40.0},
#     {"order_id": 1001, "region": "North", "revenue": 37.5},
# ]
```

### Compact equivalent

```python
compact_report = sorted(
    [
        {
            "order_id": order["order_id"],
            "region": order["region"],
            "revenue": order["qty"] * order["unit_price"],
        }
        for order in orders
        if order["status"] == "complete"
    ],
    key=lambda row: row["revenue"],
    reverse=True,
)

print(compact_report == report)  # True
```

### Compare

Both versions produce the same result. The step-by-step version exposes the output of every pipeline stage, making it easier to explain and debug. The compact version removes intermediate names but contains more ideas in one expression.

## 8. Summary

| Task | Approach A | Approach B | Central distinction |
|---|---|---|---|
| Normalize text | Chained methods | Separate steps | Concision vs. visible intermediate values |
| Keep selected items | Comprehension | `filter` | Direct selection vs. predicate application |
| Transform items | Comprehension | `map` | Direct transformation vs. function application |
| Sort a list | `list.sort()` | `sorted()` | Mutate existing list vs. return new list |
| Define a sort key | Lambda | Named function | Small local rule vs. reusable business logic |
| Build a pipeline | Intermediate variables | Nested expression | Traceability vs. compactness |

The question is not only, “Which approach works?” Ask which approach makes the intent, effects, and resulting data easiest to understand.
