import importlib.util
from pathlib import Path
import unittest


def load_student_module():
    exercise_path = Path(__file__).with_name("exercise-2.py")
    spec = importlib.util.spec_from_file_location("exercise_2", exercise_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSupportTicket(unittest.TestCase):
    def setUp(self):
        self.module = load_student_module()

    def test_ticket_state_changes_from_sample_data(self):
        ticket = self.module.SupportTicket(**self.module.SAMPLE_TICKET)

        self.assertTrue(ticket.is_urgent())
        self.assertEqual(str(ticket), "T-900 [high] Reset payroll export")

        ticket.set_priority("critical")
        self.assertEqual(ticket.priority, "critical")

        ticket.close()
        self.assertFalse(ticket.is_urgent())

    def test_invalid_priority_raises_value_error(self):
        ticket = self.module.SupportTicket("T-1", "Printer issue", "low")
        with self.assertRaises(ValueError):
            ticket.set_priority("rush")


if __name__ == "__main__":
    unittest.main()
