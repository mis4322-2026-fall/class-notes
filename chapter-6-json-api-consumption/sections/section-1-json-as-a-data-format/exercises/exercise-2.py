"""Section 1 Exercise 2: Serializing Python Data to JSON.

Implement build_json_report(records, output_format) to create JSON output.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_RECORDS = [
    {"id": 1, "product": "Laptop", "quantity": 5, "price": 1200.00},
    {"id": 2, "product": "Mouse", "quantity": 50, "price": 25.00},
    {"id": 3, "product": "Monitor", "quantity": 3, "price": 350.00},
]

SAMPLE_PRETTY = True


def build_json_report(records, pretty=False):
    """Create a JSON report from inventory records.

    Args:
        records: List of dictionaries with id, product, quantity, price
        pretty: Boolean; if True, use indentation and sorted keys

    Returns:
        A dictionary with keys:
        - json_string: JSON string representation of the records
        - total_items: Total quantity across all records
        - total_value: Sum of (quantity * price) for all records, rounded to 2 decimals
        - product_names: List of all product names
        - is_valid_json: Boolean indicating whether the json_string is valid JSON
    """
    raise NotImplementedError("Implement build_json_report(records, pretty=False)")
