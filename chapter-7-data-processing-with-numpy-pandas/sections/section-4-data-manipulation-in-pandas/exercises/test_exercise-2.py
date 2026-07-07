import importlib.util
from pathlib import Path
import unittest
import pandas as pd


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestMergeCustomerOrders(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()
        self.orders_df = pd.DataFrame(self.module.SAMPLE_ORDERS)
        self.customers_df = pd.DataFrame(self.module.SAMPLE_CUSTOMERS)

    def test_merge_and_unknowns(self):
        result = self.module.merge_customer_orders(self.orders_df, self.customers_df)

        self.assertEqual(len(result["merged"]), 3)
        self.assertEqual(result["unknown_segment_count"], 1)

    def test_segment_summary(self):
        result = self.module.merge_customer_orders(self.orders_df, self.customers_df)

        summary = result["segment_summary"]
        enterprise_revenue = float(
            summary.loc[summary["segment"] == "Enterprise", "total_revenue"].iloc[0]
        )
        unknown_revenue = float(
            summary.loc[summary["segment"] == "Unknown", "total_revenue"].iloc[0]
        )

        self.assertEqual(enterprise_revenue, 1100.0)
        self.assertEqual(unknown_revenue, 520.0)


if __name__ == "__main__":
    unittest.main()
