# Section 2.2: Repository Lifecycle

## Overview
A repository does not begin as a complex system. It usually starts as a normal project folder, then becomes tracked by Git. From there, the repository grows as files are added, updated, reviewed, and saved over time.

This section gives students a practical sense of the repository lifecycle. The goal is to understand how a Git-tracked folder moves from setup into regular use, not to master every Git feature.

## Core Concepts
- A repository starts when Git tracking is initialized in a folder.
- Files can exist in different states, such as untracked, changed, or committed.
- `git status` is the main command for understanding the current repository state.
- Repositories develop through repeated cycles of change and review.
- A repository history becomes more useful when commits are made consistently.

## Code Walkthrough (incremental)
Use a simple command sequence to observe how a repository begins:

```bash
mkdir git-practice
cd git-practice
git init
git status
```

Step 1: Create a new folder to represent a project workspace.

Step 2: Move into the folder so commands apply to the correct location.

Step 3: Run `git init` to turn the folder into a Git repository.

Step 4: Run `git status` to see the repository state before any files are added. This is the main reference point for understanding repository lifecycle changes.

Step 5: Add a simple file such as `README.md`, then run `git status` again and observe how Git reports the new file.

## Try It (optional)
Create a small practice folder, initialize Git, add one file, and describe how the `git status` output changes between each step.

## Summary
A repository lifecycle begins with initialization and continues through repeated updates. Students do not need advanced Git concepts yet. They need to understand that repositories are ordinary project folders with a structured process for tracking change.
