# Section 9.4: Mapping SQL to Python & Pandas

## Overview

This section bridges SQL results into Python dictionaries and Pandas DataFrames for downstream analysis.

## Core Concepts

- Cursor rows are often tuples unless you map them.
- Python dictionaries make records easier to use by column name.
- Pandas can load SQL query outputs directly with pd.read_sql_query.

## Code Walkthrough (incremental)

Fetch query rows and map to dictionaries:

```python
import sqlite3

query = """
SELECT s.full_name, ROUND(AVG(e.grade_point), 2) AS avg_grade
FROM students AS s
JOIN enrollments AS e ON s.student_id = e.student_id
GROUP BY s.student_id, s.full_name
ORDER BY avg_grade DESC;
"""

with sqlite3.connect("school_mis.db") as conn:
    rows = conn.execute(query).fetchall()

records = [{"full_name": row[0], "avg_grade": row[1]} for row in rows]
```

Load SQL output directly into Pandas:

```python
import pandas as pd
import sqlite3

query = """
SELECT d.name AS department, COUNT(DISTINCT e.student_id) AS enrolled_students
FROM departments AS d
LEFT JOIN courses AS c ON d.department_id = c.department_id
LEFT JOIN enrollments AS e ON c.course_id = e.course_id
GROUP BY d.department_id, d.name
ORDER BY d.name;
"""

with sqlite3.connect("school_mis.db") as conn:
    df = pd.read_sql_query(query, conn)
```

## Try It (optional)

Add one more output column in SQL and verify the DataFrame includes it.

## Summary

SQL handles focused data retrieval; Python and Pandas handle flexible post-query processing. This bridge is central to analytics workflows.
