# Exception Handling
# Write a program that asks for two number and adds them

# if    =   try
# elif  =   except
def divide_two_numbers():
    try:
        x = int(input("Whats the first number\n>"))
        y = int(input("Whats the second number\n>"))
        print(x / y)

    except ValueError:
        print("Please enter a number . . . .")
        divide_two_numbers()

    except ZeroDivisionError:
        print("Cannot divide by zero . . . .")
        divide_two_numbers()

    finally:
        print()
        
divide_two_numbers()
