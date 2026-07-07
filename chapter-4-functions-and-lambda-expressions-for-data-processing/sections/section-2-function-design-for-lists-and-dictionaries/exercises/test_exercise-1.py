import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildDepartmentSummary(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_grouped_summary_from_sample_data(self):
        result = self.module.build_department_summary(self.module.SAMPLE_RECORDS)
        self.assertEqual(result["IT"], {"count": 2, "total": 2000, "average": 1000.0})
        self.assertEqual(result["HR"], {"count": 1, "total": 450, "average": 450.0})
        self.assertEqual(result["Sales"], {"count": 1, "total": 1000, "average": 1000.0})

    def test_empty_records(self):
        self.assertEqual(self.module.build_department_summary([]), {})


if __name__ == "__main__":
    unittest.main()
