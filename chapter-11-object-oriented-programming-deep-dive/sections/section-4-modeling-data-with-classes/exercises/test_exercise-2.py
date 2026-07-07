import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestProjectTaskModel(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_builds_project_with_related_tasks(self):
        project = self.module.build_project(
            self.module.SAMPLE_PROJECT,
            self.module.SAMPLE_TASK_ROWS,
        )

        self.assertEqual(project.completion_rate(), 33.33)
        self.assertEqual(project.open_task_titles(), ["Review budget variance", "Prepare training memo"])
        self.assertEqual(
            project.snapshot(),
            {
                "project_id": "PR-88",
                "name": "ERP Rollout",
                "owner": "Maya Chen",
                "total_tasks": 3,
                "completed_tasks": 1,
                "completion_rate": 33.33,
            },
        )

    def test_project_updates_when_tasks_change(self):
        project = self.module.build_project(
            self.module.SAMPLE_PROJECT,
            self.module.SAMPLE_TASK_ROWS,
        )
        project.tasks[1].mark_complete()
        project.add_task(self.module.Task("TK-4", "Close implementation checklist", False))

        self.assertEqual(project.completion_rate(), 50.0)
        self.assertEqual(project.open_task_titles(), ["Prepare training memo", "Close implementation checklist"])


if __name__ == "__main__":
    unittest.main()
