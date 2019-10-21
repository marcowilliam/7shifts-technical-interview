import unittest
from calculator.Calculator import Calculator

class CalculatorTestExercise3(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(8, self.calculator.add("//;\n1;3;4"))
        self.assertEqual(6, self.calculator.add("//$\n1$2$3"))
        self.assertEqual(13, self.calculator.add("//@\n2@3@8"))

if __name__ == "__main__":
    unittest.main()