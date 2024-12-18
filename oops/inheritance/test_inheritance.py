import unittest

from inheritance import Dog, Cat, Mouse
from multiple_inheritance import Rabbit, Hawk, Fish

class TestInheritance(unittest.TestCase):

    def test_animal_childs(self):
        dog = Dog("Scooby")
        cat = Cat('Tom')
        mouse = Mouse('mickey')

        self.assertEqual(dog.name, 'Scooby')
        self.assertEqual(dog.is_alive, True)

        self.assertEqual(cat.name, 'Tom')
        self.assertEqual(cat.is_alive, True)

        self.assertEqual(mouse.name, 'mickey')
        self.assertEqual(mouse.is_alive, True)

    def test_methods(self):
        dog = Dog('Scooby')
        cat = Cat('Tom')
        mouse = Mouse('Mickey')

        dog.eat()
        dog.sleep()
        dog.speak()

        cat.eat()
        cat.sleep()
        cat.speak()

        mouse.eat()
        mouse.sleep()
        mouse.speak()

class TestMultipleInheritance(unittest.TestCase):

    def test_rabbit(self):
        rabbit = Rabbit("Bugs Bunny")

        rabbit.flee()
        
        # since rabbit inherits Prey class,
        # it will throw AttributeError when calling hunt() method
        with self.assertRaises(AttributeError):
            rabbit.hunt()
        
        # multi level inheritance
        rabbit.eat()
        rabbit.sleep()

    def test_hawk(self):
        hawk = Hawk("Tony")

        hawk.hunt()

        with self.assertRaises(AttributeError):
            hawk.flee()

    def test_fish(self):
        fish = Fish("Nemo")

        fish.flee()
        fish.hunt()

if __name__ == "__main__":
    unittest.main()