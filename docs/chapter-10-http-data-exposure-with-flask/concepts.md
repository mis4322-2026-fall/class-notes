# Chapter 10 Concepts: HTTP & Data Exposure with Flask

This chapter uses a web application framing to introduce how business systems expose data to users.

The goal is not deep Flask coverage. The goal is to understand how a request moves through a small server application, how Python code decides what data to return, and how that data becomes a page in the browser.

## A Web App as a Data Pipeline

In a simple web application, the browser sends a request and the server sends back a response.

You can read the basic flow like this:

`Browser -> HTTP request -> Flask route -> Python handler -> data lookup or processing -> HTTP response -> Browser`

For data and operations work, this matters because many internal tools follow the same pattern:

- A user asks for a report.
- The application reads user input.
- The server queries data.
- Python shapes the result.
- The application renders a page or returns a structured payload.

## Narrow Flask Surface Area

We keep API coverage intentionally small:

- `Flask(...)` to create the application object
- `@app.route(...)` to connect a URL to a handler
- `request.args` for query string data
- `request.form` for submitted form data
- `render_template(...)` for server-side HTML rendering
- Basic `GET` and `POST` handling

This is enough to teach the important ideas without turning the chapter into a framework reference.

## Static vs Dynamic Responses

A static response always returns the same content.

Example:

```python
@app.route("/")
def home():
    return "Operations portal online"
```

A dynamic response changes based on input or data.

```python
@app.route("/hello")
def hello():
    name = request.args.get("name", "Analyst")
    return f"Hello, {name}"
```

The second example shows why web apps are useful: the same route can respond differently depending on what the user sends.

## Templates as a Separation Layer

Handlers should gather data and make simple decisions. Templates should control presentation.

That division keeps responsibilities clearer:

- Python code prepares data.
- HTML templates display data.

This is especially useful when rendering lists, tables, and report-style output for business users.

## SQLite in a Web Workflow

SQLite is a practical teaching choice because it is lightweight and file-based.

A minimal reporting flow looks like this:

1. A browser requests a page such as `/projects`.
2. The Flask handler runs a SQL query against SQLite.
3. The query rows are shaped into dictionaries.
4. The dictionaries are passed into an HTML template.
5. The browser receives a rendered page.

This is the same conceptual pipeline used by many larger systems, just with less infrastructure.