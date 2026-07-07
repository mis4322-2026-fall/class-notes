# Section 7.1: Limitations of Native Python Structures

## Overview

This section is a quick setup section. The goal is simple: install NumPy correctly and import it in Python. We only do a lightweight preview of why NumPy helps, then move to full NumPy APIs in Section 2.

## Core Concepts

- NumPy is a third-party package, so it must be installed with `pip`.
- Virtual environments isolate package versions per project.
- Install packages after activating the virtual environment.
- Import NumPy using `import numpy as np`.
- Standard-library modules (`json`, `csv`) need no installation.
- Third-party packages (`requests`, `numpy`, `pandas`) require `pip install`.

## Setup Walkthrough (simple)

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install NumPy (and optionally Pandas for later sections):

```bash
python -m pip install --upgrade pip
pip install numpy pandas
```

Verify import and version:

```bash
python -c "import numpy as np; print(np.__version__)"
```

Import style used throughout this chapter:

```python
import numpy as np
# np is a short alias used in examples
```

Quick sanity check:

```python
import numpy as np

values = np.array([10, 20, 30, 40])
print(values.mean())
# result: 25.0
```

Package distinction reminder:

```python
# Standard library: no pip install needed
import json
import csv

# Third-party: pip install required
import requests
import numpy as np
import pandas as pd
```

Why we care (preview only): NumPy arrays are faster than Python lists for many numeric operations. You will test this in the section exercise.

## Try It (optional)

1. Create a fresh environment named `.venv-ch7`.
2. Install `numpy`.
3. Run `python -c "import numpy as np; print(np.arange(5))"`.
4. Confirm you can explain why `json` does not need pip.

## Summary

Section 1 is about setup confidence: create an environment, install NumPy with pip, and import it successfully. In Section 2, you will learn NumPy array APIs in depth.
