"""Section 1 Exercise 2: Lists as Ordered Data.

Implement build_priority_queue(tasks, urgent_tasks, resolved_task).
"""

SAMPLE_TASKS = [
    "approve_budget",
    "reconcile_invoices",
    "refresh_dashboard",
]
SAMPLE_URGENT_TASKS = ["close_month_end", "review_vendor_contract"]
SAMPLE_RESOLVED_TASK = "reconcile_invoices"


def build_priority_queue(tasks, urgent_tasks, resolved_task):
    """Return queue views after realistic list updates.

    Steps:
    - Start with a copy of tasks.
    - Insert urgent tasks at the beginning in the same order given.
    - Remove resolved_task once if it exists.

    Return a dictionary with keys:
    - queue: final queue list
    - top_three: first 3 items from queue
    - alphabetical: sorted queue list
    - queue_size: number of tasks in queue
    """
    raise NotImplementedError("Implement build_priority_queue(tasks, urgent_tasks, resolved_task)")
