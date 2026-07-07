"""Section 2 Exercise 1: Fetching and Validating API Responses.

Implement fetch_product_data(product_ids, base_url, timeout).

Use the explicit sample constants below while developing and validating your logic.
This exercise uses mock response data in tests so grading remains stable.
In live practice, call real unauthenticated GET endpoints and parse JSON.
"""

SAMPLE_PRODUCT_IDS = [101, 102, 103]
SAMPLE_BASE_URL = "https://jsonplaceholder.typicode.com"
SAMPLE_TIMEOUT = 10

# Mock response data that simulates API returns
# In the test, we'll mock requests.get to return these
SAMPLE_RESPONSE_DATA = {
    101: {"id": 101, "name": "Widget A", "price": 29.99, "stock": 100},
    102: {"id": 102, "name": "Widget B", "price": 39.99, "stock": 50},
    103: {"id": 103, "name": "Widget C", "price": 49.99, "stock": 25},
}


def fetch_product_data(product_ids, base_url, timeout=10):
    """Fetch product data from API for given IDs.

    This function makes HTTP GET requests to base_url/products/{id}.
    For testing purposes, assume the API returns JSON with product details.

    Args:
        product_ids: List of integer product IDs to fetch
        base_url: Base URL for the API (e.g., 'https://jsonplaceholder.typicode.com')
        timeout: Request timeout in seconds

    Returns:
        A dictionary with keys:
        - successful: List of successfully fetched product data (dicts)
        - failed_ids: List of product IDs that failed to fetch
        - total_requested: Number of products requested
        - total_successful: Number of products successfully fetched
        - total_value: Sum of (price * stock) for successful products, rounded to 2 decimals
    """
    raise NotImplementedError("Implement fetch_product_data(product_ids, base_url, timeout=10)")
