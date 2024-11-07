# There are a couple types of loops in python
# The far loop lets you iterate a list
# Great for looping a set number of times 
# But what if we need to loop an uncertain number of times??
# Ex. entering your password 
# You could get it right the first time 
# It could take you a million tries 
# Or anything in between 

real_password = "potato45"
entered_password = 56743
attempts = 0

# A while loop contiues looping until the condition is no longer True
while real_password != entered_password:    # Check if the entered password matches the real one
    entered_password = input("Please enter the password\n>")    # Ask for the password
    attempts = attempts + 1
    if entered_password == real_password:   # Chekc if password is correct
        print("ACCESS GRANTED")
    else:
        print(str(attempts) + " tried attempts")
        print("ACCESS DENIED")

print("Welcome!")   # End password checking

# With while loops you need to be careful for infinte loops
# An infite loop happens when you enter a while loop that can never be escaped

user_input = 0

while user_input != "exit":
    user_input = input("Enter something (type exit to quit)\n>")
    print("You entered: " +  user_input)

print("All done")