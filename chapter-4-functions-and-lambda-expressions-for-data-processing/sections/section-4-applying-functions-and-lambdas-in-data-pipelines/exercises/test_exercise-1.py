import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildRegionalRevenueReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_pipeline_report_from_sample_data(self):
        result = self.module.build_regional_revenue_report(
            self.module.SAMPLE_ORDERS,
            self.module.SAMPLE_MIN_TOTAL,
        )
        self.assertEqual(result, [("West", 540.0)])

    def test_expected_totals_and_threshold(self):
        result = self.module.build_regional_revenue_report(self.module.SAMPLE_ORDERS, 400)
        self.assertEqual(result, [("West", 540.0), ("North", 410.0)])


if __name__ == "__main__":
    unittest.main()
