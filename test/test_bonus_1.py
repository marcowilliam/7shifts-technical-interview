import unittest
from calculator.Calculator import Calculator

class CalculatorTestBonus1(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(2, self.calculator.add("2,1001"))


if __name__ == "__main__":
    unittest.main()