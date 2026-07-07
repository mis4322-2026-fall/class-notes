"""Section 3 Exercise 1: Validating and Extracting API Response Data.

Implement validate_and_extract_users(response_json) to handle real-world API data.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_RESPONSE_JSON = {
    "status": "success",
    "data": [
        {"id": 1001, "name": "Alice", "email": "alice@company.com", "active": True},
        {"id": 1002, "name": "Bob", "email": "bob@company.com", "active": True},
        {"id": 1003, "name": "Carol", "email": None, "active": False},
        {"id": 1004, "name": "David", "active": True},  # Missing email
        {"name": "Eve", "email": "eve@company.com"},  # Missing id
    ]
}


def validate_and_extract_users(response_json):
    """Validate API response and extract complete user records.

    Args:
        response_json: Parsed API response (should have 'data' key with list of users)

    Returns:
        A dictionary with keys:
        - complete_users: List of users with required fields (id, name, email all non-null)
        - incomplete_users: List of users missing required fields
        - valid_count: Number of complete user records
        - invalid_count: Number of incomplete user records
        - emails_available: List of all non-null email addresses from complete users
        - active_users_count: Count of active users in complete_users list
    """
    raise NotImplementedError("Implement validate_and_extract_users(response_json)")
