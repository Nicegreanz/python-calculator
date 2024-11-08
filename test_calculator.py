import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

        #test add()
    def test_add_negative_number(self):
        self.assertEqual(self.calc.add(-3,-2),-5)

        #test subtract()
    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(7,2),5)
    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(7,8),-1)

        # Test multiply()
    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    # Test divide()
    def test_divide_evenly(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(7, 2), 3)  # round number expected

    # Test modulo()
    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
    def test_modulo_with_remainder(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()