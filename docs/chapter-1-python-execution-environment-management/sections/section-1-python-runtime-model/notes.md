# Section 1.1: Python Runtime Model

## Overview
Students often treat Python as a black box: type a command, hope it runs, and only think about setup when something breaks. This section introduces a simpler view. Python is a program that reads instructions and tries to execute them.

For an introductory course, the goal is not to study Python internals. The goal is to build a working mental model of what happens when someone runs Python from the terminal.

## Core Concepts
- Python must be installed before it can be used.
- The Python interpreter is the executable that runs Python commands and files.
- Some errors happen before a program starts because the instructions are not valid.
- Other errors happen while a program is already running.
- Understanding this distinction makes troubleshooting less frustrating.

## Code Walkthrough (incremental)
Use commands to observe Python at a high level:

```bash
python --version
python
```

Step 1: Run `python --version` to confirm that Python is installed and available from the terminal.

Step 2: Run `python` by itself to open the interactive interpreter. This demonstrates that Python is an executable program, not just a file type.

Step 3: Exit the interpreter and discuss what happened: the system launched Python, waited for instructions, and returned control when the session ended.

## Try It (optional)
Write two plain-language examples:

1. A situation where Python cannot start a task because the instruction is invalid
2. A situation where Python starts a task but fails while running it

## Summary
Students do not need a deep internal model of Python yet. They need to know that Python is something they run, that it reads instructions, and that startup problems and run-time problems are not the same kind of issue.
