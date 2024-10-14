# Logical Operators and or !
# Comparison Operators > < == >= <=
# Arithmetic Operators + - / * % ** //

def check_eligibility(age, exp):
    # You must be at least 18 years old and have 1 year of experience to be eligible
    if age >= 18 and exp >= 1:
        print("You are eligible for the competition")

    elif age < 18:
        print("You are not old enough to compete")

    elif exp < 1:
        print("You don't have enough experience")

    else:
        print("You are not eligible for the competition")

a = int(input("Hold old are you?\n>"))
e = int(input("How many years of expience do you hace?\n>"))

check_eligibility(a, e )