## A Boolean is a specific data type tha tis only capable on having onw of two possible values
# True or False

logical_variable_name = True
print(logical_variable_name)

the_true_boolean = True
the_false_boolean = False

print(the_true_boolean)
print(the_false_boolean)

# Comparators
# populator comparator operators are
# == (Equal to), 
# > (Greater than), 
# >= (Greater than or Equal), 
# < (Less than), 
# <= (Less than or Equal), 
# != (Not Equal)
print("///// comparator operators /////")
print((1 == 2) is False)
print((1 > 2) is False)
print((1 >= 2) is False)
print((1 < 2) is True)
print((1 <= 2) is True)
print((1 != 2) is True)

## Boolean Operators

# and -> perform and operation
# or -> perform or operation
# not -> perform not operation
print("///// Boolean operators /////")
print(True and True is True)
print(True and False is False)
print(False and True is False)
print(False and False is False)

print(True or True is True)
print(True or False is True)
print(False or True is True)
print(False or False is False)

print(not True is False)
print(not False is True)

## Conditionals
# the if statement will evaluate a Boolean expression and if it True
# the code associated with it will be executed.

if 43 < 44:
    print('Forty-Three is less than Forty Four')

age = 32
if age >= 35:
    print("You are old enough to be the President.")
else:
    print("You are not old enough to be the President.")

print("Have a nice day")


# python provides a special keyword for 'else if' block elif
age = 103

if age >= 35:
    print("You are old enough to be a Representative, Senator, or the President")
elif age >= 30:
    print("You are old enough to be a Senator")
elif age >= 25:
    print("You are old enough to be a Representative")
else:
    print("You are not old enough to be a representative, Senator, or the President")

print('Have fun with age {}'.format(age))
