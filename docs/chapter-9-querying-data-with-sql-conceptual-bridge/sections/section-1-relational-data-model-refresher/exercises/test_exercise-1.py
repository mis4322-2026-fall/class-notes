import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-1.py")
    spec = importlib.util.spec_from_file_location("exercise_1", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSchemaInspection(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_get_table_names(self):
        names = self.module.get_table_names(self.module.DB_PATH)
        self.assertEqual(
            names,
            ["courses", "departments", "enrollments", "students"],
        )

    def test_get_student_table_schema(self):
        schema = self.module.get_student_table_schema(self.module.DB_PATH)
        self.assertEqual(schema[0], ("student_id", "INTEGER", 1))
        self.assertIn(("full_name", "TEXT", 0), schema)
        self.assertIn(("major_dept_id", "INTEGER", 0), schema)

    def test_count_records_by_table(self):
        counts = self.module.count_records_by_table(
            self.module.DB_PATH,
            self.module.TABLES_TO_COUNT,
        )
        self.assertEqual(counts["students"], 6)
        self.assertEqual(counts["courses"], 5)
        self.assertEqual(counts["enrollments"], 10)


if __name__ == "__main__":
    unittest.main()
