"""Section 3 Exercise 1: Combine relational data with JOIN."""

from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "data" / "school_mis.db"
TARGET_TERM = "2026-Spring"


def build_student_course_report(db_path, term):
    """Return a list of dict rows for one term using INNER JOIN.

    Each dict should contain:
        full_name, course_code, course_title, grade_point
    """
    raise NotImplementedError("Implement build_student_course_report(db_path, term)")


def compare_inner_vs_left_join_counts(db_path):
    """Return {'inner_count': int, 'left_count': int} for students to enrollments."""
    raise NotImplementedError("Implement compare_inner_vs_left_join_counts(db_path)")
