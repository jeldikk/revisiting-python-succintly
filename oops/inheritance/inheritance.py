# Inheritance: Allows a class to insert attributes and method from another class
# This helps with code reusability and extensibility
# to inherit a class used this style -> class Child(Parent):

# if you have common implementation you can keep code in parent class

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} can sleep")

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)

    # you can also have concrete class specific methods
    def speak(self):
        print("WOOFF")

    # you are overriding eat method of parent class by re-defining the class
    def eat(self):
        print(f"Dog {self.name} is very honest and it eats with noise")


class Cat(Animal):
    
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("SQUEEK")

    def eat(self):
        print(f"Mouse {self.name} eats firstly cutting into small pieces and finishes calmly")