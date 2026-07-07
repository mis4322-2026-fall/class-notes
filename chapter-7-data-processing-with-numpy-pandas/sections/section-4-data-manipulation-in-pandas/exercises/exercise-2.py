"""Section 4 Exercise 2: Merge Customer and Order Data.

Implement merge_customer_orders(orders_df, customers_df).
"""

import pandas as pd

SAMPLE_ORDERS = [
    {"order_id": 3001, "customer_id": 501, "units": 5, "price": 220.0},
    {"order_id": 3002, "customer_id": 502, "units": 3, "price": 180.0},
    {"order_id": 3003, "customer_id": 505, "units": 2, "price": 260.0},
]

SAMPLE_CUSTOMERS = [
    {"customer_id": 501, "segment": "Enterprise"},
    {"customer_id": 502, "segment": "SMB"},
    {"customer_id": 503, "segment": "Public"},
]


def merge_customer_orders(orders_df, customers_df):
    """Merge order and customer tables and compute segment revenue.

    Requirements:
    - Left join orders with customers on customer_id
    - Add revenue column = units * price
    - Fill missing segment with "Unknown"
    - Build segment summary with total_revenue and order_count

    Returns:
        {
            "merged": <DataFrame>,
            "segment_summary": <DataFrame>,
            "unknown_segment_count": int
        }
    """
    raise NotImplementedError("Implement merge_customer_orders(orders_df, customers_df)")
