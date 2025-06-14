import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = SimpleCalculator()

    # ---- ADDITION TESTS ----
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 7), 10)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -5), -7)

    def test_addition_mixed_signs(self):
        self.assertEqual(self.calc.add(-4, 10), 6)

    def test_addition_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # ---- SUBTRACTION TESTS ----
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-4, -6), 2)

    def test_subtraction_mixed_signs(self):
        self.assertEqual(self.calc.subtract(-4, 3), -7)

    def test_subtraction_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # ---- MULTIPLICATION TESTS ----
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiplication_mixed_signs(self):
        self.assertEqual(self.calc.multiply(-2, 4), -8)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # ---- DIVISION TESTS ----
    def test_division_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        self.assertEqual(self.calc.divide(-9, -3), 3)

    def test_division_mixed_signs(self):
        self.assertEqual(self.calc.divide(-8, 2), -4)

    def test_division_result_float(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == '__main__':
    unittest.main()
