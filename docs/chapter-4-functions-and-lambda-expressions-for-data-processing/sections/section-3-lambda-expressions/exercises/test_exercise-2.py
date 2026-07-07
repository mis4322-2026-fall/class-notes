import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestRankCustomersByScore(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_rank_customers(self):
        result = self.module.rank_customers_by_score(
            self.module.SAMPLE_CUSTOMERS,
            self.module.SAMPLE_MIN_SCORE,
        )
        self.assertEqual(result, ["Crown Foods", "Acme"])

    def test_tie_break_on_name(self):
        customers = [
            {"name": "Zeta", "score": 88},
            {"name": "Alpha", "score": 88},
            {"name": "Beta", "score": 70},
        ]
        result = self.module.rank_customers_by_score(customers, 80)
        self.assertEqual(result, ["Alpha", "Zeta"])


if __name__ == "__main__":
    unittest.main()
