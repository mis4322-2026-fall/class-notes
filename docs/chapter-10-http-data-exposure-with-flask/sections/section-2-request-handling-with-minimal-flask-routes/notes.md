# Section 10.2: Request Handling with Minimal Flask Routes

## Overview

This section shows how handlers receive user input. We keep the scope narrow: query parameters, form data, and the difference between GET and POST.

## Core Concepts

- `GET` usually asks for data or a page.
- Query parameters are attached to the URL, such as `/search?department=IT`.
- `POST` is commonly used when a form submits data for processing.
- Flask exposes request data through the `request` object.

Think of the data flow this way:

- User enters input in the browser.
- The browser sends that input with the HTTP request.
- Flask reads the input in the handler.
- The handler decides what response to build.

## Code Walkthrough (incremental)

Import the minimal Flask APIs used in this section.

```python
from flask import Flask, request

app = Flask(__name__)
```

Read a query parameter from a GET request.

```python
@app.route("/department")
def department():
    name = request.args.get("name", "Operations")
    return f"Department: {name}"
```

If the browser requests `/department?name=Finance`, the response becomes `Department: Finance`.

Handle both GET and POST for a small form workflow.

```python
@app.route("/budget", methods=["GET", "POST"])
def budget():
    if request.method == "POST":
        amount = request.form.get("amount", "0")
        return f"Submitted budget: {amount}"
    return "Send a POST request with budget data"
```

This pattern is common in internal business applications:

- GET shows the page or instructions.
- POST carries submitted values.

## Try It (optional)

Change the example so the GET route reads two query parameters instead of one. Then design a POST example that accepts a month and a budget amount.

## Summary

Handlers become useful when they can read request data. Query parameters support lightweight filtering, while POST form data supports simple submission workflows.