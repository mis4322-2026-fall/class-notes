import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestLoadAndCleanOrders(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_missing_values_cleaned(self):
        result = self.module.load_and_clean_orders(self.module.SAMPLE_CSV_PATH)

        self.assertEqual(result["missing_before"], 2)
        self.assertEqual(result["missing_after"], 0)

    def test_closed_revenue(self):
        result = self.module.load_and_clean_orders(self.module.SAMPLE_CSV_PATH)

        self.assertEqual(result["closed_revenue"], 2640.0)
        self.assertIn("revenue", result["dataframe"].columns.tolist())


if __name__ == "__main__":
    unittest.main()
