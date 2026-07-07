"""Section 4 Exercise 1: Modeling Data with Classes.

Implement Customer and Invoice so row-like dictionaries can be turned into related objects.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_CUSTOMER_ROW = {
    "customer_id": "C-220",
    "name": "Acme Health",
    "segment": "enterprise",
}

SAMPLE_INVOICE_ROWS = [
    {"invoice_id": "INV-2201", "amount": 800.0, "paid": False},
    {"invoice_id": "INV-2202", "amount": 450.0, "paid": True},
]


class Customer:
    """Represent one customer entity."""

    def __init__(self, customer_id, name, segment):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def __str__(self):
        """Return a readable customer label."""
        raise NotImplementedError("Implement __str__")


class Invoice:
    """Represent one invoice entity related to a Customer object."""

    def __init__(self, invoice_id, customer, amount, paid=False):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def amount_due(self):
        """Return 0 when paid, otherwise the full amount."""
        raise NotImplementedError("Implement amount_due")

    def mark_paid(self):
        """Update the invoice so it is marked as paid."""
        raise NotImplementedError("Implement mark_paid")

    def export_row(self):
        """Return a row-like dictionary for reporting or persistence."""
        raise NotImplementedError("Implement export_row")


def build_invoice_objects(customer_row, invoice_rows):
    """Return Invoice objects that all reference the same Customer object."""
    raise NotImplementedError("Implement build_invoice_objects")
