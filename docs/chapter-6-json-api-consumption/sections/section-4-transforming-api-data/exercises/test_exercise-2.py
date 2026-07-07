import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestAggregateByDepartment(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_grouping_by_department(self):
        result = self.module.aggregate_by_department(self.module.SAMPLE_EMPLOYEE_RECORDS)

        self.assertIn("Engineering", result["by_department"])
        self.assertIn("Sales", result["by_department"])
        self.assertEqual(len(result["by_department"]["Engineering"]), 3)
        self.assertEqual(len(result["by_department"]["Sales"]), 2)

    def test_department_summaries(self):
        result = self.module.aggregate_by_department(self.module.SAMPLE_EMPLOYEE_RECORDS)

        summaries = result["department_summaries"]
        self.assertIn("Engineering", summaries)
        self.assertIn("count", summaries["Engineering"])
        self.assertIn("avg_salary", summaries["Engineering"])

    def test_salary_calculations(self):
        result = self.module.aggregate_by_department(self.module.SAMPLE_EMPLOYEE_RECORDS)

        eng_summary = result["department_summaries"]["Engineering"]
        # Engineering: Alice (95000), Carol (88000), Eve (92000) = 275000
        expected_total = 95000 + 88000 + 92000
        expected_avg = round(expected_total / 3, 2)

        self.assertEqual(eng_summary["total_salary"], expected_total)
        self.assertEqual(eng_summary["avg_salary"], expected_avg)

    def test_highest_paid_employee(self):
        result = self.module.aggregate_by_department(self.module.SAMPLE_EMPLOYEE_RECORDS)

        highest = result["highest_paid_employee"]
        self.assertEqual(highest["name"], "Alice")
        self.assertEqual(highest["salary"], 95000)

    def test_departments_by_size(self):
        result = self.module.aggregate_by_department(self.module.SAMPLE_EMPLOYEE_RECORDS)

        by_size = result["departments_by_size"]
        # Engineering has 3, Sales has 2
        self.assertEqual(by_size[0][0], "Engineering")
        self.assertEqual(by_size[0][1], 3)
        self.assertEqual(by_size[1][0], "Sales")
        self.assertEqual(by_size[1][1], 2)


if __name__ == "__main__":
    unittest.main()
