import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestPrepareOrderTimeline(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_uses_sample_dataset(self):
        result = self.module.prepare_order_timeline(
            self.module.SAMPLE_INITIAL_ORDERS,
            self.module.SAMPLE_INCOMING_ORDERS,
            self.module.SAMPLE_CANCELED_ORDER,
            self.module.SAMPLE_RECENT_N,
        )

        self.assertEqual(result["orders"], [120, 135, 142, 150, 147, 160])
        self.assertEqual(result["recent"], [150, 147, 160])
        self.assertEqual(result["sorted_orders"], [120, 135, 142, 147, 150, 160])
        self.assertEqual(result["total"], 854)
        self.assertEqual(result["average"], 142.33)

    def test_handles_non_positive_recent_n(self):
        result = self.module.prepare_order_timeline([10, 20], [30], 99, 0)
        self.assertEqual(result["orders"], [10, 20, 30])
        self.assertEqual(result["recent"], [])


if __name__ == "__main__":
    unittest.main()
