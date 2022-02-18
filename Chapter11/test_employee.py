import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        firstname = "John"
        lastname = "Smith"
        salary = 35000
        self.employee = Employee(firstname, lastname, salary)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,40000)
    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary,45000)

if __name__ == "__main__":
    unittest.main()