# Section 6.1: JSON as a Data Format

## Overview

JSON is the universal format for data exchange between systems. In business workflows, you'll encounter JSON in API responses, configuration files, and data exports. Understanding how to parse, validate, and serialize JSON is fundamental to automating data workflows.

## Core Concepts

- JSON contains objects (key-value pairs), arrays (ordered lists), strings, numbers, booleans, and `null`.
- `json.loads()` parses a JSON string into Python dictionaries and lists.
- `json.dumps()` serializes Python objects back to JSON strings.
- `json.load()` reads JSON from a file; `json.dump()` writes JSON to a file.
- JSON nesting allows objects inside arrays and arrays inside objects.
- Always validate JSON structure before accessing fields to avoid KeyError and TypeError.

## Code Walkthrough (incremental)

Parse a simple JSON string to a Python dictionary.

```python
import json
json_text = '{"name": "Alice", "salary": 75000}'
data = json.loads(json_text)
# result: {'name': 'Alice', 'salary': 75000}
```

Access fields safely using `.get()` to handle missing keys.

```python
name = data.get('name')
title = data.get('title', 'Unknown')
# result: name='Alice', title='Unknown'
```

Work with JSON arrays (lists).

```python
json_array = '[{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}]'
records = json.loads(json_array)
# result: [{'id': 1, 'status': 'active'}, {'id': 2, 'status': 'inactive'}]
```

Extract all IDs from an array of objects.

```python
ids = [record['id'] for record in records]
# result: [1, 2]
```

Serialize a Python dictionary back to JSON.

```python
employee = {'name': 'Bob', 'department': 'Sales', 'salary': 65000}
json_output = json.dumps(employee)
# result: '{"name": "Bob", "department": "Sales", "salary": 65000}'
```

Pretty-print JSON for readability.

```python
pretty_json = json.dumps(employee, indent=2)
# result:
# {
#   "name": "Bob",
#   "department": "Sales",
#   "salary": 65000
# }
```

Set sort keys to alphabetize field names in output.

```python
sorted_json = json.dumps(employee, indent=2, sort_keys=True)
# result: Department, Name, Salary (alphabetical)
```

Handle nested JSON with multiple levels.

```python
nested_json = '{"company": {"name": "TechCorp", "employees": [{"name": "Carol"}]}}'
company = json.loads(nested_json)
emp_name = company['company']['employees'][0]['name']
# result: 'Carol'
```

Use `.get()` chains to safely navigate nested structures.

```python
emp_name = company.get('company', {}).get('employees', [{}])[0].get('name', 'Unknown')
# result: 'Carol' (safe even if keys are missing)
```

Determine field type and handle different JSON value types.

```python
test_data = '{"count": 42, "price": 19.99, "active": true, "notes": null}'
parsed = json.loads(test_data)
# result: count is int, price is float, active is bool, notes is None
```

## Try It (optional)

Load the provided sample JSON file `customer.json`. Extract the customer name, total purchase amount, and all order IDs. Serialize a report dictionary containing these extracted fields, then pretty-print the report as JSON.

## Summary

JSON is everywhere in modern data workflows. Mastering `json.loads()`, `json.dumps()`, safe field access via `.get()`, and nesting navigation makes you comfortable with data from APIs, files, and config systems. Build defensive code that validates structure before accessing fields.
