import importlib.util
from pathlib import Path
import unittest
import pandas as pd


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildRegionKpi(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.df = pd.read_csv(self.module.SAMPLE_CSV_PATH)

    def test_summary_shape_and_counts(self):
        result = self.module.build_region_kpi(self.df)

        self.assertEqual(result["closed_order_count"], 4)
        self.assertEqual(len(result["summary"]), 3)

    def test_revenue_metrics(self):
        result = self.module.build_region_kpi(self.df)

        self.assertEqual(result["grand_revenue"], 2880.0)
        top_region = result["summary"].iloc[0]["region"]
        self.assertEqual(top_region, "West")


if __name__ == "__main__":
    unittest.main()
