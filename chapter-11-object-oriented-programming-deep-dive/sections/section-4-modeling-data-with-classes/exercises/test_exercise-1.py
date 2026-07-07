import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestCustomerInvoiceModel(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_builds_related_objects_from_sample_rows(self):
        invoices = self.module.build_invoice_objects(
            self.module.SAMPLE_CUSTOMER_ROW,
            self.module.SAMPLE_INVOICE_ROWS,
        )

        self.assertEqual(len(invoices), 2)
        self.assertIs(invoices[0].customer, invoices[1].customer)
        self.assertEqual(str(invoices[0].customer), "C-220 | Acme Health | enterprise")
        self.assertEqual(invoices[0].amount_due(), 800.0)
        self.assertEqual(invoices[1].amount_due(), 0)
        self.assertEqual(
            invoices[0].export_row(),
            {
                "invoice_id": "INV-2201",
                "customer_id": "C-220",
                "customer_name": "Acme Health",
                "segment": "enterprise",
                "amount": 800.0,
                "paid": False,
            },
        )

    def test_mark_paid_updates_due_amount(self):
        invoices = self.module.build_invoice_objects(
            self.module.SAMPLE_CUSTOMER_ROW,
            self.module.SAMPLE_INVOICE_ROWS,
        )
        invoices[0].mark_paid()
        self.assertEqual(invoices[0].amount_due(), 0)
        self.assertTrue(invoices[0].paid)


if __name__ == "__main__":
    unittest.main()
