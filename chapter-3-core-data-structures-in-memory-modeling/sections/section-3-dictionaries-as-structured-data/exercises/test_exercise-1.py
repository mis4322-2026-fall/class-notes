import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildInventoryViews(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_inventory_views_from_sample_data(self):
        result = self.module.build_inventory_views(self.module.SAMPLE_RECORDS)
        expected = {
            "qty_by_sku": {"A100": 14, "B205": 8, "C010": 5, "D777": 9},
            "low_stock_skus": ["B205", "C010"],
            "category_counts": {"accessory": 1, "hardware": 2, "uncategorized": 1},
        }
        self.assertEqual(result, expected)

    def test_empty_records(self):
        self.assertEqual(
            self.module.build_inventory_views([]),
            {"qty_by_sku": {}, "low_stock_skus": [], "category_counts": {}},
        )


if __name__ == "__main__":
    unittest.main()
