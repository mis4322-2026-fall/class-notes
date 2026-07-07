import importlib.util
from pathlib import Path
import unittest
import json


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestParseEmployeeRecords(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_parse_all_records(self):
        result = self.module.parse_employee_records(self.module.SAMPLE_JSON_TEXT)

        self.assertEqual(result["count"], 3)
        self.assertEqual(len(result["records"]), 3)
        self.assertEqual(result["records"][0]["name"], "Alice Johnson")
        self.assertEqual(result["filtered_count"], 0)

    def test_filter_by_department(self):
        result = self.module.parse_employee_records(
            self.module.SAMPLE_JSON_TEXT,
            department_filter="Finance"
        )

        self.assertEqual(result["count"], 3)
        self.assertEqual(result["filtered_count"], 1)
        self.assertEqual(result["records"][0]["department"], "Finance")

    def test_manager_extraction(self):
        result = self.module.parse_employee_records(self.module.SAMPLE_JSON_TEXT)

        self.assertIn("David", result["managers"])
        self.assertTrue(result["has_null_managers"])

    def test_salary_calculation(self):
        result = self.module.parse_employee_records(self.module.SAMPLE_JSON_TEXT)

        expected_avg = round((85000 + 65000 + 95000) / 3, 2)
        self.assertEqual(result["avg_salary"], expected_avg)

    def test_empty_json_array(self):
        result = self.module.parse_employee_records("[]")

        self.assertEqual(result["count"], 0)
        self.assertEqual(result["avg_salary"], 0.0)


if __name__ == "__main__":
    unittest.main()
