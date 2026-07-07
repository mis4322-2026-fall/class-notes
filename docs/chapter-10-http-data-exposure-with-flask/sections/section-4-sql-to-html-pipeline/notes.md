# Section 10.4: SQL to HTML Pipeline

## Overview

This section ties the chapter together. A browser requests a page, Flask runs a SQLite query, Python shapes the rows into records, and a template renders those records as HTML.

For convenience, this section includes a ready-to-use SQLite file at `exercises/mis_projects.db` so students can run the SQL-to-HTML flow immediately.

## Core Concepts

- SQLite stores structured data for the application.
- A handler runs a query when the route is requested.
- Query rows are easier to use when shaped into dictionaries.
- Templates render the final HTML table or list.

The full flow looks like this:

`Browser -> /projects request -> Flask handler -> SQLite query -> Python record shaping -> HTML template -> Browser`

That is a practical reporting pattern.

## Code Walkthrough (incremental)

Connect to SQLite and run a small query.

```python
import sqlite3

with sqlite3.connect("mis_projects.db") as conn:
    rows = conn.execute(
        "SELECT project_name, department, budget FROM projects ORDER BY budget DESC"
    ).fetchall()
```

Shape the tuple rows into dictionaries.

```python
records = [
    {"project_name": row[0], "department": row[1], "budget": row[2]}
    for row in rows
]
```

Pass those records into a template.

```python
@app.route("/projects")
def projects():
    records = fetch_project_rows(DB_PATH)
    return render_template("projects.html", records=records)
```

Render the output as an HTML table.

```html
<table>
  <tr>
    <th>Project</th><th>Department</th><th>Budget</th>
  </tr>
  {% for row in records %}
  <tr>
    <td>{{ row.project_name }}</td>
    <td>{{ row.department }}</td>
    <td>{{ row.budget }}</td>
  </tr>
  {% endfor %}
</table>
```

This is the chapter's key bridge: SQL gets the data, Python shapes it, and HTML presents it.

## Try It (optional)

Add a filter so the route shows only one department when a query parameter is present. Keep the same data pipeline, but change the SQL inputs and the template heading.

## Summary

The SQL-to-HTML pipeline is a compact example of how a real reporting page works. A request triggers data retrieval, Python prepares the result, and a template turns the result into something a user can read in the browser.