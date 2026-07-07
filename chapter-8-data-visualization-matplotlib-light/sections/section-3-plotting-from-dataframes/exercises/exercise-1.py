"""Section 3 Exercise 1: Plot directly from a DataFrame.

Task:
1) Run the file.
2) Observe line, bar, and scatter charts created from the DataFrame.
3) Change one axis label to improve clarity.
"""

import pandas as pd
import matplotlib.pyplot as plt

SALES_DATA = [
    {"month": "Jan", "revenue_k": 12, "orders": 110},
    {"month": "Feb", "revenue_k": 15, "orders": 125},
    {"month": "Mar", "revenue_k": 14, "orders": 121},
    {"month": "Apr", "revenue_k": 18, "orders": 140},
]


def build_dataframe(records):
    return pd.DataFrame(records)


def plot_from_dataframe(df):
    plt.figure()
    ax1 = df.plot(x="month", y="revenue_k", kind="line", title="Revenue by Month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue (k$)")

    plt.figure()
    ax2 = df.plot(x="month", y="orders", kind="bar", title="Orders by Month")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Orders")

    plt.figure()
    ax3 = df.plot(x="orders", y="revenue_k", kind="scatter", title="Orders vs Revenue")
    ax3.set_xlabel("Orders")
    ax3.set_ylabel("Revenue (k$)")


if __name__ == "__main__":
    frame = build_dataframe(SALES_DATA)
    plot_from_dataframe(frame)
    plt.show()
