import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestTask(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_task_updates_state_from_sample_data(self):
        task = self.module.Task(**self.module.SAMPLE_TASK)

        task.log_hours(2.5)
        task.log_hours(4.0)
        task.mark_complete()

        self.assertTrue(task.is_over_budget())
        self.assertEqual(
            task.summary(),
            {
                "task_id": "TASK-17",
                "title": "Prepare invoice aging report",
                "assigned_to": "Rina Patel",
                "estimated_hours": 6.0,
                "hours_logged": 6.5,
                "status": "complete",
            },
        )

    def test_log_hours_rejects_non_positive_values(self):
        task = self.module.Task("TASK-1", "Draft memo", "Avery", 2.0)
        with self.assertRaises(ValueError):
            task.log_hours(0)


if __name__ == "__main__":
    unittest.main()
