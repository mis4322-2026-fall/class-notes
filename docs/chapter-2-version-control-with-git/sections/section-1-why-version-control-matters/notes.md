# Section 2.1: Why Version Control Matters

## Overview
Students often begin technical work by creating folders with names like `project-final`, `project-final-revised`, and `project-final-real`. That habit makes it hard to tell which version is current and which changes matter. Version control gives a cleaner way to manage progress.

In this course, Git is introduced early because it supports better organization from the start. Students do not need to think of Git as a developer-only tool. It is a practical system for tracking changes, recovering earlier work, and making project history easier to follow.

## Core Concepts
- Version control records how files change over time.
- Git helps replace manual file-copy workflows with a structured history.
- A saved checkpoint in Git is called a commit.
- Version history makes it easier to review progress and recover from mistakes.
- Consistent version tracking supports both solo work and team projects.

## Code Walkthrough (incremental)
Use terminal commands to connect the idea of version control to real project work:

```bash
pwd
ls
git --version
```

Step 1: Run `pwd` to confirm where you are working. Version control starts with knowing which folder represents the project.

Step 2: Run `ls` to inspect the files in that folder. This reinforces that Git tracks ordinary project files rather than a special file format.

Step 3: Run `git --version` to confirm Git is available in the terminal. This shows that Git is a tool students will use alongside Python during the course.

Step 4: Discuss the difference between manual copies of a folder and a repository with a visible change history.

## Try It (optional)
List two risks of managing coursework by duplicating folders manually and two benefits of saving work through version control.

## Summary
Version control is not just about backup. It is about making project change visible, organized, and easier to manage. For students, that means less confusion, better recovery options, and a clearer workflow for the rest of the course.
