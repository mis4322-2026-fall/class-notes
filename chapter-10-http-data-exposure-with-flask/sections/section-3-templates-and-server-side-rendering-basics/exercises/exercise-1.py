"""Section 3 Exercise 1: Render Python data into an HTML template."""

from pathlib import Path

from flask import Flask, render_template

TEMPLATE_DIR = Path(__file__).parent / "templates"
PROJECTS = [
    {"name": "ERP rollout", "owner": "Nina", "status": "On Track"},
    {"name": "Vendor cleanup", "owner": "Mateo", "status": "At Risk"},
    {"name": "Forecast refresh", "owner": "Lina", "status": "On Track"},
]


def summarize_projects(projects):
    """Return a summary dictionary with total_projects and at_risk_projects."""
    raise NotImplementedError("Implement summarize_projects(projects)")


def create_app():
    """Return a Flask app that renders overview.html with project data."""
    app = Flask(__name__, template_folder=str(TEMPLATE_DIR))

    @app.route("/overview")
    def overview():
        raise NotImplementedError(
            "Render overview.html with projects and a summary dictionary"
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True)