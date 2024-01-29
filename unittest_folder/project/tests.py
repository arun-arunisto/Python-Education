import unittest
from code.calculations import Calculator


class TestCalculator(unittest.TestCase):
    #calc = Calculator(24, 36)
    def setUp(self):
        self.calc = Calculator(24, 36)
    #test for addition
    def test_add(self):
        self.assertEqual(self.calc.add(),60,
                         "The add() method is wrong")
    #test for subtraction
    def test_sub(self):
        self.assertEqual(self.calc.sub(), -12,
                         "The sub() method is wrong")
    #test for multiplication
    def test_mul(self):
        self.assertEqual(self.calc.mul(), 864,
                         "The mul() method is wrong")
    #test for division
    def test_div(self):
        self.assertEqual(self.calc.div(), 0.6666666666666666,
                         "The div() method is wrong")

if __name__ == '__main__':
    unittest.main()
