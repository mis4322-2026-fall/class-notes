"""Section 1 Exercise 1: Why OOP Exists.

Implement CustomerRecord to show how a class can hold both customer data and customer-related behavior.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_CUSTOMER = {
    "customer_id": "C-104",
    "name": "Northwind Office Supply",
    "credit_limit": 5000.0,
    "balance": 4200.0,
    "is_active": True,
}


class CustomerRecord:
    """Represent one row-like customer entity."""

    def __init__(self, customer_id, name, credit_limit, balance, is_active=True):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def remaining_credit(self):
        """Return remaining available credit rounded to 2 decimals."""
        raise NotImplementedError("Implement remaining_credit")

    def is_over_limit(self):
        """Return True when balance exceeds credit_limit."""
        raise NotImplementedError("Implement is_over_limit")

    def summary(self):
        """Return a dictionary summary of the customer record."""
        raise NotImplementedError("Implement summary")
