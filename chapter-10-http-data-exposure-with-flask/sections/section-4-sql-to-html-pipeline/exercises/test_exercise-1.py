import importlib.util
from pathlib import Path
import tempfile
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSection4Exercise1(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "mis_projects.db"
        self.module.initialize_database(self.db_path)
        self.app = self.module.create_app(self.db_path)
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_fetch_project_rows(self):
        rows = self.module.fetch_project_rows(self.db_path)
        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["project_name"], "ERP rollout")
        self.assertEqual(rows[0]["department"], "Operations")
        self.assertEqual(rows[0]["budget"], 125000)
        self.assertEqual(rows[0]["task_count"], 2)

    def test_projects_route_renders_html_table(self):
        response = self.client.get("/projects")
        body = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Project Report", body)
        self.assertIn("ERP rollout", body)
        self.assertIn("Finance", body)
        self.assertIn("125000", body)
        self.assertIn("2", body)


if __name__ == "__main__":
    unittest.main()