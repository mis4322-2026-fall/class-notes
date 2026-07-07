"""Section 3 Exercise 2: Load and Clean CSV into DataFrame.

Implement load_and_clean_orders(csv_path).
"""

from pathlib import Path
import pandas as pd

SAMPLE_CSV_PATH = Path(__file__).parent / "data" / "orders_sample.csv"


def load_and_clean_orders(csv_path):
    """Load CSV and produce a cleaned DataFrame.

    Cleaning rules:
    - Fill missing units with 0 and cast to int
    - Fill missing price with 0.0
    - Standardize region with title case
    - Add revenue column = units * price

    Returns:
        {
            "dataframe": <cleaned DataFrame>,
            "missing_before": int,
            "missing_after": int,
            "closed_revenue": float
        }
    """
    raise NotImplementedError("Implement load_and_clean_orders(csv_path)")
