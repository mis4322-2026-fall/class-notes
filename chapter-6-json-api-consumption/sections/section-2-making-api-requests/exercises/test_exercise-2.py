import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch, Mock


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSearchProjects(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    @patch('requests.get')
    def test_search_with_status_filter(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = [
            item for item in self.module.SAMPLE_SEARCH_RESPONSE_DATA
            if item['status'] == 'active'
        ]
        mock_get.return_value = response

        result = self.module.search_projects(
            self.module.SAMPLE_SEARCH_QUERY,
            status_filter=self.module.SAMPLE_STATUS,
            limit=self.module.SAMPLE_LIMIT,
            base_url=self.module.SAMPLE_BASE_URL
        )

        self.assertEqual(result["match_count"], 3)
        self.assertIn("search", result["request_url"])
        self.assertEqual(result["query_params"]["q"], self.module.SAMPLE_SEARCH_QUERY)

    @patch('requests.get')
    def test_query_params_included(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = self.module.SAMPLE_SEARCH_RESPONSE_DATA
        mock_get.return_value = response

        result = self.module.search_projects(
            "test",
            status_filter="active",
            limit=20
        )

        self.assertEqual(result["query_params"]["q"], "test")
        self.assertEqual(result["query_params"]["status"], "active")
        self.assertEqual(result["query_params"]["limit"], 20)

    @patch('requests.get')
    def test_unique_owners_extracted(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = self.module.SAMPLE_SEARCH_RESPONSE_DATA
        mock_get.return_value = response

        result = self.module.search_projects("analytics")

        self.assertIsInstance(result["owners"], list)
        self.assertTrue(len(result["owners"]) > 0)

    @patch('requests.get')
    def test_request_url_construction(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = []
        mock_get.return_value = response

        result = self.module.search_projects(
            "query",
            base_url="https://custom.api.com"
        )

        self.assertIn("https://custom.api.com", result["request_url"])


if __name__ == "__main__":
    unittest.main()
