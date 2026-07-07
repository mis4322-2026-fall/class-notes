# Section 5.1: File Input/Output Basics

## Overview

In data and operations work, many tasks begin with reading raw text exports and end with writing cleaned summaries. This section introduces foundational file APIs so you can build repeatable data workflows.

## Core Concepts

- File modes control intent: read (`"r"`), write (`"w"`), append (`"a"`).
- Context managers (`with`) close files safely.
- Text files are processed line by line, often with cleanup rules.
- Writing output files creates durable artifacts for downstream reporting.

## Code Walkthrough (incremental)

Open and read an entire file.

```python
# read the full file contents as one string
with open("daily_notes.txt", "r", encoding="utf-8") as handle:
    content = handle.read()

# immediate result: you can inspect the first characters
print(content[:40])
```

Read lines and clean newline characters.

```python
with open("daily_notes.txt", "r", encoding="utf-8") as handle:
    # strip removes trailing newline and extra spaces
    lines = [line.strip() for line in handle]

# immediate result: list of cleaned lines
print(lines)
```

Read a single line when you only need the header.

```python
with open("daily_notes.txt", "r", encoding="utf-8") as handle:
    # read only the first line
    first_line = handle.readline().strip()

# immediate result: one cleaned line
print(first_line)
```

Write a new file from a list of values.

```python
totals = ["North: 2000.00", "South: 980.00"]

with open("region_report.txt", "w", encoding="utf-8") as handle:
    # each write call appends text to the file buffer
    handle.write("Region Totals\n")
    for row in totals:
        handle.write(f"{row}\n")

# immediate result: file now contains a report body
```

Append additional data without overwriting.

```python
with open("region_report.txt", "a", encoding="utf-8") as handle:
    # append mode preserves existing content
    handle.write("Grand Total: 2980.00\n")

# immediate result: previous content remains plus one appended line
```

Use `pathlib.Path` for clearer path handling.

```python
from pathlib import Path

report_path = Path("outputs") / "region_report.txt"
report_path.parent.mkdir(exist_ok=True)

with report_path.open("w", encoding="utf-8") as handle:
    handle.write("Generated from File I/O section demo\n")

# immediate result: report path is created relative to project folder
```

## Try It (optional)

Create `daily_counts.txt` with one integer per line. Write a script that reads the file, computes total and average, and writes `daily_counts_summary.txt`.

## Summary

File I/O basics establish reliable input and output behavior. Using clear modes, `with` blocks, and line-by-line processing helps you build scripts that are both safe and repeatable.
