from unittest import TestCase
import Program

class Test(TestCase):
    def test_binary_search(self):
        arr = [10, 20, 30, 40, 50]

        self.assertEqual(Program.binary_search(arr, 0, len(arr), 30), 2)
        # self.fail()

    def test_binary_search_1(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(Program.binary_search(arr, 0, len(arr) - 1, 60), -1)

    def test_binary_search_2(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(Program.binary_search(arr, 0, len(arr) - 1, 9), -1)

    def test_check_condition_PIT(self):
        person = {'age': 18, 'salary': 11000000}
        self.assertEqual(Program.check_condition_PIT(person.get("age"), person.get("salary")), True)

    def test_check_condition_PIT_1(self):
        person = {'age': 18, 'salary': 10000000}
        self.assertEqual(Program.check_condition_PIT(person.get("age"), person.get("salary")), False)

    def test_check_condition_PIT_2(self):
        person = {'age': 17, 'salary': 11000000}
        self.assertEqual(Program.check_condition_PIT(person.get("age"), person.get("salary")), False)