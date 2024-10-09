speed = int(input("What is the wind speed in MPH of the hurricane\n>"))

if speed < 74:
    print("Tropical Storm")

elif speed < 96:
    print("Category 1")

elif speed < 111:
    print("Category 2")
    
elif speed < 130:
    print("Category 3")

elif speed < 157:
    print("Category 4")

elif speed >= 157:
    print("Category 5")