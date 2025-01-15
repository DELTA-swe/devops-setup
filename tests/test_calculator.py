import unittest
from utils.calculator import Calculator  

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test fixture by creating a Calculator object.

        This method is called before each test method is called.
        """
        self.calc = Calculator()

    def test_add(self):
        """
        Tests the add method in the Calculator class.

        Verifies that the addition of two numbers returns the correct result.
        """
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        """
        Tests the subtract method in the Calculator class.

        Verifies that the subtraction of two numbers returns the correct result.
        """
        
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """
        Tests the multiply method in the Calculator class.

        Verifies that the multiplication of two numbers returns the correct result.
        """

        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """
        Tests the divide method in the Calculator class.
        
        Verifies that the division of two numbers returns the correct result,
        and that a ZeroDivisionError is raised when dividing by zero.
        """
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
