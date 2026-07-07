"""Section 1 Exercise 1: Static and dynamic responses in a minimal Flask app."""

from flask import Flask

APP_STATUS = "MIS Operations Portal"
SALES_SNAPSHOT = {
    "open_orders": 12,
    "late_shipments": 3,
}


def create_app():
    """Return a Flask app with one static route and one dynamic route."""
    app = Flask(__name__)

    @app.route("/")
    def home():
        raise NotImplementedError("Return a static text response for the portal home page")

    @app.route("/snapshot")
    def snapshot():
        raise NotImplementedError(
            "Return a dynamic text response using SALES_SNAPSHOT values"
        )

    return app


if __name__ == "__main__":
    create_app().run(debug=True)