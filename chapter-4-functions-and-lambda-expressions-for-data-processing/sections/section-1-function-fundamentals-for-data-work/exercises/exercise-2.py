"""Section 1 Exercise 2: Function Fundamentals for Data Work.

Implement evaluate_service_levels(response_times, sla_target).
"""

SAMPLE_RESPONSE_TIMES = [18, 42, 33, 55, 27, 61]
SAMPLE_SLA_TARGET = 40


def evaluate_service_levels(response_times, sla_target):
    """Evaluate service-level performance metrics.

    Return a dictionary with keys:
    - total_tickets
    - avg_response_time (rounded to 2 decimals)
    - within_sla_count: number of values <= sla_target
    - breach_count: number of values > sla_target
    - sla_rate: within_sla_count / total_tickets rounded to 2 decimals (0 when empty)
    """
    raise NotImplementedError("Implement evaluate_service_levels(response_times, sla_target)")
