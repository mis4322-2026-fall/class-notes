# Section 2.3: Core Git Workflow

## Overview
Once a repository exists, students need a repeatable way to work inside it. The core Git workflow is the routine of checking what changed, selecting what should be saved, and recording a clear checkpoint.

This workflow appears throughout the rest of the course. Students should leave this section understanding the order of common Git actions and the purpose of each step.

## Core Concepts
- The working directory contains current project files.
- Staging is the step where students choose which changes are prepared for the next commit.
- A commit is a saved checkpoint with a message explaining the change.
- `git status` helps students decide what to do next.
- `git log` shows previously saved checkpoints.

## Code Walkthrough (incremental)
Use the most common workflow commands in order:

```bash
git status
git add README.md
git commit -m "Add project notes"
git log --oneline
```

Step 1: Run `git status` to inspect the current state before saving anything.

Step 2: Run `git add README.md` to prepare one file for the next checkpoint. This introduces staging as a deliberate selection step.

Step 3: Run `git commit -m "Add project notes"` to save the staged change with a short, meaningful message.

Step 4: Run `git log --oneline` to confirm that the repository now contains visible history.

Step 5: Discuss why short, specific commit messages are more useful than vague messages such as `update`.

## Try It (optional)
Think of a small file change and write two possible commit messages for it: one vague and one clear. Explain which message would be more useful later.

## Summary
The core Git workflow is a repeated pattern: inspect changes, stage intentionally, commit clearly, and review history when needed. This routine helps students manage project progress without relying on memory or duplicate folders.
