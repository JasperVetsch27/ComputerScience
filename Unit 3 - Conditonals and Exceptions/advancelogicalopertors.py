# Amazon free shipping eligibility system
# Loyaly customer OR purchases of over $25
# Under 18, you need parent consent to purchase

def free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("You are eligible for free shipping")

    else:
        print("Ineligible for free shipping")

prime = True
cost = 5
age = 100
consent = False

free_shipping(prime, cost, age, consent)