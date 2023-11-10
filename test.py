from decimal import DivisionByZero
import unittest

def division(num1, num2):
    if type(num1) not in [int, float] or type(num2) not in [int, float]:
        raise TypeError
    if num2 == 0:
        raise DivisionByZero
    
    return round(num1 / num2, 8)

class DivisionTest(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(4,2), 2)
        self.assertEqual(division(10,2), 5)
        self.assertEqual(division(0.009,0.003), 3)
        self.assertRaises(DivisionByZero, division, 4, 0)

    def test_values(self):
        self.assertRaises(TypeError, division, 'a', 2)
        self.assertRaises(TypeError, division, [4], 2)
        self.assertRaises(TypeError, division, None, None)
        self.assertEqual(division(4.4, 2), 2.2)

if __name__ == '__main__':
    unittest.main()