# object = A bundle of related attributes (variables) and methods (functions)
# you need a class to create many objects

# class is like a blueprint which describes different properties of instantiated object
# and methods which describe the business logic what happens with these attributes

# lets create a Car class and also create an object

class Car:
    # constructor of the class
    # dunder method ( double underscore method )
    # constructor receives arguments which helps to configure the object
    # self is similar to this ( also called the object we are working on )
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        return "you are driving {}".format(self.model)

    def stop(self):
        return "stop :{}".format(self.model)
    
    def describe(self):
        print("{} {} {}".format(self.year, self.color, self.model))