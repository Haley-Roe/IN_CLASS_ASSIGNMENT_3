import unittest
from app import multiply_nums
class TestApp(unittest.TestCase):
    def test_multiply_two_numbers(self):
        self.assertEqual(multiply_nums(2, 3), 6)

    def test_multiply_multiple_numbers(self):
        self.assertEqual(multiply_nums(2, 3, 4), 24)

    def test_multiply_decimal_and_negative_numbers(self):
        self.assertEqual(multiply_nums(2.5, -2), -5.0)

    def test_multiply_one_number(self):
        self.assertEqual(multiply_nums(7), 7)

if __name__ == "__main__":
    unittest.main()
