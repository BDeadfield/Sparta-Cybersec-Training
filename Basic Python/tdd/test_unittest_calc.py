import unittest
import calculator

class Calctest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.addition(2, 5), 7)
        self.assertEqual(calculator.addition(12, 15), 27)
        self.assertEqual(calculator.addition(-1, 9), 8)
        self.assertEqual(calculator.addition(0, 0), 0)
