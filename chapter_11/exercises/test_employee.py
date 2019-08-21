import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    """Tests for Employee class."""

    def setUp(self):
        """Create an Employee."""
        self.my_employee = Employee('john', 'doe', 120000)

    def test_give_default_raise(self):
        """Test that increase the annual salary by the default value (5000)."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 125000)

    def test_give_custom_raise(self):
        """Test that increase the annual salary by a custom value."""
        self.my_employee.give_raise(8500)
        self.assertEqual(self.my_employee.annual_salary, 128500)


if __name__ == '__main__':
    unittest.main()
