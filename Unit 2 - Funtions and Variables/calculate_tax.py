def calculate_tax():
    print("Name of item " + name)
    print("Price of item and tax is " + tax)



name = input("name of item\n>")
price = float(input("Price of item\n>"))
tax = str(price * 1.06875)


calculate_tax()