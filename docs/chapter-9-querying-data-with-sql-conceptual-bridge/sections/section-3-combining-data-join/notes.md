# Section 9.3: Combining Data (JOIN)

## Overview

This section introduces JOIN operations so you can combine related records across tables.

## Core Concepts

- INNER JOIN keeps only matching rows across tables.
- LEFT JOIN keeps all rows from the left table, even when no match exists on the right.
- Join keys usually map a primary key to a foreign key.

## Code Walkthrough (incremental)

Join students to enrollments for one term:

```sql
SELECT s.full_name, e.course_id, e.grade_point
FROM students AS s
INNER JOIN enrollments AS e
    ON s.student_id = e.student_id
WHERE e.term = '2026-Spring';
```

Add courses for a readable report:

```sql
SELECT s.full_name, c.course_code, c.title, e.grade_point
FROM students AS s
INNER JOIN enrollments AS e
    ON s.student_id = e.student_id
INNER JOIN courses AS c
    ON e.course_id = c.course_id
WHERE e.term = '2026-Spring'
ORDER BY s.full_name, c.course_code;
```

Conceptual LEFT JOIN comparison:

```sql
SELECT s.full_name, e.enrollment_id
FROM students AS s
LEFT JOIN enrollments AS e
    ON s.student_id = e.student_id;
```

If a student has no enrollment, LEFT JOIN still returns that student with NULL values for enrollment columns.

## Try It (optional)

Run the same query with INNER JOIN and LEFT JOIN and compare row counts.

## Summary

JOIN operations let you ask cross-table business questions. INNER JOIN is common for matched data, while LEFT JOIN helps preserve entities that currently have no related records.
