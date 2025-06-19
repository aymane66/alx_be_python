import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator (unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, -5), -4)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(-4, 2), -6)
        self.assertEqual(self.calc.subtract(10, -1), 11)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(-3 , 4), -12)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-4, -2), 8)


    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-5, 2), -2.5)
        self.assertEqual(self.calc.divide(15, -3), -5)
        self.assertEqual(self.calc.divide(-20, -2), 10)
        self.assertEqual(self.calc.divide(20, 0), None)
        self.assertEqual(self.calc.divide(-2, 0), None)
        self.assertEqual(self.calc.divide(5, 0), None)

