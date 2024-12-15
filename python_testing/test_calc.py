import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        actual = calc.add(2, 3)
        self.assertEqual(actual, 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(2, -2), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-5, 10), -15)
        self.assertEqual(calc.subtract(3, -4), 7)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 3), 30)
        self.assertEqual(calc.multiply(-1, 10), -10)
        self.assertEqual(calc.multiply(10, 0), 0)
        self.assertEqual(calc.multiply(0.01, 10), 0.1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(-5, 2), -2.5)
        self.assertEqual(calc.divide(5, -2), -2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)
        
        #below code is with context manager
        with self.assertRaises(ValueError):
            calc.divide(5, 0)
 
if __name__ == "__main__":
    unittest.main()