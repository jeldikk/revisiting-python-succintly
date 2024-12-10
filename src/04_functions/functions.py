# DRY: Dont repeat yourself
# Instead of repeating several lines of code every time you want to perform 

def say_hello():
    print("Say Hello !")

say_hello()

'''
A function will have to be defined before it can be called. Define your function in python program before calling it.
'''
# below code will throw NameError 

# hello_world()

# def hello_world():
#     print("Hello World!")


def hello_name(name):
    print("Hello {}!".format(name))

hello_name('Erin')
hello_name('Everybody')

# if a function definition accepts parameters, it means the parameters are required. You can make them optional by assigning a default value to parameters

# You can make some parameters as optional and some required

# required parameters should come first later optional ones

def full_name(first_name, last_name = "Doe"):
    print("Hello, {} {}".format(last_name, first_name))

full_name('Kamal Kumar', "Jeldi") # -> Jeldi Kamal Kumar

full_name("Kamal Kumar") # -> Doe Kamal Kumar


def wish_good_morning(name):
    '''
        Here goes the doc strings or documentation string.
        This space acts as a brief summary of the function
    '''
    print("Good Morning, {}".format(name))


def even_or_odd(number):
    '''
        Determines if number provided is even or odd
    '''
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(5))

def is_even(number):
    if number % 2 == 0:
        return True
    return False

def is_odd(number):
    if number % 2 == 0:
        return False
    return True

'''
we can also combine multiple functions to create beautiful python programs
'''

def get_name():
    user_input = input("Enter your name :")
    return user_input

def say_name(name):
    print("Hello, {}".format(name))

def get_and_say_name():
    user_input = get_name()
    say_name(user_input)

get_and_say_name()