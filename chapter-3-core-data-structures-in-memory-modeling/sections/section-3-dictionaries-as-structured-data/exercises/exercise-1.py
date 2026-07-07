"""Section 3 Exercise 1: Dictionaries as Structured Data.

Implement build_inventory_views(records).
"""

SAMPLE_RECORDS = [
    {"sku": "A100", "qty": 14, "reorder_level": 10, "category": "accessory"},
    {"sku": "B205", "qty": 8, "reorder_level": 12, "category": "hardware"},
    {"sku": "C010", "qty": 5, "reorder_level": 6},
    {"sku": "D777", "qty": 9, "reorder_level": 9, "category": "hardware"},
]


def build_inventory_views(records):
    """Build dictionary-based inventory summary views.

    Return keys:
    - qty_by_sku: dictionary mapping sku -> qty
    - low_stock_skus: sorted list where qty < reorder_level
    - category_counts: category -> number of records (missing category -> "uncategorized")
    """
    raise NotImplementedError("Implement build_inventory_views(records)")
