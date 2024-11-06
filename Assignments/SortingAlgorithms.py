# Bubble Sort

import random
numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),]

print(numbers)

steps = 0    # Variable for how many steps we are talking, start at zero

for i in range(4):
   for i in range(4):   
        if numbers[i] > numbers[i + 1]: # Comparing numbers to each other to determine the greater one
            numbers[i], numbers[i +1] = numbers[i + 1], numbers[i]  # Swap the two numbers if the one is greater
            steps = steps + 1   # Increase number of steps 
print(numbers)
print("Completed in " + str(steps) + " steps")
# Quick Sort

import random
numbers1 = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
print(numbers1)

def quick_sort(n):
    pivot = n[-1]   # Set pivot as the last number
    # First number from the left that is larger than the pivot 
    # First number from the right that is smaller than the pivot

    lPos = 0
    rPos = len(n)-1

    for j in range(0, len(n)):
        for i in range(0, len(n)):
            if i > pivot:
                lPos = i
                break

        for i in range(len(n)-1, -1, -1):
            if n[i] < pivot:
                rPos = i
                break
        
        if lPos > rPos:
            # Swtich pivot with item from left
            n[lPos], n[-1] = n[-1], n[lPos]
            # Stop sorting
            break
        else:
            n[lPos], n[rPos] = n[rPos], n[lPos]

    print(n)

quick_sort(numbers1)




