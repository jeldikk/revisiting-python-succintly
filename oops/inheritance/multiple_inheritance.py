# multiple inheritance means; a class inheriting from more than one parent class
# class C(A, B):

# multi level inheritance mean; a inheriting a class that inherits an other class
# C(B) <- B(A) <- A

# this is a grand parent class
# added to demonstrate multi level inheritance
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} can eat")

    def sleep(self):
        print(f"{self.name} can sleep")

# these are parent classes
class Prey(Animal):
    
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    
    def hunt(self):
        print(f"{self.name} is Hunting")

# these are child classes
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass

class Fish(Predator, Prey):
    pass