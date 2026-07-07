"""Section 2 Exercise 1: Loops and List Comprehensions.

Implement build_amount_report(amounts, high_threshold).
"""

SAMPLE_AMOUNTS = [45.0, None, 120.5, -5, 510.0, 85.25, 999.0]
SAMPLE_HIGH_THRESHOLD = 500


def build_amount_report(amounts, high_threshold):
    """Return cleaned values, category labels, and high-value count.

    Rules:
    - Ignore None and negative values.
    - Round kept values to 2 decimals.
    - Category per kept value:
      - low: < 100
      - medium: >= 100 and < high_threshold
      - high: >= high_threshold

    Return keys:
    - valid_amounts
    - categories
    - high_value_count
    """
    raise NotImplementedError("Implement build_amount_report(amounts, high_threshold)")
