import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-5, 7), 2)
        self.assertRaises(TypeError, add, 5, "7")
        self.assertRaises(TypeError, add, "5", 7)



    def test_subtract(self):

        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(-7, 5), -12)
        self.assertEqual(subtract(7, -5), 12)
        self.assertRaises(TypeError, subtract, 7, "5")




if __name__ == "__main__":
    unittest.main()
