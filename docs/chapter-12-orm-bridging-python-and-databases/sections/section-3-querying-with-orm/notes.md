# Section 12.3: Querying with ORM

## Overview

After defining model classes, the next step is querying data. Django ORM provides readable query chains that map to common SQL operations.

Use the shared starter project models as your query baseline so Chapter 13 views can reuse the same entities.

## Core Concepts

- `all()` returns all rows as model objects.
- `filter()` applies conditions.
- `get()` fetches exactly one expected record.
- `order_by()` controls sorting.
- `values()` and `values_list()` return selected fields.

## Code Walkthrough (incremental)

Start with all customer records.

```python
Customer.objects.all()
```

Filter to active customers.

```python
Customer.objects.filter(is_active=True)
```

Sort active customers by name.

```python
Customer.objects.filter(is_active=True).order_by("name")
```

Return only selected fields.

```python
Customer.objects.filter(is_active=True).values("name", "credit_limit")
```

Retrieve one known record.

```python
Customer.objects.get(customer_code="C-100")
```

Each step is still class-based and object-aware, which keeps data access aligned with OOP thinking.

## Try It (optional)

Write a query chain for `Invoice` that filters unpaid invoices and sorts by due date.

## Summary

Django ORM querying is expressive and incremental. You can compose simple methods to express business questions without dropping into raw SQL for every case.
