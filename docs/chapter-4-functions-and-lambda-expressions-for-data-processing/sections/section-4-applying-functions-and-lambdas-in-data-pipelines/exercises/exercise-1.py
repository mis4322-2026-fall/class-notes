"""Section 4 Exercise 1: Applying Functions and Lambdas in Data Pipelines.

Implement build_regional_revenue_report(orders, min_total).
"""

SAMPLE_ORDERS = [
    {"region": "North", "qty": 10, "unit_price": 25.0, "status": "complete"},
    {"region": "South", "qty": 5, "unit_price": 100.0, "status": "pending"},
    {"region": "North", "qty": 8, "unit_price": 20.0, "status": "complete"},
    {"region": "West", "qty": 6, "unit_price": 90.0, "status": "complete"},
    {"region": "South", "qty": 3, "unit_price": 120.0, "status": "complete"},
]
SAMPLE_MIN_TOTAL = 500


def build_regional_revenue_report(orders, min_total):
    """Build a thresholded regional revenue report.

    Rules:
    - Keep only orders where status == "complete"
    - Revenue per row = qty * unit_price
    - Aggregate revenue by region
    - Keep only regions where total >= min_total
    - Return a list of tuples: (region, total), sorted by total descending
    - Use at least one lambda expression
    """
    raise NotImplementedError("Implement build_regional_revenue_report(orders, min_total)")
