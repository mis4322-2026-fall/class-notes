# Section 9.2: Core Queries (SELECT, WHERE)

## Overview

This section practices the most common SQL clauses you will use daily: SELECT, WHERE, ORDER BY, and LIMIT.

## Core Concepts

- SELECT chooses columns.
- WHERE filters rows by condition.
- ORDER BY sorts output.
- LIMIT returns only a subset of rows.

Start with one table at a time before introducing joins.

## Code Walkthrough (incremental)

Return selected columns from enrollments:

```sql
SELECT student_id, course_id, grade_point
FROM enrollments;
```

Filter for strong grades:

```sql
SELECT student_id, course_id, grade_point
FROM enrollments
WHERE grade_point >= 3.7;
```

Sort by highest grade and cap to top rows:

```sql
SELECT student_id, course_id, grade_point
FROM enrollments
WHERE grade_point >= 3.5
ORDER BY grade_point DESC, enrollment_id ASC
LIMIT 5;
```

Use SQLite from Python:

```python
import sqlite3

query = """
SELECT student_id, course_id, grade_point
FROM enrollments
WHERE grade_point >= ?
ORDER BY grade_point DESC, enrollment_id ASC
LIMIT ?;
"""

with sqlite3.connect("school_mis.db") as conn:
    rows = conn.execute(query, (3.5, 5)).fetchall()
```

## Try It (optional)

Change the threshold from 3.5 to 3.8 and compare the number of returned rows.

## Summary

These clauses form the foundation of practical SQL querying. You can answer many business questions using only SELECT, WHERE, ORDER BY, and LIMIT.
