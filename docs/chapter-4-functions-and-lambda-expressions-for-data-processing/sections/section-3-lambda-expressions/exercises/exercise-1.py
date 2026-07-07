"""Section 3 Exercise 1: Lambda Expressions.

Implement select_profitable_products(products, min_margin).
"""

SAMPLE_PRODUCTS = [
    {"name": "Laptop", "cost": 650, "price": 900},
    {"name": "Mouse", "cost": 12, "price": 25},
    {"name": "Desk", "cost": 110, "price": 150},
    {"name": "Monitor", "cost": 140, "price": 240},
]
SAMPLE_MIN_MARGIN = 80


def select_profitable_products(products, min_margin):
    """Filter and rank products by margin, then return product names.

    Rules:
    - Margin = price - cost
    - Keep products where margin >= min_margin
    - Sort kept products by margin descending
    - Return list of names in sorted order
    - Use at least one lambda expression
    """
    raise NotImplementedError("Implement select_profitable_products(products, min_margin)")
