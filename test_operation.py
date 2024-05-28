# test_operations.py
import unittest
from app import addition, soustraction, multiplication, division

class TestOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 3), 2)
        self.assertEqual(soustraction(10, 7), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(-2, 4), -8)

    def test_division(self):
        self.assertAlmostEqual(division(10, 2), 5)
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == "__main__":
    unittest.main()
