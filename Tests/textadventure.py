def Start_Adventure():  # Back round information to give context behind the story
    print("Your name is Bob and you have randomly come across a very suspicious looking facility with a dark mist around it")
    print("1. Turn back around being too scared to enter the scary place")
    print("2. Enter through the door which is mysteriously covered in a thick fog, so you can't see inside")

    choice_1 = input("> ")  # First choice in the story 

    if choice_1 == "1":
        Go_Home()

    elif choice_1 == "2":
        Enter_Building()
            
    else:
        print("Invalid Choice, Try Again")
        Start_Adventure()

def Go_Home():
    print("You're a scaredy cat and decide not to have a totatlly fun adventure")
    print("You walk through the forest the facility still on your mind and are suddenly attacked by a shadowy figure")
    print("Your screams echo between the trees and you are never seen again")
    print("Game Over")  # First ending in the game

def Enter_Building():
    print("You enter through the door which loudly creaks and are greated with a dimly lighted front office")
    print("The lights shutter and in the corner of your eye you see two doors, one with danger written on it in red and the other saying safe")

Start_Adventure()   # End of Encounter One

def Door_Choice():
    print("1. Enter though the door that says Danger on it nervous to see what you will find inside")
    print("2. Enter though the door that says Safe on it feeling confident in your choice")

    choice_2 = input("> ")

    if choice_2 == "1":
        Inside_Creepy_Door()

    elif choice_2 == "2":
        Inisde_Safe_Door()

Door_Choice()



