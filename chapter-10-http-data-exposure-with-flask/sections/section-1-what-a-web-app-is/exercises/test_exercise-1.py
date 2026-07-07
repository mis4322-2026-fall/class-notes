import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSection1Exercise1(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.app = self.module.create_app()
        self.client = self.app.test_client()

    def test_home_route_returns_static_message(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "MIS Operations Portal is online")

    def test_snapshot_route_returns_dynamic_message(self):
        response = self.client.get("/snapshot")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_data(as_text=True),
            "Open orders: 12 | Late shipments: 3",
        )


if __name__ == "__main__":
    unittest.main()