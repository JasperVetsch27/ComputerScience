
ans_1 = input("What is the best pen color\n>")
ans_2 = input("What is the best season\n>")
ans_3 = input("What is the best food\n>")
ans_4 = input("What is the best pet to have\n>")
ans_5 = input("What is the best subject in school\n>")

def tally_score():
    score = 0
    if ans_1.lower() ==  "red":
        score = score + 1
    if ans_2.lower() == "summer":
        score = score + 1 
    if ans_3.lower() == "burger":
        score = score + 1 
    if ans_4.lower() == "cat":
        score = score + 1 
    if ans_5.lower() == "math":
        score = score + 1 
    print(str(score) + " out of 5 questions correct")

tally_score()