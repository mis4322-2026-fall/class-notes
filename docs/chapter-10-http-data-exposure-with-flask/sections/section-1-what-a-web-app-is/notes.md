# Section 10.1: What a Web App Is

## Overview

This section introduces the web application as a system of requests, decisions, and responses. The emphasis is conceptual: what the browser does, what the server does, and how a route and handler fit between them.

## Core Concepts

- The browser sends an HTTP request to a server.
- A route matches the requested URL.
- A handler function runs Python code for that route.
- The handler returns a response.
- Static responses stay the same; dynamic responses depend on input or data.

You can picture the flow like this:

`Browser -> request -> route -> handler -> response -> Browser`

That model is simple, but it is enough to explain dashboards, report pages, search screens, and internal business tools.

## Code Walkthrough (incremental)

Create a minimal Flask app object.

```python
from flask import Flask

app = Flask(__name__)
```

Add one static route.

```python
@app.route("/")
def home():
    return "Operations portal online"
```

When the browser asks for `/`, Flask finds the route and runs `home()`.

Add a dynamic route.

```python
@app.route("/snapshot")
def snapshot():
    active_projects = 4
    return f"Active projects: {active_projects}"
```

This route still returns text, but now the response is built from Python data.

Compare the two responses:

- `/` always returns the same message.
- `/snapshot` builds a response using current values.

That difference is the starting point for understanding web applications.

## Try It (optional)

Sketch your own route map for an internal business tool. Include one static page and two dynamic pages. For each page, note what input it might read and what output it should return.

## Summary

A web app is a request/response system. The browser asks for something, the server decides what code to run, and the handler returns a response. Routes and handlers are the basic pieces that make that happen.