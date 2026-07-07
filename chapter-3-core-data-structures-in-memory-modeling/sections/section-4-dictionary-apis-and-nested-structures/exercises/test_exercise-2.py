import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildCustomerOrderSummary(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_nested_customer_order_aggregation(self):
        result = self.module.build_customer_order_summary(
            self.module.SAMPLE_CUSTOMERS,
            self.module.SAMPLE_MIN_REVENUE,
        )

        self.assertEqual(result["revenue_by_customer"], {"Acme": 800.0, "Blue Harbor": 360.0})
        self.assertEqual(result["qualifying_customers"], ["Acme"])
        self.assertEqual(result["order_count_by_customer"], {"Acme": 3, "Blue Harbor": 1})

    def test_empty_input(self):
        result = self.module.build_customer_order_summary([], 100)
        self.assertEqual(
            result,
            {
                "revenue_by_customer": {},
                "qualifying_customers": [],
                "order_count_by_customer": {},
            },
        )


if __name__ == "__main__":
    unittest.main()
