import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestPythonPandasMapping(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_fetch_honor_roll(self):
        rows = self.module.fetch_honor_roll(self.module.DB_PATH, 3.7)
        self.assertEqual(rows[0]["full_name"], "Ana Silva")
        self.assertEqual(rows[1]["full_name"], "Elena Ruiz")
        self.assertAlmostEqual(rows[0]["avg_grade"], 3.87, places=2)
        self.assertAlmostEqual(rows[1]["avg_grade"], 3.7, places=2)

    def test_load_department_summary_df(self):
        df = self.module.load_department_summary_df(self.module.DB_PATH)
        self.assertEqual(df.shape[0], 3)
        self.assertEqual(
            df.columns.tolist(),
            ["department", "enrolled_students", "avg_grade"],
        )
        is_row = df[df["department"] == "Information Systems"].iloc[0]
        self.assertEqual(int(is_row["enrolled_students"]), 4)
        self.assertAlmostEqual(float(is_row["avg_grade"]), 3.64, places=2)


if __name__ == "__main__":
    unittest.main()
