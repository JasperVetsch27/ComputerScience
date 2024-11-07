import random 
Number = random.randint(0,101)
print(Number)
User = -1
attempts = 0

while Number != User:
    attempts += 1
    try:
        User = int(input("Guess the number between 1 and 100\n>"))
        if User < Number:
            print("Your number is lower than the number")

        elif User > Number:
            print("Your number is higher than the number")
    except:
        print("Not quite")


print("CORRECT")
print("You got it in " + str(attempts) + " tries")