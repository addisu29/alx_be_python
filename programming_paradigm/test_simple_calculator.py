import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # Addition tests
    def test_add_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)
        self.assertAlmostEqual(self.calc.add(-1.2, 1.2), 0.0)

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(10**12, 10**12), 2 * 10**12)

    # Subtraction tests
    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    # Multiplication tests
    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(0, 1000), 0)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 0.2), 0.5, places=7)

    # Division tests
    def test_divide_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)

    def test_divide_by_zero(self):
        """When divisor is zero, the method is specified to return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_precision(self):
        # check a case that produces a repeating decimal
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result, 1/3, places=7)

if __name__ == "__main__":
    unittest.main()