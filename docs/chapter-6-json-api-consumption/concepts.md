# Concepts

Chapter 6 introduces JSON as a universal data format and APIs as the standard way to consume remote data in business workflows. In earlier chapters, you worked with CSV files and in-memory data structures. Here, you connect those skills to web services so your scripts can fetch, parse, and transform live data from business systems, weather services, payment platforms, and analytics providers.

## JSON as a Data Format

JSON (JavaScript Object Notation) is a lightweight, human-readable format for structured data.

Key ideas:
- JSON uses objects (dictionaries), arrays (lists), strings, numbers, booleans, and `null`.
- `json.loads()` parses JSON text into Python dictionaries.
- `json.dumps()` serializes Python dictionaries to JSON text.
- JSON is language-independent and widely adopted across REST APIs and data systems.
- Python's `json` module handles encoding/decoding safely.

## Making API Requests

An API (Application Programming Interface) is a contract for asking remote services to return data.

Key ideas:
- HTTP methods: `GET` retrieves data, `POST` sends data, `PUT`/`PATCH` update, `DELETE` removes.
- URLs contain a base endpoint plus resource path and optional query parameters.
- The `requests` library simplifies HTTP communication in Python.
- `requests.get()` sends a GET request and returns a Response object.
- Always handle network errors and unexpected response codes gracefully.

Scope for this course:
- Focus on unauthenticated `GET` requests only.
- Use real public endpoints (for example OpenMeteo and JSONPlaceholder) plus local JSON files.
- You are expected to understand HTTP verb, path, query parameters, status code, and JSON serialization/deserialization.
- Mocked requests in tests are used only to make grading stable and reproducible when network conditions change.

## Handling API Responses

API responses include metadata (headers, status codes) and data (body).

Key ideas:
- HTTP status codes: 200-299 (success), 400-499 (client error), 500-599 (server error).
- `.json()` method on a Response object parses the response body as JSON.
- `.status_code` property reveals whether the request succeeded.
- Responses often include pagination info, timestamps, and nested structures.
- Always validate response structure before processing fields.

## Transforming API Data

Raw API data often requires filtering, aggregation, and reshaping for reporting.

Key ideas:
- Dictionary comprehensions and `filter()` help select and reshape records.
- API data may include redundant fields, missing values, and inconsistent types.
- Build intermediate functions to isolate transformation logic for testing.
- Aggregations (sums, counts, grouping) often follow data cleanup.
- Store transformed output in dictionaries or lists for further analysis or export.

## Why This Matters

Modern data and operations roles depend on integrating data from multiple systems: HR platforms, CRM tools, weather APIs for demand forecasting, payment processors, and analytics engines. Practical API and JSON skills let you automate data collection from external sources into reliable decision-ready reports and dashboards.
