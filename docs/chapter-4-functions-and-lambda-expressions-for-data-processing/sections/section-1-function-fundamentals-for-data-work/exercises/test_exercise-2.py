import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestEvaluateServiceLevels(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_service_level_metrics(self):
        result = self.module.evaluate_service_levels(
            self.module.SAMPLE_RESPONSE_TIMES,
            self.module.SAMPLE_SLA_TARGET,
        )
        self.assertEqual(result["total_tickets"], 6)
        self.assertEqual(result["avg_response_time"], 39.33)
        self.assertEqual(result["within_sla_count"], 3)
        self.assertEqual(result["breach_count"], 3)
        self.assertEqual(result["sla_rate"], 0.5)

    def test_empty_input(self):
        result = self.module.evaluate_service_levels([], 30)
        self.assertEqual(
            result,
            {
                "total_tickets": 0,
                "avg_response_time": 0,
                "within_sla_count": 0,
                "breach_count": 0,
                "sla_rate": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
