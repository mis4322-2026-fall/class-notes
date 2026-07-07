"""Section 2 Exercise 1: Read query parameters and form data with Flask."""

from flask import Flask, request

DEFAULT_DEPARTMENT = "Operations"
APPROVAL_LIMIT = 5000


def create_app():
    """Return a Flask app with narrow GET and POST examples."""
    app = Flask(__name__)

    @app.route("/lookup")
    def lookup():
        raise NotImplementedError(
            "Read a query parameter named department and return a text response"
        )

    @app.route("/approval", methods=["GET", "POST"])
    def approval():
        raise NotImplementedError(
            "Handle GET with instructions and POST with request.form data"
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True)