import unittest
from super_function import Circle, Square, Triangle

class TestSuperFunction(unittest.TestCase):
    
    def test_circle(self):
        circle = Circle(5, 'red', True)

        circle.describe()

        self.assertEqual(circle.radius, 5)
        self.assertEqual(circle.color, 'red')
        self.assertEqual(circle.is_filled, True)

    def test_square(self):
        square = Square(10, 'blue', False)
        square.describe()
        self.assertEqual(square.side, 10)
        self.assertEqual(square.color, 'blue')
        self.assertEqual(square.is_filled, False)

    def test_triangle(self):
        triangle = Triangle(10, 10, 'blue', True)
        triangle.describe()
        self.assertEqual(triangle.width, 10)
        self.assertEqual(triangle.height, 10)
        self.assertEqual(triangle.color, 'blue')
        self.assertEqual(triangle.is_filled, True)
        



if __name__ == "__main__":
    unittest.main()
