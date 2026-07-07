"""Section 1 Exercise 1: Match business questions to chart types.

This is a light coding exercise focused on chart choice, not plotting complexity.

Task:
1) Complete recommend_chart_type so each scenario returns one of:
   - "line"
   - "bar"
   - "scatter"
2) Run this file and review the printed recommendations.
3) For each scenario, write one sentence explaining why the recommendation fits.
"""

SCENARIOS = [
    {
        "name": "Monthly Revenue Trend",
        "question": "How has monthly revenue changed from January to June?",
        "x_type": "time",
        "y_type": "numeric",
    },
    {
        "name": "Sales by Region",
        "question": "Which region has the highest total sales this quarter?",
        "x_type": "category",
        "y_type": "numeric",
    },
    {
        "name": "Marketing Spend and Signups",
        "question": "Do higher campaign budgets tend to align with more signups?",
        "x_type": "numeric",
        "y_type": "numeric",
    },
    {
        "name": "Tickets by Team",
        "question": "Which support team handled the most tickets?",
        "x_type": "category",
        "y_type": "numeric",
    },
]


def recommend_chart_type(scenario):
    """Return a basic chart type based on simple field rules."""
    if scenario["x_type"] == "time":
        return "line"
    if scenario["x_type"] == "category":
        return "bar"
    return "scatter"


def build_recommendations(scenarios):
    """Return (scenario_name, chart_type) pairs."""
    return [(item["name"], recommend_chart_type(item)) for item in scenarios]


if __name__ == "__main__":
    for name, chart in build_recommendations(SCENARIOS):
        print(f"{name}: {chart}")
