import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestValidateAndExtractUsers(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_complete_users_extracted(self):
        result = self.module.validate_and_extract_users(self.module.SAMPLE_RESPONSE_JSON)

        self.assertEqual(result["valid_count"], 2)
        # Alice and Bob have all required fields
        self.assertEqual(len(result["complete_users"]), 2)

    def test_incomplete_users_tracked(self):
        result = self.module.validate_and_extract_users(self.module.SAMPLE_RESPONSE_JSON)

        self.assertEqual(result["invalid_count"], 3)
        # Carol (null email), David (missing email), Eve (missing id)
        self.assertEqual(len(result["incomplete_users"]), 3)

    def test_emails_extracted(self):
        result = self.module.validate_and_extract_users(self.module.SAMPLE_RESPONSE_JSON)

        self.assertEqual(len(result["emails_available"]), 2)
        self.assertIn("alice@company.com", result["emails_available"])
        self.assertIn("bob@company.com", result["emails_available"])

    def test_active_users_counted(self):
        result = self.module.validate_and_extract_users(self.module.SAMPLE_RESPONSE_JSON)

        self.assertEqual(result["active_users_count"], 2)

    def test_empty_data_list(self):
        response = {"status": "success", "data": []}
        result = self.module.validate_and_extract_users(response)

        self.assertEqual(result["valid_count"], 0)
        self.assertEqual(result["invalid_count"], 0)


if __name__ == "__main__":
    unittest.main()
