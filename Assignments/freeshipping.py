def free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("You are eligible for free shipping")

    else:
        print("Ineligible for free shipping")

prime = False
cost = 25.1
age = 100
consent = False

free_shipping(prime, cost, age, consent)