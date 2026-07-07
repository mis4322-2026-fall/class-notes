"""Section 4 Exercise 1: Filtering and Reshaping API Data.

Implement transform_sales_records(raw_records, min_amount) to filter and reshape data.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_RAW_RECORDS = [
    {
        "transaction_id": "T001",
        "timestamp": "2024-01-15T10:30:00",
        "customer": {"id": 101, "name": "Alice"},
        "amount": 250.75,
        "status": "completed",
    },
    {
        "transaction_id": "T002",
        "timestamp": "2024-01-15T11:00:00",
        "customer": {"id": 102, "name": "Bob"},
        "amount": 50.00,
        "status": "completed",
    },
    {
        "transaction_id": "T003",
        "timestamp": "2024-01-15T11:30:00",
        "customer": {"id": 101, "name": "Alice"},
        "amount": 199.99,
        "status": "failed",
    },
    {
        "transaction_id": "T004",
        "timestamp": "2024-01-15T12:00:00",
        "customer": {"id": 103, "name": "Carol"},
        "amount": 500.00,
        "status": "completed",
    },
]

SAMPLE_MIN_AMOUNT = 100


def transform_sales_records(raw_records, min_amount=0):
    """Filter and reshape sales records.

    Args:
        raw_records: List of raw transaction records from API
        min_amount: Minimum transaction amount to include (filters < min_amount)

    Returns:
        A dictionary with keys:
        - simplified: List of simplified dicts with transaction_id, customer_name, amount, status
        - completed_only: List of completed transactions meeting min_amount threshold
        - filtered_count: Number of records after filtering
        - total_filtered_revenue: Sum of amounts in completed_only, rounded to 2 decimals
        - unique_customers: List of unique customer names from completed_only
    """
    raise NotImplementedError("Implement transform_sales_records(raw_records, min_amount=0)")
