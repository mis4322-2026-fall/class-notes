"""Section 2 Exercise 2: Function Design for Lists and Dictionaries.

Implement build_team_workload_report(tickets).
"""

SAMPLE_TICKETS = [
    {"team": "App", "hours": 6.5, "priority": "high"},
    {"team": "Infra", "hours": 3.0, "priority": "medium"},
    {"team": "App", "hours": 2.5, "priority": "low"},
    {"team": "Infra", "hours": 5.0, "priority": "high"},
    {"team": "Data", "hours": 4.0, "priority": "medium"},
]


def build_team_workload_report(tickets):
    """Return workload metrics grouped by team.

    Return a dictionary keyed by team with values:
    - ticket_count
    - total_hours (rounded to 2 decimals)
    - high_priority_count
    - average_hours (rounded to 2 decimals)
    """
    raise NotImplementedError("Implement build_team_workload_report(tickets)")
