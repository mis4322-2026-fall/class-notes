import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestInvoiceRecord(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_invoice_row_from_sample_data(self):
        invoice = self.module.InvoiceRecord(**self.module.SAMPLE_INVOICE)

        self.assertEqual(invoice.total_with_tax(), 1337.5)
        self.assertEqual(invoice.status_label(), "OPEN")
        self.assertEqual(
            invoice.as_row(),
            {
                "invoice_id": "INV-3001",
                "customer_id": "C-104",
                "amount": 1250.0,
                "tax_rate": 0.07,
                "total": 1337.5,
                "paid": False,
            },
        )

    def test_paid_invoice_status(self):
        invoice = self.module.InvoiceRecord("INV-9", "C-1", 500.0, 0.1, True)
        self.assertEqual(invoice.status_label(), "PAID")
        self.assertEqual(invoice.total_with_tax(), 550.0)


if __name__ == "__main__":
    unittest.main()
