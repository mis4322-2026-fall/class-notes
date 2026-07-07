import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSection3Exercise1(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.app = self.module.create_app()
        self.client = self.app.test_client()

    def test_summarize_projects(self):
        summary = self.module.summarize_projects(self.module.PROJECTS)
        self.assertEqual(summary, {"total_projects": 3, "at_risk_projects": 1})

    def test_overview_renders_template_with_data(self):
        response = self.client.get("/overview")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Project Overview", body)
        self.assertIn("ERP rollout", body)
        self.assertIn("At Risk", body)
        self.assertIn("Total projects: 3", body)
        self.assertIn("At-risk projects: 1", body)


if __name__ == "__main__":
    unittest.main()