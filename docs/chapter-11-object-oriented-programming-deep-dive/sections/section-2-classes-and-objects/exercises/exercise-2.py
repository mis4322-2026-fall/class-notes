"""Section 2 Exercise 2: Classes and Objects.

Implement EmployeeProfile to practice object instantiation and state inspection.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_EMPLOYEE = {
    "employee_id": "E-204",
    "full_name": "Jordan Lee",
    "department": "Finance",
    "title": "Senior Analyst",
    "manager": "Dana Holt",
}


class EmployeeProfile:
    """Represent one employee profile."""

    def __init__(self, employee_id, full_name, department, title, manager=None):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def profile(self):
        """Return a dictionary representation of the employee state."""
        raise NotImplementedError("Implement profile")

    def email_alias(self):
        """Return a simple department-based email alias."""
        raise NotImplementedError("Implement email_alias")

    def __repr__(self):
        """Return a detailed developer-friendly representation."""
        raise NotImplementedError("Implement __repr__")
