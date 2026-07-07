# Section 12.1: The Problem ORM Solves

## Overview

As data use grows, writing raw SQL for every read and write can become repetitive and hard to maintain. ORM helps by letting you use class-based Python patterns while still working with relational data.

Use this chapter's `starter-project/` as your common reference. The examples assume the `operations` app and consistent models (`Customer`, `Project`, `WorkItem`).

## Core Concepts

- Raw SQL is powerful but can become verbose for common app operations.
- ORM gives a higher-level API that maps model classes to tables.
- Query intent becomes easier to read in Python terms.
- ORM encourages consistent data access patterns across a team.
- This mirrors Chapter 11: class design first, then object operations.

## Code Walkthrough (incremental)

Start with a raw SQL statement that answers a business question.

```sql
SELECT customer_name, credit_limit
FROM customer
WHERE is_active = 1
ORDER BY customer_name;
```

Now compare the equivalent Django ORM intent.

```python
Customer.objects.filter(is_active=True).order_by("customer_name").values(
    "customer_name", "credit_limit"
)
```

Notice the shift:

- SQL-first expression becomes class-first expression.
- The query starts from a model (`Customer`) that represents a business entity.
- The code reads like object operations, not string assembly.

## Try It (optional)

Take one SQL query you already know (`SELECT ... WHERE ...`). Rewrite it into a Django ORM chain using a model name and one filter.

## Summary

ORM helps reduce repetitive SQL plumbing and keeps data access closer to OOP concepts you already know: classes, instances, and methods.
