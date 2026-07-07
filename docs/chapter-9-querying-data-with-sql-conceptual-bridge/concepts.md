# Chapter 9 Concepts: Querying Data with SQL (Conceptual Bridge)

This chapter connects your Python data skills to relational data querying.

For data and operations work, data often lives in relational databases. SQL is the language used to ask business questions against that data. In this chapter, we focus on practical querying and interpretation, not database administration.

## Why SQL in a Business Workflow

- Python is strong for automation and transformation.
- SQL is strong for filtering, combining, and summarizing data at the source.
- Together, SQL + Python + Pandas form a common analytics workflow.

## Core Relational Ideas

- Table: A structured set of records.
- Row: One record.
- Column: One attribute of a record.
- Primary key: Unique identifier per row.
- Foreign key: Link from one table to another.

These relationships let you model common business entities such as students, departments, courses, and enrollments.

## SQL Query Patterns in Scope

- SELECT specific columns you need.
- WHERE to filter rows.
- ORDER BY to sort results.
- LIMIT to return a manageable number of rows.
- JOIN to combine related tables.

## SQLite as a Practical Learning Platform

SQLite is file-based, lightweight, and easy to use with Python.

Minimal connection pattern:

```python
import sqlite3

with sqlite3.connect("school_mis.db") as conn:
    rows = conn.execute("SELECT full_name FROM students LIMIT 3;").fetchall()
```

## Bridging to Pandas

Instead of manually looping through cursor rows, you can load query results directly into a DataFrame:

```python
import pandas as pd
import sqlite3

with sqlite3.connect("school_mis.db") as conn:
    df = pd.read_sql_query("SELECT * FROM enrollments;", conn)
```

This is often the fastest path from operational data to analysis and visualization.
