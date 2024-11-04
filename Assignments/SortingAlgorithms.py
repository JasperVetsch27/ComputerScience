# Bubble Sort
import random
numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),]

print(numbers)

for i in range(4):
   steps = 0    # Variable for how many steps we are talking, start at zero
   for i in range(4):   
        if numbers[i] > numbers[i + 1]: # Comparing numbers to each other to determine the greater one
            numbers[i], numbers[i +1] = numbers[i + 1], numbers[i]  # Swap the two numbers if the one is greater
            steps = steps + 1   # Increase number of steps 
print(numbers)
print("Completed in " + str(steps) + " steps")
# Merge Sort 

