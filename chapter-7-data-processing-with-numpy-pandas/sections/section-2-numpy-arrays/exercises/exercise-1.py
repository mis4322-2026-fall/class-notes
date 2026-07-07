"""Section 2 Exercise 1: NumPy Branch Performance Metrics.

Implement analyze_branch_performance(sales_matrix).
"""

import numpy as np

SAMPLE_SALES_MATRIX = np.array([
    [1200, 1320, 1280, 1400],
    [980, 1025, 1100, 1150],
    [1500, 1490, 1530, 1600],
], dtype=float)


def analyze_branch_performance(sales_matrix):
    """Compute branch and week metrics from a 2D sales matrix.

    Args:
        sales_matrix: 2D NumPy array where rows=branches and columns=weeks

    Returns:
        {
            "shape": (rows, cols),
            "weekly_totals": np.ndarray,
            "branch_averages": np.ndarray,
            "overall_total": float,
            "top_branch_index": int
        }
    """
    raise NotImplementedError("Implement analyze_branch_performance(sales_matrix)")
