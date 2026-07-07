# Section 6.3: Handling API Responses

## Overview

API responses are rarely perfect. Fields may be missing, values may be null, nested structures may be inconsistent, and pagination may split data across multiple calls. This section teaches defensive programming practices for real-world API data.

## Core Concepts

- HTTP status codes classify success (2xx), client error (4xx), and server error (5xx).
- `.status_code` must be checked before accessing `.json()`.
- `.json()` may raise JSONDecodeError if the response body is not valid JSON.
- API responses often have a wrapper structure: `{"status": "ok", "data": {...}}`.
- Missing fields must be handled via `.get()` with defaults.
- Pagination splits large result sets across multiple pages.
- Field validation prevents downstream errors in data processing.

## Code Walkthrough (incremental)

Check status code before parsing JSON.

```python
import requests
response = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': 37.77, 'longitude': -122.41, 'current': 'temperature_2m'})
if 200 <= response.status_code < 300:
    data = response.json()
else:
    data = None
# result: data is populated only for 2xx success codes
```

Use status code classes for cleaner conditions.

```python
if response.ok:  # True for 2xx status codes
    data = response.json()
else:
    data = None
# result: .ok is cleaner than checking range
```

Handle JSONDecodeError when body is not JSON.

```python
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    data = None
    print("Response body is not valid JSON")
# result: Malformed JSON doesn't crash the program
```

Extract a nested field with safe defaults.

```python
response = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': 40.71, 'longitude': -74.01, 'current': 'temperature_2m,weather_code'})
payload = response.json()
temp = payload.get('current', {}).get('temperature_2m', 'Unknown')
# result: Returns 'Unknown' even if 'current' or 'temperature_2m' is missing
```

Validate a list in the response before iterating.

```python
response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
items = response.json()
if isinstance(items, list):
    for item in items:
    print(item.get('title', 'N/A'))
# result: Prevents iteration errors and safely reads post titles
```

Handle pagination by constructing multiple requests.

```python
all_records = []
page = 1
while True:
    response = requests.get('https://jsonplaceholder.typicode.com/comments', params={'_page': page, '_limit': 25})
    if response.ok:
        records = response.json()
        all_records.extend(records)
        if not records or len(records) < 25:
            break
    else:
        break
    page += 1
# result: all_records contains items from all pages
```

Validate field types before processing.

```python
response = requests.get('https://dummyjson.com/products/1')
data = response.json()
total = data.get('price')
if isinstance(total, (int, float)):
    rounded_total = round(total, 2)
else:
    rounded_total = 0.0
# result: Prevents type errors in calculations
```

Check for required fields and track missing data.

```python
response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
transactions = response.json()
complete = [t for t in transactions if 'id' in t and 'title' in t]
incomplete = [t for t in transactions if 'id' not in t or 'title' not in t]
# result: incomplete records are tracked separately
```

Use get_text() as fallback when response is not JSON.

```python
response = requests.get('https://httpbin.org/html')
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    text = response.text
    print(f"Response was not JSON: {text[:100]}")
# result: Inspect raw response for debugging
```

## Try It (optional)

Write a function that fetches paginated data from an API, validates each record has required fields, and returns both complete and incomplete records separately. Handle network errors and malformed responses gracefully.

## Summary

Production API consumers are defensive. Check status codes, handle missing fields, validate types, and expect the unexpected. These practices prevent cascading failures and make debugging easier when things go wrong.
