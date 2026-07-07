import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestJoinQueries(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_build_student_course_report(self):
        rows = self.module.build_student_course_report(
            self.module.DB_PATH,
            self.module.TARGET_TERM,
        )
        self.assertEqual(len(rows), 8)
        self.assertEqual(
            rows[0],
            {
                "full_name": "Ana Silva",
                "course_code": "MIS201",
                "course_title": "Data Management",
                "grade_point": 3.7,
            },
        )
        self.assertEqual(rows[-1]["full_name"], "Elena Ruiz")

    def test_compare_inner_vs_left_join_counts(self):
        result = self.module.compare_inner_vs_left_join_counts(self.module.DB_PATH)
        self.assertEqual(result["inner_count"], 10)
        self.assertEqual(result["left_count"], 11)


if __name__ == "__main__":
    unittest.main()
