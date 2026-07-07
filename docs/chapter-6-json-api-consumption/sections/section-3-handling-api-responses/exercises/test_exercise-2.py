import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestPaginateAndAggregate(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_aggregate_multiple_pages(self):
        responses = [self.module.SAMPLE_PAGE_1, self.module.SAMPLE_PAGE_2]
        result = self.module.paginate_and_aggregate(responses)

        self.assertEqual(result["transaction_count"], 4)
        self.assertEqual(result["successful_pages"], 2)
        self.assertEqual(result["failed_pages"], 0)

    def test_total_amount_calculation(self):
        responses = [self.module.SAMPLE_PAGE_1, self.module.SAMPLE_PAGE_2]
        result = self.module.paginate_and_aggregate(responses)

        # 100.50 + 250.00 + 175.75 + 300.00 = 826.25
        expected_total = 826.25
        self.assertEqual(result["total_amount"], expected_total)

    def test_handle_failed_pages(self):
        responses = [self.module.SAMPLE_PAGE_1, self.module.SAMPLE_PAGE_3_ERROR]
        result = self.module.paginate_and_aggregate(responses)

        self.assertEqual(result["successful_pages"], 1)
        self.assertEqual(result["failed_pages"], 1)
        self.assertEqual(result["transaction_count"], 2)

    def test_unique_products_extracted(self):
        responses = [self.module.SAMPLE_PAGE_1, self.module.SAMPLE_PAGE_2]
        result = self.module.paginate_and_aggregate(responses)

        self.assertEqual(len(result["products"]), 4)
        self.assertIn("A001", result["products"])
        self.assertIn("B002", result["products"])

    def test_empty_response_list(self):
        result = self.module.paginate_and_aggregate([])

        self.assertEqual(result["transaction_count"], 0)
        self.assertEqual(result["successful_pages"], 0)
        self.assertEqual(result["total_amount"], 0.0)


if __name__ == "__main__":
    unittest.main()
