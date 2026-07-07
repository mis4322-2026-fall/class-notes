import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch, Mock


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestFetchProductData(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    @patch('requests.get')
    def test_fetch_all_successful(self, mock_get):
        # Mock successful responses for all products
        def mock_response(url, timeout=10):
            product_id = int(url.split('/')[-1])
            response = Mock()
            response.status_code = 200
            response.json.return_value = self.module.SAMPLE_RESPONSE_DATA[product_id]
            return response

        mock_get.side_effect = mock_response

        result = self.module.fetch_product_data(
            self.module.SAMPLE_PRODUCT_IDS,
            self.module.SAMPLE_BASE_URL,
            self.module.SAMPLE_TIMEOUT
        )

        self.assertEqual(result["total_requested"], 3)
        self.assertEqual(result["total_successful"], 3)
        self.assertEqual(result["failed_ids"], [])
        self.assertEqual(len(result["successful"]), 3)

    @patch('requests.get')
    def test_total_value_calculation(self, mock_get):
        def mock_response(url, timeout=10):
            product_id = int(url.split('/')[-1])
            response = Mock()
            response.status_code = 200
            response.json.return_value = self.module.SAMPLE_RESPONSE_DATA[product_id]
            return response

        mock_get.side_effect = mock_response

        result = self.module.fetch_product_data(
            self.module.SAMPLE_PRODUCT_IDS,
            self.module.SAMPLE_BASE_URL
        )

        # Widget A: 29.99 * 100 = 2999, Widget B: 39.99 * 50 = 1999.50, Widget C: 49.99 * 25 = 1249.75
        expected_total = round(2999 + 1999.50 + 1249.75, 2)
        self.assertEqual(result["total_value"], expected_total)

    @patch('requests.get')
    def test_handle_some_failures(self, mock_get):
        def mock_response(url, timeout=10):
            product_id = int(url.split('/')[-1])
            response = Mock()
            if product_id == 102:
                response.status_code = 404
                return response
            response.status_code = 200
            response.json.return_value = self.module.SAMPLE_RESPONSE_DATA[product_id]
            return response

        mock_get.side_effect = mock_response

        result = self.module.fetch_product_data(
            self.module.SAMPLE_PRODUCT_IDS,
            self.module.SAMPLE_BASE_URL
        )

        self.assertEqual(result["total_requested"], 3)
        self.assertEqual(result["total_successful"], 2)
        self.assertIn(102, result["failed_ids"])

    @patch('requests.get')
    def test_empty_product_list(self, mock_get):
        result = self.module.fetch_product_data([], self.module.SAMPLE_BASE_URL)

        self.assertEqual(result["total_requested"], 0)
        self.assertEqual(result["total_successful"], 0)
        self.assertEqual(result["total_value"], 0.0)


if __name__ == "__main__":
    unittest.main()
