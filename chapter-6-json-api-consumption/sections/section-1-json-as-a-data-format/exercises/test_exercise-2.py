import importlib.util
from pathlib import Path
import unittest
import json


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildJsonReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_report_with_sample_data(self):
        result = self.module.build_json_report(self.module.SAMPLE_RECORDS, pretty=False)

        self.assertEqual(result["total_items"], 58)
        self.assertEqual(result["total_value"], 8450.0)
        self.assertEqual(len(result["product_names"]), 3)
        self.assertIn("Laptop", result["product_names"])
        self.assertTrue(result["is_valid_json"])

    def test_json_string_is_valid(self):
        result = self.module.build_json_report(self.module.SAMPLE_RECORDS)

        try:
            json.loads(result["json_string"])
            is_valid = True
        except json.JSONDecodeError:
            is_valid = False

        self.assertTrue(is_valid)

    def test_product_names_correct_order(self):
        result = self.module.build_json_report(self.module.SAMPLE_RECORDS)

        self.assertEqual(result["product_names"][0], "Laptop")
        self.assertEqual(result["product_names"][1], "Mouse")
        self.assertEqual(result["product_names"][2], "Monitor")

    def test_total_value_calculation_precision(self):
        records = [{"id": 1, "product": "Item", "quantity": 3, "price": 10.33}]
        result = self.module.build_json_report(records)

        expected_value = round(3 * 10.33, 2)
        self.assertEqual(result["total_value"], expected_value)

    def test_empty_records_list(self):
        result = self.module.build_json_report([])

        self.assertEqual(result["total_items"], 0)
        self.assertEqual(result["total_value"], 0.0)
        self.assertEqual(result["product_names"], [])


if __name__ == "__main__":
    unittest.main()
