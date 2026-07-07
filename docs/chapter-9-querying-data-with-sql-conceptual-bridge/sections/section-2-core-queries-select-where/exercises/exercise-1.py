"""Section 2 Exercise 1: Core SELECT/WHERE queries in SQLite."""

from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "data" / "school_mis.db"
QUERY_CASES = {
    "high_scores": {"min_grade_point": 3.7, "limit": 4},
    "is_courses": {"department_id": 1, "limit": 3},
}


def fetch_high_scores(db_path, min_grade_point=3.7, limit=4):
    """Return (student_id, course_id, grade_point) rows from enrollments.

    Apply WHERE, ORDER BY grade desc (then enrollment_id asc), and LIMIT.
    """
    raise NotImplementedError("Implement fetch_high_scores(db_path, min_grade_point, limit)")


def fetch_courses_by_department(db_path, department_id, limit=3):
    """Return (course_code, title) rows filtered by department_id.

    Sort by course_code and apply LIMIT.
    """
    raise NotImplementedError("Implement fetch_courses_by_department(db_path, department_id, limit)")
