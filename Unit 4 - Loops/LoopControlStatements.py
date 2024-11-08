# Loop control statements
# Allow you to chnage how loops operate
# Do things like quit the loop early, skip the current loop, and even do nothing
# break, continue. and pass

# break 
# exits a loop prematurely, before it was suppose to end 

# Examole

fruits = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in fruits:
    if fruit == "bug":
        print("You found a bug in the bag")
        break
    else:
        print("You ate a " + fruit)

# continue
# Skips the curent loop 
# It does not exit the entire loop, just moves on to the next iteration

# Example

orders = [15, 30, 35, 23, 100, 3, 10, 22]

# Only apply discount for orders above 20$

for order in orders:
    if order < 20:
        continue    # Skips the rest if the loop iteration and goes to the next iteration
    print(str(order) + " disocunted 5% to " + str(order * 0.95))

# pass
# Does nothing 
# Usually used as a placeholder while writing code
# Text adventure project

def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass
