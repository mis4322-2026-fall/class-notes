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


class TestRunServicePipeline(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_pipeline_metrics_and_output_csv(self):
        input_path = DATA_DIR / "service_requests.csv"

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "team_sla_report.csv"

            result = self.module.run_service_pipeline(input_path, output_path)

            self.assertEqual(result["source_rows"], 8)
            self.assertEqual(result["closed_rows"], 7)
            self.assertEqual(
                result["team_metrics"],
                [
                    {
                        "team": "Apps",
                        "closed_count": 2,
                        "high_priority_closed": 2,
                        "avg_resolution_hours": 5.75,
                        "sla_status": "meets_sla",
                    },
                    {
                        "team": "Infra",
                        "closed_count": 2,
                        "high_priority_closed": 1,
                        "avg_resolution_hours": 8.25,
                        "sla_status": "at_risk",
                    },
                    {
                        "team": "Data",
                        "closed_count": 3,
                        "high_priority_closed": 1,
                        "avg_resolution_hours": 10.67,
                        "sla_status": "at_risk",
                    },
                ],
            )

            with output_path.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))

            self.assertEqual([row["team"] for row in rows], ["Apps", "Infra", "Data"])
            self.assertEqual(rows[0]["avg_resolution_hours"], "5.75")
            self.assertEqual(rows[2]["sla_status"], "at_risk")


if __name__ == "__main__":
    unittest.main()
