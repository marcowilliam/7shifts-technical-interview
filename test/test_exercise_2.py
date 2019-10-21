import unittest
from calculator.Calculator import Calculator

class CalculatorTestExercise2(unittest.TestCase):
    calculator = Calculator()
    def test_add_with_line_break(self):
        self.assertEqual(6, self.calculator.add("1\n,2,3"))
        self.assertEqual(7, self.calculator.add("1,\n2,4"))

if __name__ == "__main__":
    unittest.main()