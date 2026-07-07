"""Section 3 Exercise 2: Dictionaries as Structured Data.

Implement build_customer_credit_views(customers, min_credit_limit).
"""

SAMPLE_CUSTOMERS = [
    {"customer_id": "C001", "name": "Acme Retail", "credit_limit": 15000, "region": "North"},
    {"customer_id": "C002", "name": "Blue Harbor", "credit_limit": 8000, "region": "West"},
    {"customer_id": "C003", "name": "Crown Foods", "credit_limit": 22000, "region": "North"},
    {"customer_id": "C004", "name": "Delta Office", "credit_limit": 5000},
]
SAMPLE_MIN_CREDIT_LIMIT = 10000


def build_customer_credit_views(customers, min_credit_limit):
    """Build dictionary views for customer credit analysis.

    Return a dictionary with keys:
    - limit_by_customer: customer_id -> credit_limit
    - qualified_customers: sorted list of customer_id where credit_limit >= min_credit_limit
    - region_counts: region -> number of customers (missing region -> "unknown")
    """
    raise NotImplementedError("Implement build_customer_credit_views(customers, min_credit_limit)")
