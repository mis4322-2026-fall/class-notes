"""Section 4 Exercise 2: Modeling Data with Classes.

Implement Project and Task so a project can manage a collection of related task objects.
Use the explicit sample constants below while developing your solution.
"""

SAMPLE_PROJECT = {
    "project_id": "PR-88",
    "name": "ERP Rollout",
    "owner": "Maya Chen",
}

SAMPLE_TASK_ROWS = [
    {"task_id": "TK-1", "title": "Map legacy fields", "completed": True},
    {"task_id": "TK-2", "title": "Review budget variance", "completed": False},
    {"task_id": "TK-3", "title": "Prepare training memo", "completed": False},
]


class Task:
    """Represent one project task."""

    def __init__(self, task_id, title, completed=False):
        raise NotImplementedError("Store the incoming values as instance attributes")

    def mark_complete(self):
        """Update the task so completed becomes True."""
        raise NotImplementedError("Implement mark_complete")


class Project:
    """Represent one project entity that owns multiple tasks."""

    def __init__(self, project_id, name, owner, tasks=None):
        raise NotImplementedError("Store the incoming values and initialize tasks safely")

    def add_task(self, task):
        """Append a Task object to this project."""
        raise NotImplementedError("Implement add_task")

    def completion_rate(self):
        """Return the completion percentage rounded to 2 decimals."""
        raise NotImplementedError("Implement completion_rate")

    def open_task_titles(self):
        """Return titles for tasks that are not yet complete."""
        raise NotImplementedError("Implement open_task_titles")

    def snapshot(self):
        """Return a dictionary summary of the project state."""
        raise NotImplementedError("Implement snapshot")


def build_project(project_row, task_rows):
    """Build a Project object from row-like project and task dictionaries."""
    raise NotImplementedError("Implement build_project")
