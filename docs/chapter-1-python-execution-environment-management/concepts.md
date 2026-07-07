# Concepts

## Why Execution Environments Matter
In this course, Python is not just a programming language. It is also a tool students will run from a terminal, connect to packages, and use across different projects. That means students need a simple mental model for what Python is, where it runs, and why setup matters.

For learners, this chapter is about working comfortably with the Python environment rather than writing complex programs. The goal is to understand the parts students will interact with throughout the class: the Python executable, virtual environments, and package installation.

## Python Runtime Model
At a high level, Python follows a basic flow:

1. A user runs Python
2. Python reads instructions from a file or command
3. Python attempts to execute those instructions

For this chapter, students do not need an internal systems view of bytecode or the Python Virtual Machine. What matters is recognizing that some problems happen before a program starts and others happen while it is running.

## Interpreter Modes in Practice
The Python interpreter can be used in several practical ways:

- Run a script file
- Run a module with `python -m`
- Run a short one-line command with `python -c`
- Open an interactive session

Students should understand these as different ways to access the same Python installation. The focus is not on implementation details, but on knowing when each mode is useful.

## Virtual Environments (`venv`)
A virtual environment gives a project its own isolated Python package space. This helps students avoid conflicts between class exercises, personal experiments, and future projects.

The key idea is simple: instead of installing everything globally, each project can keep its own tools and libraries.

Students should leave this chapter knowing why virtual environments exist, how to create one, and how to tell whether it is active.

## Package Management (`pip`)
`pip` is the standard tool for installing Python packages. In this course, students will use it to add the libraries needed for later chapters.

At a foundations level, the important ideas are:

- Packages are installed into a specific Python environment
- A project can keep track of its dependencies in `requirements.txt`
- Careful package management makes it easier to reproduce results on another machine
