"""Section 1 Exercise 2: Why OOP Exists.

Implement InvoiceRecord to keep invoice data and invoice-specific behavior together.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_INVOICE = {
    "invoice_id": "INV-3001",
    "customer_id": "C-104",
    "amount": 1250.0,
    "tax_rate": 0.07,
    "paid": False,
}


class InvoiceRecord:
    """Represent one invoice entity and its core behaviors."""

    def __init__(self, invoice_id, customer_id, amount, tax_rate, paid=False):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def total_with_tax(self):
        """Return invoice amount including tax, rounded to 2 decimals."""
        raise NotImplementedError("Implement total_with_tax")

    def status_label(self):
        """Return PAID when paid is True, otherwise OPEN."""
        raise NotImplementedError("Implement status_label")

    def as_row(self):
        """Return a row-like dictionary representation of the invoice."""
        raise NotImplementedError("Implement as_row")
