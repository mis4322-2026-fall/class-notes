import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestCoreQueries(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_fetch_high_scores(self):
        case = self.module.QUERY_CASES["high_scores"]
        rows = self.module.fetch_high_scores(
            self.module.DB_PATH,
            case["min_grade_point"],
            case["limit"],
        )
        self.assertEqual(
            rows,
            [
                (1, 105, 4.0),
                (1, 102, 3.9),
                (3, 103, 3.8),
                (5, 105, 3.8),
            ],
        )

    def test_fetch_courses_by_department(self):
        case = self.module.QUERY_CASES["is_courses"]
        rows = self.module.fetch_courses_by_department(
            self.module.DB_PATH,
            case["department_id"],
            case["limit"],
        )
        self.assertEqual(
            rows,
            [
                ("MIS201", "Data Management"),
                ("MIS310", "Business Analytics"),
                ("MIS330", "Data Warehousing"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
