import importlib.util
from pathlib import Path
import unittest
import numpy as np


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestAnalyzeBranchPerformance(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_shape_and_totals(self):
        result = self.module.analyze_branch_performance(self.module.SAMPLE_SALES_MATRIX)

        self.assertEqual(result["shape"], (3, 4))
        np.testing.assert_allclose(
            result["weekly_totals"],
            np.array([3680.0, 3835.0, 3910.0, 4150.0])
        )
        self.assertEqual(result["overall_total"], 15575.0)

    def test_branch_averages_and_top_index(self):
        result = self.module.analyze_branch_performance(self.module.SAMPLE_SALES_MATRIX)

        np.testing.assert_allclose(
            result["branch_averages"],
            np.array([1300.0, 1063.75, 1530.0])
        )
        self.assertEqual(result["top_branch_index"], 2)


if __name__ == "__main__":
    unittest.main()
