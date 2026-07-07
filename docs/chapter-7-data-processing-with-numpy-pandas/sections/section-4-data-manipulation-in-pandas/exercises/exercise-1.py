"""Section 4 Exercise 1: Region KPI Aggregation in Pandas.

Implement build_region_kpi(df).
"""

from pathlib import Path
import pandas as pd

SAMPLE_CSV_PATH = Path(__file__).parent / "data" / "orders_pipeline.csv"


def build_region_kpi(df):
    """Create a region KPI summary from an orders DataFrame.

    Requirements:
    - Add revenue column = units * price
    - Keep only rows where status == "Closed"
    - Group by region and compute:
      orders (count), total_units (sum), total_revenue (sum)
    - Sort by total_revenue descending

    Returns:
        {
            "summary": <DataFrame>,
            "closed_order_count": int,
            "grand_revenue": float
        }
    """
    raise NotImplementedError("Implement build_region_kpi(df)")
