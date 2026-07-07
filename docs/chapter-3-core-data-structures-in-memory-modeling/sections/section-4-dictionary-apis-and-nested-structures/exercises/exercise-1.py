"""Section 4 Exercise 1: Dictionary APIs and Nested Structures.

Implement build_department_report(records, min_total).
"""

SAMPLE_RECORDS = [
    {
        "department": "IT",
        "purchases": [
            {"item": "Laptop", "quantity": 2, "unit_cost": 900.0},
            {"item": "Monitor", "quantity": 3, "unit_cost": 210.0},
        ],
    },
    {
        "department": "HR",
        "purchases": [
            {"item": "Chair", "quantity": 4, "unit_cost": 120.0},
        ],
    },
    {
        "department": "IT",
        "purchases": [
            {"item": "Dock", "quantity": 5, "unit_cost": 80.0},
        ],
    },
]
SAMPLE_MIN_TOTAL = 1000


def build_department_report(records, min_total):
    """Return nested aggregation report by department.

    Return keys:
    - totals: department -> total spend rounded to 2 decimals
    - above_threshold: only departments where total >= min_total
    """
    raise NotImplementedError("Implement build_department_report(records, min_total)")
