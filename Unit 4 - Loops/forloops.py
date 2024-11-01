# For Loops
# This is a BIG deal
# For loops allow the programmer to repeat, or what we call loop

# Write a program that prints the numbers one through ten 

# For <temp var> in <list>:

for i in range(50,100):
    print(i)

top_foods = ["Eggs Bendict", "Fried Chicken", "Mac n Cheese"]
# Go through every food in top foods
# Repeats everythig in the for loop for each item in the list
# Where food equals the current item 
for food in top_foods:
    print(food)


# PRACRICE: Create a list of groceries-
# Contains MIlk, Eggs, Bread, Butter, Apples
# Ask for user input on an item they purchased
# If the item was on the list, print ("<item> crossed off the list!")
# Remove that item from the list
# You will need to use a for loop to search for that item 
# You will need an if statement in the for loop to check

List = ["milk", "eggs", "bread", "butter", "apples"]

purchased_item = input("What foods have you purchased already\n> ")

for Food in List:
    if Food == purchased_item.lower():
        print(Food + " checked off the list")
        List.remove(Food)

print(List)

# Create a list of five random number from 0-100
# Use a for loops to find the sum of those numbers 

import random
Number_List = [random.radint(0, 100), random.radint(0, 100), random.radint(0, 100), random.radint(0, 100), random.radint(0, 100)]

for Number in Number_List:
    