# Amazon free shipping eligibility system
# Loyaly customer OR purchases of over $25
# Under 18, you need parent consent to purchase

def free_shipping(prime, cost, age, consent):
    if (prime or cost >= 25) and (age >= 18 or consent):
        print("You are eligible for free shipping")

    else:
        print("Ineligible for free shipping")

prime = True
cost = 5
age = 100
consent = Fals

free_shipping(prime, cost, age, consent)