'''
Try creating a program that will ask the user how far they wish to travel. If they express a desire to 
travel less than three miles, have the program tell them to walk. If they desire to travel more than three 
miles, but less than three hundred miles, advise them that they should drive. In any instance where 
they want to travel three hundred or more miles, tell them to fly

< 3miles -> walk
> 3miles -> drive
> 300miles -> fly
'''

distance = float(input("How far you wish to travel(in miles) ? :"))

if distance <= 3:
    print("Advising you to travel by walk")
elif distance > 3 and distance <= 300:
    print("Advising you to travel by driving")
else:
    print("Advise you to travel by flying")
