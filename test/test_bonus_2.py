import unittest
from calculator.Calculator import Calculator

class CalculatorTestBonus2(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(6, self.calculator.add("//***\n1***2***3"))

if __name__ == "__main__":
    unittest.main()