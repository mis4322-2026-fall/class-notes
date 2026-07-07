# Section 1.4: Package Management (pip)

## Overview
`pip` is the tool students will use to install the libraries needed for course activities. This section introduces package management as a practical skill, not as a deep software engineering topic.

The emphasis here is on knowing what `pip` does, where packages get installed, and why projects should track dependencies clearly.

## Core Concepts
- `pip` installs packages into the currently active Python environment.
- `requirements.txt` is a simple way to list project dependencies.
- Installing packages inside a virtual environment is safer than installing them globally.
- Clear dependency tracking makes it easier to reproduce class and project work.

## Code Walkthrough (incremental)
Use these commands to see basic package management in action:

```bash
python -m pip --version
python -m pip list
python -m pip install requests
python -m pip freeze
```

Step 1: Check that `pip` is available through the active Python interpreter.

Step 2: List installed packages to see what is already in the environment.

Step 3: Install a package and observe that the environment changes.

Step 4: Use `python -m pip freeze` to see how dependencies can be recorded for reuse.

## Try It (optional)
Answer these reflection questions:

1. Why is it helpful to install packages inside a virtual environment?
2. Why might two students get different results if they install different package versions?
3. What is the value of saving dependencies to a file?

## Summary
At an introductory level, package management means knowing how to add tools to a project environment and how to keep track of what was installed. That foundation supports everything that comes later in the course.
