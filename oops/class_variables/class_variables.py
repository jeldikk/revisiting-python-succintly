# class variables = Shared among all instances of a class
# these are defined outside constructor
# allows to share data among all instances created from that class
# on other hand, instance variables are defined inside constructor

class Student:

    class_year = 2024
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1
