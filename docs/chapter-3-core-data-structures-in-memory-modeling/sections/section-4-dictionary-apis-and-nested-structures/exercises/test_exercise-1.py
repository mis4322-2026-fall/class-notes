import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildDepartmentReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_department_report_from_sample_data(self):
        result = self.module.build_department_report(
            self.module.SAMPLE_RECORDS,
            self.module.SAMPLE_MIN_TOTAL,
        )
        self.assertEqual(
            result,
            {
                "totals": {"IT": 2830.0, "HR": 480.0},
                "above_threshold": {"IT": 2830.0},
            },
        )

    def test_missing_purchases_treated_as_empty(self):
        records = [{"department": "Finance"}, {"department": "Finance", "purchases": []}]
        result = self.module.build_department_report(records, 1)
        self.assertEqual(result, {"totals": {"Finance": 0.0}, "above_threshold": {}})


if __name__ == "__main__":
    unittest.main()
