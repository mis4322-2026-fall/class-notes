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


class TestBuildApprovedCategoryReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_report_metrics_and_output_csv(self):
        input_path = DATA_DIR / "monthly_expenses.csv"

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "approved_expense_report.csv"

            result = self.module.build_approved_category_report(input_path, output_path)

            self.assertEqual(result["included_rows"], 6)
            self.assertEqual(result["grand_total"], 3800.0)
            self.assertEqual(
                result["category_metrics"],
                {
                    "Software": {
                        "transaction_count": 2,
                        "total_amount": 950.0,
                        "average_amount": 475.0,
                    },
                    "Training": {
                        "transaction_count": 2,
                        "total_amount": 550.0,
                        "average_amount": 275.0,
                    },
                    "Travel": {
                        "transaction_count": 2,
                        "total_amount": 2300.0,
                        "average_amount": 1150.0,
                    },
                },
            )

            with output_path.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))

            self.assertEqual([row["category"] for row in rows], ["Travel", "Software", "Training"])
            self.assertEqual(rows[0]["total_amount"], "2300.00")
            self.assertEqual(rows[1]["average_amount"], "475.00")


if __name__ == "__main__":
    unittest.main()
