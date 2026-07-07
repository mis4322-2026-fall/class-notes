"""Section 4 Exercise 2: Applying Functions and Lambdas in Data Pipelines.

Implement build_team_cost_pipeline(tickets, min_cost).
"""

SAMPLE_TICKETS = [
    {"team": "App", "hours": 4.0, "hourly_rate": 80, "status": "resolved"},
    {"team": "Infra", "hours": 2.0, "hourly_rate": 100, "status": "open"},
    {"team": "App", "hours": 3.5, "hourly_rate": 80, "status": "resolved"},
    {"team": "Data", "hours": 5.0, "hourly_rate": 90, "status": "resolved"},
    {"team": "Infra", "hours": 6.0, "hourly_rate": 100, "status": "resolved"},
]
SAMPLE_MIN_COST = 500


def build_team_cost_pipeline(tickets, min_cost):
    """Build a pipeline report of resolved ticket costs by team.

    Rules:
    - Keep only resolved tickets
    - Cost per ticket = hours * hourly_rate
    - Aggregate cost by team
    - Keep only teams where aggregated cost >= min_cost
    - Return sorted list of tuples (team, cost) by cost descending
    - If two teams have equal cost, sort those ties by team name ascending
    - Use named functions for stages and lambdas for sort/filter where practical
    """
    raise NotImplementedError("Implement build_team_cost_pipeline(tickets, min_cost)")
