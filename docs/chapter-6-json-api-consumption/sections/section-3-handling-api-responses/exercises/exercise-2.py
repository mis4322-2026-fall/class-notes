"""Section 3 Exercise 2: Handling Paginated API Responses.

Implement paginate_and_aggregate(page_responses) to handle multiple response pages.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_PAGE_1 = {
    "status": 200,
    "data": [
        {"id": 1, "product_id": "A001", "amount": 100.50},
        {"id": 2, "product_id": "A002", "amount": 250.00},
    ],
    "has_next": True,
    "page": 1,
}

SAMPLE_PAGE_2 = {
    "status": 200,
    "data": [
        {"id": 3, "product_id": "B001", "amount": 175.75},
        {"id": 4, "product_id": "B002", "amount": 300.00},
    ],
    "has_next": False,
    "page": 2,
}

SAMPLE_PAGE_3_ERROR = {
    "status": 500,
    "data": None,
    "error": "Internal server error",
}


def paginate_and_aggregate(page_responses):
    """Aggregate transactions from multiple paginated API responses.

    Args:
        page_responses: List of API response dictionaries from different pages

    Returns:
        A dictionary with keys:
        - all_transactions: List of all valid transactions from successful responses
        - successful_pages: Count of responses with status 200 and valid data
        - failed_pages: Count of responses with non-200 status or no data
        - total_amount: Sum of all transaction amounts, rounded to 2 decimals
        - transaction_count: Total number of valid transactions
        - products: List of unique product_ids from all transactions
    """
    raise NotImplementedError("Implement paginate_and_aggregate(page_responses)")
