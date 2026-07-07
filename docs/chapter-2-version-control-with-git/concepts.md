# Concepts

## Why Git Belongs Early in the Course
Git is a version control system. It helps students keep track of how files change over time. In an business context, that matters because projects often evolve through revisions, corrections, and collaboration. Instead of replacing files manually or keeping multiple confusing copies, Git provides a structured record of what changed and when.

For this chapter, Git should be understood as a workflow tool rather than a deep software engineering topic. Students are learning how to manage project progress, reduce mistakes, and maintain clearer project history.

## A Simple Mental Model
Git is easiest to understand as three connected ideas:

1. A folder contains project files.
2. Git watches changes made inside that folder.
3. Students choose which changes to save as checkpoints called commits.

This model is enough to support the rest of the course. Students do not need advanced internals yet. They need confidence with the basic sequence of checking status, preparing changes, and saving a meaningful checkpoint.

## Repositories as Project Containers
A Git repository is a project folder that Git can track. Once a repository is created, Git can report what is new, what has changed, and what has already been saved.

Typical early commands look like this:

```bash
git init
git status
git add .
git commit -m "Initial project setup"
```

These commands are not meant to be memorized all at once. The main goal is to recognize the flow: create a repository, inspect changes, stage work, and save a checkpoint.

## Why This Matters in Python Projects
As students move deeper into Python, their work will include scripts, data files, dependency lists, and documentation. Git helps keep those artifacts organized. If something breaks, Git history can help identify when the change happened. If a project needs to be shared, Git makes the folder structure and file history easier to understand.

For learners, the practical value is straightforward:

- less confusion from duplicate folders
- easier recovery after mistakes
- clearer progress over time
- better preparation for team-based technical work

## Scope for This Foundations Chapter
This chapter focuses on introductory Git usage:

- why version control matters
- how a repository begins and develops
- what the everyday Git workflow looks like
- how Git fits into a Python course project

Students do not need branching strategies, merge conflict resolution, or remote collaboration in depth yet. The priority is building a stable baseline workflow they can use throughout the course.
