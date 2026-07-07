import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestTransformSalesRecords(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_simplified_output_structure(self):
        result = self.module.transform_sales_records(self.module.SAMPLE_RAW_RECORDS)

        self.assertTrue(len(result["simplified"]) > 0)
        for record in result["simplified"]:
            self.assertIn("transaction_id", record)
            self.assertIn("customer_name", record)
            self.assertIn("amount", record)
            self.assertIn("status", record)

    def test_filter_by_min_amount(self):
        result = self.module.transform_sales_records(
            self.module.SAMPLE_RAW_RECORDS,
            min_amount=self.module.SAMPLE_MIN_AMOUNT
        )

        # Only T001 (250.75), T004 (500.00) should be in completed_only
        self.assertEqual(result["filtered_count"], 2)
        self.assertTrue(all(r["amount"] >= self.module.SAMPLE_MIN_AMOUNT for r in result["completed_only"]))

    def test_completed_transactions_only(self):
        result = self.module.transform_sales_records(self.module.SAMPLE_RAW_RECORDS)

        # All in completed_only should have status 'completed'
        self.assertTrue(all(r["status"] == "completed" for r in result["completed_only"]))

    def test_total_filtered_revenue(self):
        result = self.module.transform_sales_records(
            self.module.SAMPLE_RAW_RECORDS,
            min_amount=self.module.SAMPLE_MIN_AMOUNT
        )

        # T001: 250.75 + T004: 500.00 = 750.75
        expected_total = 750.75
        self.assertEqual(result["total_filtered_revenue"], expected_total)

    def test_unique_customers(self):
        result = self.module.transform_sales_records(self.module.SAMPLE_RAW_RECORDS)

        self.assertTrue(len(result["unique_customers"]) > 0)
        self.assertIsInstance(result["unique_customers"], list)


if __name__ == "__main__":
    unittest.main()
