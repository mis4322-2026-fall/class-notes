import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_product_snapshot_from_sample_data(self):
        product = self.module.Product(**self.module.SAMPLE_PRODUCT)

        self.assertEqual(product.inventory_value(), 537.0)
        self.assertEqual(
            product.snapshot(),
            {
                "sku": "P-410",
                "name": "Barcode Scanner",
                "unit_price": 89.5,
                "quantity_on_hand": 6,
                "inventory_value": 537.0,
            },
        )
        self.assertEqual(str(product), "P-410 | Barcode Scanner | 6 units")

    def test_objects_keep_separate_state(self):
        first = self.module.Product("P-1", "Mouse", 20.0, 5)
        second = self.module.Product("P-2", "Keyboard", 35.0, 3)

        self.assertEqual(first.snapshot()["name"], "Mouse")
        self.assertEqual(second.snapshot()["name"], "Keyboard")


if __name__ == "__main__":
    unittest.main()
