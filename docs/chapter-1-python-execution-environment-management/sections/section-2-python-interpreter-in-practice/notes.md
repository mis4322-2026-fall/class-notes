# Section 1.2: Python Interpreter in Practice

## Overview
The Python interpreter can be used in several different ways. Early in the course, students should be comfortable recognizing these entry points and understanding why one might be used instead of another.

This section stays practical: the emphasis is on common terminal commands, not on program structure.

## Core Concepts
- Script mode runs a Python file.
- Module mode uses `python -m` to run a module or tool that is installed in the environment.
- Command mode uses `python -c` for a short one-line instruction.
- Interactive mode opens a live Python session.
- Different modes are useful for different classroom and business tasks.

## Code Walkthrough (incremental)
Use these commands to see the modes in practice:

```bash
python --version
python -c "print('hello from python')"
python -m pip --version
python
```

Step 1: Use `python --version` to confirm which Python executable you are using.

Step 2: Use `python -c` to run one short command without creating a file.

Step 3: Use `python -m pip --version` to see module mode in practice. This shows that Python can run an installed tool through the interpreter.

Step 4: Run `python` to open the interactive session and compare it to the other modes.

## Try It (optional)
Match each task below to the best interpreter mode and explain your choice:

1. Quick one-line test
2. Running a saved class exercise file
3. Installing or checking a Python tool
4. Exploring Python interactively during a lab

## Summary
Students should leave this section recognizing that the Python executable can be used in more than one way. The main goal is confidence with the command patterns they will keep seeing throughout the course.
