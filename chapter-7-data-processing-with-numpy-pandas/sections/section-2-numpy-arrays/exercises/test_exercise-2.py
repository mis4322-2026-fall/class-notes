import importlib.util
from pathlib import Path
import unittest
import numpy as np


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestProjectGrowthAndFlags(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_projected_values(self):
        result = self.module.project_growth_and_flags(
            self.module.SAMPLE_SALES_MATRIX,
            self.module.SAMPLE_GROWTH_RATE,
            self.module.SAMPLE_TARGET,
        )

        expected = np.array([
            [220.0, 264.0, 286.0],
            [198.0, 209.0, 231.0],
            [330.0, 352.0, 341.0],
        ])
        np.testing.assert_allclose(result["projected"], expected)

    def test_flags_counts_and_max(self):
        result = self.module.project_growth_and_flags(
            self.module.SAMPLE_SALES_MATRIX,
            self.module.SAMPLE_GROWTH_RATE,
            self.module.SAMPLE_TARGET,
        )

        self.assertEqual(result["met_target_count"], 5)
        self.assertEqual(result["max_projected"], 352.0)
        self.assertEqual(result["met_target_flags"][0, 0], "below")
        self.assertEqual(result["met_target_flags"][2, 1], "met")


if __name__ == "__main__":
    unittest.main()
