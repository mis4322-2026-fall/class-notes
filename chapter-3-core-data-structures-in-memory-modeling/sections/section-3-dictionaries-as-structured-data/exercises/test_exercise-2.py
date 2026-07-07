import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildCustomerCreditViews(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_customer_credit_views(self):
        result = self.module.build_customer_credit_views(
            self.module.SAMPLE_CUSTOMERS,
            self.module.SAMPLE_MIN_CREDIT_LIMIT,
        )

        self.assertEqual(
            result["limit_by_customer"],
            {"C001": 15000, "C002": 8000, "C003": 22000, "C004": 5000},
        )
        self.assertEqual(result["qualified_customers"], ["C001", "C003"])
        self.assertEqual(result["region_counts"], {"North": 2, "West": 1, "unknown": 1})

    def test_empty_customers(self):
        result = self.module.build_customer_credit_views([], 10000)
        self.assertEqual(
            result,
            {"limit_by_customer": {}, "qualified_customers": [], "region_counts": {}},
        )


if __name__ == "__main__":
    unittest.main()
