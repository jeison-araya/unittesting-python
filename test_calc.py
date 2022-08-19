import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_sum_numbers(self):
        result = calc.sum_numbers(10, 5)
        self.assertEqual(result, 15)

    def test_substraction(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        result = calc.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, calc.divide, 10, 0)
