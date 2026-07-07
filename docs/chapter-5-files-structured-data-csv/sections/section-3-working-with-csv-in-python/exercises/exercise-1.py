"""Section 3 Exercise 1: Working with CSV in Python.

Build an approved-expenses report grouped by category.
"""

from pathlib import Path

# Starter dataset path used by tests and classroom demos.
SAMPLE_EXPENSES_PATH = Path(__file__).parent / "data" / "monthly_expenses.csv"


def build_approved_category_report(input_csv_path, output_csv_path):
    """Create a category-level report from approved expense transactions.

    Input columns:
    - month
    - category
    - amount
    - approved

    Requirements:
    1. Load rows using csv.DictReader.
    2. Keep rows where approved == "yes" (case-insensitive).
    3. Aggregate by category:
       - transaction_count
       - total_amount
       - average_amount
    4. Write output_csv_path with columns:
       category,transaction_count,total_amount,average_amount
       Sort rows by total_amount descending, then category ascending.

    Return:
    {
        "included_rows": <int>,
        "grand_total": <float>,
        "category_metrics": {
            "Category": {
                "transaction_count": <int>,
                "total_amount": <float>,
                "average_amount": <float>,
            },
            ...
        }
    }
    """
    raise NotImplementedError(
        "Implement build_approved_category_report(input_csv_path, output_csv_path)"
    )
