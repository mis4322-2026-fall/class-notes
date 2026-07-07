"""Section 4 Exercise 2: Aggregating and Grouping API Data.

Implement aggregate_by_department(employee_records) to group and summarize data.

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_EMPLOYEE_RECORDS = [
    {"id": 1, "name": "Alice", "department": "Engineering", "salary": 95000, "years": 5},
    {"id": 2, "name": "Bob", "department": "Sales", "salary": 65000, "years": 3},
    {"id": 3, "name": "Carol", "department": "Engineering", "salary": 88000, "years": 4},
    {"id": 4, "name": "David", "department": "Sales", "salary": 70000, "years": 2},
    {"id": 5, "name": "Eve", "department": "Engineering", "salary": 92000, "years": 6},
]


def aggregate_by_department(employee_records):
    """Group employees by department and compute summaries.

    Args:
        employee_records: List of employee dictionaries with id, name, department, salary, years

    Returns:
        A dictionary with keys:
        - by_department: Dict mapping department name to list of employees in that department
        - department_summaries: Dict with keys for each department containing:
            - count: number of employees
            - avg_salary: average salary rounded to 2 decimals
            - total_salary: sum of all salaries in the department
            - avg_tenure: average years of service rounded to 2 decimals
        - highest_paid_employee: Dict with employee data for highest salary across all employees
        - departments_by_size: List of tuples (department_name, count) sorted by count descending
    """
    raise NotImplementedError("Implement aggregate_by_department(employee_records)")
