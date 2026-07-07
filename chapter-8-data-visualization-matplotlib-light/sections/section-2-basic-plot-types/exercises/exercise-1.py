"""Section 2 Exercise 1: Build three basic plots.

This exercise keeps the API surface intentionally small:
- line plot
- bar plot
- scatter plot
- simple title and axis labels

Task:
1) Run the script.
2) Inspect the three chart windows.
3) Update one title so it is clearer for a non-technical stakeholder.
"""

import matplotlib.pyplot as plt

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
VISITORS = [120, 135, 128, 150, 160]

PRODUCTS = ["A", "B", "C"]
UNITS_SOLD = [42, 35, 51]

AD_SPEND = [200, 350, 500, 650, 800]
SIGNUPS = [22, 30, 41, 44, 58]


def plot_line():
    plt.figure()
    plt.plot(DAYS, VISITORS)
    plt.title("Daily Website Visitors")
    plt.xlabel("Day")
    plt.ylabel("Visitors")


def plot_bar():
    plt.figure()
    plt.bar(PRODUCTS, UNITS_SOLD)
    plt.title("Units Sold by Product")
    plt.xlabel("Product")
    plt.ylabel("Units")


def plot_scatter():
    plt.figure()
    plt.scatter(AD_SPEND, SIGNUPS)
    plt.title("Ad Spend vs Signups")
    plt.xlabel("Ad Spend ($)")
    plt.ylabel("Signups")


if __name__ == "__main__":
    plot_line()
    plot_bar()
    plot_scatter()
    plt.show()
