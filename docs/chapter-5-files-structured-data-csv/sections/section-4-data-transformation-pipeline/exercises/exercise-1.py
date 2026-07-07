"""Section 4 Exercise 1: Data Transformation Pipeline.

Implement a closed-service-request reporting pipeline.
"""

from pathlib import Path

# Starter dataset path used by tests and classroom demos.
SAMPLE_REQUESTS_PATH = Path(__file__).parent / "data" / "service_requests.csv"


def run_service_pipeline(input_csv_path, output_csv_path):
    """Run a complete CSV transformation pipeline for service requests.

    Input columns:
    - request_id
    - team
    - priority
    - status
    - resolution_hours
    - opened_date

    Requirements:
    1. Read with csv.DictReader.
    2. Keep only rows where status == "closed" (case-insensitive).
    3. Aggregate by team:
       - closed_count
       - high_priority_closed
       - avg_resolution_hours (rounded to 2 decimals)
    4. Derive sla_status:
       - "meets_sla" if avg_resolution_hours <= 8
       - "at_risk" otherwise
    5. Write output CSV columns:
       team,closed_count,high_priority_closed,avg_resolution_hours,sla_status
       Sort rows by avg_resolution_hours ascending, then team ascending.

    Return:
    {
        "source_rows": <int>,
        "closed_rows": <int>,
        "team_metrics": [
            {
                "team": <str>,
                "closed_count": <int>,
                "high_priority_closed": <int>,
                "avg_resolution_hours": <float>,
                "sla_status": <str>,
            },
            ...
        ]
    }

    team_metrics in the return value must follow the same sorted order as the output CSV.
    """
    raise NotImplementedError("Implement run_service_pipeline(input_csv_path, output_csv_path)")
