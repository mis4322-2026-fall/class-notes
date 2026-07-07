import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestEmployeeProfile(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_employee_profile_from_sample_data(self):
        employee = self.module.EmployeeProfile(**self.module.SAMPLE_EMPLOYEE)

        self.assertEqual(
            employee.profile(),
            {
                "employee_id": "E-204",
                "full_name": "Jordan Lee",
                "department": "Finance",
                "title": "Senior Analyst",
                "manager": "Dana Holt",
            },
        )
        self.assertEqual(employee.email_alias(), "jordan.lee@finance.example.com")
        self.assertEqual(
            repr(employee),
            "EmployeeProfile(employee_id='E-204', full_name='Jordan Lee', department='Finance', title='Senior Analyst', manager='Dana Holt')",
        )

    def test_manager_can_be_optional(self):
        employee = self.module.EmployeeProfile("E-1", "Casey Brown", "HR", "Coordinator")
        self.assertIsNone(employee.profile()["manager"])
        self.assertEqual(employee.email_alias(), "casey.brown@hr.example.com")


if __name__ == "__main__":
    unittest.main()
