"""
Try to create a dictionary that has a listing of people and includes one interesting fact about each of them. 

Display each person and their interesting fact on the screen. 
From there, alter a fact about one of the people on the list. 
Also, add an extra person and corresponding fact to the list. Display the newly created list of people and facts. 
Try running the program multiple times and take note of whether the 
order changes. 
"""

def display_facts(idict):
    for name, fact in idict.items():
        print("Name: {}, Fact: {}".format(name, fact))

interesting_facts = dict()

interesting_facts['Jeff'] = 'Was born in France.'
interesting_facts['David'] = 'Was a mascot in college.'
interesting_facts['Anna'] = 'Has arachnophobia.'

display_facts(interesting_facts)
print()

interesting_facts['Dylan'] = 'Has a pet hedgehog.'
interesting_facts['Jeff'] = 'Was born in France.'

display_facts(interesting_facts)
print()

interesting_facts['David'] = 'Can Juggle.'
interesting_facts['Anna'] = 'Has arachnophobia.'
display_facts(interesting_facts)
print()




