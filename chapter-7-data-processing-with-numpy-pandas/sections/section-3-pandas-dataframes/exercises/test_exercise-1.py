import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildOrdersDataFrame(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_dataframe_properties(self):
        result = self.module.build_orders_dataframe(self.module.SAMPLE_ORDERS)

        self.assertEqual(result["row_count"], 4)
        self.assertIn("revenue", result["columns"])
        self.assertEqual(result["north_orders"], 2)

    def test_total_revenue(self):
        result = self.module.build_orders_dataframe(self.module.SAMPLE_ORDERS)

        self.assertEqual(result["total_revenue"], 4050.0)


if __name__ == "__main__":
    unittest.main()
