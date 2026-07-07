"""Section 4 Exercise 1: Map SQL query output to Python and Pandas."""

from pathlib import Path
import sqlite3

import pandas as pd

DB_PATH = Path(__file__).parent / "data" / "school_mis.db"
SAMPLE_STUDENT_LABELS = [
    {"full_name": "Ana Silva", "major": "Information Systems"},
    {"full_name": "Carla Gomez", "major": "Finance"},
]


def fetch_honor_roll(db_path, min_average=3.7):
    """Return list[dict] with keys full_name and avg_grade for students meeting threshold."""
    raise NotImplementedError("Implement fetch_honor_roll(db_path, min_average)")


def load_department_summary_df(db_path):
    """Return a DataFrame with columns: department, enrolled_students, avg_grade."""
    raise NotImplementedError("Implement load_department_summary_df(db_path)")
