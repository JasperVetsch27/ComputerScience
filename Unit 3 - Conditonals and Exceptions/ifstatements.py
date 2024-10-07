#If statements evaluate boolean expressions
#Make decisions about which code to run next

#Take a temperature
#Print "<Temperature> is hot" if the temperature is >=80
#Otherwise, print ",temperature is not hot"
temperature = 81
#If, bollean expression :
#Sort of like a function, no parenthesis
if temperature >= 80:
    print(str(temperature) + " degrees is hot")

else: #else takes no condition and runs when the if above is false
    print(str(temperature) + " degrees is not hot")
