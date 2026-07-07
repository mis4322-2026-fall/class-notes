"""Section 4 Exercise 2: Dictionary APIs and Nested Structures.

Implement build_customer_order_summary(customers, min_revenue).
"""

SAMPLE_CUSTOMERS = [
    {
        "customer": "Acme",
        "orders": [
            {"order_id": "O-100", "qty": 10, "unit_price": 25.0},
            {"order_id": "O-101", "qty": 4, "unit_price": 100.0},
        ],
    },
    {
        "customer": "Blue Harbor",
        "orders": [
            {"order_id": "O-200", "qty": 3, "unit_price": 120.0},
        ],
    },
    {
        "customer": "Acme",
        "orders": [
            {"order_id": "O-102", "qty": 2, "unit_price": 75.0},
        ],
    },
]
SAMPLE_MIN_REVENUE = 700


def build_customer_order_summary(customers, min_revenue):
    """Aggregate nested order totals by customer.

    Return a dictionary with keys:
    - revenue_by_customer: customer -> rounded revenue
    - qualifying_customers: sorted list of customers with revenue >= min_revenue
    - order_count_by_customer: customer -> number of order rows processed
    """
    raise NotImplementedError("Implement build_customer_order_summary(customers, min_revenue)")
