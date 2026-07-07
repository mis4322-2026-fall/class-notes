"""Section 2 Exercise 1: Classes and Objects.

Implement Product so it can be instantiated and inspected like a small inventory entity.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_PRODUCT = {
    "sku": "P-410",
    "name": "Barcode Scanner",
    "unit_price": 89.5,
    "quantity_on_hand": 6,
}


class Product:
    """Represent one product in inventory."""

    def __init__(self, sku, name, unit_price, quantity_on_hand):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def inventory_value(self):
        """Return unit_price multiplied by quantity_on_hand."""
        raise NotImplementedError("Implement inventory_value")

    def snapshot(self):
        """Return a dictionary snapshot of the product state."""
        raise NotImplementedError("Implement snapshot")

    def __str__(self):
        """Return a readable one-line description of the product."""
        raise NotImplementedError("Implement __str__")
