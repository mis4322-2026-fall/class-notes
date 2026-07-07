import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildTeamWorkloadReport(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_team_workload_report(self):
        result = self.module.build_team_workload_report(self.module.SAMPLE_TICKETS)
        self.assertEqual(
            result["App"],
            {
                "ticket_count": 2,
                "total_hours": 9.0,
                "high_priority_count": 1,
                "average_hours": 4.5,
            },
        )
        self.assertEqual(
            result["Infra"],
            {
                "ticket_count": 2,
                "total_hours": 8.0,
                "high_priority_count": 1,
                "average_hours": 4.0,
            },
        )
        self.assertEqual(
            result["Data"],
            {
                "ticket_count": 1,
                "total_hours": 4.0,
                "high_priority_count": 0,
                "average_hours": 4.0,
            },
        )

    def test_empty_tickets(self):
        self.assertEqual(self.module.build_team_workload_report([]), {})


if __name__ == "__main__":
    unittest.main()
