# Concepts

Chapter 7 introduces NumPy and Pandas as practical tools for business-oriented data processing. In earlier chapters, you used Python lists, dictionaries, functions, files, and API responses. Here, you scale those same ideas to larger numeric workloads and table-shaped datasets that are common in reporting.

## Package and Environment Review (Required Before Coding)

Before using NumPy or Pandas, review package setup basics:

- Use a virtual environment to isolate project dependencies.
- Use `pip` to install third-party packages.
- Import installed packages inside Python code.
- Verify versions so your team works with consistent behavior.

Recommended command flow:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install numpy pandas
python -c "import numpy as np; import pandas as pd; print(np.__version__, pd.__version__)"
```

Important correctness note:

- `json` and `csv` are standard-library modules, so no `pip install` is required.
- `requests`, `numpy`, and `pandas` are third-party packages and must be installed with `pip`.

## Why Native Python Structures Hit Limits

Lists and dictionaries are flexible and excellent for foundational programming. However, for large datasets, they present practical limits:

- Numeric operations require explicit loops and manual accumulation.
- Type consistency is harder to enforce.
- Multi-column analysis and grouping logic becomes verbose.
- Performance often degrades as data size grows.

NumPy and Pandas reduce this friction by providing optimized data structures and high-level APIs.

## NumPy Arrays

NumPy introduces the `ndarray`, a dense, typed, n-dimensional array.

Key ideas:

- A single array stores values in contiguous memory for fast operations.
- Array operations are vectorized, so one expression can process many values.
- `dtype`, `shape`, and broadcasting make numeric transformations explicit and efficient.
- Aggregations (`sum`, `mean`, `min`, `max`) are built in and predictable.

For business contexts, NumPy is useful for fast metric calculations, score normalization, thresholding, and matrix-style transformations.

## Pandas DataFrames

Pandas builds on NumPy and provides labeled tabular structures.

Key ideas:

- A `DataFrame` stores rows and named columns, similar to a worksheet or SQL result.
- A `Series` represents a single column.
- APIs support import/export (`read_csv`, `to_csv`), filtering, sorting, grouping, and reshaping.
- Missing values, mixed column types, and date handling are first-class concerns.

For students, DataFrames map naturally to operational datasets: orders, tickets, invoices, attendance logs, campaign results, and HR records.

## Data Manipulation Workflow in Pandas

A repeatable business workflow usually follows this sequence:

1. Load data from CSV/API/database extracts.
2. Inspect schema (`dtypes`, null counts, sample rows).
3. Clean values and standardize types.
4. Filter and create derived columns.
5. Group and aggregate for KPI summaries.
6. Export prepared results for reporting.

This chapter focuses on practical transformations you can reuse directly in course projects and workplace scripts.
