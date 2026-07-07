# Section 6.2: Making API Requests

## Overview

APIs are the primary way business systems exchange data. Rather than waiting for exports or running manual queries, you can write scripts that ask external services for data on demand. The `requests` library abstracts HTTP details so you can focus on data workflows.

## Core Concepts

- HTTP GET retrieves data; POST sends data; PUT/PATCH update; DELETE removes.
- An API endpoint is a URL targeting a specific resource or action.
- Query parameters modify requests: `GET /api/products?category=electronics&limit=10`.
- Response objects contain status codes, headers, and body data.
- The `requests` library simplifies HTTP communication.
- `requests.get(url)` sends a GET request and returns a Response object.
- Always check `response.status_code` before accessing `response.json()`.
- Network timeouts and connection errors must be handled gracefully.

## Code Walkthrough (incremental)

Import the requests library.

```python
import requests
# requests is a third-party library; install via: pip install requests
```

Send a simple GET request and check the status.

```python
response = requests.get('https://jsonplaceholder.typicode.com/users')
status = response.status_code
# result: 200 if successful, 404 if not found, 500 if server error
```

Access the response body as JSON.

```python
data = response.json()
# result: parsed dictionary or list from response body
```

Build a URL with query parameters.

```python
url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1, '_limit': 5}
response = requests.get(url, params=params)
# result: GET /posts?userId=1&_limit=5
```

Add headers to a request (e.g., authentication token).

```python
headers = {'Accept': 'application/json'}
response = requests.get('https://jsonplaceholder.typicode.com/users', headers=headers)
# result: Request explicitly asks for JSON response
```

Handle successful responses by checking status code first.

```python
response = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': 40.71, 'longitude': -74.01, 'current': 'temperature_2m'})
if response.status_code == 200:
    data = response.json()
else:
    data = None
# result: data is populated only if status is 200
```

Handle a 404 error gracefully.

```python
response = requests.get('https://api.open-meteo.com/v1/not-a-real-endpoint')
if response.status_code == 404:
    print("Resource not found")
elif response.status_code == 200:
    data = response.json()
# result: Explicit error handling prevents crashes
```

Use try-except to handle network errors.

```python
try:
    response = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': 37.77, 'longitude': -122.41, 'current': 'temperature_2m'}, timeout=5)
    data = response.json()
except requests.exceptions.RequestException as e:
    data = None
    print(f"Request failed: {e}")
# result: Timeout and connection errors are caught
```

Extract individual fields from a response.

```python
response = requests.get('https://jsonplaceholder.typicode.com/users/1')
user = response.json()
name = user.get('name', 'Unknown')
email = user.get('email', 'unknown@example.com')
# result: Safe field extraction prevents KeyError
```

Combine multiple requests to build a complete record.

```python
user_response = requests.get('https://jsonplaceholder.typicode.com/users/1')
user = user_response.json()
orders_response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
orders = orders_response.json()
# result: user and orders combined into one workflow
```

## Real-World Example: Weather Data API

This example uses OpenMeteo, a free public weather API that requires no authentication.

Fetch current weather for a city by geographic coordinates.

```python
import requests
# Get current weather for San Francisco (37.77, -122.41)
response = requests.get(
    'https://api.open-meteo.com/v1/forecast',
    params={'latitude': 37.77, 'longitude': -122.41, 'current': 'temperature_2m,precipitation'}
)
# result: GET /forecast?latitude=37.77&longitude=-122.41&current=...
```

Parse the response and extract current temperature.

```python
if response.ok:
    data = response.json()
    current = data.get('current', {})
    temp = current.get('temperature_2m')
    print(f"Temperature: {temp}°C")
# result: Temperature: 18.5°C (or actual current value)
```

Build a reusable function to fetch weather for different locations.

```python
def get_weather(latitude, longitude):
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,relative_humidity_2m,weather_code'
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.ok:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

# Call the function
result = get_weather(40.71, -74.01)  # New York
# result: result is a dict with 'current' and 'timezone' keys
```

Extract multiple weather fields from the response.

```python
if result:
    current = result.get('current', {})
    temp = current.get('temperature_2m', 'N/A')
    humidity = current.get('relative_humidity_2m', 'N/A')
    weather_code = current.get('weather_code', 'N/A')
    print(f"Temp: {temp}°C, Humidity: {humidity}%, Code: {weather_code}")
# result: Temp: 15.2°C, Humidity: 65%, Code: 80
```

## Try It (optional)

1. Use the OpenMeteo weather API to fetch current weather for your location
2. Extract temperature, humidity, and weather code
3. Handle errors gracefully (network failures, invalid coordinates, timeouts)
4. Keep focus on unauthenticated GET requests and JSON responses only

## Summary

Network requests are the gateway to dynamic data workflows. Mastering `requests.get()`, status code checking, timeout handling, and safe field extraction makes you comfortable integrating external systems into Python scripts. Always validate before accessing fields. Real APIs like OpenMeteo demonstrate these patterns in practice.
