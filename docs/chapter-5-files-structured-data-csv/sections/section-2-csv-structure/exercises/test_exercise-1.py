import csv
import importlib.util
from pathlib import Path
import tempfile
import unittest


DATA_DIR = Path(__file__).parent / "data"


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestValidateOrdersCsv(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_validation_summary_and_cleaned_output(self):
        input_path = DATA_DIR / "orders_raw.csv"

        with tempfile.TemporaryDirectory() as tmp_dir:
            cleaned_path = Path(tmp_dir) / "orders_clean.csv"

            result = self.module.validate_orders_csv(input_path, cleaned_path)

            self.assertEqual(result["total_rows"], 7)
            self.assertEqual(result["valid_rows"], 4)
            self.assertEqual(result["invalid_rows"], 3)
            self.assertEqual(
                result["department_totals"],
                {
                    "Finance": 399.0,
                    "HR": 301.0,
                    "IT": 749.97,
                    "Operations": 240.0,
                },
            )

            with cleaned_path.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))

            self.assertEqual(len(rows), 4)
            self.assertEqual(
                rows[0],
                {
                    "order_id": "1001",
                    "customer": "Acme",
                    "department": "IT",
                    "quantity": "3",
                    "unit_price": "249.99",
                    "line_total": "749.97",
                },
            )
            self.assertEqual(rows[-1]["order_id"], "1007")
            self.assertEqual(rows[-1]["line_total"], "240.00")


if __name__ == "__main__":
    unittest.main()
