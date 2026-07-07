"""Section 2 Exercise 2: Loops and List Comprehensions.

Implement build_region_performance(records, target).
"""

SAMPLE_RECORDS = [
    {"region": "North", "sales": 1200},
    {"region": "South", "sales": 800},
    {"region": "North", "sales": 900},
    {"region": "West", "sales": 1300},
    {"region": "South", "sales": 1500},
]
SAMPLE_TARGET = 2000


def build_region_performance(records, target):
    """Aggregate by region and return performance labels.

    Return a list of dictionaries sorted by region name.
    Each dictionary must contain:
    - region
    - total_sales
    - status: "met" when total_sales >= target else "below"

    Use loops for aggregation and a list comprehension for final row creation.
    """
    raise NotImplementedError("Implement build_region_performance(records, target)")
