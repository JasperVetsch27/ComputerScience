#string functions
#A group of like-functions that manipulate strings
#That modify strings 
#Super easy and convnient to use 
#Python would not be fun withough them

#   .Lower()
#converts a string to all lowercase
#No matter what the input is, it is converted to lowercase
#And the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower() #Converts to "lord of the rings"
real_answer = "Lord of the Rings"
real_answer = real_answer.lower()
print(input_answer == real_answer)


#   .upper()
#Converts  a string to uppercase!
x = "Hello wordl".upper()
print(x)    #prints HELLO WORLD

#   .capitalize()
#Converts to lowercase, then capilaizes the first letter
y = "HElLo WoRld"   #prints Hello world 

#   .title()
#Converts a string to titlecase
#Capital first letter of words 

#   .swapcase()
#It inverts the casing of each character
