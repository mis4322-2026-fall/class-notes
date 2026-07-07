import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildAmountReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_report_from_sample_data(self):
        result = self.module.build_amount_report(
            self.module.SAMPLE_AMOUNTS,
            self.module.SAMPLE_HIGH_THRESHOLD,
        )

        self.assertEqual(result["valid_amounts"], [45.0, 120.5, 510.0, 85.25, 999.0])
        self.assertEqual(result["categories"], ["low", "medium", "high", "low", "high"])
        self.assertEqual(result["high_value_count"], 2)

    def test_threshold_edge_is_high(self):
        result = self.module.build_amount_report([100, 200], 200)
        self.assertEqual(result["categories"], ["medium", "high"])
        self.assertEqual(result["high_value_count"], 1)


if __name__ == "__main__":
    unittest.main()
