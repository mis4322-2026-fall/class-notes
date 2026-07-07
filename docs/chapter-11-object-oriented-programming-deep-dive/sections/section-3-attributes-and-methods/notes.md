# Section 11.3: Attributes and Methods

## Overview

Once a class exists, the next question is how objects behave over time. This section focuses on instance attributes, methods that read and update state, and lightweight validation that keeps invalid business values out of an object.

## Core Concepts

- Instance attributes hold the current state of one object.
- Methods can read and update that state through `self`.
- State changes should be intentional and easy to trace.
- Lightweight validation keeps bad inputs from silently corrupting a business entity.
- String representations make object state easier to inspect during development and reporting.

## Code Walkthrough (incremental)

Start with a task object that stores state.

```python
class Task:
    def __init__(self, task_id, title, estimated_hours):
        self.task_id = task_id
        self.title = title
        self.estimated_hours = estimated_hours
        self.hours_logged = 0
        self.status = "open"
```

Add a method that updates state.

```python
class Task:
    def __init__(self, task_id, title, estimated_hours):
        self.task_id = task_id
        self.title = title
        self.estimated_hours = estimated_hours
        self.hours_logged = 0
        self.status = "open"

    def log_hours(self, hours):
        self.hours_logged += hours
```

That method works, but it accepts invalid input. Add validation.

```python
def log_hours(self, hours):
    if hours <= 0:
        raise ValueError("hours must be positive")
    self.hours_logged += hours
```

Add another method that changes state in a different way.

```python
def mark_complete(self):
    self.status = "complete"
```

Now the object can answer business questions about itself.

```python
def is_over_budget(self):
    return self.hours_logged > self.estimated_hours
```

The important pattern is simple: the object owns the data, and its methods own the rules for changing that data.

## Try It (optional)

Create a small `SupportTicket` class with `priority`, `status`, and a method that rejects invalid priority values. Then add one method that closes the ticket and another that reports whether it is urgent.

## Summary

Attributes hold state, and methods manage that state. When validation and updates live inside the class, the business model becomes safer and easier to understand.
