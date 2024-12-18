# super() = function used in a child class to call methods of parent class( superclass )
# allows you to extend the functionality of the inherited methods

from abc import ABC

class Shape(ABC):
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, radius, color, is_filled):
        super().__init__(color, is_filled)
        self.radius = radius
        # self.color = color
        # self.is_filled = is_filled

class Square(Shape):
    def __init__(self, side, color, is_filled):
        super().__init__(color, is_filled)
        self.side = side
        # self.color = color
        # self.is_filled = is_filled
    
    def describe(self):
        super().describe()
        print(f"It is a Square with are {self.side ** 2}")

class Triangle(Shape):
    def __init__(self, height, width, color, is_filled):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width
        # self.color = color
        # self.is_filled = is_filled