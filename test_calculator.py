import unittest
from calculator import add, subtract, multiply, divide

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


    def test_multiply(self):

        self.assertEqual(multiply(7, 5), 35)
        self.assertEqual(multiply(-7, 5), -35)
        self.assertEqual(multiply(7, -5), -35)
        self.assertRaises(TypeError, (multiply( 7, "5")))


    def test_divide(self):

        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
        self.assertRaises(TypeError, divide, "10", 5)
        



if __name__ == "__main__":
    unittest.main()
