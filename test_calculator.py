import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-5, 7), 2)
        self.assertRaises(TypeError, add, 5, "7")
        self.assertRaises(TypeError, add, "5", 7)

if __name__ == "__main__":
    unittest.main()
