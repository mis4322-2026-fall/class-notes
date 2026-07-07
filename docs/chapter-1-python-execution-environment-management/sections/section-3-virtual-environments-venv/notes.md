# Section 1.3: Virtual Environments (venv)

## Overview
Virtual environments are one of the most important setup habits in Python. They help students keep one project's packages separate from another project's packages.

At this stage, students do not need deep implementation details. They need to understand what a virtual environment is for and how to work with one confidently.

## Core Concepts
- A virtual environment is a project-specific Python setup.
- Activating the environment changes which `python` and `pip` commands the shell uses.
- This helps avoid package conflicts between projects.
- Virtual environments make class work easier to reproduce.

## Code Walkthrough (incremental)
Use these commands as a standard setup sequence:

```bash
python -m venv .venv
source .venv/bin/activate
python --version
python -m pip --version
deactivate
```

Step 1: Create a virtual environment for the project with `python -m venv .venv`.

Step 2: Activate it so the shell starts using that environment's Python tools.

Step 3: Check `python --version` and `python -m pip --version` to confirm the active environment is the one you expect.

Step 4: Run `deactivate` when you are finished.

## Try It (optional)
Create a short checklist for yourself:

1. How do you create the environment?
2. How do you activate it?
3. How do you know it is active?
4. How do you leave it?

## Summary
Students should think of a virtual environment as a clean workspace for Python packages. It keeps projects separate and reduces avoidable setup problems during the course.
