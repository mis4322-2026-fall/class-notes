import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestCustomerRecord(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_customer_summary_from_sample_data(self):
        customer = self.module.CustomerRecord(**self.module.SAMPLE_CUSTOMER)

        self.assertEqual(customer.remaining_credit(), 800.0)
        self.assertFalse(customer.is_over_limit())
        self.assertEqual(
            customer.summary(),
            {
                "customer_id": "C-104",
                "name": "Northwind Office Supply",
                "balance": 4200.0,
                "remaining_credit": 800.0,
                "is_active": True,
            },
        )

    def test_over_limit_detection(self):
        customer = self.module.CustomerRecord("C-900", "Apex Labs", 1000.0, 1350.0, True)
        self.assertTrue(customer.is_over_limit())
        self.assertEqual(customer.remaining_credit(), -350.0)


if __name__ == "__main__":
    unittest.main()
