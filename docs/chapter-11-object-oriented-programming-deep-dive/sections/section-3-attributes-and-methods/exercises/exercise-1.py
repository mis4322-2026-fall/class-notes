"""Section 3 Exercise 1: Attributes and Methods.

Implement Task so it can update internal state and apply lightweight validation.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_TASK = {
    "task_id": "TASK-17",
    "title": "Prepare invoice aging report",
    "assigned_to": "Rina Patel",
    "estimated_hours": 6.0,
}


class Task:
    """Represent one business task."""

    def __init__(self, task_id, title, assigned_to, estimated_hours):
        raise NotImplementedError("Store the incoming values and initialize status and hours_logged")

    def log_hours(self, hours):
        """Add hours to hours_logged, rejecting non-positive values."""
        raise NotImplementedError("Implement log_hours")

    def mark_complete(self):
        """Update the task status to complete."""
        raise NotImplementedError("Implement mark_complete")

    def is_over_budget(self):
        """Return True when hours_logged exceeds estimated_hours."""
        raise NotImplementedError("Implement is_over_budget")

    def summary(self):
        """Return a dictionary summary of the current task state."""
        raise NotImplementedError("Implement summary")
