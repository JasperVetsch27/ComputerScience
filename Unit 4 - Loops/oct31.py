# Python has four types of collections
# Turple
# Set
# List
# Dictonary

# Today, were going to focus on lists 
# A list is a way to store more than one value in a single variable
# Those values in the list are called ITEMS
# Items can be accessed by their index (postition in the list)

best_elden_ring_weapons = ["Blashemous Blade", "Moonveil", "River of Bloods", "Iron Ball"]

best_years = [1776, 1985, 1994, 1957]

# Print the index of the value in the list
print(best_years.index(1985))


print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

# List items can be changed!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

# Remove the last item in the list by its postion in the list
best_elden_ring_weapons.pop(3)
print(best_elden_ring_weapons)

#Remove an item by its value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

# Add a new item to the end of a list 
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)


# Strings are lists 
# Strings are just a list of characters 
word = "potato"
print(word[0])


