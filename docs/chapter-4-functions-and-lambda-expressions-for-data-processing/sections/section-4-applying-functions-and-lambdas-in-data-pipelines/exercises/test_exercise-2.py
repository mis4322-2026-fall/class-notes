import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestBuildTeamCostPipeline(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_team_cost_pipeline(self):
        result = self.module.build_team_cost_pipeline(
            self.module.SAMPLE_TICKETS,
            self.module.SAMPLE_MIN_COST,
        )
        self.assertEqual(result, [("App", 600.0), ("Infra", 600.0)])

    def test_threshold_filter(self):
        result = self.module.build_team_cost_pipeline(self.module.SAMPLE_TICKETS, 550)
        self.assertEqual(result, [("App", 600.0), ("Infra", 600.0)])


if __name__ == "__main__":
    unittest.main()
