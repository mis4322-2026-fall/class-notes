"""Section 4 Exercise 1: Query SQLite data and render it into HTML."""

from pathlib import Path
import sqlite3

from flask import Flask, render_template

TEMPLATE_DIR = Path(__file__).parent / "templates"
DB_PATH = Path(__file__).parent / "mis_projects.db"
SEED_PROJECTS = [
    (1, "ERP rollout", "Operations", 125000),
    (2, "Budget dashboard", "Finance", 88000),
    (3, "Vendor portal", "Procurement", 64000),
]
SEED_TASKS = [
    (1, 1, "Data mapping", "Complete"),
    (2, 1, "User training", "In Progress"),
    (3, 2, "KPI definitions", "Complete"),
    (4, 3, "Supplier survey", "Not Started"),
]


def initialize_database(db_path):
    """Create a small SQLite database for the exercise."""
    with sqlite3.connect(db_path) as conn:
        conn.execute("DROP TABLE IF EXISTS tasks")
        conn.execute("DROP TABLE IF EXISTS projects")
        conn.execute(
            """
            CREATE TABLE projects (
                project_id INTEGER PRIMARY KEY,
                project_name TEXT NOT NULL,
                department TEXT NOT NULL,
                budget INTEGER NOT NULL
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE tasks (
                task_id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                task_name TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects(project_id)
            )
            """
        )
        conn.executemany("INSERT INTO projects VALUES (?, ?, ?, ?)", SEED_PROJECTS)
        conn.executemany("INSERT INTO tasks VALUES (?, ?, ?, ?)", SEED_TASKS)


def fetch_project_rows(db_path):
    """Return list[dict] with project_name, department, budget, and task_count."""
    raise NotImplementedError("Implement fetch_project_rows(db_path)")


def create_app(db_path=DB_PATH):
    """Return a Flask app that renders projects.html from SQLite query results."""
    app = Flask(__name__, template_folder=str(TEMPLATE_DIR))

    @app.route("/projects")
    def projects():
        raise NotImplementedError(
            "Render projects.html with records from fetch_project_rows(db_path)"
        )

    return app


if __name__ == "__main__":
    initialize_database(DB_PATH)
    create_app().run(debug=True)