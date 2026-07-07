# Section 9.1: Relational Data Model Refresher

## Overview

This section revisits the relational model using a realistic business dataset for students, departments, courses, and enrollments.

## Core Concepts

- A table stores one type of entity (for example, students).
- A row is a single entity record.
- A column is one attribute of that entity.
- A primary key uniquely identifies each row.
- A foreign key links related tables.

In practice, relationships matter more than isolated records. For example, enrollments connect students to courses.

## Code Walkthrough (incremental)

Create a quick SQLite connection and inspect available tables:

```python
import sqlite3

with sqlite3.connect("school_mis.db") as conn:
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
    ).fetchall()
    print(tables)
```

Inspect the students table structure:

```python
with sqlite3.connect("school_mis.db") as conn:
    schema = conn.execute("PRAGMA table_info(students);").fetchall()
    for col in schema:
        print(col)
```

Count rows in each table:

```python
with sqlite3.connect("school_mis.db") as conn:
    student_count = conn.execute("SELECT COUNT(*) FROM students;").fetchone()[0]
    course_count = conn.execute("SELECT COUNT(*) FROM courses;").fetchone()[0]
    enrollment_count = conn.execute("SELECT COUNT(*) FROM enrollments;").fetchone()[0]

print(student_count, course_count, enrollment_count)
```

## Try It (optional)

Add a new department row and rerun the table count query. Confirm which table count changed and why.

## Summary

Relational modeling organizes business data into connected tables. Understanding keys and relationships makes later SQL queries easier to reason about.
