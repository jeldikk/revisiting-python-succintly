import unittest
from abstract_classes import Car, MotorCycle, Boat

class TestAbstractClasses(unittest.TestCase):
    
    def test_car(self):
        car = Car()

        car.go()
        car.stop()

    def test_motorcycle(self):
        motor_cycle = MotorCycle()
        motor_cycle.go()
        motor_cycle.stop()

    def test_boat(self):
        boat = Boat()

        boat.go()
        boat.stop()

if __name__ == "__main__":
    unittest.main()