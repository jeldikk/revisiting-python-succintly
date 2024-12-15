## Dictionaries

# dictionary is another python data type which hold key-value pairs, which are referred to as items

# Dictionaries are generated using comma separated items surrounded by curly braces

# dictionary_name = { key1: value1, key2: value2, key3: value3 }

# create a new dictionary
contacts = {
    'David': '111-222',
    'Tom': '555-777'
}

isinstance(contacts, dict) # -> True

david_contact = contacts['David']
tom_contact = contacts['Tom']

print("Tom Contact: {}, David Contact: {}".format(tom_contact, david_contact))

# Updating an existing key in dictionary
contacts['David'] = '888-999'
david_contact = contacts['David']
print("David contact is updated to {}".format(david_contact))


# add new key to dictionary
contacts['Nora'] = "333-444"
print(contacts)

## Removing items from dictionary
# lets add a item 'Kamal': '000-0000' and then again delete the key
contacts['Kamal'] = "000-0000"
print(contacts)

# lets delete the ky
del contacts['Kamal']

print("after deleting item: kamal {}".format(contacts))

## values for keys in a dict can be of any type i.e., str, int, float, list, and another dict (nesting dictionaries)

contacts = {
    'David': ['555-4444', '555-0000'],
    'Tom': '5555-5677'
}
print(contacts)

print("David contacts are :")
for number in contacts['David']:
    print(number)

## Finding a key in Dictionary

# 'key' in dictionary.keys() -> returns True if key is present else false

person = {
    'name': 'kamal',
    'age': 30,
    'aadhar': '',
    'pan': ''
}

print(isinstance(person, dict))

print("is 'name' key present? : {}".format('name' in person.keys()))
print("is 'passport' key present ? :{}".format('passport' in person.keys()))


## Looping through dictionary items

# using key in <dictionary> format
for key in contacts:
    print("name: {}, number: {}".format(key, contacts[key]))

# using key, value in <dictionary> format
for key, value in person.items():
    print("key: {}, value: {}".format(key, value))

