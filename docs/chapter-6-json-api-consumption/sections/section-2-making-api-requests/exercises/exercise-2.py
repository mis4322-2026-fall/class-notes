"""Section 2 Exercise 2: Building and Parameterizing API Requests.

Implement search_projects(search_query, status_filter, limit, base_url).

Use the explicit sample constants below while developing and validating your logic.
This exercise uses mock response data in tests so grading remains stable.
In live practice, call real unauthenticated GET endpoints and parse JSON.
"""

SAMPLE_SEARCH_QUERY = "analytics"
SAMPLE_STATUS = "active"
SAMPLE_LIMIT = 5
SAMPLE_BASE_URL = "https://jsonplaceholder.typicode.com"

# Mock response data simulating API search results
SAMPLE_SEARCH_RESPONSE_DATA = [
    {"id": 1, "name": "Analytics Dashboard", "status": "active", "owner": "Alice"},
    {"id": 2, "name": "Data Analytics v2", "status": "active", "owner": "Bob"},
    {"id": 3, "name": "Web Analytics Tracker", "status": "archived", "owner": "Carol"},
    {"id": 4, "name": "Real-time Analytics", "status": "active", "owner": "David"},
]


def search_projects(search_query, status_filter=None, limit=10, base_url="https://jsonplaceholder.typicode.com"):
    """Search for projects via API with query parameters.

    This function makes an HTTP GET request to base_url/search with query parameters.

    Args:
        search_query: Search term to find in project names
        status_filter: Optional status value (e.g., 'active', 'archived')
        limit: Maximum number of results to return
        base_url: Base URL for the API

    Returns:
        A dictionary with keys:
        - results: List of matching projects (each a dict with id, name, status, owner)
        - query_params: Dictionary of the query parameters sent to API
        - match_count: Number of matching projects found
        - owners: List of unique owner names from results
        - request_url: The full URL that would be sent (for debugging)
    """
    raise NotImplementedError("Implement search_projects(search_query, status_filter=None, limit=10, base_url=...)")
