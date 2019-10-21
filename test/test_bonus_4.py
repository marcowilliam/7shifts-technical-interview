import unittest
from calculator.Calculator import Calculator

class CalculatorTestBonus4(unittest.TestCase):
    calculator = Calculator()
    def test_add(self):
        self.assertEqual(9, self.calculator.add("//$$,@@@,**\n1$$2@@@3**3"))

if __name__ == "__main__":
    unittest.main()