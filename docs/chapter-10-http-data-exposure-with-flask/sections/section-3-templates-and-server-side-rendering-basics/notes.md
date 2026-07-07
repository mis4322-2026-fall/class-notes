# Section 10.3: Templates and Server-Side Rendering Basics

## Overview

This section explains how Python data becomes HTML. The important idea is separation: handlers prepare data, while templates describe how that data should appear in the browser.

## Core Concepts

- A handler can pass variables into an HTML template.
- The template decides how to display those values.
- Server-side rendering means the server builds the HTML before sending it to the browser.
- Templates are useful for report summaries, lists, and tables.

This keeps the workflow readable:

`request -> handler -> Python data -> template -> HTML response`

## Code Walkthrough (incremental)

Import the minimal template helper.

```python
from flask import Flask, render_template

app = Flask(__name__)
```

Prepare a small set of records in Python.

```python
projects = [
    {"name": "ERP rollout", "owner": "Nina"},
    {"name": "Budget dashboard", "owner": "Ravi"},
]
```

Pass those records into a template.

```python
@app.route("/projects")
def projects_view():
    return render_template("projects.html", projects=projects)
```

In the template, loop over the records.

```html
<ul>
  {% for project in projects %}
    <li>{{ project.name }} - {{ project.owner }}</li>
  {% endfor %}
</ul>
```

The handler does not hard-code HTML for every row. It passes data to the template, and the template repeats the display pattern.

## Try It (optional)

Add one more field such as status or priority and update the template to show it. Then decide whether that formatting belongs in Python or in HTML.

## Summary

Templates turn Python data into browser output. In a simple Flask app, the handler prepares values and `render_template(...)` sends those values into an HTML structure.