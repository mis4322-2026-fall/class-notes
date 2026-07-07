"""Section 1 Exercise 1: Inspect a relational schema in SQLite.

Implement the functions below using sqlite3.
"""

from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "data" / "school_mis.db"
TABLES_TO_COUNT = ["students", "courses", "enrollments"]


def get_table_names(db_path):
    """Return all table names sorted alphabetically."""
    raise NotImplementedError("Implement get_table_names(db_path)")


def get_student_table_schema(db_path):
    """Return student schema as (column_name, column_type, is_primary_key) tuples."""
    raise NotImplementedError("Implement get_student_table_schema(db_path)")


def count_records_by_table(db_path, table_names):
    """Return a dict mapping each table name to row count."""
    raise NotImplementedError("Implement count_records_by_table(db_path, table_names)")
