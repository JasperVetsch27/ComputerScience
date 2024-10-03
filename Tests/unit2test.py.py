#1

word_1 = input("Type in a random word\n>")
word_2 = input("Type another random word\n>")
word_3 = input("Type a final random word\n>")

print(word_1 + word_2 + word_3)

#2

def add_three(a, b, c):
    print(a + b + c)

number_1 = int(input("Give me a integer\n>"))
number_2 = int(input("Give me a integer\n>"))
number_3 = int(input("Give me a integer\n>"))

add_three(number_1, number_2, number_3)

#3

def data_three():
    a = int(input("Give me a whole number\n>"))
    b = float(input("Give me a number with a decimal in it\n>"))
    c = input("Give me any word that first comes to mind\n>")
    d = str(a + b)
    print(d + c)

data_three()