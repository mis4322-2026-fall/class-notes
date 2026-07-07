# Section 2.4: Git in Python Projects

## Overview
As the course progresses, students will work with Python files, dependency lists, documentation, and possibly data files. Git helps keep those project parts organized. It also provides a reliable history when a project changes over time.

This section connects Git to the kind of Python coursework students will complete in later chapters. The focus is not on advanced repository design. The focus is on using Git to support a clean, understandable class project.

## Core Concepts
- Git can track Python scripts, Markdown files, and dependency files together.
- A repository helps show when project setup changes, not just when code changes.
- Meaningful commit history makes troubleshooting easier.
- Project files such as `README.md` and `requirements.txt` are important parts of the repository.
- Good Git habits support reproducibility and collaboration.

## Code Walkthrough (incremental)
Use commands that reflect a simple Python project folder:

```bash
ls
git status
git add README.md requirements.txt
git commit -m "Track project documentation and dependencies"
```

Step 1: Run `ls` to identify common Python project files in the folder.

Step 2: Run `git status` to see which project files are new or changed.

Step 3: Run `git add README.md requirements.txt` to stage project-support files that matter for setup and reproducibility.

Step 4: Run `git commit -m "Track project documentation and dependencies"` to save a checkpoint that explains a meaningful project-level change.

Step 5: Discuss why tracking setup files is useful when another person needs to understand or run the project later.

## Try It (optional)
Look at a Python project folder and identify three files you would want Git to track from the beginning. Explain why each file matters.

## Summary
Git supports more than source code. In Python projects, it helps students manage scripts, setup files, and documentation as one organized unit. That foundation will make later technical work easier to maintain and easier to share.
