"""Section 1 Exercise: Compare Python list vs NumPy array performance.

Goal:
- Create one large list of numbers
- Measure time to compute the square of each value using a Python list comprehension
- Measure time to compute the square of each value using a NumPy vectorized operation
- Print both timings and a simple speedup ratio

No unit tests are required for this exercise.
"""

import time
import numpy as np

SAMPLE_SIZE = 1_000_000


def compare_list_vs_numpy_performance(size=SAMPLE_SIZE):
    """Return timing results for list vs NumPy squaring.

    Returns a dictionary with:
    - list_seconds
    - numpy_seconds
    - speedup (list_seconds / numpy_seconds)
    """
    values_list = list(range(size))

    list_start = time.perf_counter()
    squared_list = [x * x for x in values_list]
    list_seconds = time.perf_counter() - list_start

    values_array = np.array(values_list)

    numpy_start = time.perf_counter()
    squared_array = values_array * values_array
    numpy_seconds = time.perf_counter() - numpy_start

    if numpy_seconds == 0:
        speedup = float("inf")
    else:
        speedup = list_seconds / numpy_seconds

    # Keep outputs referenced so students can inspect behavior if needed.
    _ = squared_list[0], squared_array[0]

    return {
        "list_seconds": list_seconds,
        "numpy_seconds": numpy_seconds,
        "speedup": speedup,
    }


if __name__ == "__main__":
    results = compare_list_vs_numpy_performance()
    print(f"List time:  {results['list_seconds']:.6f} sec")
    print(f"NumPy time: {results['numpy_seconds']:.6f} sec")
    print(f"Speedup:    {results['speedup']:.2f}x")
