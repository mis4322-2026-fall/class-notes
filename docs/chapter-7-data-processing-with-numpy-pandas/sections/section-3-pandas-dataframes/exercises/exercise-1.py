"""Section 3 Exercise 1: Build and Inspect a DataFrame.

Implement build_orders_dataframe(records).
"""

import pandas as pd

SAMPLE_ORDERS = [
    {"order_id": 1001, "region": "North", "units": 5, "price": 220.0},
    {"order_id": 1002, "region": "West", "units": 3, "price": 180.0},
    {"order_id": 1003, "region": "North", "units": 7, "price": 210.0},
    {"order_id": 1004, "region": "South", "units": 2, "price": 250.0},
]


def build_orders_dataframe(records):
    """Create a DataFrame and basic summaries from order records.

    Returns:
        {
            "dataframe": <DataFrame with added revenue column>,
            "row_count": int,
            "columns": list,
            "total_revenue": float,
            "north_orders": int
        }
    """
    raise NotImplementedError("Implement build_orders_dataframe(records)")
