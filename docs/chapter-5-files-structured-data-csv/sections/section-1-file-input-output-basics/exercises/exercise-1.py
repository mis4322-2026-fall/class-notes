"""Section 1 Exercise 1: File Input/Output Basics.

Build a small text-file processing workflow for regional sales logs.
"""

from pathlib import Path

# Starter dataset path used by tests and classroom demos.
SAMPLE_INPUT_PATH = Path(__file__).parent / "data" / "sales_log.txt"


def process_sales_log(input_path, output_path):
    """Read a raw sales log, aggregate totals, and write a summary report.

    Input file format (one record per line):
    region,amount

    Example line:
    North,1250.50

    Requirements:
    1. Read all lines from input_path.
    2. A valid line has exactly two comma-separated fields and a numeric amount.
    3. Ignore blank lines.
    4. Aggregate sales totals by region for valid rows.
    5. Write output_path with this format:
       Region Totals
       East: 1100.00
       North: 2000.00
       South: 980.00
       West: 2000.00
       Grand Total: 6080.00

       Regions must be sorted alphabetically.

    Return a dictionary:
    {
        "line_count": <int>,
        "valid_count": <int>,
        "invalid_count": <int>,
        "region_totals": {"Region": total_float, ...},
    }
    """
    raise NotImplementedError("Implement process_sales_log(input_path, output_path)")
