## Lists in python are organised collections of items. the items can be of various data types themselves.

# list_name = [item_1, item_2, item_3]
animals = ['lion', 'tiger', 'seal']

# you can create list using square brackets []
empty_list = []

#indexing in lists starts from 0 to n-1 (n is length of list)

first_animal = animals[0]
second_animal = animals[1]
third_animal = animals[2]
print("first : {}, second: {}, third: {}".format(first_animal, second_animal, third_animal))

# lists in python are mutable i.e., you can set new value using indexing syntax

animals[2] = 'Wolf'

print("Update third animal is : {}".format(animals[2]))

## python also provides negative index; -1 points to last and -2 to second from last and so on

last_item = animals[-1]
first_from_last = animals[-2]
second_from_last = animals[-3]

print("last: {}, first_from_last: {}, second_from_last : {}".format(last_item, first_from_last, second_from_last))


## Adding Items to a list

# use append(item) to add items to the end of list

vegetables = ['onion', 'tomato', 'chilli']

vegetables.append('cabbage')
print(vegetables)

## add multiple items as list to end of list using extend() method
ages = ['baby', 'toddler', 'kid']
ages.extend(['young', 'adult', 'old'])
print(ages)

# use insert(index, item) to add item at specified index
ages.insert(3, 'monster')
ages = ages + ['very_old', 'dead_old', 'dead']
print(ages) # remember index starts from 0, so inserting item at #3 will add item at 4th position

## list slices
# list[m:n] -> items from m to n-1 indices
# list[:n] -> items from 0 to n-1 indices
# list[m:] -> items from m to end 
# list[:] -> returns all items

print("all items {}".format(ages))
print("ages[3:7] :{}".format(ages[3:7]))
print("ages[:7] :{}".format(ages[:7]))
print("ages[3:] :{}".format(ages[3:]))
print("ages[:] :{}".format(ages[:]))

# slices are also work in strings

## Finding an item in list
# use <list>.index(item) to check if item exists in list
# this will return the index of first occurrence of item if multiple items exists
# else this will throw error

try:
    kamal_index = ages.index('kamal')
except:
    print("item kamal is not found in list")

## Looping through a list

# for loop: looping over the items in list
for item in ages:
    print(item)

# python also provides while loop; while loop will execute based on a condition
print("--------------------------")
print("This is using while loop")
print("--------------------------")
index = 0

while index < len(ages):
    print(ages[index])
    index = index + 1

## sorting a list

other_ages = ages[:]
print(other_ages)
other_ages.sort() # this will sort the items in place
print(other_ages)

# if you don't want to sort in place and return the sorted list in new array use sorted global function
sorted_ages = sorted(ages)
print(sorted_ages)
print(ages)

## Ranges
# range() function produces a list that begins at zero and continues upto, but not including the stop.

range(5) # -> iterator with items [0, 1, 2, 3, 4]

# range(m, n, step) -> m to n-1 numbers in a list
for i in range(7):
    print(i)

for num in range(2, 10, 2):
    print(num)