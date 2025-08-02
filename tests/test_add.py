import unittest
from add import add_numbers, subtract_numbers


class TestAddFunctions(unittest.TestCase):
    # Test Addition Function
    def test_add_positive_numbers(self):
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add_numbers(-1, -1)
        self.assertEqual(result, -2)

    def test_add_zero(self):
        result = add_numbers(0, 5)
        self.assertEqual(result, 5)

    def test_add_float_numbers(self):
        result = add_numbers(1.5, 2.5)
        self.assertEqual(result, 4.0)

    # Test Subtraction Function
    def test_subtract_positive_numbers(self):
        result = subtract_numbers(10, 4)
        self.assertEqual(result, 6)

    def test_subtract_negative_numbers(self):
        result = subtract_numbers(-1, -1)
        self.assertEqual(result, 0)

    def test_subtract_zero(self):
        result = subtract_numbers(0, 5)
        self.assertEqual(result, -5)

    def test_subtract_float_numbers(self):
        result = subtract_numbers(5.5, 2.5)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()