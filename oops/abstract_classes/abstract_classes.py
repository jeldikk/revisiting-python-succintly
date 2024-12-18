# Abstract Class: A class that cannot be instantiated on its own;
# abstract classes are meant to be subclasses.
# They can contain abstract methods,
# Benefits of Abstract classes:
# 1. Prevents instantiation of the class itself
# 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class MotorCycle(Vehicle):

    def go(self):
        print("You ride the motor cycle")

    def stop(self):
        print("You stop the motor cycle")


class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")