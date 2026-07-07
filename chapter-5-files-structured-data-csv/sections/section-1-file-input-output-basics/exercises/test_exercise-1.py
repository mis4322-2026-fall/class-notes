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


class TestProcessSalesLog(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_process_sales_log_summary_and_output_file(self):
        input_path = DATA_DIR / "sales_log.txt"

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "region_report.txt"

            result = self.module.process_sales_log(input_path, output_path)

            self.assertEqual(result["line_count"], 8)
            self.assertEqual(result["valid_count"], 6)
            self.assertEqual(result["invalid_count"], 2)
            self.assertEqual(
                result["region_totals"],
                {
                    "East": 1100.0,
                    "North": 2000.0,
                    "South": 980.0,
                    "West": 2000.0,
                },
            )

            report_text = output_path.read_text(encoding="utf-8")
            self.assertEqual(
                report_text,
                "\n".join(
                    [
                        "Region Totals",
                        "East: 1100.00",
                        "North: 2000.00",
                        "South: 980.00",
                        "West: 2000.00",
                        "Grand Total: 6080.00",
                    ]
                )
                + "\n",
            )


if __name__ == "__main__":
    unittest.main()
