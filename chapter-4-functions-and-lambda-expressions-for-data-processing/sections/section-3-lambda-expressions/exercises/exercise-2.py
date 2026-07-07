"""Section 3 Exercise 2: Lambda Expressions.

Implement rank_customers_by_score(customers, min_score).
"""

SAMPLE_CUSTOMERS = [
    {"name": "Acme", "score": 91, "region": "North"},
    {"name": "Blue Harbor", "score": 84, "region": "West"},
    {"name": "Crown Foods", "score": 96, "region": "North"},
    {"name": "Delta Office", "score": 73, "region": "South"},
]
SAMPLE_MIN_SCORE = 85


def rank_customers_by_score(customers, min_score):
    """Return ranked customer names by score.

    Rules:
    - Keep only customers with score >= min_score
    - Sort by score descending; tie-break by name ascending
    - Return list of names
    - Use lambda expressions for filtering and sorting
    """
    raise NotImplementedError("Implement rank_customers_by_score(customers, min_score)")
