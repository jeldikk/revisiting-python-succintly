## A string is utilized to represent text

# In Python string are always surrounded by quotes ( either single or double)

# with single quotes
vegetable = 'asparagus'

# with double quotes
vegetable = "asparagus"

## Using double quotes within strings
sentence = 'He said, "That asparagus tastes great"'

## Using single quotes within strings
sentence = "That's some great tasting asparagus!"

# what if you are looking to use both single and double quotes in the same string
sentence_in_double = "He said, \"That's some great tasting asparagus!\""

sentence_in_single = 'He said,"That\'s some great tasting asparagus!"'


## Indexing

# indexing in python starts from 0 and ends with N - 1 (where N is the length of string)

## Accessing characters at those particular indices
first_character = vegetable[0] # -> a
second_character = vegetable[1] # -> s
third_character = vegetable[2] # -> p
fourth_character = vegetable[3] # -> a

## Built-in Functions

# A function is an action performing section of reusable code. 
# Functions have name and are called. 
# functions can also accept arguments and return values


### print() -> it will display the value on screen

vegetable = 'asparagus'
print(vegetable) # passing a variable as argument

print('onion') # passing a literal as argument


### len() -> when a string is passed as argument, it returns the length of the string

vegetable_len = len(vegetable)
print(vegetable_len)

# above two statements can also be written as
print(len(vegetable))

print(len('asparagus'))

## String Methods

# absolutely everything in python is an object
# object also have functions, these are called as methods

vegetable = 'Asparagus'
print(vegetable.lower()) # -> asparagus

print(vegetable.upper()) # -> ASPARAGUS

## Concatenation
concatenated_string = 'Python ' + 'is' + ' fun.'
print(concatenated_string) # -> 'Python is fun.'

# similarly
first = 'Python'
second = 'is'
third = 'fun'
sentence = first + ' ' + second + ' ' + third + '.'
print(sentence) # -> 'Python is fun.'


# Repeating strings
# <string> * num_of_times
print('-'*12) # -> ------------ # 12 -'s

## str() function
# str() will convert non-strings like numbers to strings
version = 3
print('Python is ' + str(version) + ' is fun.')


## Formatting strings
## generating strings using concatenating is tedious and error prone
## So we can use format() method to create formatted strings

print('Python {} fun.'.format('is')) # -> Python is fun.
print('{} {} {}{}'.format('Python', 'is', 'fun', '.')) # same as above

# using args indexes
print('Python {0} {1} and {1} {0} awesome'.format('is', 'fun'))

## formatting and justifying data using extra special characters
print('{0:8} | {1:<8}'.format('Vegetable', 'Quantity'))

print('{0:9} | {1:<8}'.format('Asparagus', 2.33333))







