import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_priority_queue_from_sample_data(self):
        result = self.module.build_priority_queue(
            self.module.SAMPLE_TASKS,
            self.module.SAMPLE_URGENT_TASKS,
            self.module.SAMPLE_RESOLVED_TASK,
        )

        self.assertEqual(
            result["queue"],
            [
                "close_month_end",
                "review_vendor_contract",
                "approve_budget",
                "refresh_dashboard",
            ],
        )
        self.assertEqual(
            result["top_three"],
            ["close_month_end", "review_vendor_contract", "approve_budget"],
        )
        self.assertEqual(
            result["alphabetical"],
            [
                "approve_budget",
                "close_month_end",
                "refresh_dashboard",
                "review_vendor_contract",
            ],
        )
        self.assertEqual(result["queue_size"], 4)

    def test_missing_resolved_task(self):
        result = self.module.build_priority_queue(["a"], ["b"], "x")
        self.assertEqual(result["queue"], ["b", "a"])


if __name__ == "__main__":
    unittest.main()
