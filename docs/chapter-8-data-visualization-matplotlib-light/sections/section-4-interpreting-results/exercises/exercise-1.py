"""Section 4 Exercise 1: Interpret chart output responsibly.

Task:
1) Run the script to generate a line chart and scatter plot.
2) Read the interpretation dictionary printed at the end.
3) Replace one caution sentence with your own improved wording.
"""

import matplotlib.pyplot as plt

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
RESOLUTION_RATE = [72, 74, 73, 78, 79, 80]

AD_SPEND = [200, 350, 500, 650, 800, 950]
SIGNUPS = [22, 30, 41, 44, 58, 61]


def plot_context():
    plt.figure()
    plt.plot(MONTHS, RESOLUTION_RATE)
    plt.title("Support Ticket Resolution Rate")
    plt.xlabel("Month")
    plt.ylabel("Resolution Rate (%)")

    plt.figure()
    plt.scatter(AD_SPEND, SIGNUPS)
    plt.title("Ad Spend vs Signups")
    plt.xlabel("Ad Spend ($)")
    plt.ylabel("Signups")


def build_interpretation():
    """Return a simple interpretation with one insight and one caution."""
    return {
        "observation": "Resolution rate rises overall from January to June.",
        "possible_interpretation": "Process improvements may be helping team performance.",
        "caution": "The chart alone cannot confirm cause; staffing and ticket complexity may also matter.",
    }


if __name__ == "__main__":
    plot_context()
    print(build_interpretation())
    plt.show()
