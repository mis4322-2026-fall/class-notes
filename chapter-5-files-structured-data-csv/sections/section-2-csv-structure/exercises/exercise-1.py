"""Section 2 Exercise 1: CSV Structure.

Validate and clean an incoming orders CSV file.
"""

from pathlib import Path

# Starter dataset path used by tests and classroom demos.
SAMPLE_ORDERS_PATH = Path(__file__).parent / "data" / "orders_raw.csv"


def validate_orders_csv(input_csv_path, cleaned_csv_path):
    """Validate rows, write cleaned records, and return summary metrics.

    Input columns:
    - order_id
    - customer
    - department
    - quantity
    - unit_price

    A row is valid when:
    1. All columns above are non-empty after strip.
    2. quantity is an integer > 0.
    3. unit_price is a float > 0.

    For valid rows:
    - Compute line_total = quantity * unit_price (rounded to 2 decimals).
    - Write cleaned rows to cleaned_csv_path with columns:
      order_id,customer,department,quantity,unit_price,line_total

    Return:
    {
        "total_rows": <int>,
        "valid_rows": <int>,
        "invalid_rows": <int>,
        "department_totals": {"Department": total_float, ...}
    }

    department_totals should be based on line_total values from valid rows.
    """
    raise NotImplementedError("Implement validate_orders_csv(input_csv_path, cleaned_csv_path)")
