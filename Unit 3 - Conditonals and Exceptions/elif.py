x = int(input("What is x\n>"))

if x > 0:
    print("x is a positive number!")

elif x < 0:
    print("x is a negative number!")

else:
    print("x is zero")

color = input("What color is the traffic light\n>")

if color.lower() == "green":
    print("GO")

elif color.lower == "red":
    print("STOP")

elif color.lower() == "yellow":
    print("YIELD")

else:
    print("Not the color of the light")

