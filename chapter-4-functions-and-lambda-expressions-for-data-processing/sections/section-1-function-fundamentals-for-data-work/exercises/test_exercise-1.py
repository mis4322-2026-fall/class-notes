import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestComputeSalesMetrics(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_metrics_for_sample_data(self):
        result = self.module.compute_sales_metrics(self.module.SAMPLE_DAILY_SALES)
        self.assertEqual(
            result,
            {
                "count": 4,
                "total": 4700,
                "average": 1175.0,
                "max": 1420,
                "min": 980,
            },
        )

    def test_empty_input(self):
        result = self.module.compute_sales_metrics([])
        self.assertEqual(
            result,
            {"count": 0, "total": 0, "average": 0, "max": None, "min": None},
        )


if __name__ == "__main__":
    unittest.main()
