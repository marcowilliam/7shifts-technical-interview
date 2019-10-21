import unittest
from calculator.Calculator import Calculator

class CalculatorTestExercise1(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(8, self.calculator.add("1,2,5"))

    def test_empty_string(self):
        self.assertEqual(0, self.calculator.add(""))

    def test_returns_int(self):
        self.assertIsInstance(self.calculator.add("1,2,5"), int)

if __name__ == "__main__":
    unittest.main()