'''
Try creating a Python program that will capture and display a person’s grocery shopping list. Make it so 
the program will continually prompt the user for another item until the point where they enter a blank 
item. After all the items have been entered, try displaying the shopping list back to the user.
'''

groceries = []
while(True):
    grocery_item = input("Enter an item for your grocery list (Press <Enter> when done) :")
    # print("grocery_item is {}".format(grocery_item))
    if grocery_item == '':
        break
    groceries.append(grocery_item)

print("Grocery Bag contains :")
print('-'*100)
for item in sorted(groceries):
    print(item)




