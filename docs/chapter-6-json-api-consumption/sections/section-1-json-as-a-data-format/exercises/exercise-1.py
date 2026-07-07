"""Section 1 Exercise 1: Parsing JSON and Extracting Data.

Implement parse_employee_records(json_text) to parse JSON and extract specific fields.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_JSON_TEXT = '''[
  {
    "id": 101,
    "name": "Alice Johnson",
    "department": "Finance",
    "salary": 85000,
    "manager": "David"
  },
  {
    "id": 102,
    "name": "Bob Smith",
    "department": "Sales",
    "salary": 65000,
    "manager": null
  },
  {
    "id": 103,
    "name": "Carol White",
    "department": "Engineering",
    "salary": 95000,
    "manager": "David"
  }
]'''

SAMPLE_DEPARTMENT = "Finance"
SAMPLE_EXPECTED_MANAGERS = ["David", None]


def parse_employee_records(json_text, department_filter=None):
    """Parse JSON employee records and optionally filter by department.

    Args:
        json_text: JSON string containing list of employee objects
        department_filter: Optional department name to filter by

    Returns:
        A dictionary with keys:
        - records: List of all parsed employee records (each is a dict)
        - count: Total number of records
        - filtered_count: Number of records matching department_filter (0 if no filter)
        - managers: List of unique manager names (excluding None)
        - has_null_managers: Boolean indicating if any record has null manager
        - avg_salary: Average salary of all records, rounded to 2 decimals (0.0 if no records)
    """
    raise NotImplementedError("Implement parse_employee_records(json_text, department_filter=None)")
