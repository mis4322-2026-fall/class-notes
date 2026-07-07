"""Section 1 Exercise 1: Lists as Ordered Data.

Implement prepare_order_timeline(initial_orders, incoming_orders, canceled_order, recent_n).

Use the explicit sample constants below while developing and validating your logic.
"""

SAMPLE_INITIAL_ORDERS = [120, 135, 128, 142]
SAMPLE_INCOMING_ORDERS = [150, 147, 160]
SAMPLE_CANCELED_ORDER = 128
SAMPLE_RECENT_N = 3


def prepare_order_timeline(initial_orders, incoming_orders, canceled_order, recent_n):
    """Return ordered timeline views and summary metrics.

    Return a dictionary with keys:
    - orders: updated list after extending incoming_orders and removing canceled_order once
    - recent: last recent_n values (or [] when recent_n <= 0)
    - sorted_orders: ascending sorted version of orders
    - total: sum of orders
    - average: rounded average to 2 decimals (0 when orders is empty)
    """
    raise NotImplementedError("Implement prepare_order_timeline(initial_orders, incoming_orders, canceled_order, recent_n)")
