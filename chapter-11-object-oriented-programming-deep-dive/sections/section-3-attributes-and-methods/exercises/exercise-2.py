"""Section 3 Exercise 2: Attributes and Methods.

Implement SupportTicket to practice state changes and simple validation.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_TICKET = {
    "ticket_id": "T-900",
    "title": "Reset payroll export",
    "priority": "high",
    "status": "open",
    "owner": "Luis Gomez",
}

VALID_PRIORITIES = {"low", "medium", "high", "critical"}


class SupportTicket:
    """Represent one support ticket."""

    def __init__(self, ticket_id, title, priority, status="open", owner=None):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def set_priority(self, priority):
        """Update priority after validating it against VALID_PRIORITIES."""
        raise NotImplementedError("Implement set_priority")

    def close(self):
        """Update ticket status to closed."""
        raise NotImplementedError("Implement close")

    def is_urgent(self):
        """Return True for open tickets with priority high or critical."""
        raise NotImplementedError("Implement is_urgent")

    def __str__(self):
        """Return a readable one-line description of the ticket."""
        raise NotImplementedError("Implement __str__")
