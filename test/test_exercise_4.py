import unittest
from calculator.Calculator import Calculator, NegativesNotAllowed

class CalculatorTestExercise4(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        with self.assertRaises(NegativesNotAllowed) as context:
            self.calculator.add("//;\n1;3;-4;-5")
        self.assertEqual("[-4, -5]", str(context.exception))

if __name__ == "__main__":
    unittest.main()