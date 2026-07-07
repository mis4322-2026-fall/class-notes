import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSection2Exercise1(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.app = self.module.create_app()
        self.client = self.app.test_client()

    def test_lookup_uses_default_department_when_missing(self):
        response = self.client.get("/lookup")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "Department lookup: Operations")

    def test_lookup_reads_query_parameter(self):
        response = self.client.get("/lookup?department=Finance")
        self.assertEqual(response.get_data(as_text=True), "Department lookup: Finance")

    def test_approval_get_returns_instructions(self):
        response = self.client.get("/approval")
        self.assertEqual(response.get_data(as_text=True), "Submit a POST request with amount and owner")

    def test_approval_post_returns_decision(self):
        response = self.client.post(
            "/approval",
            data={"amount": "6200", "owner": "Alicia"},
        )
        self.assertEqual(
            response.get_data(as_text=True),
            "Owner Alicia submitted 6200.0 | Decision: manager review",
        )


if __name__ == "__main__":
    unittest.main()