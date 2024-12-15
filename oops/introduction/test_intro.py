from intro import Car
import unittest

class IntroTestCases(unittest.TestCase):

    def testing_instantiation(self):
        car = Car('Toyota', 2012, 'red', False)

        print(car) # this print the memory address of the object

        self.assertEqual(car.color, 'red')
        self.assertEqual(car.model, 'Toyota')
        self.assertEqual(car.for_sale, False)
        self.assertEqual(car.year, 2012)

    def testing_multiple_instances(self):
        car1 = Car('Mustang', 2024, "red", False)
        car2 = Car("Ford", 2000, 'blue', True)

        car1.describe()
        car2.describe()
    
    def testing_methods(self):
        car1 = Car("Mustang", 2024, "red", False)
        car2 = Car("Ford", 2000, 'blue', True)

        self.assertEqual(car1.drive(), 'you are driving Mustang')
        self.assertEqual(car2.drive(), 'you are driving Ford')

        self.assertEqual(car1.stop(), 'stop :Mustang')
        self.assertEqual(car2.stop(), 'stop :Ford')


if __name__ == "__main__":
    unittest.main()