import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSelectProfitableProducts(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_filter_and_sort_by_margin(self):
        result = self.module.select_profitable_products(
            self.module.SAMPLE_PRODUCTS,
            self.module.SAMPLE_MIN_MARGIN,
        )
        self.assertEqual(result, ["Laptop", "Monitor"])

    def test_no_matches_returns_empty_list(self):
        products = [
            {"name": "Cable", "cost": 8, "price": 10},
            {"name": "Adapter", "cost": 15, "price": 18},
        ]
        result = self.module.select_profitable_products(products, 10)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
