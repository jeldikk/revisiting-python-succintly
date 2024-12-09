## Numbers

# Just add variable_name = <number-value>

height = 70
temperature = 98.6

print(height)
print(temperature)

'''
It is important to note that Python supports both integers and floating point numbers. 

Integers are numbers without a decimal point, otherwise known as whole numbers. 

Floating point numbers however will always contain a decimal point. 

The data type for integers is int, while the data type for floating 
point numbers is float.
'''

'''
    Python interpreter is capable of performing several operations using numbers
    + (addition), - (subtraction), * (multiplication), / (division), ** (exponent), % (modulo)
'''

'''
>>> 5%4 = 1
>>> -5 % 4 = 3 ( why is it like this ??)
'''
sum = 3 + 2
difference = 88 -2
product = 4 * 2
quotient = 16/4
power = 3 ** 2
remainder = 7 % 3

print("sum :{}".format(sum))
print("difference :{}".format(difference))
print('product :{}'.format(product))
print('quotient :{}'.format(quotient))
print('power :{}'.format(power))
print('remainder :{}'.format(remainder))


# int() function
## convert a string into an integer
quantity_string = '4'
total = int(quantity_string) + 1
print(total)

# float() function
## convert a string into a floating point number
quantity_float = float(quantity_string)
print(quantity_float)

