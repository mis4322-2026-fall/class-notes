import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildRegionPerformance(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_region_totals_and_status(self):
        result = self.module.build_region_performance(
            self.module.SAMPLE_RECORDS,
            self.module.SAMPLE_TARGET,
        )
        self.assertEqual(
            result,
            [
                {"region": "North", "total_sales": 2100, "status": "met"},
                {"region": "South", "total_sales": 2300, "status": "met"},
                {"region": "West", "total_sales": 1300, "status": "below"},
            ],
        )

    def test_empty_input(self):
        self.assertEqual(self.module.build_region_performance([], 100), [])


if __name__ == "__main__":
    unittest.main()
