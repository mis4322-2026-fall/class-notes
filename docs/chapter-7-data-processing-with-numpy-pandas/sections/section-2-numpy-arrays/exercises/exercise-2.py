"""Section 2 Exercise 2: Growth Projection and Target Flags.

Implement project_growth_and_flags(sales_matrix, growth_rate, target).
"""

import numpy as np

SAMPLE_SALES_MATRIX = np.array([
    [200, 240, 260],
    [180, 190, 210],
    [300, 320, 310],
], dtype=float)

SAMPLE_GROWTH_RATE = 0.10
SAMPLE_TARGET = 250.0


def project_growth_and_flags(sales_matrix, growth_rate, target):
    """Apply growth projection and compute target flags.

    Returns:
        {
            "projected": np.ndarray,
            "met_target_flags": np.ndarray,  # same shape, values "met" or "below"
            "met_target_count": int,
            "max_projected": float
        }
    """
    raise NotImplementedError(
        "Implement project_growth_and_flags(sales_matrix, growth_rate, target)"
    )
