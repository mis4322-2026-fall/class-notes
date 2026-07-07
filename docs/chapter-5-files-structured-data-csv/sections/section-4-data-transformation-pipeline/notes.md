# Section 5.4: Data Transformation Pipeline

## Overview

A pipeline organizes data work into clear stages: load, validate, transform, aggregate, and export. This structure is essential for reporting because each stage can be tested and revised without rewriting everything.

## Core Concepts

- Pipeline stages reduce complexity in file-based workflows.
- Validation should happen before metric calculations.
- Aggregations should produce clear, business-readable outputs.
- Output CSV files should be deterministic (stable sort and schema).

## Code Walkthrough (incremental)

Stage 1: Load source records.

```python
import csv

with open("service_requests.csv", "r", encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

# immediate result: raw row dictionaries
print(len(rows))
```

Inspect one row before transforming.

```python
# inspect raw shape early
print(rows[0])
```

Stage 2: Filter rows for reporting scope.

```python
# include closed requests only
closed_rows = [row for row in rows if row["status"].strip().lower() == "closed"]

# immediate result: narrowed dataset for SLA calculations
print(len(closed_rows))
```

Sort filtered rows for deterministic processing order.

```python
# stable ordering by team then opened date
closed_rows = sorted(closed_rows, key=lambda row: (row["team"], row["opened_date"]))

# immediate result: predictable row order
print(closed_rows[0]["team"], closed_rows[0]["opened_date"])
```

Stage 3: Aggregate by team.

```python
team_stats = {}
for row in closed_rows:
    team = row["team"].strip()
    hours = float(row["resolution_hours"])
    is_high = row["priority"].strip().lower() == "high"

    if team not in team_stats:
        team_stats[team] = {"closed_count": 0, "high_priority_closed": 0, "hours_total": 0.0}

    team_stats[team]["closed_count"] += 1
    team_stats[team]["hours_total"] += hours
    if is_high:
        team_stats[team]["high_priority_closed"] += 1

# immediate result: team-level counters and hour totals
print(team_stats)
```

Stage 4: Derive final metrics.

```python
for team, stats in team_stats.items():
    avg_hours = stats["hours_total"] / stats["closed_count"]

    # keep business metric rounded for reporting clarity
    stats["avg_resolution_hours"] = round(avg_hours, 2)

    # immediate classification from metric threshold
    stats["sla_status"] = "meets_sla" if avg_hours <= 8 else "at_risk"

# immediate result: each team now has avg and SLA status
print(team_stats)
```

Stage 5: Export report rows.

```python
import csv

report_rows = sorted(
    team_stats.items(), key=lambda item: (item[1]["avg_resolution_hours"], item[0])
)

fieldnames = ["team", "closed_count", "high_priority_closed", "avg_resolution_hours", "sla_status"]
with open("team_sla_report.csv", "w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    for team, stats in report_rows:
        writer.writerow(
            {
                "team": team,
                "closed_count": stats["closed_count"],
                "high_priority_closed": stats["high_priority_closed"],
                "avg_resolution_hours": f"{stats['avg_resolution_hours']:.2f}",
                "sla_status": stats["sla_status"],
            }
        )

# immediate result: report CSV written in stable sorted order
```

## Try It (optional)

Add a new pipeline stage that excludes records with resolution hours equal to `0` before aggregation. Compare the change in SLA status.

## Summary

A transformation pipeline turns raw CSV files into decision-ready metrics. Clear stage boundaries make these workflows easier to maintain, test, and adapt.
