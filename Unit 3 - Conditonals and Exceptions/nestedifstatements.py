# Nested if statements 
prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("You are eligible for free shipping!")
    elif consent:
            print("You are eligible for free shipping!")
    else:
            print("You are not eligible for free shipping!")

elif cost >= 25:
    if age >= 18:
        print("You are eligible for free shipping!")
    elif consent:
         print("You are eligible for free shipping!")
    else:
        print("You are not eligible for free shipping!")
else:
    print("You are not eligible for free shipping!")



# Do we need an umbrella?
# Need an umbrella if it is raining and we are outside 
raining = input("It is raining today?\n>".lower())
outside = input("Are you going outside today?\n>".lower())

if raining == "yes":
    if outside == "yes":
        print("Bring an umbrella")
    else:
         print("Don't bring an umbrella")

else:
     print("Don't Bring an umbrella")

